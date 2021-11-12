Daftar_Kontak = {'Nama':['Fawwaz','John'],
                 'Nomor':['0818880521','0818880297']
}

x = 0

print('Selamat datang!')
print('--- Menu --- ')
print('1. Daftar Kontak ')
print('2. Tambah Kontak' )
print('3. Keluar')

Nomor_Menu = int(input(f'Masukkan nomor menu yang ingin dipilih: '))

if Nomor_Menu == 1:
    for y in Daftar_Kontak:
        print(f"Nama : {Daftar_Kontak['Nama'][x]}")
        print(f"Nomor: {Daftar_Kontak['Nomor'][x]}")
        x+=1

elif Nomor_Menu == 2:
    Daftar_Kontak['Nama'].append(input('Nama Kontak: '))
    Daftar_Kontak['Nomor'].append(input('Nomor Telepon: '))
    print('Kontak berhasil ditambahkan')

elif Nomor_Menu == 3:
    print('Program selesai, sampai jumpa!')
    
else:
    print('Menu tidak tersedia ')
