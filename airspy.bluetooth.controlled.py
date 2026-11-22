
import subprocess
from pathlib import Path
import os
import serial
from datetime import datetime

BT_PORT = "COM3"
BAUD_RATE = 9600

# see parameters at:  https://github.com/josevcm/nfc-laboratory#deviceradioairspy--airspy-mini--r2
FREQUENCY_HZ = 40.68
SAMPLE_RATE_HZ = 10000000

output = "yyyy.mm.dd__hh.mm.ss__capture.raw"
AIRSPY_TOOLS_DIR = Path(r"C:\Airspy")
INFO = AIRSPY_TOOLS_DIR / "airspy_info.exe"
RX = AIRSPY_TOOLS_DIR / "airspy_rx.exe"

def run_command(args):
    result = subprocess.run(
        [str(x) for x in args],
        cwd=str(AIRSPY_TOOLS_DIR),
        text=True,
        capture_output=True,
        timeout=30,
    )
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    if result.returncode != 0:
        raise RuntimeError(
            f"Command failed with code {result.returncode}"
        )

def detect_airspy_device():
    run_command([INFO])

if __name__ == "__main__":
    detect_airspy_device()
    print(f"Listening for Bluetooth commands on {BT_PORT}...")

    with serial.Serial(BT_PORT, BAUD_RATE, timeout=1) as bt:

        output_file_counter = 0
        while True:
            if bt.in_waiting == 0: continue
            command = bt.readline().decode('utf-8').strip().lower()

            if command == 'start':
                output_file_counter += 1
                current_datetime_str = datetime.now().strftime("%Y.%m.%d__%H.%M.%S")
                output = current_datetime_str + output[20:]

                cmd = [
                    RX,
                    "-f", str(FREQUENCY_HZ),
                    "-a", str(SAMPLE_RATE_HZ),
                    "-r", str(output),
                ]

                with open("airspy_log.txt", "w", encoding="utf-8") as log:
                    process = subprocess.Popen(
                        [str(x) for x in cmd],
                        cwd=str(AIRSPY_TOOLS_DIR),
                        stdout=log,
                        stderr=subprocess.STDOUT,
                        text=True,
                    )
                bt.write(b'Recording...\n')
                print('\nStarted IQ recording {}: {}'.format(output_file_counter, " ".join(map(str, cmd))))

            elif command == 'stop':
                process.terminate()
                bt.write(b'Stopped recording\n')
                print('Stopped IQ recording')
            elif command == 'shutdown':
                process.kill()
                bt.write(b'Killing process...\n')
                bt.write(b'Shutting down...\n')
                print('\nShutting down...')
                os.system('shutdown /s /t 1')
                