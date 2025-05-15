# Among-Us Shell

A custom terminal interface written in Python, designed to simulate a minimal command-line shell environment with themed responses and core command support. Developed as a learning project by [Eesa Ayub (sudo-hecc)](https://github.com/sudo-hecc), this shell features dynamic command execution, path navigation, and a themed startup experience.

---

## Features

- Command-line interface written in Python
- Role assignment (Imposter or Crewmate) for contextual prompts
- Runs standard shell commands using `os.system()`
- Recognizes and handles:
  - `cd` (with tilde `~` expansion)
  - `clear`
  - `exit`
  - `neofetch` (custom ASCII output)
  - Custom `impo rm -rf <target>` syntax for educational simulation
- Displays working directory in the prompt
- Uses [`rich`](https://github.com/Textualize/rich) for styled terminal output

---

## Requirements

- Python 3.8+
- `rich`
- A `themetune.mp3` file or `pygame` error may show. It can be found at https://tuna.voicemod.net/sound/24225899-3086-47e3-a873-1464e84586cf. Rename to `themetune.mp3`

Install dependencies:

```bash
pip3 install rich
```

## Note
It has been made primarily for Mac OS (using Unix terminals) so errors may occur on any other OS.
