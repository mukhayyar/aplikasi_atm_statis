from random import randint
from datetime import datetime
import getpass
from customers import Customers

atm = Customers(3214, 10000)

while True:
    id = int(getpass.getpass('Masukkan pin anda.....'))
    trial = 0

    while id == 'abcdefghijklmnopqrstuvwxyz' and 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        print('Pin yang anda masukkan salah, sisa percobaan '+ str(3 - trial)+' x')
        id = int(getpass.getpass('Masukkan pin anda.....'))

        trial += 1

        if trial == 3:
            print('Error')
            exit()

    while id != atm.checkPin() and trial < 3:
        print('Pin yang anda masukkan salah, sisa percobaan '+ str(3 - trial)+' x')
        id = int(getpass.getpass('Masukkan pin anda.....'))

        trial += 1

        if trial == 3:
            print('Error')
            exit()

    while id == atm.checkPin():
        print('Selamat Datang')
        print(datetime.now())
        print('1. Cek Saldo')
        print('2. Debet')
        print('3. Deposit')
        print('4. Ganti Pin')
        print('5. Exit')
        
        pil = int(input('Masukkan pilihan anda: '))

        while pil == 1:
            print('Saldo Anda: '+str(atm.checkBalance()))
            break

        while pil == 2:
            print('Saldo Anda: '+str(atm.checkBalance()))
            nominal = int(input('Sebutkan nominal yang ingin anda ambil: '))
            if nominal > atm.checkBalance():
                print('Saldo tidak mencukupi!')
            print('Saldo berhasil ditarik!')
            print('Sisa saldo anda adalah '+str(atm.debet_saldo(nominal)))
            print('Resi anda:'+str(randint(1,100000))+str(datetime.now()))
            break

        while pil == 3:
            print('Saldo Anda: '+str(atm.checkBalance()))
            nominal = int(input('Berapa nominal saldo yang ingin ditambah: '))
            print('Deposit berhasil!')
            print('Sisa saldo anda adalah '+str(atm.simpan_saldo(nominal)))
            print('Resi anda:'+str(randint(1,100000))+str(datetime.now()))
            break

        while pil == 4:
            print('Pin anda sebelumnya: '+str(atm.checkPin()))
            pin = int(input('Masukkan pin terbaru: '))
            print('Pin berhasil diganti')
            break

        while pil == 5:
            print('Sampai jumpa kembali')
            print('Resi anda:'+str(randint(1,100000))+'-'+str(datetime.now()))
            exit()