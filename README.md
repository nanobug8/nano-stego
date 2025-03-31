# nano-stego<br>
WAV Steganography Analyzer<br>
Version 1.0 – Audio File Analysis<br>

# Description<br>
This Python script analyzes WAV audio files to detect possible steganographic messages hidden using LSB (Least Significant Bit) encoding. The tool is particularly useful for identifying HiddenWave-based steganography, as it checks for patterns that indicate hidden messages.<br>


# How It Works<br>
Extracts the least significant bits (LSB) from each byte of the audio file.<br>
Reconstructs potential hidden messages from extracted bits.<br>
Analyzes the message content, specifically looking for patterns (such as repeated # characters), which indicate HiddenWave steganography.<br>
Reports whether steganography is detected based on the percentage of special characters.<br>
<br>
# Installation & Requirements<br>
Python 3.x<br>
Standard Python libraries (os, wave, argparse)<br>
<br>
<br>
Follow these steps to clone, set up, and run nano-stego on your system:<br>
  git clone https://github.com/nanobug8/nano-stego<br>
  cd nano-stego<br>
 <br>
# Usage<br>
To analyze a WAV file, run:<br>
  python stegoanalyzer.py -f <path_to_wav_file><br>
Example:<br>
  python stegoanalyzer.py -f secret_audio.wav<br>
If steganography is detected, the script will report the number of suspicious characters and the probability of hidden data.<br>
<br>
# Features<br>
✔️ Automated Analysis – Extracts and decodes possible messages.<br>
✔️ Pattern Detection – Identifies steganographic artifacts (e.g., excessive # characters).<br>
✔️ HiddenWave Signature Check – Helps detect steganography based on known encoding methods.<br>
✔️ Lightweight & Fast – Runs quickly with minimal dependencies.<br>

Author<br>
Developed by nanobug8/nano_bit<br>

## References<br>
This tool is inspired by and builds upon research from other steganography tools:<br>

- HiddenWave: [techchipnet/HiddenWave](https://github.com/techchipnet/HiddenWave)<br>
