#! /bin/bash

clean.sh $1

bibliofy.sh $1
glossify.sh $1
bibliofy.sh $1

