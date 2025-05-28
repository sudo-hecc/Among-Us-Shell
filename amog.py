import sys
import readline
from rich import print
from rich.console import Console
import random
import os
import pygame

#====CLEAR IMMEDIANTLY====
os.system("cls" if os.name == "nt" else "printf '\033c'")

try:
    pygame.init()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    theme_path = os.path.join(script_dir, "themetune.mp3")
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
    pygame.mixer.music.load(theme_path)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1.0)  # Set volume to maximum (1.0)
except pygame.error as e:
    print(f"[red]Error loading theme tune: {e}[/red]")
    print("[red]Make sure the 'themetune.mp3' file is in the same directory as this script.[/red]")

sys.stdout.write("\033]0;SUSSY SHELL\a")
sys.stdout.flush()

console = Console()
console.print("[blue]Welcome to SUSSY SHELL[/blue]")

role = random.choice(["imposter", "crewmate"])
if role == "imposter":
    console.print("[red]You are the Imposter. Kill everyone[/red]")
else:
    console.print("[green]You are a Crewmate. Find the imposter[/green]")

def main():
    global role
    while True:
        try:
            user_input = console.input(f"[blue]{os.getcwd()} TASK: [/blue]")

            if user_input == "exit":
                if role == "imposter":
                    console.print("[red]Crewmate wins! (imposter left game)[/red]")
                else:
                    console.print("[green]Exiting... Your crewmates shall find that imposter[/green]")
                sys.exit()

            elif user_input == "clear" or user_input == "clr":
                os.system("cls" if os.name == "nt" else "printf '\033c'")

            elif user_input == "neofetch":
                console.print("""[red]
                    ⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣯⢎⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⣈⣼⣿⠿⠳⠳⠳⠳⠣⠀⢄⠀⠀⠀
                    ⠀⠀⠀⣨⣿⣿⣿⣿⣿⣯⣮⣮⣮⣾⠇⠀⠀⠀
                    ⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠀⠀⠀⠀
                    ⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀
                    ⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
                    ⠀⠀⣰⣿⣿⣿⡿⠓⠑⠱⣷⣿⣿⣿⠌⠀⠀⠀
                    ⠀⠀⣿⣿⣿⣿⡇⠀⠀⠀⠀⢹⣿⣿⣷⠀⠀⠀
                    created by [bold red]EESA AYUB (sudo-hecc on github)
                    as an Amongus themed terminal. DON'T BE SUS[/bold red]
                [/red]""")

            elif user_input == "":
                continue

            elif user_input.startswith("impo rm -rf"):
                if role == "imposter":
                    if user_input[12:].lower() == "red":
                        console.print("[bold red]AYO! YOU'RE RED! WHY ARE YOU TRYING TO DELETE YOURSELF?![/bold red]")
                    else:
                        console.print(f"[bold red]{user_input[12:].upper()} has been deleted[/bold red]")
                else:
                    console.print(f"[bold red]AYO THAT SUS! WHY ARE YOU TRYING TO DELETE {user_input[12:].upper()}?![/bold red]")
            
            elif user_input == "venv":
                os.system("python3 -m venv venv; source venv/bin/activate" if os.name != "nt" else r"python -m venv venv; venv\Scripts\activate.bat")
            
            elif "python" in user_input:
                output = "python3 " + user_input[8:] if os.name != "nt" else "python " + user_input[7:]
                os.system(output)

            elif "pip" in user_input:
                output = "pip3 " + user_input[4:] if os.name != "nt" else "pip " + user_input[4:]
                os.system(output)

            elif user_input.startswith("impo kill"):
                if role == "imposter":
                    console.print(f"[bold red]{user_input[10:].upper()} has been sabotaged[/bold red]")
                else:
                    console.print(f"[bold red]AYO THAT SUS! WHY ARE YOU TRYING TO SABOTAGE {user_input[10:].upper()}?![/bold red]")

            elif user_input == "switch":
                os.system("printf '\033c'")
                if role == "imposter":
                    console.print("[green]You are now a Crewmate. Find the imposter[/green]")
                    role = "crewmate"
                else:
                    console.print("[red]You are now the Imposter. Kill everyone[/red]")
                    role = "imposter"
            
            else:
                try:
                    if user_input.startswith("cd "):
                        path = os.path.expanduser("~")
                        if user_input[3:].startswith("~/"):
                            path = os.path.join(path, user_input[5:])
                        else:
                            path = user_input[3:]
                        try:
                            os.chdir(path)
                        except FileNotFoundError:
                            console.print(f"[red]SUSSY SHELL: No such folder: {path}[/red]")
                        except NotADirectoryError:
                            console.print(f"[red]SUSSY SHELL: Not a directory: {path}[/red]")
                        except PermissionError:
                            console.print(f"[red]SUSSY SHELL: Permission denied for: {path}[/red]")
                    else:
                        os.system(user_input)
                except Exception as e:
                    console.print(f"[red]SUSSY SHELL: {e}[/red]")

        except KeyboardInterrupt:
            if role == "imposter":
                console.print("[red]Crewmate wins! (imposter left game)[/red]")
            else:
                console.print("[green]Exiting... Your crewmates shall find that imposter[/green]")
            sys.exit()

if __name__ == "__main__":
    main()
