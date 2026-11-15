#!/bin/bash
# Copyright 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
# License LGPL-3.0-or-later (https://www.gnu.org/licenses/lgpl).
#
# Run by please zerobug / please test before the tests of web_context_help_tour
# (declared in readme/__manifest__.rst).
#
# Odoo 10 plays the browser tests (HttpCase.phantom_js) with PhantomJS: when the
# phantomjs executable is missing the test is silently skipped, not run.
# This script installs PhantomJS 2.1.1 locally, in tests/.phantomjs/ (ignored by
# git), and nothing else on the machine: test_tour_player.py puts tests/test_bin
# in front of the PATH of the Odoo test process only when that local copy exists,
# and test_bin/phantomjs runs it with the environment it needs.
# Nothing is downloaded when the local copy is already there.
set -u
DIR=$(cd "$(dirname "$0")" && pwd)
PJS_VER=2.1.1
PJS_NAME=phantomjs-$PJS_VER-linux-x86_64
PJS_URL=https://github.com/Medium/phantomjs/releases/download/v$PJS_VER/$PJS_NAME.tar.bz2
PJS_SHA256=86dd9a4bf4aee45f1a84c9f61cf1947c1d6dce9b9e8d2a907105da7852460d2f
PJS_DIR=$DIR/.phantomjs
PJS_BIN=$PJS_DIR/bin/phantomjs

chmod +x "$DIR/test_bin/phantomjs"

if [[ -x $PJS_BIN ]]; then
    echo "before_test: PhantomJS already installed in $PJS_DIR"
    exit 0
fi
if [[ $(uname -m) != "x86_64" ]]; then
    echo "before_test: PhantomJS $PJS_VER is built for x86_64 only," \
         "browser tests will be skipped" >&2
    exit 1
fi
# The static build still needs the font libraries of the system
for lib in libfontconfig.so.1 libfreetype.so.6; do
    if ! ldconfig -p | grep -q "$lib"; then
        echo "before_test: $lib not found, install it (apt install" \
             "libfontconfig1 libfreetype6)" >&2
        exit 1
    fi
done

TMP=$(mktemp -d "${TMPDIR:-/tmp}/phantomjs.XXXXXX")
trap 'rm -rf "$TMP"' EXIT
echo "before_test: downloading $PJS_URL"
if command -v curl >/dev/null 2>&1; then
    curl -sSL --max-time 600 -o "$TMP/$PJS_NAME.tar.bz2" "$PJS_URL"
else
    wget -q -O "$TMP/$PJS_NAME.tar.bz2" "$PJS_URL"
fi
if [[ $? -ne 0 || ! -s "$TMP/$PJS_NAME.tar.bz2" ]]; then
    echo "before_test: download failed, browser tests will be skipped" >&2
    exit 1
fi
if ! echo "$PJS_SHA256  $TMP/$PJS_NAME.tar.bz2" | sha256sum -c --quiet -; then
    echo "before_test: checksum mismatch, PhantomJS not installed" >&2
    exit 1
fi
# Only the executable is kept: the archive also carries examples and docs
if ! tar -xjf "$TMP/$PJS_NAME.tar.bz2" -C "$TMP" "$PJS_NAME/bin/phantomjs"; then
    echo "before_test: cannot extract the archive (bzip2 missing?)" >&2
    exit 1
fi
mkdir -p "$PJS_DIR/bin"
mv "$TMP/$PJS_NAME/bin/phantomjs" "$PJS_BIN"
chmod +x "$PJS_BIN"
echo "before_test: PhantomJS $PJS_VER installed in $PJS_DIR"
exit 0
