#!/bin/bash

AMOG_PATH=$(mdfind -onlyin "$HOME" "kMDItemFSName == 'amog.py'" | head -n 1)

if [ -z "$AMOG_PATH" ]; then
  echo "Error: amog.py not found in your home directory."
  exit 1
fi

python3 "$AMOG_PATH"
