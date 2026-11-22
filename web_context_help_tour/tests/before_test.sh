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

# The test database is created from a template database (createdb ... template), but
# Odoo keeps the attachment files (web assets) in a filestore directory per database:
# without the template files the test database logs an ERROR for every missing
# attachment and zerobug marks the run as FAILED. Copy the template files (never
# overwriting) in the filestore of the test database.
MODULE=$(basename "$(dirname "$DIR")")
VER=$(sed -nE 's/.*"version": *"([0-9]+)\..*/\1/p' "$(dirname "$DIR")/__manifest__.py" | head -n1)
DATA_DIR=""
for CONF in "/etc/odoo/odoo$VER-ee.conf" "/etc/odoo/odoo$VER.conf"; do
    if [ -z "$DATA_DIR" ] && [ -r "$CONF" ]; then
        DATA_DIR=$(sed -nE 's/^data_dir *= *(.*[^ ]) *$/\1/p' "$CONF" | head -n1)
    fi
done
[ -z "$DATA_DIR" ] && DATA_DIR="$HOME/.local/share/Odoo$VER"
FILESTORE="$DATA_DIR/filestore"
if [ -d "$FILESTORE/template_${MODULE}_$VER" ]; then
    mkdir -p "$FILESTORE/test_${MODULE}_$VER"
    cp -rn "$FILESTORE/template_${MODULE}_$VER/." "$FILESTORE/test_${MODULE}_$VER/"
fi
