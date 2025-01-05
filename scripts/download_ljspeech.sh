#!/bin/sh

wget -t 0 -c https://data.keithito.com/data/speech/LJSpeech-1.1.tar.bz2
tar -jxf LJSpeech-1.1.tar.bz2

python src/resample.py