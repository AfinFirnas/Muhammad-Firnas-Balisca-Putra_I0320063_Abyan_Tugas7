# Program Fungsi String
Nama = str(input('Masukkan Nama Anda : '))
c = Nama.center(40,'-')
print(c)

a = Nama.count('a')
print('\nNama Anda memiliki huruf a sebanyak : ',a)

mulai = Nama.startswith(str(input('\nNama Anda dimulai dengan : ')))
print(mulai)

akhir = Nama.endswith(str(input('\nNama Anda diakhiri dengan : ')))
print(akhir)