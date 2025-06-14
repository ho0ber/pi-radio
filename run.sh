#!/bin/sh

sudo apt-get install git mpg321 python3 -y
git pull
python3 -m install -r requirements.txt
source env.sh

while :; do
    python radio.py
    sleep 1
done
