// main.c - 模拟物联网固件主程序
#include <stdio.h>
#include <stdint.h>
#include "sensor.h"

int main(void) {
   
    printf("设备启动...\n");

    
    init_sensor();

   
    for (int i = 0; i < 5; i++) {
        uint16_t value = read_sensor();
        printf("第 %d 次读取，传感器值为: %d\n", i + 1, value);
    }

    printf("固件运行完成，准备关机...\n");
    return 0;
}
