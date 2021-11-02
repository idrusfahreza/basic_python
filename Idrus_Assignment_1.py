# Question 1: 
# Buatlah sebuah program yang menerima 3 input dari user. 
# Input tersebut berupa:
# 1. Nama bertipe data string
# 2. Umur bertipe data integer
# 3. Tinggi bertipe data float 

# Lalu tampilkan ke layar dengan format:
# Nama saya [Nama], umur saya [Umur] tahun dan tinggi saya [Tinggi] cm.


Nama = input("Siapa nama anda?")
Umur = input("Berapa umur anda?")
Tinggi = input("Berapa tinggi badan anda?")

print(f"Nama saya {Nama}, umur saya {Umur} tahun dan tinggi saya {Tinggi} cm.")


# Quetion 2:
# Buatlah sebuah program yang dapat menghitung luas lingkaran.
# Program meminta input dari user berupa angka sebagai jari-jari lingkaran.
# Program menghitung luas lingkaran dengan rumus πr² 
# Π = 22/7
# r = jari - jari lingkaran 
# Lalu tampilkan ke layar dengan format:
# Hint: untuk menampilkan tanda kuadrat gunakan print(“\u00b2”)

# Luas lingkaran dengan jari-jari [jari-jari lingkaran] cm adalah [luas lingkaran] cm².

jarijari_lingkaran = float(input("berapa jari-jari lingkaran yang anda inginkan?"))
luas_lingkaran = ((22/7)*jarijari_lingkaran**2)

print(f"Luas lingkaran dengan jari-jari {jarijari_lingkaran} cm adalah {luas_lingkaran:.2f} cm\u00b2.")


# Question 3:
# Buatlah sebuah program untuk menentukan apakah seorang siswa lulus ujian atau tidak. Siswa dinyatakan lulus apabila nilai ujian teori dan ujian praktek minimal 70. 
# Program menerima input berupa nilai ujian teori dan praktek, nilai ujian dapat berupa bilangan desimal.

# Jika nilai ujian teori dan praktek minimal 70,  maka program akan menampilkan:
# Selamat, anda lulus!
	
# 	Jika nilai ujian teori minimal 70 dan nilai ujian praktek kurang dari 70:
# Anda harus mengulang ujian praktek.

# 	Jika nilai ujian teori kurang dari 70 dan nilai ujian praktek minimal 70:
# Anda harus mengulang ujian teori.

# 	Jika nilai ujian teori dan ujian praktek kurang dari 70:
# Anda harus mengulang ujian teori dan praktek.

ujian_teori = float(input("Berapa nilai ujian teori anda?"))
ujian_praktek = float(input("Berapa nilai ujian praktek anda?"))


if ujian_teori>=70 and ujian_praktek>=70:
    print("Selamat, anda lulus!")
elif ujian_teori>=70 and ujian_praktek<70:
    print("Anda harus mengulang ujian praktek.")
elif ujian_teori<70 and ujian_praktek>=70:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")