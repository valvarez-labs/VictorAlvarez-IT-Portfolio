#!/bin/bash
if [ $# -ne 2 ]; then
  echo "Has de passar 2 paràmetres"
  exit 1
fi

old=$1
new=$2

if [ ! -e "$old" ]; then
  echo "L'arxiu original no existeix"
  exit 1
fi

if [ -e "$new" ]; then
  echo "El nou nom ja existeix"
  exit 1
fi

mv "$old" "$new"
