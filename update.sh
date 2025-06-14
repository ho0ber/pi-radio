#!/bin/bash

sudo apt-get install git mpg321 python3 python3-pip -y
git pull
python3 -m pip install -r requirements.txt --break-system-packages
