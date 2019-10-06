import librosa
import wave
import numpy as np
import matplotlib.pyplot as plt
import pyaudio

def sound_output(wav):
    chunk = 1024
    f = wave.open(wav,"rb")
    p = pyaudio.PyAudio()
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)
    print(f.getsampwidth())
    data = f.readframes(chunk)
    while data:
        stream.write(data)
        data = f.readframes(chunk)

    stream.stop_stream()
    stream.close()

    p.terminate()

def modulate_voice(wav, file_name):
    y, sr = librosa.load(wav, sr=16000)
    lnegth = len(y)
    y2 = y[:3]

    index = 4
    while 1:
        y2 = np.append(y2,y[index:index+3])
        index += 4
        if index >= lnegth:
            break

    librosa.output.write_wav(file_name+'.wav', y2, sr)


if __name__ == "__main__":
    wav = "sample_audio.wav"
    modulate_voice(wav,"Modulated_voice")
    #sound_output(wav)
