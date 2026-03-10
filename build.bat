@echo off
echo Building firmware...
make clean
make
if %errorlevel% neq 0 (
    echo Build failed!
    exit /b 1
)
echo Build success!