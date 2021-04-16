# Program Fungsi Numerik
import math
angka1 = int(input('Angka Pertama : '))
angka2 = int(input('Angka Kedua :'))
angka3 = int(input('Angka ketiga :'))

max = max(angka1,angka2,angka3)
print('Nilai terbesar dari ketiga angka tersebut adalah : ',max)

min = min(angka1,angka2,angka3)
print('\nNilai terkecil dari ketiga angka tersebut adalah : ',min)

akar = int(input('\nAngka yang ingin di akar : '))
print('Akar dari bilangan tersebut adalah : ',math.sqrt(akar))

import random
acak = range(0,int(input('Masukkan sampai angka keberapa Anda ingin mengacak')))
print('\nAngka yang Anda dapatkan adalah : ',random.choice(acak))
