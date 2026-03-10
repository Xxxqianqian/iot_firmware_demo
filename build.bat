@echo off
echo ==== 正在全量编译工程 ====
if not exist bin mkdir bin

:: 1. 编译 src 目录下所有的业务代码
javac -d bin -cp "lib\junit-4.13.2.jar;lib\hamcrest-core-1.3.jar" src\*.java

:: 2. 编译 test 目录下的测试代码，并引用 bin 里的业务类
javac -d bin -cp "bin;lib\junit-4.13.2.jar;lib\hamcrest-core-1.3.jar" test\*.java

if %errorlevel% neq 0 (
    echo [ERROR] 编译失败，请检查源码依赖！
    exit /b 1
)
echo ==== 编译成功 ====