#!/bin/bash

cd ~/chives

git pull

cd ~

python3 -m chives.monitor.dfWriteTester

cd ~/chives
git add .

now=`date`
git commit -m "monitor daily update $now"

git push
