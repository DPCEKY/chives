#!/bin/bash

cd ~/chives

git pull

cd ~

python3 -m chives.monitor.option

cd ~/chives
git add .

now=`date`
git commit -m "monitor weekly option $now"

git push
