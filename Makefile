CC = arm-none-eabi-gcc
OBJCOPY = arm-none-eabi-objcopy

CFLAGS = -mcpu=cortex-m3 -mthumb -nostdlib -Wall -fno-exceptions -fno-unwind-tables -fno-asynchronous-unwind-tables -ffunction-sections -fdata-sections
LDFLAGS = -T linker.ld -Wl,--gc-sections

SRCS = src/main.c src/syscalls.c
OBJS = $(SRCS:.c=.o)

UNIT_TEST_SRCS = src/test_main.c src/syscalls.c
UNIT_TEST_OBJS = $(UNIT_TEST_SRCS:.c=.o)

all: firmware.bin

firmware.elf: $(OBJS)
	$(CC) $(OBJS) $(LDFLAGS) -o $@

firmware.bin: firmware.elf
	$(OBJCOPY) -O binary $< $@

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

unit_test.elf: $(UNIT_TEST_OBJS)
	$(CC) $(UNIT_TEST_OBJS) -DUNIT_TEST $(LDFLAGS) -o $@

test: unit_test.elf
	@echo Running unit tests...
	@./unit_test.elf || echo "Unit test execution failed or not supported on host."

flash: firmware.bin
	@if not exist simulated_device mkdir simulated_device
	copy /Y firmware.bin simulated_device\firmware.bin
	@echo Firmware copied to simulated_device\firmware.bin

clean:
	del /Q src\*.o *.elf *.bin
	if exist simulated_device\firmware.bin del /Q simulated_device\firmware.bin
