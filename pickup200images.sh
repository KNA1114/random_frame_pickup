#!/bin/bash

VIDEOPATH=$(ls *.mp4)

for i in $VIDEOPATH; do
    for j in `seq 1 200`; do
        python randomPickupper.py $i
    done
done
