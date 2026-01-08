#!/bin/bash
git init
git add .
git commit -m "Deploy Big Ten TDA Visualization"
git branch -M main
echo "deployment ready. Create a repo on GitHub, then run: git remote add origin <url> && git push -u origin main"

