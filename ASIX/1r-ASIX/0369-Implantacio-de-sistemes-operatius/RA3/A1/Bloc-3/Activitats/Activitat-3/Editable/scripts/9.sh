#!/bin/bash
echo "1) ps"
echo "2) free"
echo "3) top"
read -p "Selecciona: " op
case $op in
 1) ps ;;
 2) free ;;
 3) top ;;
 *) echo "Opció no vàlida" ;;
esac
