/* Copyright 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
 * License LGPL-3.0-or-later (https://www.gnu.org/licenses/lgpl).
 *
 * VERSION-DEPENDENT: Odoo 18 adapter.
 * Editor plugin of the help pages: button of the floating toolbar (and "/"
 * command) inserting a video of the video directory, played on click.
 * While editing a video is not editable: Backspace or Delete next to it
 * removes it as a whole, instead of its hidden fallback text.
 */
import {Plugin} from "@html_editor/plugin";
import {closestBlock} from "@html_editor/utils/blocks";
import {rightPos} from "@html_editor/utils/position";
import {withSequence} from "@html_editor/utils/resource";
import {_t} from "@web/core/l10n/translation";
import {HelpVideoDialog} from "./help_video_dialog";

export const VIDEO_URL = "/web_context_help/video/";

export function videoUrl(name) {
    return VIDEO_URL + name.split("/").map(encodeURIComponent).join("/");
}

/**
 * Element locked while editing: the paragraph holding only the video, else
 * the video itself.
 */
function lockedElement(video) {
    const parent = video.parentElement;
    const alone =
        parent &&
        ["P", "DIV"].includes(parent.tagName) &&
        parent.childElementCount === 1 &&
        [...parent.childNodes].every(
            (child) => child === video || !child.textContent.trim()
        );
    return alone ? parent : video;
}

function videosOf(root) {
    if (!root || root.nodeType !== Node.ELEMENT_NODE) {
        return [];
    }
    const videos = [...root.querySelectorAll("video")];
    return root.tagName === "VIDEO" ? [root, ...videos] : videos;
}

export class HelpVideoPlugin extends Plugin {
    static id = "wchVideo";
    static dependencies = ["selection", "history", "dialog"];
    resources = {
        user_commands: [
            {
                id: "wchInsertVideo",
                title: _t("Help video"),
                description: _t("Insert a video of the help video directory"),
                icon: "fa-film",
                run: this.openVideoDialog.bind(this),
            },
        ],
        toolbar_groups: withSequence(90, {id: "wch_video"}),
        toolbar_items: [
            {
                id: "wch_video",
                groupId: "wch_video",
                commandId: "wchInsertVideo",
            },
        ],
        powerbox_items: [{categoryId: "media", commandId: "wchInsertVideo"}],
        normalize_handlers: this.lockVideos.bind(this),
        clean_for_save_handlers: ({root}) => this.unlockVideos(root),
    };

    lockVideos(root) {
        for (const video of videosOf(root)) {
            lockedElement(video).setAttribute("contenteditable", "false");
        }
    }

    unlockVideos(root) {
        for (const video of videosOf(root)) {
            const locked = lockedElement(video);
            if (locked.getAttribute("contenteditable") === "false") {
                locked.removeAttribute("contenteditable");
            }
        }
    }

    openVideoDialog() {
        return this.dependencies.dialog.addDialog(HelpVideoDialog, {
            onSelect: (video) => this.insertVideo(video),
        });
    }

    /**
     * Insert the video in its own paragraph after the block of the
     * selection: the selected text is kept.
     */
    insertVideo(video) {
        const selection = this.dependencies.selection.getEditableSelection();
        let block = closestBlock(selection.endContainer);
        if (!block || block === this.editable || !this.editable.contains(block)) {
            block = null;
        }
        // Out of lists and tables: a paragraph is not allowed there
        block = block?.closest("table") || block;
        while (block && ["UL", "OL", "LI"].includes(block.parentElement?.tagName)) {
            block = block.parentElement;
        }
        const url = videoUrl(video.name);
        const paragraph = this.document.createElement("p");
        const player = this.document.createElement("video");
        player.setAttribute("src", url);
        player.setAttribute("controls", "");
        player.setAttribute("preload", "metadata");
        player.setAttribute("style", "max-width:100%; width:960px;");
        player.setAttribute("title", video.name);
        const link = this.document.createElement("a");
        link.setAttribute("href", `${url}?download=1`);
        link.textContent = _t("download it");
        player.append(_t("The browser cannot play the video: "), link, ".");
        paragraph.append(player);
        if (block) {
            block.after(paragraph);
        } else {
            this.editable.append(paragraph);
        }
        const [anchorNode, anchorOffset] = rightPos(paragraph);
        this.dependencies.selection.setSelection({anchorNode, anchorOffset});
        this.dependencies.history.addStep();
    }
}
