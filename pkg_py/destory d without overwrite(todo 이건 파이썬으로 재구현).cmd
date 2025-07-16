 
set initial_position=%cd%
REM c:
REM d:
REM e:
REM f:

mkdir "`"
cd "`"
for /r %%i in (*.*) do move "%%i" "%initial_position%"


cd ..
for /f "usebackq delims=" %%i in (`"dir /s /b /ad | sort /r"`) do rd "%%i" 2>NUL 
 