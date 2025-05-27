#!/bin/bash

# Check the operating system
if [[ "$OSTYPE" == "darwin"* ]]; then
  # macOS: Use mdfind to locate amog.py
  AMOG_PATH=$(mdfind -onlyin "$HOME" "kMDItemFSName == 'amog.py'" | head -n 1)
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
  # Linux: Use find to locate amog.py
  AMOG_PATH=$(find "$HOME" -name "amog.py" 2>/dev/null | head -n 1)
else
  echo "Error: Unsupported operating system."
  exit 1
fi

# Check if amog.py was found
if [ -z "$AMOG_PATH" ]; then
  echo "Error: amog.py not found in your home directory."
  exit 1
fi

# Check if Python 3 is installed
if ! command -v python3 &>/dev/null; then
  echo "Error: Python 3 is not installed. Please install it and try again."
  exit 1
fi

# Execute the script
echo "Running amog.py from: $AMOG_PATH"
python3 "$AMOG_PATH"