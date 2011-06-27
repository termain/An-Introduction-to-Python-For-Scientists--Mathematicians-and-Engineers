#! /bin/bash

pdflatex  "${1}.tex"
makeglossaries "${1}"
pdflatex  "${1}.tex"
makeglossaries "${1}"
pdflatex  "${1}.tex"
