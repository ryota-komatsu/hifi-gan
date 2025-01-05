from pathlib import Path

import torchaudio
from tqdm import tqdm

wav_dir = Path("LJSpeech-1.1/wavs")
wav16k_dir = Path("LJSpeech-1.1/wavs16k")
wav16k_dir.mkdir(exist_ok=True)

with open("LJSpeech-1.1/metadata.csv") as f:
    lines = f.readlines()

for line in tqdm(lines):
    wav_name = line.split("|")[0]
    wav_path = wav_dir / (wav_name + ".wav")
    wav16k_path = wav16k_dir / (wav_name + ".wav")

    wav, sr = torchaudio.load(wav_path)
    wav = torchaudio.functional.resample(wav, sr, 16000)
    torchaudio.save(wav16k_path, wav, 16000)
