@echo off
echo ==== Running JUnit Tests ====

REM
set CLASSPATH=.;bin;lib\junit-4.13.2.jar;lib\hamcrest-core-1.3.jar

REM
java -cp "%CLASSPATH%" org.junit.runner.JUnitCore MainTest

REM
if errorlevel 1 (
    echo Tests failed.
    exit /b 1
) else (
    echo All tests passed.
)