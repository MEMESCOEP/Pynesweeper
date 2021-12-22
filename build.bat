@echo off
color 0a
cls

SET STARTTIME=%TIME%
echo Build started at    : %STARTTIME%

if "%1%"=="-debug" goto buildDebug
if "%2%"=="-debug" goto buildDebug

:buildNormal
echo Building...
pyinstaller --onefile --noconsole --debug=all pynesweeper.py
if "%ERRORLEVEL%" NEQ "0" goto buildError
echo Done.
goto Done

:buildDebug
echo Building (DEBUG MODE)...
pyinstaller --onefile --debug=all pynesweeper.py
if "%ERRORLEVEL%" NEQ "0" goto buildError
echo Moving...
move /Y .\dist\pynesweeper.exe .\pynesweeper-debug.exe
echo Done.
echo Done.
goto Done



:Done
echo Moving...
move /Y .\dist\pynesweeper.exe .\pynesweeper.exe
echo Done.



echo.

set ENDTIME=%TIME%


rem Change formatting for the start and end times
    for /F "tokens=1-4 delims=:.," %%a in ("%STARTTIME%") do (
       set /A "start=(((%%a*60)+1%%b %% 100)*60+1%%c %% 100)*100+1%%d %% 100"
    )

    for /F "tokens=1-4 delims=:.," %%a in ("%ENDTIME%") do ( 
       IF %ENDTIME% GTR %STARTTIME% set /A "end=(((%%a*60)+1%%b %% 100)*60+1%%c %% 100)*100+1%%d %% 100" 
       IF %ENDTIME% LSS %STARTTIME% set /A "end=((((%%a+24)*60)+1%%b %% 100)*60+1%%c %% 100)*100+1%%d %% 100" 
    )

    rem Calculate the elapsed time by subtracting values
    set /A elapsed=end-start

    rem Format the results for output
    set /A hh=elapsed/(60*60*100), rest=elapsed%%(60*60*100), mm=rest/(60*100), rest%%=60*100, ss=rest/100, cc=rest%%100
    if %hh% lss 10 set hh=0%hh%
    if %mm% lss 10 set mm=0%mm%
    if %ss% lss 10 set ss=0%ss%
    if %cc% lss 10 set cc=0%cc%

    set DURATION=%hh%:%mm%:%ss%.%cc%
    echo Build started at    : %STARTTIME%
    echo Build finished at   : %ENDTIME%

    echo Build took %DURATION%

echo.
echo.
echo Finished.
timeout 5 > NUL
goto EOF

rem Measure-Command { .\build.bat }




:buildError
color 04
echo.

set ENDTIME=%TIME%


rem Change formatting for the start and end times
    for /F "tokens=1-4 delims=:.," %%a in ("%STARTTIME%") do (
       set /A "start=(((%%a*60)+1%%b %% 100)*60+1%%c %% 100)*100+1%%d %% 100"
    )

    for /F "tokens=1-4 delims=:.," %%a in ("%ENDTIME%") do ( 
       IF %ENDTIME% GTR %STARTTIME% set /A "end=(((%%a*60)+1%%b %% 100)*60+1%%c %% 100)*100+1%%d %% 100" 
       IF %ENDTIME% LSS %STARTTIME% set /A "end=((((%%a+24)*60)+1%%b %% 100)*60+1%%c %% 100)*100+1%%d %% 100" 
    )

    rem Calculate the elapsed time by subtracting values
    set /A elapsed=end-start

    rem Format the results for output
    set /A hh=elapsed/(60*60*100), rest=elapsed%%(60*60*100), mm=rest/(60*100), rest%%=60*100, ss=rest/100, cc=rest%%100
    if %hh% lss 10 set hh=0%hh%
    if %mm% lss 10 set mm=0%mm%
    if %ss% lss 10 set ss=0%ss%
    if %cc% lss 10 set cc=0%cc%

    set DURATION=%hh%:%mm%:%ss%.%cc%
    echo Build started at    : %STARTTIME%
    echo Build failed at   : %ENDTIME%

    echo Total build time   : %DURATION%

echo.
echo.
echo Build Failed.
pause
color 0a
goto EOF2

:runFile
start "" pynesweeper.exe
goto EOF2

:runFileDBG
start "" pynesweeper.exe -debug
goto EOF2




:EOF
if "%1%"=="-run" goto runFile
if "%2%"=="-run" goto runFile
if "%1%"=="-rundebug" goto runFileDBG
if "%2%"=="-rundebug" goto runFileDBG


rem End Of File
:EOF2
