#include "sensor.h"
#include <stdlib.h>
#include <time.h>

void init_sensor(void) {
    srand((unsigned) time(NULL));
}

uint16_t read_sensor(void) {
    return rand() % 1000;  // 模拟 0~999 范围的传感器值
}
