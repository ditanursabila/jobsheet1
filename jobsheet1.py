import random
from guess import tebakAngka

tebak = tebakAngka()
tebak.jawaban = random.randint(1,10)
tebak.tebakan = int(input("tebak angka dari 1 s.d 10: "))

if tebak.cek():
    print("Jawaban kamu benar!")
else:
    print("Jawaban kamu salah!")
