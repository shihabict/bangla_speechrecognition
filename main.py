from bangla_tts import generate

# usage 1 (saving to path)

file_names = generate(["আমার সোনার বাংলা আমি তোমাকে ভালোবাসি"], save_path = "static") # will be saved to static folder
print(file_names)

# usage 2 (getting numpy arrays for the signals)

gen_wavs = generate(["আমার সোনার বাংলা আমি তোমাকে ভালোবাসি"]) # will return an array containing the speech and sampling rate
print(gen_wavs[0])
print(f"signal length: {gen_wavs[0][0].shape}")
print(f"samplign rate: {gen_wavs[0][1]}")