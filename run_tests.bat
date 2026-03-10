@echo off
echo ==== 正在诊断环境与路径 ====
:: 打印当前路径
cd
:: 查找 MainTest.class 的位置
dir /s /b MainTest.class

echo ==== 正在运行测试 ====
set CLASSPATH=.;bin;lib\junit-4.13.2.jar;lib\hamcrest-core-1.3.jar
java -cp "%CLASSPATH%" org.junit.runner.JUnitCore MainTest

if errorlevel 1 (
    echo [ERROR] 测试失败，请查看上面的目录诊断结果。
    exit /b 1
) else (
    echo All tests passed.
)