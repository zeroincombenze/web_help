#!/bin/bash
# Copyright 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
# License LGPL-3.0-or-later (https://www.gnu.org/licenses/lgpl).
#
# Run by please zerobug / please test before the tests of web_context_help_tour:
# prepares the Chrome wrapper used by the browser tests (see test_tour_player.py).
DIR=$(cd "$(dirname "$0")" && pwd)
chmod +x "$DIR/chrome_bin/google-chrome"
if [ ! -x /usr/bin/google-chrome ] && ! command -v chromium >/dev/null 2>&1 \
        && ! command -v chromium-browser >/dev/null 2>&1; then
    echo "before_test: no Chrome/Chromium found, browser tests will fail" >&2
    exit 1
fi
