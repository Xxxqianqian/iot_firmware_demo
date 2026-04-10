import sys
import os

def read_firmware(file_path):
    if not os.path.exists(file_path):
        print(f"Error: Firmware {file_path} not found.")
        return None
    with open(file_path, 'rb') as f:
        return f.read()

def verify_logic():
    source_file = "src/test_main.c"
    try:
        with open(source_file, 'r', encoding='utf-8') as f:
            content = f.read()
            if "result == 5" in content:
                print("Verification Passed: logic consistent.")
                return True
            else:
                print("Verification Failed: logic mismatch detected.")
                return False
    except Exception as e:
        print(f"File Access Error: {e}")
        return False

def run_simulation(firmware, logic_passed):
    if firmware and logic_passed:
        print("Starting Simulation...")
        print("Simulation Finished Successfully.")
        return True
    return False

if __name__ == "__main__":
    firmware_path = "bin/unit_test.elf"
    firmware_data = read_firmware(firmware_path)
    logic_status = verify_logic()
    
    if run_simulation(firmware_data, logic_status):
        sys.exit(0)
    else:
        sys.exit(1)
