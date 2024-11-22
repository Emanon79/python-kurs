#!/bin/bash

requirements=$1

if [ ! -f .python-kurs-venv/bin/activate ]; then
    python3 -m venv .python-kurs-venv
fi

. .python-kurs-venv/bin/activate

if [ ! -z "$requirements" ]; then
    if [ -f "$requirements" ]; then
	pip3 install -r "$requirements"
    else
	echo "Given requirements file does not exist!"
	exit 1
    fi
fi
