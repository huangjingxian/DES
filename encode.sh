#!/bin/sh

python a2b.py < ./encode/enc0
make
./DES --mode enc --file ./encode/enc
python b2a.py < ./encode/ans