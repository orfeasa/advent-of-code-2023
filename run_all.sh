#!/bin/bash

for day in {01..25}
do
    PYFILE="./day_$day/main.py"
    if [[ -f "$PYFILE" ]]; then
        echo "#### Day $day ####"
        if command -v python3.10 &>/dev/null; then
            python3.10 "$PYFILE" && printf "\n"
        else
            echo "Error: Python 3.10 is not installed."
        fi
    fi
done
