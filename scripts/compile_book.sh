#! /bin/bash

mkdir -p $PYTHONFORSMELOCATION/book/tmp
cd $PYTHONFORSMELOCATION/book/tmp

sh $PYTHONFORSMELOCATION/scripts/compile_tex.sh $PYTHONFORSMELOCATION/book/AnIntroductionToPythonForScienceMathAndEngineering

mv $PYTHONFORSMELOCATION/book/tmp/AnIntroductionToPythonForScienceMathAndEngineering.pdf $PYTHONFORSMELOCATION
