# simulated_device/test_missing.py

from run_device import read_firmware, run_firmware

def test_missing_file():
    # 传入一个不存在的固件文件名，触发 FileNotFoundError 分支
    firmware = read_firmware("non_existent_firmware.bin")
    run_firmware(firmware)

if __name__ == "__main__":
    test_missing_file()
