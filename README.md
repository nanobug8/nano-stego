# nano-stego
WAV Steganography Analyzer
Version 1.0 – Audio File Analysis

# Description
This Python script analyzes WAV audio files to detect possible steganographic messages hidden using LSB (Least Significant Bit) encoding. The tool is particularly useful for identifying HiddenWave-based steganography, as it checks for patterns that indicate hidden messages.


# How It Works
Extracts the least significant bits (LSB) from each byte of the audio file.
Reconstructs potential hidden messages from extracted bits.
Analyzes the message content, specifically looking for patterns (such as repeated # characters), which indicate HiddenWave steganography.
Reports whether steganography is detected based on the percentage of special characters.

# Installation & Requirements
Python 3.x
Standard Python libraries (os, wave, argparse)

Follow these steps to clone, set up, and run nano-stego on your system:
  git clone https://github.com/nanobug8/nano-stego
  cd nano-stego
 
# Usage
To analyze a WAV file, run:
  python stegoanalyzer.py -f <path_to_wav_file>
Example:
  python stegoanalyzer.py -f secret_audio.wav
If steganography is detected, the script will report the number of suspicious characters and the probability of hidden data.

# Features
✔️ Automated Analysis – Extracts and decodes possible messages.
✔️ Pattern Detection – Identifies steganographic artifacts (e.g., excessive # characters).
✔️ HiddenWave Signature Check – Helps detect steganography based on known encoding methods.
✔️ Lightweight & Fast – Runs quickly with minimal dependencies.

Author
Developed by nanobug8/nano_bit

## References
This tool is inspired by and builds upon research from other steganography tools:

- HiddenWave: [techchipnet/HiddenWave](https://github.com/techchipnet/HiddenWave)
