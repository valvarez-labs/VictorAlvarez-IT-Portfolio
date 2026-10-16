#!/bin/bash
read -p "Nom d'usuari: " user

for i in 1 2; do
  read -s -p "Password: " p1; echo
  read -s -p "Repeteix password: " p2; echo
  if [ "$p1" == "$p2" ]; then
    echo "Hola $user benvingut a ...."
    exit 0
  else
    echo "Passwords no coincideixen"
  fi
done

echo "Error: no coincideixen dues vegades"
