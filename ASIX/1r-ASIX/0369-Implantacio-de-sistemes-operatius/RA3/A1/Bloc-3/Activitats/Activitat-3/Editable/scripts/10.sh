#!/bin/bash
suma(){ echo $(( $1 + $2 )); }
resta(){ echo $(( $1 - $2 )); }
mult(){ echo $(( $1 * $2 )); }
div(){ echo $(( $1 / $2 )); }

read -p "Valor 1: " a
read -p "Valor 2: " b

echo "Suma: $(suma $a $b)"
echo "Resta: $(resta $a $b)"
echo "Multiplicació: $(mult $a $b)"
echo "Divisió: $(div $a $b)"
