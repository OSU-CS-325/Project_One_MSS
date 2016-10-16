#!/bin/bash

rm final-report/final_report.ipynb 
python nbmerge.py report/header_page.ipynb enumeration/enumeration.ipynb better-enumeration/betterEnumeration.ipynb divide-and-conquer/divide_and_conquer.ipynb linear-time/linearTime.ipynb report/testing_writeup.ipynb > report/final_report.ipynb 
