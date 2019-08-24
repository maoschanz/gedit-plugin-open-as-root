#!/bin/bash

if (( $EUID == 0 )); then
	INSTALL_DIR="/usr/lib/x86_64-linux-gnu/gedit/plugins/"
else
	INSTALL_DIR="$HOME/.local/share/gedit/plugins"
fi

mkdir -p $INSTALL_DIR

echo "Installing plugin files in $INSTALL_DIR"
cp open_as_root.plugin $INSTALL_DIR/open_as_root.plugin
cp open_as_root.py $INSTALL_DIR/open_as_root.py

echo "Done."
exit 0

