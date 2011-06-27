#! /bin/bash

SUFFIXES=".aux .bbl .blg .glg .glo .gls .ist .log .out .pdf"

for ENDING in $SUFFIXES; do
    rm "$1$ENDING"
done

rm *.log
