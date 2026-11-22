
import wave
import argparse

# to run:
# py raw.to.wav.py input.raw output.wav

parser = argparse.ArgumentParser()
parser.add_argument('raw_filename')
parser.add_argument('output_filename')
args = parser.parse_args()

# raw_file = "capture.raw"
raw_file = args.raw_filename
# wav_file = "output.wav"
wav_file = args.output_filename

# airspy mini, nfc-a: sample rate = 10000000, stereo, 16-bit
sample_rate = 10000000   # Hz
channels = 2          # 1 = mono, 2 = stereo
sample_width = 2      # 2 = 16-bit, 1 = 8-bit, 4 = 32-bit

with open(raw_file, "rb") as f:
    raw_data = f.read()

with wave.open(wav_file, "wb") as wav:
    wav.setnchannels(channels)
    wav.setsampwidth(sample_width)
    wav.setframerate(sample_rate)
    wav.writeframes(raw_data)

print(f"\nConverted {raw_file} to {wav_file}")
