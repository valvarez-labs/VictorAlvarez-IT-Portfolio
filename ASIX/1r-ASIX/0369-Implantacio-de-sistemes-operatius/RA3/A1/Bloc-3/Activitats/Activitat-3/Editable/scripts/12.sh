#!/bin/bash
read -p "Número: " n
for i in $(seq 10); do
  echo "$n x $i = $((n*i))"
done
