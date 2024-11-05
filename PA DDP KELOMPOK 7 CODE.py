import csv
import pwinput as pin
import time 
import os 
import sys
from prettytable import PrettyTable

#basic ------------------------------------------------------------------------------------------------------------
akun = {"id": "", "password": ""}
data_daftar = {"nama": "", "umur": "", "domisili": "", "status": "", "email": "", "no_wa": ""}
status_daftar = {"pembayaran": "", "lowongan_yang_dipilih": "", "status_daftar": ""}

def clear():  # template clear
    os.system("cls || clear")

def delay():  # template delay
    time.sleep(1)

def pilihan(isi):  # template menu
    print(40 * "-")
    print(isi)
    print(40 * "-")

def any_key_hasil_daftar():
    x = input("enter to quit: ")
    if not x :
        print("Exiting the Program.")
        hasil_daftar()
    else:
        print("Exiting the Program.")
        hasil_daftar()
#------------------------------------------------------------------------------------------------------------------

#tabel ------------------------------------------------------------------------------------------------------------
def table_data_akun():
   with open('data_akun.csv', mode='r') as file:
      csv_reader = csv.reader(file)
      tableinv = PrettyTable()
      tableinv.field_names = ["nickname","password"]
      for row in csv_reader:
         tableinv.add_row(row)
      print(tableinv)

def table_data_pendaftar():
   with open('data_pendaftar.csv', mode='r') as file:
      csv_reader = csv.reader(file)
      tableinv = PrettyTable()
      tableinv.field_names = ["nama","umur","domisili","status","email","no wa","status_pendaftaran"]
      for row in csv_reader:
         tableinv.add_row(row)
      print(tableinv)

def tabel_data_pendaftar_belum_acc():
   with open('data_pendaftar.csv', mode='r') as file:
      csv_reader = csv.reader(file)
      tableinv = PrettyTable()
      tableinv.field_names = ["nama","umur","domisili","status","email","no wa","status_pendaftaran"]
      for row in csv_reader:
         if row[6].lower() == "belum_acc":
            tableinv.add_row(row)
      print(tableinv)

def tabel_data_pendaftar_wawancara():
   with open('data_pendaftar.csv', mode='r') as file:
      csv_reader = csv.reader(file)
      tableinv = PrettyTable()
      tableinv.field_names = ["nama","umur","domisili","status","email","no wa","status_pendaftaran"]
      for row in csv_reader:
         if row[6].lower() == "wawancara":
            tableinv.add_row(row)
      print(tableinv)

def tabel_data_pendaftar_diterima():
   with open('data_pendaftar.csv', mode='r') as file:
      csv_reader = csv.reader(file)
      tableinv = PrettyTable()
      tableinv.field_names = ["nama","umur","domisili","status","email","no wa","status_pendaftaran"]
      for row in csv_reader:
         if row[6].lower() == "diterima":
            tableinv.add_row(row)
      print(tableinv)

