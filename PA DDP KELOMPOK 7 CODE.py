#Import ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import csv
import pwinput as pin
import time 
import os 
import sys
from prettytable import PrettyTable
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#basic ------------------------------------------------------------------------------------------------------------
akun = {"id": "", "password": "","e-money": "0"}
data_daftar = {"nama": "", "umur": "", "domisili": "", "status": "", "email": "", "no_wa": ""}
status_daftar = {"status_daftar": ""}
status_lowongan ={"lowongan_yang_dipilih":"","harga_daftar":""}
syarat_status_daftar = ("pelajar","single","menikah")

nomor_id = {"gopay":"","dana":"","m-banking":""}
pin_ = {"gopay":"","dana":"","m-banking":""}

data_csv_akun = 'data_akun.csv'           #path to file opsi lain
data_csv_pendaftar = 'data_pendaftar.csv' #path to file opsi lain
data_csv_lowongan = 'data_lowongan.csv'   #path to file opsi lain

def clear():  # template clear
    os.system("cls || clear")

def delay():  # template delay
    time.sleep(1)

def pilihan(isi):  # template menu
    print(80 * "-")
    print(isi)
    print(80 * "-")

def any_key_hasil_daftar():        #Enter to Exit
    x = input("enter to quit: ")
    if not x :
        print("Exiting the Program.")
        hasil_daftar()
    else:
        print("Exiting the Program.")
        hasil_daftar()


def invoice(id,layanan):         #Invoice
    print(80 * "-")
    print(f"""Struck Pendaftaran
          
Nama Pendaftar: {data_daftar['nama']}
Lowongan Yang Dipilih: {status_lowongan["lowongan_yang_dipilih"]}
Harga Pendaftaran: {status_lowongan['harga_daftar']}

No id: {id}

pendaftaran anda sudah selesai, untuk selanjutnya akan di proses

Terima kasih Sudah menggunakan layanan {layanan}""")
    print(80 * "-")



def invoice_ambaney():         #Invoice ambaney
    print(80 * "-")
    print(f"""Struck Pendaftaran
          
Nama Pendaftar: {data_daftar['nama']}
Lowongan Yang Dipilih: {status_lowongan["lowongan_yang_dipilih"]}
Harga Pendaftaran: {status_lowongan['harga_daftar']}

id akun: {akun["id"]}

pendaftaran anda sudah selesai, untuk selanjutnya akan di proses

Terima kasih Sudah menggunakan layanan ambaney""")
    print(80 * "-")

#------------------------------------------------------------------------------------------------------------------

#tabel ------------------------------------------------------------------------------------------------------------
def table_data_akun():
   with open(data_csv_akun, mode='r') as file:
      csv_reader = csv.reader(file)
      tableinv = PrettyTable()
      tableinv.field_names = ["nickname","password"]
      for row in csv_reader:
         tableinv.add_row(row)
      print(tableinv)

def table_data_pendaftar():
   with open(data_csv_pendaftar, mode='r') as file:
      csv_reader = csv.reader(file)
      tableinv = PrettyTable()
      tableinv.field_names = ["nama","umur","domisili","status","email","no wa","status_pendaftaran","lowongan"]
      for row in csv_reader:
         tableinv.add_row(row)
      print(tableinv)

def tabel_data_pendaftar_belum_acc():
   with open(data_csv_pendaftar, mode='r') as file:
      csv_reader = csv.reader(file)
      tableinv = PrettyTable()
      tableinv.field_names = ["nama","umur","domisili","status","email","no wa","status_pendaftaran","lowongan"]
      for row in csv_reader:
         if row[6].lower() == "belum_acc":
            tableinv.add_row(row)
      print(tableinv)

def tabel_data_pendaftar_wawancara():
   with open(data_csv_pendaftar, mode='r') as file:
      csv_reader = csv.reader(file)
      tableinv = PrettyTable()
      tableinv.field_names = ["nama","umur","domisili","status","email","no wa","status_pendaftaran","lowongan"]
      for row in csv_reader:
         if row[6].lower() == "wawancara":
            tableinv.add_row(row)
      print(tableinv)

