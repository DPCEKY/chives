#!/bin/bash

su -i

sudo apt-get update
sudo apt-get upgrade -y

sudo apt-get install git
sudo apt install vim -y
sudo apt-get install mailutils -y

sudo apt-get install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update

sudo apt-get install build-essential libpq-dev libssl-dev openssl libffi-dev zlib1g-dev
sudo apt-get install python3-pip python3.7-dev -y
sudo apt-get install python3.7

sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 10

pip3 install pandas bs4 scipy

pip3 install yfinance

git pull git@github.com:DPCEKY/chives.git
