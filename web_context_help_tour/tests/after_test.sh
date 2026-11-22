#!/bin/bash
# Copyright 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
# License LGPL-3.0-or-later (https://www.gnu.org/licenses/lgpl).
#
# Run by please zerobug / please test after the tests of web_context_help_tour:
# removes the filestore of the test database filled by before_test.sh.
DIR=$(cd "$(dirname "$0")" && pwd)
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
[ -n "$VER" ] && rm -rf "$FILESTORE/test_${MODULE}_$VER"
