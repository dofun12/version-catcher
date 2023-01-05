#!/bin/bash
mkdir -p linux-amd-x86-64
pyinstaller main.py --onefile --name version-catcher
mv dist/version-catcher ./linux-amd-x86-64