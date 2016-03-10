#!/bin/bash

while getopts fc opt;
do
  case $opt in
  	f)
	  t=$(( $2 * 9 / 5 + 32))
	  echo $t
      ;;
    c)
      t=$(( ($2 - 32) * 5 / 9))
      echo $t
      ;;
  esac
done