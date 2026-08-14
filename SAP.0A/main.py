import soundfile as sf
import sounddevice as sd
import os

from scipy.io.wavfile import write

choice = input("Seçiminiz: ")

if choice == "1":
    fs = 44100  # Sample rate
    seconds = 5  # Duration of recording

    print(sd.query_devices())
    print("Varsayılan giriş:", sd.default.device)
    device = int(input("Kayıt cihazını seçiniz: "))
    file_name = input("Kayıt dosyasının adını giriniz: ")
    myrecording = sd.rec(
        int(seconds * fs),
        samplerate=fs,
        channels=2,
        device=device
    )
    sd.wait()  # Wait until recording is finished
    write(f"{file_name}.wav", fs, myrecording)
    print("kayıt sona erdi.")
    file_size = os.path.getsize(f"{file_name}.wav")
    file_size_kb = int(file_size / 1024)
    print("Dosya boyutu:", file_size_kb, "KB.")




elif choice == "2":
    file_name = input("Dosya Adını giriniz:")

    try:
        data, fs = sf.read(file_name)
        sf.write('myfile.flac', data, fs)

    except:
        print("Dosya bulunamadı veya okunamadı.")

    duration = int(len(data) / fs)
    Minute = int(duration / 60)
    Second = duration % 60

    print("Dosyanız:", Minute, "dakika,", Second, "saniye.")

    file_size = os.path.getsize(file_name)
    file_size_kb = int(file_size / 1024)

    print("Dosya boyutu:", file_size_kb, "KB.")

elif choice == "3":
    quit()

else:
    print("Sadece 3 seçenek bulunmaktadır. Lütfen geçerli bir seçim yapınız.")
    quit()

