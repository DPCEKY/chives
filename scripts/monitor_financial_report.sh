#!/bin/bash

cd ~/chives

git pull

cd ~

python3 -m chives.monitor.financialInfo

cd ~/chives
git add .

now=`date`
git commit -m "monitor monthly financial report $now"

git push
