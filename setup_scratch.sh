#!/bin/bash
#conda create -n -y blog pelican bs4 ghp-import
pip install pelican-jupyter
wget -c https://github.com/getpelican/pelican-plugins/archive/master.zip && unzip master.zip && mv pelican-plugins-master pelican-plugins
git clone --recursive https://github.com/getpelican/pelican-themes pelican-themes-git
cp -r pelican-themes-git pelican-themes

pip install -U ipython notebook nbconvert webassets cssmin pelican[Markdown]

