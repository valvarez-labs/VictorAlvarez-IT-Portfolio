#!/bin/bash
if [ $# -ne 2 ]; then
  echo "Uso: $0 num1 num2"
  exit 1
fi
echo "Suma: $(($1+$2))"
