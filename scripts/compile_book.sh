#! /bin/bash

mkdir -p $PYTHONFORSMELOCATION/book/tmp
cp $PYTHONFORSMELOCATION/book/*.tex $PYTHONFORSMELOCATION/book/tmp
cp $PYTHONFORSMELOCATION/book/*.bib $PYTHONFORSMELOCATION/book/tmp
cd $PYTHONFORSMELOCATION/book/tmp

sh compile_tex.sh AnIntroductionToPythonForScienceMathAndEngineering

mv $PYTHONFORSMELOCATION/book/tmp/AnIntroductionToPythonForScienceMathAndEngineering.pdf $PYTHONFORSMELOCATION
