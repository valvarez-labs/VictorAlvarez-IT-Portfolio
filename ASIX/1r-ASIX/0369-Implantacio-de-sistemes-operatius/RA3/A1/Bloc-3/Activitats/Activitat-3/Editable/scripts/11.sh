#!/bin/bash
read -p "Caràcter: " c
if [[ $c =~ [a-zA-Z] ]]; then
  echo "És una lletra"
elif [[ $c =~ [0-9] ]]; then
  echo "És un número"
else
  echo "És un caràcter especial"
fi
