import csv
import pwinput as pin
import time 
import os 
import prettytable

csv_file = 'data.csv'

def clear():                              #template clear
    os.system("cls || clear")

def delay():                              #template delay
   time.sleep(1)

def pilihan(isi):                         #template menu
   print(40 * "-")
   print(isi)
   print(40 * "-") 

def sign_up():
   clear()
   id = input("Masukkan id: ")
   found = False
   with open(csv_file, mode='r') as file:
      csv_reader = csv.reader(file)
      for row in csv_reader:
         if row[0] == id:
            print("akun yang sama ditemukan")
            found = True
            delay()
            sign_up()
   if not found:
      password = pin.pwinput("Masukkan pass: ", '*')
      with open(csv_file, mode='a', newline='') as file:
         csv_writer = csv.writer(file)
         csv_writer.writerow([id,password])
      print(f"Data {id} berhasil ditambahkan.")
      delay()
      menu()

def login():
    clear()
    id = input("masukin id: ")
    rows = []
    found = False
    with open(csv_file, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0] == id:
                password_login = input("masukan password: ")
                if password_login == row[1]:
                    found = True
                    print(f"selamat datang {id}")
                    menu_user()
                else:
                    print("password atau id salah")
                    delay()
                    break
            else:
                rows.append(row)
    if not found:
      print(f"ID atau Password salah")
      return

def pass_admin():
   while True:
      clear() 
      pass_asli = ("admin123")
      password = input("masukan pass admin: ")
      if password ==  pass_asli:
         menu_admin()
         delay()
      else:
         print("password tidak valid")
         delay()
         break

def menu_admin():
   try: 
      while True:
         clear()
         pilihan("""Selamat datang di menu admin 
1.Admin Loker
2.Lampiran Pendaftar
3.Exit """)
         pil_admin = int(input("pilihan: "))
         if pil_admin == 1:
            print("admin loker")
         elif pil_admin == 2:
            print("lampiran pendaftar")
         elif pil_admin == 3:
            menu()
         else:
            print("pilihan tidak valid")
   except ValueError:
      print("pilihan tidak valid")
      delay()

def lampiran_pendaftar():
   try: 
      while True:
         clear()
         pilihan("""Lampiran pendaftar 
1.Tabel Yang daftar
2.Tabel ACC ke wawancara
3.Tabel Yang sudah Diterima
4.Exit """)
         pil_admin = int(input("pilihan: "))
         if pil_admin == 1:
            print("admin loker")
         elif pil_admin == 2:
            print("lampiran pendaftar")
         elif pil_admin == 3:
            print("tabel yang sudah diterima")
         elif pil_admin == 4:
            break
         else:
            print("pilihan tidak valid")
   except ValueError:
      print("pilihan tidak valid")
      delay()   

def menu_user():
   try: 
      while True:
         clear()
         pilihan(f"""Selamat datang di menu user 
1.Daftar Pekerjaan
2.Hasil Daftar
3.Exit """)
         pil_admin = int(input("pilihan: "))
         if pil_admin == 1:
            print("Daftar Pekerjaan")
         elif pil_admin == 2:
            print("Hasil Daftar")
         elif pil_admin == 3:
            menu()
         else:
            print("pilihan tidak valid")
   except ValueError:
      print("pilihan tidak valid")
      delay()

def menu():
   while True:
      clear()
      pilihan("""1.Sign Up
2.Login
3.Admin Menu
4.Exit""")
      choice = input("Pilihan: ")
      if choice == '1':
         sign_up()
         delay()
      elif choice == '2':
         login()
         delay()
      elif choice == '3':
         pass_admin()
         delay()
      elif choice == '4':
         break
      else:
         print("Pilihan tidak valid, coba lagi.")
         delay()

menu()