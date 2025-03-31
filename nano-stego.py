import os
import wave
import argparse

# Función para mostrar el banner
def banner():
    print(r'''
                                        _______________________________ ________ ________   
  ____ _____    ____   ____            /   _____/\__    ___/\_   _____//  _____/ \_____  \  
 /    \\__  \  /    \ /  _ \   ______  \_____  \   |    |    |    __)_/   \  ___  /   |   \ 
|   |  \/ __ \|   |  (  <_> ) /_____/  /        \  |    |    |        \    \_\  \/    |    \
|___|  (____  /___|  /\____/          /_______  /  |____|   /_______  /\______  /\_______  /
     \/     \/     \/                         \/                    \/        \/         \/ 
                                                                                      
          Esteganografía en WAV 
          v1.0 - Análisis de archivo de audio
          nanobug8/nano_bit
    ''')

# Función para detectar esteganografía en un archivo WAV
def detect_stego(wav_file):
    with wave.open(wav_file, mode='rb') as waveaudio:
        frame_bytes = bytearray(list(waveaudio.readframes(waveaudio.getnframes())))

    # Extraer los LSB 
    extracted_bits = [str(byte & 1) for byte in frame_bytes]
    
    # Agrupar en bloques de 8 bits y convertirlos en caracteres ASCII
    # bits = [''.join(map(str, bits[i:i+8])) for i in range(0, len(bits), 8)]     
    extracted_message = ''.join(chr(int(''.join(extracted_bits[i:i+8]), 2)) 
                                for i in range(0, len(extracted_bits), 8))

    # Mostrar el mensaje extraído
    print(extracted_message)

    # Como vimos en el codigo de la herramienta HiddenWave, cuando realiza stego, completa los bloques de 8 bytes
    # con el caracter "hash" al final de cada byte, por lo que para controlar si fue utiliza esta herramienta una solucion
    # es contar la cantidad de '#'
    hash_count = extracted_message.count('#')
    message_length = len(extracted_message)

    # Si hay un porcentaje alto de '#', hay alta probabilidad de esteganografía

    if message_length > 0 and hash_count / message_length > 0.5: 
        print(f"Posible esteganografía detectada en {wav_file}: {hash_count} '#' encontrados.")
    else:
        print("No se detectó esteganografía en: ",wav_file)

# Codigo reutilizado de HiddenWave
def help():
    print("\033[92mAnaliza un archivo WAV en busca de esteganografía.\033[0m")
    print('''usage: stegoanalyzer.py [-h] [-f AUDIO_PATH]

optional arguments:
  -h, --help    show this help message and exit
  -f AUDIO_PATH  Cargue un archivo de audio wav''')

def main():
    banner()
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', help='Cargue un archivo de audio wav', dest='audiopath')
    args = parser.parse_args()
    wav_file = args.audiopath

    if not wav_file:
        help()
        return

    print("Por favor, espere...")
    detect_stego(wav_file)

if __name__ == '__main__':
    main()
