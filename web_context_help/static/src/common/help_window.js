/* Copyright 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
 * License LGPL-3.0-or-later (https://www.gnu.org/licenses/lgpl).
 *
 * Help window script: plain ES5, shared by every Odoo version.
 * Talks to the Odoo tab (window.opener) through postMessage.
 */
(function () {
    "use strict";
    var config = window.wchConfig || {};
    var labels = config.labels || {};
    var FOLLOW_KEY = "web_context_help.follow";

    function post(message) {
        if (window.opener && !window.opener.closed) {
            window.opener.postMessage(message, window.location.origin);
            window.opener.focus();
        }
    }

    function getFollow() {
        try {
            return window.localStorage.getItem(FOLLOW_KEY) !== "0";
        } catch (e) {
            return true;
        }
    }

    function setFollow(value) {
        try {
            window.localStorage.setItem(FOLLOW_KEY, value ? "1" : "0");
        } catch (e) {
            // storage unavailable: follow stays on
        }
        post({type: "wch_follow", value: value});
    }

    function onClick(ev) {
        var el = ev.target.closest ? ev.target.closest("a.wch-field, a.wch-tour") : null;
        if (!el) {
            return;
        }
        ev.preventDefault();
        if (el.classList.contains("wch-field")) {
            post({type: "wch_highlight", field: el.getAttribute("data-field")});
        } else {
            post({type: "wch_tour", tour: el.getAttribute("data-tour")});
        }
    }

    function text(tag, value, cls) {
        var el = document.createElement(tag);
        el.textContent = value;
        if (cls) {
            el.className = cls;
        }
        return el;
    }

    function showAnswers(results) {
        var box = document.getElementById("wch_answers");
        box.innerHTML = "";
        if (!results.length) {
            box.appendChild(text("p", labels.none || "No answer found", "wch-none"));
            return;
        }
        results.forEach(function (res) {
            var item = document.createElement("div");
            item.className = "wch-answer";
            var link = text("a", res.title || res.page_title);
            link.href = res.url;
            item.appendChild(link);
            if (res.page_title && res.page_title !== res.title) {
                item.appendChild(text("span", " — " + res.page_title, "wch-page"));
            }
            item.appendChild(text("p", res.snippet));
            box.appendChild(item);
        });
    }

    function ask(ev) {
        ev.preventDefault();
        var question = document.getElementById("wch_question").value;
        if (!question.trim()) {
            return;
        }
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/web_context_help/ask");
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onload = function () {
            var data = JSON.parse(xhr.responseText);
            showAnswers((data.result && data.result.results) || []);
        };
        xhr.send(
            JSON.stringify({
                jsonrpc: "2.0",
                method: "call",
                params: {
                    question: question,
                    context: {
                        model: config.model,
                        page_key: config.page_key,
                        lang: config.lang,
                    },
                },
            })
        );
    }

    // Find in page, like Ctrl+F: case and accent insensitive, white space
    // runs as one space, across inline markup (bold, links...) of a block
    var matches = [];
    var current = -1;
    var searched = "";
    // Max distance, in words of the same block, between the searched words
    var NEAR = 12;
    var anyWord = false;

    function fold(ch) {
        if (ch.normalize) {
            ch = ch.normalize("NFD").replace(/[̀-ͯ]/g, "");
        }
        return ch.toLowerCase();
    }

    function clearMatches() {
        var marks = document.querySelectorAll("mark.wch-match");
        for (var i = 0; i < marks.length; i++) {
            var parent = marks[i].parentNode;
            parent.replaceChild(document.createTextNode(marks[i].textContent), marks[i]);
            parent.normalize();
        }
        matches = [];
        current = -1;
    }

    var BLOCKS = "p, li, dt, dd, h1, h2, h3, h4, h5, h6, td, th, pre, caption, " +
        "blockquote, div, section, main";

    // Text nodes of root grouped by block (paragraph, list item...), in order
    function textBlocks(root) {
        var blocks = [];
        var last = null;
        var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
            acceptNode: function (node) {
                return node.parentNode.closest("script, style")
                    ? NodeFilter.FILTER_REJECT
                    : NodeFilter.FILTER_ACCEPT;
            },
        });
        while (walker.nextNode()) {
            var node = walker.currentNode;
            var block = node.parentNode.closest(BLOCKS) || root;
            if (block !== last) {
                blocks.push([]);
                last = block;
            }
            blocks[blocks.length - 1].push(node);
        }
        return blocks;
    }

    // Folded text: lower case, no accents, every run of white space as one
    // space; leading white space dropped when after is the end of a space.
    // onChar(i) is called for each folded char with its offset in value.
    function foldText(value, onChar, after) {
        var folded = "";
        var space = after === undefined || after === " ";
        for (var i = 0; i < value.length; i++) {
            var f = fold(value.charAt(i));
            for (var j = 0; j < f.length; j++) {
                var ch = /\s/.test(f.charAt(j)) ? " " : f.charAt(j);
                if (ch === " " && space) {
                    continue;
                }
                space = ch === " ";
                folded += ch;
                if (onChar) {
                    onChar(i);
                }
            }
        }
        return folded;
    }

    function wrap(node, from, to) {
        var tail = node.splitText(from);
        tail.splitText(to - from);
        var mark = document.createElement("mark");
        mark.className = "wch-match";
        tail.parentNode.replaceChild(mark, tail);
        mark.appendChild(tail);
        return mark;
    }

    // Folded text of a block, with the [node, offset] of each folded char
    function blockText(nodes) {
        var folded = "";
        var map = [];
        nodes.forEach(function (node, n) {
            folded += foldText(
                node.nodeValue,
                function (i) {
                    map.push([n, i]);
                },
                folded ? folded.charAt(folded.length - 1) : " "
            );
        });
        return {nodes: nodes, folded: folded, map: map};
    }

    // Ranges [start, end) of needle in the folded text, not overlapping
    function occurrences(folded, needle) {
        var ranges = [];
        var pos = folded.indexOf(needle);
        while (pos >= 0) {
            ranges.push([pos, pos + needle.length]);
            pos = folded.indexOf(needle, pos + needle.length);
        }
        return ranges;
    }

    // Ranges of the words of a block: every word, or only the occurrences
    // having all the other words within NEAR words of the same block
    function wordRanges(block, words, near) {
        var found = words.map(function (word) {
            return occurrences(block.folded, word).map(function (range) {
                var number = block.folded.slice(0, range[0]).split(" ").length;
                return {range: range, number: number};
            });
        });
        var ranges = [];
        found.forEach(function (occs, w) {
            occs.forEach(function (occ) {
                var keep = !near || found.every(function (others, o) {
                    return o === w || others.some(function (other) {
                        return Math.abs(other.number - occ.number) <= NEAR;
                    });
                });
                if (keep) {
                    ranges.push(occ.range);
                }
            });
        });
        return ranges;
    }

    // Sorted, overlapping ranges joined (e.g. "in" inside "invoice")
    function joinRanges(ranges) {
        var joined = [];
        ranges
            .slice()
            .sort(function (a, b) {
                return a[0] - b[0];
            })
            .forEach(function (range) {
                var last = joined[joined.length - 1];
                if (last && range[0] <= last[1]) {
                    last[1] = Math.max(last[1], range[1]);
                } else {
                    joined.push(range.slice());
                }
            });
        return joined;
    }

    // Marks the ranges of a block; a range across inline markup gets one mark
    // per text node. Returns a list of marks for each range.
    function markBlock(block, ranges) {
        var nodes = block.nodes;
        var map = block.map;
        // Segments [range, from, to] of every node
        var segments = nodes.map(function () {
            return [];
        });
        ranges.forEach(function (range, r) {
            var first = map[range[0]];
            var last = map[range[1] - 1];
            for (var n = first[0]; n <= last[0]; n++) {
                var from = n === first[0] ? first[1] : 0;
                var to = n === last[0] ? last[1] + 1 : nodes[n].nodeValue.length;
                if (to > from) {
                    segments[n].push([r, from, to]);
                }
            }
        });
        var found = ranges.map(function () {
            return [];
        });
        nodes.forEach(function (node, n) {
            // From the end, so the offsets of the previous segments stay valid
            for (var k = segments[n].length - 1; k >= 0; k--) {
                var seg = segments[n][k];
                found[seg[0]].unshift(wrap(node, seg[1], seg[2]));
            }
        });
        return found;
    }

    function showCount() {
        document.getElementById("wch_find_count").textContent = matches.length
            ? current + 1 + "/" + matches.length +
              (anyWord ? " · " + (labels.any_word || "any word") : "")
            : "";
    }

    function goTo(index) {
        if (!matches.length) {
            showCount();
            return;
        }
        if (current >= 0) {
            matches[current].forEach(function (mark) {
                mark.classList.remove("wch-current");
            });
        }
        current = (index + matches.length) % matches.length;
        matches[current].forEach(function (mark) {
            mark.classList.add("wch-current");
        });
        matches[current][0].scrollIntoView({block: "center"});
        showCount();
    }

    // Search in 2 steps: every word of the query is found, then only the
    // occurrences near all the other words are kept; when none is kept, every
    // occurrence is shown ("any word"). A query in quotes is an exact phrase.
    function find(query) {
        clearMatches();
        searched = query;
        anyWord = false;
        var text = query.trim();
        var phrase = text.length > 1 && text.charAt(0) === '"' &&
            text.charAt(text.length - 1) === '"';
        var folded = foldText(phrase ? text.slice(1, -1) : text).trim();
        var words = [];
        (phrase ? [folded] : folded.split(" ")).forEach(function (word) {
            if (word && words.indexOf(word) < 0) {
                words.push(word);
            }
        });
        // Words of 1-2 letters (di, il, in...) are found inside too many
        // words: ignored in a multi-word search, unless all words are short
        var long = words.filter(function (word) {
            return word.length > 2;
        });
        if (words.length > 1 && long.length) {
            words = long;
        }
        if (words.length) {
            var root = document.querySelector(".wch-content") || document.body;
            var blocks = textBlocks(root).map(blockText);
            var near = words.length > 1;
            var ranges = blocks.map(function (block) {
                return wordRanges(block, words, near);
            });
            var kept = ranges.some(function (r) {
                return r.length;
            });
            if (near && !kept) {
                anyWord = true;
                ranges = blocks.map(function (block) {
                    return wordRanges(block, words, false);
                });
            }
            blocks.forEach(function (block, b) {
                matches = matches.concat(markBlock(block, joinRanges(ranges[b])));
            });
        }
        goTo(0);
    }

    function setupFind() {
        var input = document.getElementById("wch_find");
        if (!input) {
            return;
        }
        var timer = null;
        input.addEventListener("input", function () {
            clearTimeout(timer);
            timer = setTimeout(function () {
                find(input.value);
            }, 200);
        });
        function step(delta) {
            clearTimeout(timer);
            if (matches.length && input.value === searched) {
                goTo(current + delta);
            } else {
                find(input.value);
            }
        }
        document.getElementById("wch_find_prev").addEventListener("click", function () {
            step(-1);
        });
        document.getElementById("wch_find_next").addEventListener("click", function () {
            step(1);
        });
        input.addEventListener("keydown", function (ev) {
            if (ev.key === "Enter") {
                ev.preventDefault();
                step(ev.shiftKey ? -1 : 1);
            } else if (ev.key === "Escape") {
                input.value = "";
                find("");
            }
        });
        // Ctrl+F goes to the find box; pressed again opens the browser search
        document.addEventListener("keydown", function (ev) {
            if ((ev.ctrlKey || ev.metaKey) && ev.key === "f" &&
                document.activeElement !== input) {
                ev.preventDefault();
                input.focus();
                input.select();
            }
        });
    }

    document.addEventListener("DOMContentLoaded", function () {
        setupFind();
        var follow = document.getElementById("wch_follow");
        follow.checked = getFollow();
        follow.addEventListener("change", function () {
            setFollow(follow.checked);
        });
        var askForm = document.getElementById("wch_ask");
        if (askForm) {
            askForm.addEventListener("submit", ask);
        }
        document.addEventListener("click", onClick);
        post({type: "wch_ready", page_key: config.page_key});
    });
})();