def tabel_untuk_user():              
    with open('data_pendaftar.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        tableinv = PrettyTable()
        tableinv.field_names = ["nama", "status_pendaftaran"]
        next(csv_reader)
        for row in csv_reader:
            tableinv.add_row([row[0], row[6]])
        print(tableinv)

def tabel_untuk_user_sorting_by_nama():              
    with open('data_pendaftar.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        tableinv = PrettyTable()
        tableinv.field_names = ["nama", "status_pendaftaran"]
        next(csv_reader)
        for row in csv_reader:
            tableinv.add_row([row[0], row[6]])
        tableinv.sortby = "nama"
        print(tableinv)

def tabel_untuk_user_sorting_by_lowongan_pekerjaan():              
    with open('data_pendaftar.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        tableinv = PrettyTable()
        tableinv.field_names = ["nama", "status_pendaftaran"]
        next(csv_reader)
        for row in csv_reader:
            tableinv.add_row([row[0], row[6]])
        tableinv.sortby = "status_pendaftaran"
        print(tableinv)

def tabel_untuk_user_search_nama():
    tabel_untuk_user()              
    search_name = input("Masukkan nama yang ingin dicari: ").lower()
    found = False
    
    with open('data_pendaftar.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        tableinv = PrettyTable()
        tableinv.field_names = ["nama", "status_pendaftaran"]

        next(csv_reader)

        for row in csv_reader:
            if row[0].lower() == search_name: 
                tableinv.add_row([row[0], row[6]])
                found = True

        if found:
            clear()
            print(tableinv)
        else:
            print(f"Data dengan nama '{search_name}' tidak ditemukan.")
#-------------------------------------------------------------------------------------------------------------------

#Menu utama -------------------------------------------------------------------------------------------------------------
def menu():  # MENU UTAMA
    try:
        while True:
            clear()
            pilihan("""Selamat Datang Di PT.Ambalingham Apa yang bisa kami bantu?
1. Sign Up
2. Login
3. Admin Menu
4. Help
5. Exit""")
            choice = int(input("Pilihan: "))
            if choice == 1:
                sign_up()
                delay()
            elif choice == 2:
                login()
                delay()
            elif choice == 3:
                pass_admin()
                delay()
            elif choice == 4:
                clear()
                print("untuk mendaftar anda harus terlebih dahulu sign up dan login (user)")
                print("pada menu admin anda bertindak sebagai hrd atau admin (admin)")
                x = input("enter to quit: ")
                if not x :
                    print("Exiting the Program.")
                    menu()
                else:
                    print("Exiting the Program.")
                    menu()
            elif choice == 5:
                exit()
            else:
                print("Pilihan tidak valid.")
                delay()
                menu()
    except ValueError:
        print("Pilihan tidak valid.")
        delay()
        menu()
#-------------------------------------------------------------------------------------------------------------------

#sign up dan login-------------------------------------------------------------------------------------------------------------
def sign_up():  # SIGN UP
    try:
        clear()
        akun["id"] = input("Masukkan id: ")
        if len(akun["id"]) >= 4:
            with open('data_akun.csv', mode='r') as file_data_akun:
                akun_reader = csv.reader(file_data_akun)
                for row in akun_reader:
                    if row[0] == akun["id"]: 
                        print("Akun yang sama ditemukan.")
                        delay()
                        return  
            while True:
                clear()
                akun["password"] = pin.pwinput("Create pass: ", '*')
                if len(akun["password"]) >= 6:
                    with open("data_akun.csv", mode='a', newline='') as akun_file:
                        tulis_akun = csv.writer(akun_file)
                        tulis_akun.writerow([akun["id"], akun["password"]])
                    print(f"Data {akun['id']} berhasil ditambahkan.")
                    delay()
                    menu()
                    return
                else:
                    print("Password harus memiliki minimal 6 karakter.")
                    delay()
        else:
            print("ID harus memiliki minimal 4 karakter.")
            delay()
            sign_up()
    except ValueError:
        print("Input tidak valid.")
        delay()

def login():  # LOGIN
    clear()
    akun["id"] = input("Masukkan id: ")

    updated_rows = []
    found = False

    with open('data_akun.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0] == akun["id"]:
                found = True
                akun["password"] = input("Password: ")
                if row[1] == akun["password"]:
                    print(f"Selamat datang {akun['id']} di PT.Ambalingham")
                    delay()
                    menu_user()
                else:
                    print("Password salah.")
                    delay()
                    return
            else:
                updated_rows.append(row)

    if not found:
        print(f"Data dengan ID {akun['id']} tidak ditemukan.")
        delay()
#-------------------------------------------------------------------------------------------------------------------

#ADMIN---------------------------------------------------------------------------------------------------------------
def pass_admin():  # PASS ADMIN
    while True:
        clear() 
        pass_asli = "admin123"
        akun["password"] = pin.pwinput("Masukkan pass admin: ", '*')
        if akun["password"] == pass_asli:
            menu_admin()
            delay()
        else:
            print("Password tidak valid.")
            delay()
            break

def menu_admin():  # MENU ADMIN
    try: 
        while True:
            clear()
            pilihan("""Selamat datang di menu admin 
1. Admin Loker
2. Lampiran Pendaftar
3. Exit """)
            pil_admin = int(input("Pilihan: "))
            if pil_admin == 1:
                input_loker()
            elif pil_admin == 2:
                lampiran_pendaftar()
            elif pil_admin == 3:
                menu()
            else:
                print("Pilihan tidak valid.")
                delay()
    except ValueError:
        print("Pilihan tidak valid.")
        delay()
#-------------------------------------------------------------------------------------------------------------------

#fitur admin-----------------------------------------------------------------------------------------------------------------
def lampiran_pendaftar():  # LAMPIRAN PENDAFTAR
    try: 
        while True:
            clear()
            table_data_pendaftar()
            pilihan("""Lampiran Pendaftar
1. Tabel Yang Belum di Acc
2. Tabel yang Wawancara
3. Tabel Yang Sudah Diterima
4. Exit""")
            pil_admin = int(input("Pilihan: "))
            if pil_admin == 1:
                pendaftar_belum_acc()
            elif pil_admin == 2:
                tabel_wawancara()
            elif pil_admin == 3:
                tabel_diterima()
            elif pil_admin == 4:
                menu()
            else:
                print("Pilihan tidak valid.")
    except ValueError:
        print("Pilihan tidak valid.")
        delay()   

def input_loker():               #bagian pras---------------------------------------
    print("Bagian Pras")
#-------------------------------------------------------------------------------------------------------------------

#fitur lampiran pendaftar--------------------------------------------------------------------------------------------------------------
def pendaftar_belum_acc():                   #belum acc
    clear()
    tabel_data_pendaftar_belum_acc()
    pilihan("""1.hapus pendaftar 
2.acc pendaftar ke sesi wanwacara
3.Exit""")
    pil_tabel_pendaftaran = input("pilihan: ")

    if pil_tabel_pendaftaran == "1":
        clear()
        tabel_data_pendaftar_belum_acc()
        nama = input("Masukkan nama yang ingin dihapus: ")
        updated_rows = []
        found = False

        with open("data_pendaftar.csv", mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row[0] == nama:
                    found = True
                    print(f"Data {nama} berhasil dihapus.")
                    delay()
                else:
                    updated_rows.append(row)
        if not found:
            print(f"Data dengan nama {nama} tidak ditemukan.")
            delay()
            return
        with open("data_pendaftar.csv", mode='w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(updated_rows)

    elif pil_tabel_pendaftaran == "2":
        clear()
        tabel_data_pendaftar_belum_acc()
        nama = input("Masukkan nama yang ingin diupdate statusnya menjadi 'wawancara': ")
        updated_rows = []
        found = False

        with open("data_pendaftar.csv", mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row[0] == nama:
                    found = True
                    row[6] = "wawancara" 
                    print(f"Status pendaftaran untuk {nama} berhasil diubah menjadi wawancara")
                    delay()
                updated_rows.append(row)  
        if not found:
            print(f"Data dengan nama {nama} tidak ditemukan.")
            delay()
            return
        with open("data_pendaftar.csv", mode='w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(updated_rows)

    elif pil_tabel_pendaftaran == "3":
        lampiran_pendaftar()
    else:
        print("pilihan tidak valid")
        delay()
        pendaftar_belum_acc()

def tabel_wawancara():                         #wawancara
    clear()
    tabel_data_pendaftar_wawancara()
    pilihan("""1.hapus pendaftar 
2.acc pendaftar
3.Exit""")
    pil_tabel_pendaftaran = input("pilihan: ")

    if pil_tabel_pendaftaran == "1":
        clear()
        tabel_data_pendaftar_wawancara()
        nama = input("Masukkan nama yang ingin dihapus: ")
        updated_rows = []
        found = False

        with open("data_pendaftar.csv", mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row[0] == nama:
                    found = True
                    print(f"Data {nama} berhasil dihapus.")
                    delay()
                else:
                    updated_rows.append(row)
        if not found:
            print(f"Data dengan nama {nama} tidak ditemukan.")
            delay()
            return
        with open("data_pendaftar.csv", mode='w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(updated_rows)

    elif pil_tabel_pendaftaran == "2":
        clear()
        tabel_data_pendaftar_wawancara()
        nama = input("Masukkan nama yang ingin diterima:  ")
        updated_rows = []
        found = False

        with open("data_pendaftar.csv", mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row[0] == nama:
                    found = True
                    row[6] = "diterima" 
                    print(f"Status pendaftaran untuk {nama} berhasil diubah menjadi wawancara")
                    delay()
                updated_rows.append(row)  
        if not found:
            print(f"Data dengan nama {nama} tidak ditemukan.")
            delay()
            return
        with open("data_pendaftar.csv", mode='w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(updated_rows)

    elif pil_tabel_pendaftaran == "3":
        lampiran_pendaftar()
    else:
        print("pilihan tidak valid")
        delay()
        tabel_wawancara()

def tabel_diterima():                  #diterima
    clear()
    tabel_data_pendaftar_diterima()
    pilihan("""1.hapus pendaftar 
2.Exit""")
    pil_tabel_pendaftaran = input("pilihan: ")

    if pil_tabel_pendaftaran == "1":
        clear()
        tabel_data_pendaftar_diterima()
        nama = input("Masukkan nama yang ingin dihapus: ")
        updated_rows = []
        found = False

        with open("data_pendaftar.csv", mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row[0] == nama:
                    found = True
                    print(f"Data {nama} berhasil dihapus.")
                    delay()
                else:
                    updated_rows.append(row)
        if not found:
            print(f"Data dengan nama {nama} tidak ditemukan.")
            delay()
            return
        with open("data_pendaftar.csv", mode='w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(updated_rows)

    elif pil_tabel_pendaftaran == "2":
        lampiran_pendaftar()
    else:
        print("pilihan tidak valid")
        delay()
        tabel_diterima()
#-------------------------------------------------------------------------------------------------------------------

#USER --------------------------------------------------------------------------------------------------------------
def menu_user():  # MENU USER
    try: 
        while True:
            clear()
            pilihan(f"""Selamat datang di PT.Ambalingham, {akun['id']} apa yang bisa kami bantu?
1. Mendaftar Pekerjaan
2. Hasil Daftar
3. Exit""")
            pil_user = int(input("Pilihan: "))
            if pil_user == 1:
                Mendaftar_Pekerjaan()
            elif pil_user == 2:
                hasil_daftar()
            elif pil_user == 3:
                menu()
            else:
                print("Pilihan tidak valid.")
                delay()
                menu_user
    except ValueError:
        print("Pilihan tidak valid.")
        delay()
        menu_user()

def bayar_daftar():               #Bagian SHafa ---------------------------------------
    print("bagian shafa")

def Mendaftar_Pekerjaan():
    nama = input("Masukkan nama: ")
    umur = input("Masukkan umur: ")
    domisili = input("masukan domisili: ")
    status = input("masukan status: ")
    email = input("masukan email: ")
    no_wa = input("masukan no wa: ")
    status_pendaftaran = "belum_acc"
    with open("data_pendaftar.csv", mode='a', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([nama, umur, domisili,status,email,no_wa,status_pendaftaran])
    print(f"Data dengan nama {nama} berhasil ditambahkan.")
    delay()

def hasil_daftar():              #belum
    clear()
    tabel_untuk_user()
    pilihan("""1.sorting menggunakan nama
2.sorting menggunakan lowongan
3.search nama
4.Exit""")
    pilihan_daftar_user = input("pilihan: ")
    if pilihan_daftar_user == "1":
        clear()
        tabel_untuk_user_sorting_by_nama()
        any_key_hasil_daftar()

    elif pilihan_daftar_user == "2":
        clear()
        tabel_untuk_user_sorting_by_lowongan_pekerjaan()
        any_key_hasil_daftar()
    
    elif pilihan_daftar_user == "3":
        clear()
        tabel_untuk_user_search_nama()
        any_key_hasil_daftar()
            
    elif pilihan_daftar_user == "4":
        menu_user()
    else:
        print("pilihan tidak valid")
        delay()
        hasil_daftar()
#-------------------------------------------------------------------------------------------------------------------

#RUN COMMAND---------------------------------------------------------------------------------------------------------------

menu()

#-------------------------------------------------------------------------------------------------------------------