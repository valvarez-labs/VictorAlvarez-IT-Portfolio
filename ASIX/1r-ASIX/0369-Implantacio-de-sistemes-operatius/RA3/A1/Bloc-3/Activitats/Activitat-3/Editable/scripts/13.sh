#!/bin/bash
read -p "Fitxer: " f
if [ ! -e "$f" ]; then
  echo "FITXER NO EXISTENT"
elif [ ! -s "$f" ]; then
  echo "FITXER BUIT"
else
  cat "$f"
fi
