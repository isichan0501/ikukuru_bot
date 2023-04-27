@echo off

:: Anacondaの仮想環境を自動的に検出するためのスクリプト
:: https://stackoverflow.com/a/55727295
for /f "delims=" %%a in ('where anaconda') do set "ANACONDA=%%~dpa"
set "ANACONDA=%ANACONDA:\=/%"

call %ANACONDA%/Scripts/activate.bat py39
python myscript.py
call %ANACONDA%/Scripts/deactivate.bat
