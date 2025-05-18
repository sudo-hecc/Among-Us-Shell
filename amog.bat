@echo off
REM Define the home directory
set HOME_DIR=%USERPROFILE%

REM Search for amog.py starting from the home directory
for /r "%HOME_DIR%" %%i in (amog.py) do (
    python "%%i"
    goto :EOF
)

REM If amog.py is not found, display an error message
echo amog.py not found in the home directory or its subdirectories.
pause