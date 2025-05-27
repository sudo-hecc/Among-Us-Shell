@echo off

REM Search for amog.py in the home directory
for /f "delims=" %%i in ('where /r "%USERPROFILE%" amog.py 2^>nul') do (
    set AMOG_PATH=%%i
    goto :FOUND
)

REM If amog.py is not found, display an error message
echo Error: amog.py not found in your home directory.
pause
exit /b

:FOUND
python "%AMOG_PATH%"