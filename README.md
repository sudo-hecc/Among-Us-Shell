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
- Optional audio support via [`pygame`](https://www.pygame.org/news) (for theme sound)

---

## Requirements

- Python 3.8+
- `rich`

Install dependencies:

```bash
pip3 install rich