def tabel_data_pendaftar_diterima():
   with open(data_csv_pendaftar, mode='r') as file:
      csv_reader = csv.reader(file)
      tableinv = PrettyTable()
      tableinv.field_names = ["nama","umur","domisili","status","email","no wa","status_pendaftaran","lowongan"]
      for row in csv_reader:
         if row[6].lower() == "diterima":
            tableinv.add_row(row)
      print(tableinv)

def tabel_untuk_user():              
    with open(data_csv_pendaftar, mode='r') as file:
        csv_reader = csv.reader(file)
        tableinv = PrettyTable()
        tableinv.field_names = ["nama", "status_pendaftaran"]
        next(csv_reader)
        for row in csv_reader:
            tableinv.add_row([row[0], row[6]])
        print(tableinv)

def tabel_untuk_user_sorting_by_nama():              
    with open(data_csv_pendaftar, mode='r') as file:
        csv_reader = csv.reader(file)
        tableinv = PrettyTable()
        tableinv.field_names = ["nama", "status_pendaftaran"]
        next(csv_reader)
        for row in csv_reader:
            tableinv.add_row([row[0], row[6]])
        tableinv.sortby = "nama"
        print(tableinv)

def tabel_untuk_user_sorting_by_lowongan_pekerjaan():              
    with open(data_csv_pendaftar, mode='r') as file:
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
    
    with open(data_csv_pendaftar, mode='r') as file:
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

def table_syarat_mendaftar():
    tableinv = PrettyTable()
    tableinv.field_names = ["No","syarat"]
    tableinv.add_row(["1","Nama lengkap",])
    tableinv.add_row(["2","Umur minimal 18 tahun dan maksimal 45 tahun"])
    tableinv.add_row(["3","Domisili, Sekarang Tinggal"])
    tableinv.add_row(["4","Status bisa berupa pelajar,single dan menikah"])
    tableinv.add_row(["5","Email lengkap"])
    tableinv.add_row(["6","No Wa merupakan No asli sekarang dan harus 12 digit angka"])
    return tableinv

show_table_syarat_mendaftar = table_syarat_mendaftar()

def table_data_lowongan():
   with open(data_csv_lowongan, mode='r') as file:
      csv_reader = csv.reader(file)
      tableinv = PrettyTable()
      tableinv.field_names = ["Nama Lowongan","Harga Daftar (Rp)"]
      for row in csv_reader:
         tableinv.add_row(row)
      print(tableinv)
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
                print("terima kasih sampai jumpa ")
                delay()
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
        akun["e-money"] = "0"
        akun["id"] = input("Masukkan id: ")
        if len(akun["id"]) >= 4:
            with open(data_csv_akun, mode='r') as file_data_akun:
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
                    with open(data_csv_akun, mode='a', newline='') as akun_file:
                        tulis_akun = csv.writer(akun_file)
                        tulis_akun.writerow([akun["id"], akun["password"],akun["e-money"]])
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

    with open(data_csv_akun, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0] == akun["id"]:
                found = True
                akun["password"] = pin.pwinput("Password: ")
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
            menu_admin()

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
                admin_input_loker()
            elif pil_admin == 2:
                lampiran_pendaftar()
            elif pil_admin == 3:
                menu()
            else:
                print("Pilihan tidak valid.")
                delay()
                menu_admin()
    except ValueError:
        print("Pilihan tidak valid.")
        delay()
        menu_admin()
#-------------------------------------------------------------------------------------------------------------------

#fitur admin-----------------------------------------------------------------------------------------------------------------
def lampiran_pendaftar():  # LAMPIRAN PENDAFTAR
    try: 
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
        print("Pilihan tidak valid")
        delay()   

def admin_input_loker():               # INPUT LOKER
   try:
         clear()
         table_data_lowongan()
         pilihan("""1.Menambahkan Lowongan Kerja
2.Menghapus Lowongan Kerja
3.Exit""")
         pilihan_loker = int(input("pilihan: "))
         if pilihan_loker == 1:
            masukan_pekerjaan()
         elif pilihan_loker == 2:
            hapus_pekerjaan()
         elif pilihan_loker == 3:
            print()
         else:
            print("pilihan tidak valid")
            delay()
   except ValueError:
      print("pilihan tidak valid")
      delay()
    
