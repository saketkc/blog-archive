#!/bin/bash
set -e 
pelican content -o output -s publishconf.py
ghp-import output -r origin -b master
git push origin master -f
