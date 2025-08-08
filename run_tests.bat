@echo off
echo ==== Running JUnit Tests ====

REM Set the classpath, including test dependencies and compiled classes
set CLASSPATH=bin;lib\junit-4.13.2.jar;lib\hamcrest-core-1.3.jar

REM Execute tests
java -cp %CLASSPATH% org.junit.runner.JUnitCore MainTest

REM Check test result
if errorlevel 1 (
    echo Tests failed.
    exit /b 1
) else (
    echo All tests passed.
)
