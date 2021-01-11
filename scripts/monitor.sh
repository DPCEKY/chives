#!/bin/bash

su -i
cd ~

git pull

python3 -m chives.monitor.dfWriteTester

cd ~/chives
git add .

now=`date`
git commit -m "monitor daily update $now"

git push