#-------------------------------------------------------------------------------------------------------------------

#fitur input loker------------------------------------------------------------------------------------------------------------
def masukan_pekerjaan():
   clear()
   table_data_lowongan()
   job_name = input('masukan nama pekerjaan: ')
   job_price = input('masukan harga daftar: ')
   
   with open(data_csv_lowongan, mode='a', newline='',encoding='utf-8') as file:
         csv_writer = csv.writer(file)
         csv_writer.writerow([job_name,job_price])
   print(f"Data dengan nama {job_name} berhasil ditambahkan.")
   delay()
   loop_input_loker()


def loop_input_loker():
   pilihan("""1.Nambah loker lagi
2.Exit""")
   pilihan_input_loker = input("pilihan: ")
   if pilihan_input_loker == "1":
        masukan_pekerjaan()
   elif pilihan_input_loker == "2":
       admin_input_loker()
   else:
       print("pilihan tidak valid")
       delay()
       loop_input_loker()

def hapus_pekerjaan():
   clear()
   table_data_lowongan()
   job_name = input('masukan nama lowongan yang ingin dihapus: ')
   rows = []
   found = False
   try:
      with open(data_csv_lowongan, mode='r', newline='') as lowongan:
                     lowongan_reader = csv.reader(lowongan)
                     for row in lowongan_reader:
                        if row[0] != job_name:
                           rows.append(row) 
                        else:
                           found = True
      if found:
         with open(data_csv_lowongan, mode='w', newline='') as lowongan:
               lowongan_writer = csv.writer(lowongan)
               
               lowongan_writer.writerows(rows)  

         print("lowongan kerja berhasil dihapus.")
         delay()
         admin_input_loker()
      else:
         print("id lowongan tidak ditemukan.")
         delay()
         admin_input_loker()
         
   except FileNotFoundError:
         print(f'Data tidak ditemukan')
         delay()
         admin_input_loker()
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

        with open(data_csv_pendaftar, mode='r') as file:
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
        with open(data_csv_pendaftar, mode='w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(updated_rows)

    elif pil_tabel_pendaftaran == "2":
        clear()
        tabel_data_pendaftar_belum_acc()
        nama = input("Masukkan nama yang ingin diupdate statusnya menjadi 'wawancara': ")
        updated_rows = []
        found = False

        with open(data_csv_pendaftar, mode='r') as file:
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
        with open(data_csv_pendaftar, mode='w', newline='') as file:
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

        with open(data_csv_pendaftar, mode='r') as file:
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
        with open(data_csv_pendaftar, mode='w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(updated_rows)

    elif pil_tabel_pendaftaran == "2":
        clear()
        tabel_data_pendaftar_wawancara()
        nama = input("Masukkan nama yang ingin diterima:  ")
        updated_rows = []
        found = False

        with open(data_csv_pendaftar, mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row[0] == nama:
                    found = True
                    row[6] = "diterima" 
                    print(f"Status pendaftaran untuk {nama} berhasil diubah menjadi diterima")
                    delay()
                updated_rows.append(row)  
        if not found:
            print(f"Data dengan nama {nama} tidak ditemukan.")
            delay()
            return
        with open(data_csv_pendaftar, mode='w', newline='') as file:
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

        with open(data_csv_pendaftar, mode='r') as file:
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
        with open(data_csv_pendaftar, mode='w', newline='') as file:
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
def menu_user():                # MENU USER
    try: 
        while True:
            clear()
            pilihan(f"""Selamat datang di PT.Ambalingham, {akun['id']} apa yang bisa kami bantu?
1. Mendaftar Pekerjaan
2. Hasil Daftar
3. Top Up ambaney
4. Exit""")
            pil_user = int(input("Pilihan: "))
            if pil_user == 1:
                Mendaftar_Pekerjaan()
            elif pil_user == 2:
                hasil_daftar()
            elif pil_user == 3:
                top_up()
            elif pil_user == 4:
                menu()
            else:
                print("Pilihan tidak valid.")
                delay()
                menu_user()
    except ValueError:
        print("Pilihan tidak valid.")
        delay()
        menu_user()

def top_up(): #belum fix ama akun
    clear()
    try:
        top = int(input("Masukkan jumlah yang anda inginkan: "))
    except ValueError:
        print("Input harus berupa angka.")
        delay()
        top_up()

    updated_rows = []
    found = False

    with open(data_csv_akun, mode='r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  
        updated_rows.append(header)  
        for row in csv_reader:
            if row[0] == akun["id"]: 
                found = True
                pass_word = input("masukan password akun anda: ")
                if pass_word == row[1]:
                    current_balance = int(row[2]) 
                    new_balance = current_balance + top
                    row[2] = str(new_balance)
                    print(f"Saldo berhasil ditambahkan.")
                    delay()
                else:
                    print("password salah")
                    menu_user()
            updated_rows.append(row)
    if not found:
        print("Data dengan akun tidak ditemukan.")
        delay()
        menu()

    with open(data_csv_akun, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(updated_rows)
    print("Data berhasil diperbarui.")

def menu_pembayaran():
    try:
        clear()
        pilihan("""Menu Pembayaran:\n
1. Ambaney
2. Gopay
3. Dana
4. M-Banking
5. Exit """)
        pilih_menu = input("Pilih metode pembayaran: ")
        if pilih_menu == '1':
            ambaney()
        elif pilih_menu == '2':
            pembayaran_gopay()
        elif pilih_menu == '3':
            pembayaran_dana()
        elif pilih_menu == '4':
            pembayaran_m_banking()
        elif pilih_menu == '5':
            y_or_t = input("Apakah Anda yakin untuk keluar (semua proses daftar akan hilang) (y/t): ").lower()
            if y_or_t == 'y':
                menu_user()
            else:
                menu_pembayaran()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            delay()
            menu_pembayaran()
    except ValueError:
        print(f"Terjadi error:")
        delay()
        menu_pembayaran()

def ambaney(): #E-money bugged
    updated_rows = []
    found = False
    with open(data_csv_akun, mode='r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        updated_rows.append(header)
        for row in csv_reader:
            if row[0] == akun["id"]: 
                found = True
                clear()
                pilihan(f"""Kamu mempunyai amabaney sebesar {row[2]}. Apakah kamu ingin melanjutkan dengan membayar {status_lowongan['harga_daftar']}?
1. Iya
2. Exit""")
                pilihan_saldo = input("Pilihan: ")

                if pilihan_saldo == "1":
                    try:
                        conc = int(row[2]) 
                        konc = int(next(iter(status_lowongan["harga_daftar"])))  
                        if conc >= konc:
                            new_money = conc - konc
                            row[2] = str(new_money)
                            clear()
                            print(f"Pembayaran berhasil, Sisa saldo ambaney: {row[2]}")
                            invoice_ambaney()
                            time.sleep(10)
                        else:
                            print("e-money anda tidak cukup.")
                            delay()
                            menu_pembayaran()
                    except ValueError:
                        print("Data tidak valid.")
                        delay()
                        menu_pembayaran()
                elif pilihan_saldo == "2":
                    menu_pembayaran()
                else:
                    ambaney()
            updated_rows.append(row)
    if not found:
        print("Data dengan akun tidak ditemukan.")
        delay()
        menu()
    with open(data_csv_akun, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(updated_rows)
    print("Data berhasil diperbarui.")

def pembayaran_gopay():
    try:
        nomor_id["gopay"] = input("Masukkan ID Gopay: ")
        pin_["gopay"] = pin.pwinput("Masukkan PIN Anda: ")
        clear()
        invoice(nomor_id["gopay"],"goPay")
        time.sleep(10)
    except ValueError:
        print("Bukan angka yang kamu masukan")
        delay()
        menu_pembayaran()

def pembayaran_dana():
    try:
        nomor_id["dana"] = input("Masukkan ID Dana: ")
        pin_["dana"] = pin.pwinput("Masukkan PIN Anda: ")
        clear()
        invoice(nomor_id["dana"],"Dana")
        time.sleep(10)
    except ValueError:
        print("Bukan angka yang kamu masukan")
        delay()
        menu_pembayaran()

def pembayaran_m_banking():
    try:
        clear()
        pilihan("""Menu Pembayaran M-Banking:\n
1. BCA
2. BRI
3. Mandiri
4. Exit """)
        pilih_bank = input("Masukkan pilihan: ")

        if pilih_bank in ['1', '2', '3']:
            bank_names = {'1': 'BCA', '2': 'BRI', '3': 'Mandiri'}
            nomor_id["m-banking"] = input("Masukkan nomor rekening: ")
            pin_["m-banking"] = pin.pwinput("Masukkan PIN Anda: ")
            clear()
            invoice(nomor_id["m-banking"], bank_names[pilih_bank])
            time.sleep(10)

        elif pilih_bank == '4':
            menu_pembayaran()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            delay()
            pembayaran_m_banking()
    except ValueError:
        print("Bukan angka yang anda masukan")
        delay()
        pembayaran_m_banking()

#------------------------------------------------------------------------------------

#fitur input lowongan  sebagai user---------------------------------------------------
def input_lowongan_user():
    clear()
    table_data_lowongan()
    status_lowongan["lowongan_yang_dipilih"] = input("\nmasukan nama lowongan yang ingin di daftar: ")

    with open(data_csv_lowongan, mode='r') as file:
        csv_reader = csv.reader(file)
        match_found = False
        for row in csv_reader:
            if row[0] == status_lowongan["lowongan_yang_dipilih"]:
                print(f"Lowongan yang Anda pilih adalah: {status_lowongan["lowongan_yang_dipilih"]}")
                print(f"Harga daftarnya Rp.{row[1]}")
                status_lowongan["harga_daftar"] = {row[1]}
                match_found = True
                delay()
                return

        if not match_found:
            print("Lowongan tidak ditemukan, silakan coba lagi.")
            input_lowongan_user()

def Mendaftar_Pekerjaan():        #Mendaftar Pekerjaan
    try:
        clear()
        pilihan("""syarat-syarat mendaftar di PT.Ambalihngham""")
        print(show_table_syarat_mendaftar)
        print("Silahkan Daftar\n")
        data_daftar["nama"] = input("Masukkan nama lengkap: ")
        data_daftar["umur"] = int(input("Masukkan umur: "))
        data_daftar["domisili"] = input("masukan domisili: ")
        data_daftar["status"] = input("masukan status: ")
        data_daftar["email"] = input("masukan email: ")
        data_daftar["no_wa"] = input("masukan no wa: ")
        status_daftar["status_daftar"] = "belum_acc"
        if data_daftar["umur"] < 18 or data_daftar["umur"] > 45:
            print("umur anda tidak memenuhi syarat")
            delay()
            menu_user()

        elif data_daftar["status"] not in syarat_status_daftar:          
            print("status anda tidak sesuai syarat")
            delay()
            menu_user()

        elif len(data_daftar["no_wa"]) < 12 or len(data_daftar["no_wa"]) > 12:
            print("no wa anda tidak valid")
            delay()
            menu_user()

        else:
            input_lowongan_user()
            menu_pembayaran()
            required_keys = ["nama", "umur", "domisili", "status", "email", "no_wa"]
            if all(key in data_daftar for key in required_keys) and "status_daftar" in status_daftar:
                with open(data_csv_pendaftar, mode='a', newline='', encoding='utf-8') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerow([data_daftar["nama"], data_daftar["umur"], data_daftar["domisili"],
                                        data_daftar["status"], data_daftar["email"], data_daftar["no_wa"],
                                        status_daftar["status_daftar"],status_lowongan["lowongan_yang_dipilih"]])
                    print(f"Data dengan nama {data_daftar['nama']} berhasil ditambahkan ")
                    time.sleep(4)
                    return
            else:
                print("Data tidak lengkap.")
                delay()
                menu_user()
    except ValueError:
        print("umur anda bukan merupakan angka")
        delay()
        Mendaftar_Pekerjaan()

def hasil_daftar():                     #Hasil Daftar
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

#RUN COMMAND--------------------------------------------------------------------------------------------------------

menu()

#-------------------------------------------------------------------------------------------------------------------
