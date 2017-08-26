#!/usr/bin/env bash
set -o nounset
set -o errexit
set -o pipefail

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REL="$DIR/dist"

PY_BIN="python"

function build() {
    local PKG="$1"
    local PKG_PATH="$DIR/$PKG"
    local PKG_DIST="$PKG_PATH/dist"

    echo "[$PKG] Clean dist ..."
    rm -rf "$REL"

    echo "[$PKG] Build ..."
    "$PY_BIN" setup.py sdist 2>&1 > /dev/null

    echo "[$PKG] Clean temporary build artifacts ..."
    rm -rf "$DIR/src/$PKG.egg-info"

    echo "[$PKG] Rename artifacts ..."
    mv --force --verbose "$REL/$(ls $REL | head -n 1)" "$REL/$PKG-latest.zip"
}

build google_translate_api

echo 'Done.'