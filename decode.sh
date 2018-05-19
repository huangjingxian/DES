#!/bin/sh

python a2b.py < ./decode/dec0
make
./DES --mode dec --file ./decode/dec
python b2a.py < ./decode/ans