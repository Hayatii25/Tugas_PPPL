

def menu():
    print("=" * 23 )
    print("     KALKULATOR |"      )
    print("=" * 23 ) 
    print("1.Penjumlahan(+)")
    print("2.Pengurangan(-)")
    print("3.Perkalian(x)")
    print("4.Pembagian(/)")
    print("5.Keluar")
    pilihan_user = input("Silakan Pilih Operasi: ")
    return pilihan_user

def penjumlahan(angka1,angka2):
    operasi = angka1 + angka2
    print(f"Hasilnya adalah {operasi}")
    return operasi

def pengurangan(angka1,angka2):
    operasi = angka1 - angka2
    print(f"Hasilnya adalah {operasi}")
    return operasi

def Perkalian(angka1,angka2):
    operasi = angka1 * angka2
    print(f"Hasilnya adalah {operasi}")
    return operasi

def Pembagian(angka1,angka2):
    operasi = angka1 / angka2
    print(f"Hasilnya adalah {operasi}")
    return operasi


#kode utama

while True:
    pilihan = menu()
    if pilihan == "1":
        angka1 = int(input("Masukan angka1!: "))
        angka2 = int(input("Masukan angka2!: "))
        penjumlahan(angka1, angka2)

    elif pilihan == "2":
        angka1 = int(input("Masukan angka1!: "))
        angka2 = int(input("Masukan angka2!: "))
        pengurangan(angka1, angka2)

    elif pilihan == "3":
        angka1 = int(input("Masukan angka1!: "))
        angka2 = int(input("Masukan angka2!: "))
        Perkalian(angka1, angka2)

    elif pilihan == "4":
        angka1 = int(input("Masukan angka1!: "))
        angka2 = int(input("Masukan angka2!: "))
        Pembagian(angka1, angka2)
    
    elif pilihan == "5":
        exit()