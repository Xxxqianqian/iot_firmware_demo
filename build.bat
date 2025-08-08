@echo off
echo ==== Start compiling Java project ====

:: Create bin folder if not exists
if not exist bin (
    mkdir bin
)

:: Compile all Java files in src
for /r src %%f in (*.java) do (
    echo Compiling: %%f
    javac -d bin "%%f"
    if %errorlevel% neq 0 (
        echo Compilation failed!
        exit /b 1
    )
)

echo ==== Compilation finished ====

:: Simulate firmware output
echo This is a firmware file. > bin\firmware.bin
