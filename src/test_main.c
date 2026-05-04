#include <stdio.h>
#include <stdlib.h>

// 声明要测试的函数
int add(int a, int b);

int main() {
    int result = add(2, 3);
    if (result == 5) {
        printf("add() test passed.\n");
        return 0;  // 0表示测试通过
    } else {
        printf("add() test failed: expected 5, got %d\n", result);
        return 1;  // 非0表示测试失败
    }
}
