#!/bin/bash

git pull
source env.sh

while :; do
    python radio.py
    sleep 1
done
