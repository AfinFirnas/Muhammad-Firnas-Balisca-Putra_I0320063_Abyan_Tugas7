def panggil(func):
    return func
def helloworld():
    return 'HELLO WORLD'
def main():
    daftarnama = ['Adit,Adi,Cinta,Budi']
    print('Keadaan Awal')
    print(daftarnama)

    print('\n menggunakan sorted():')
    print(sorted(daftarnama))

    daftarnama.sort(key=lambda n: n.lower())

    print('\nkeadaan akhir:')
    print(daftarnama)
main()
