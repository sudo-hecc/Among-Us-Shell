# Among-Us Shell — User Manual

Welcome! This guide will help you get started with **Among-Us Shell**, a simple Python command-line shell.

---

## Features

- Colorful and user-friendly command-line interface  
- Basic shell commands like `ls`, `cd`, `help`, and `exit`  
- Custom prompt showing your current directory  
- Built with Python using `rich` for styling and `pygame` for additional features  
- Lightweight and easy to run on any system with Python 3.13+  
- Designed for learning and experimentation 

---

## 1. Requirements

- Python 3.13 or newer installed  
- Python packages: [`rich`](https://github.com/Textualize/rich), [`pygame`](https://github.com/pygame/pygame) and [`readline`](https://github.com/ludwigschwardt/python-gnureadline?tab=readme-ov-file)
- A [`themetune.mp3`](https://tuna.voicemod.net/sound/24225899-3086-47e3-a873-1464e84586cf)

---

## 2. Installing Dependencies

Open your terminal and install the required Python packages by running:

```bash
pip3 install -r requirements.txt
```

---

## List of custom made commands

- `venv` - creates a virtual envoirnment and activates it.
- `python3` and `pip3` are shortened to `python` and `pip`.
- `impo rm -rf <target>` - if you are imposter, the terminal prints `<target> has been deleted`.
- `impo kill <target>` - sabotages a process e.g. `impo kill O2` returns `O2 has been sabotaged`.
- `clr` or `clear` - clears the terminal.
- `exit` launches into your default terminal such as `zsh` and displays a message based on your role.
- On start, you have a 50/50 chance of being imposter or crew mate.
- Uses `pygame` to play Among Us theme tune.
- Uses `rich` for styling text in the terminal

### Note:
If you are on Windows, using Powershell is recommended for the ASCII escape codes used by [`rich`](https://github.com/Textualize/rich)
