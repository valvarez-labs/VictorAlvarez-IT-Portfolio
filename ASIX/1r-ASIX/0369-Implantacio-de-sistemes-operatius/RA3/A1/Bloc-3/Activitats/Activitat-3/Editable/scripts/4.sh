#!/bin/bash
read -p "Directorio: " dir
if [ -d "$dir" ]; then
  echo "DIRECTORI JA EXISTEIX"
  ls -l "$dir"
else
  echo "DIRECTORI NO EXISTEIX"
  mkdir "$dir"
fi
