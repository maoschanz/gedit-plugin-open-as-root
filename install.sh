#!/bin/bash

if [ ! -d "$HOME/.local/share/gedit" ]; then
	mkdir ~/.local/share/gedit
fi
if [ ! -d "$HOME/.local/share/gedit/plugins" ]; then
	mkdir ~/.local/share/gedit/plugins
fi

cp open_as_root.plugin ~/.local/share/gedit/plugins/open_as_root.plugin
cp open_as_root.py ~/.local/share/gedit/plugins/open_as_root.py

#sudo cp markdown_preview.py /usr/lib/x86_64-linux-gnu/gedit/plugins/open_as_root.py
#sudo cp markdown_preview.plugin /usr/lib/x86_64-linux-gnu/gedit/plugins/open_as_root.plugin

