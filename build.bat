@echo off
echo
if not exist bin mkdir bin

javac -d bin src\*.java

echo
javac -d bin -cp "bin;lib\junit-4.13.2.jar;lib\hamcrest-core-1.3.jar" test\MainTest.java

echo