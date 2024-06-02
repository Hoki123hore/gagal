print("Program Kasir Sederhana")
pembeli = input("Masukkan nama pembeli: ")
print("Nama pembeli:", pembeli)

print("a. Kantin Melati")
print("b. Kantin Mawar")
print("c. Kantin Kenanga")
print("d. Kantin Dahlia")
print("e. Kantin Edelweis")
print("f. Kantin Aster")
print("g. Kantin Anggrek")
print("h. Kantin Anyelir")
kantin = input("Masukkan pilihan: ")

def fungsimakanan():
    global totalmkn
    global porsi
    global mkn
    
def fungsiminuman():
    global totalmnum
    global mnum
    global gelas


    if kantin == 'a':
        print("----------------- MENU MAKANAN MELATI ---------------")
        print("1. Permen hothotpop -------- Rp. 500")
        print("2. Bola susu -------- Rp. 500")
        print("3. 3 Permen toples -------- Rp. 1000")
        print("4. 3 Permen Yupi -------- Rp. 2000")
        print("5. Keripik kaca dan cikruh ------- Rp. 2000")
        print("6. Cheesestik ----- Rp. 2000")
        print("7. Qtela ----- Rp. 2500")
        print("8. Chitato ----- Rp. 2500")
        print("9. Sarigandum ----- Rp. 2500")
        print("10. Choki stick ----- Rp. 2500")
        print("11. Momotaro ----- Rp. 2500")
        print("12. Better ----- Rp. 2500")
        print("13. Wafer Nabati ----- Rp. 2500")
        print("14. Vegetable cheesestick ----- Rp. 2500")
        print("15. Beng beng -------- Rp. 2500")
        print("16. Arden -------- Rp. 2500")
        print("17. Duo sus -------- Rp. 2500")
        print("18. Pisangers -------- Rp. 5000")
        print("19. Basreng Karedok ------- Rp. 5000")
        print("20. Aneka Mie -------- Rp. 7000")
        nomor = int(input("Masukkan pilihan: "))
        porsi = int(input("Berapa porsi: "))
        
        if nomor == 1:
            totalmkn = porsi * 500
            mkn = "Permen hothotpop"
        elif nomor == 2:
            totalmkn = porsi * 500
            mkn = "Bola susu"
        elif nomor == 3:
            totalmkn = porsi * 1000
            mkn = "3 Permen toples"
        elif nomor == 4:
            totalmkn = porsi * 2000
            mkn = "3 Permen Yupi"
        elif nomor == 5:
            totalmkn = porsi * 2000
            mkn = "Keripik kaca dan cikruh"
        elif nomor == 6:
            totalmkn = porsi * 2000
            mkn = "Cheesestik"
        elif nomor == 7:
            totalmkn = porsi * 2500
            mkn = "Qtela"
        elif nomor == 8:
            totalmkn = porsi * 2500
            mkn = "Chitato"
        elif nomor == 9:
            totalmkn = porsi * 2500
            mkn = "Sarigandum"
        elif nomor == 10:
            totalmkn = porsi * 2500
            mkn = "Choki stick"
        elif nomor == 11:
            totalmkn = porsi * 2500
            mkn = "Momotaro"
        elif nomor == 12:
            totalmkn = porsi * 2500
            mkn = "Better"
        elif nomor == 13:
            totalmkn = porsi * 2500
            mkn = "Wafer Nabati"
        elif nomor == 14:
            totalmkn = porsi * 2500
            mkn = "Vegetable cheesestick"
        elif nomor == 15:
            totalmkn = porsi * 2500
            mkn = "Beng beng"
        elif nomor == 16:
            totalmkn = porsi * 2500
            mkn = "Arden"
        elif nomor == 17:
            totalmkn = porsi * 2500
            mkn = "Duo sus"
        elif nomor == 18:
            totalmkn = porsi * 5000
            mkn = "Pisangers"
        elif nomor == 19:
            totalmkn = porsi * 5000
            mkn = "Basreng Karedok"
        elif nomor == 20:
            totalmkn = porsi * 7000
            mkn = "Aneka Mie"
        else:
            print("Pilihan tidak ada, silahkan masukkan lagi!")
            fungsimakanan()
        
        print(porsi, mkn, "= Rp", totalmkn)


    print("\n----------------- MENU MINUMAN ---------------")
    print("1. Teh Gelas -------- Rp. 1000")
    print("2. 3 Air Cup Gelas -------- Rp. 2000")
    print("3. Le Minerale -------- Rp. 5000")
    print("4. Ale-ale -------- Rp. 1000")
    print("5. Teh Pucuk -------- Rp. 5000")
    print("6. Floridina -------- Rp. 5000")
    print("7. Teh Kotak -------- Rp. 5000")
    print("8. Susu Cimory -------- Rp. 1000")
    
    nomor = int(input("Masukkan Pilihan: "))
    gelas = int(input("Berapa Gelas: "))
    
    if nomor == 1:
        totalmnum = gelas * 1000
        mnum = "Teh Gelas"
    elif nomor == 2:
        totalmnum = gelas * 2000
        mnum = "3 Air Cup Gelas"
    elif nomor == 3:
        totalmnum = gelas * 5000
        mnum = "Le Minerale"
    elif nomor == 4:
        totalmnum = gelas * 1000
        mnum = "Ale-ale"
    elif nomor == 5:
        totalmnum = gelas * 5000
        mnum = "Teh Pucuk"
    elif nomor == 6:
        totalmnum = gelas * 5000
        mnum = "Floridina"
    elif nomor == 7:
        totalmnum = gelas * 5000
        mnum = "Teh Kotak"
    elif nomor == 8:
        totalmnum = gelas * 1000
        mnum = "Susu Cimory"
    else:
        print("Pilihan tidak ada, silahkan masukkan lagi!")
        fungsiminuman()
    
    print(gelas, mnum, "= Rp", totalmnum)

if kantin == 'b':
  print ("----------------- MENU MAKANAN MAWAR ---------------")
  print ("1. Pisang Keju -------- Rp. 5000")
  print ("2. Sandwich -------- Rp. 5000")
  print ("3. Burger -------- Rp. 7000")
  print ("4. Cheese Burger -------- Rp. 8000")
  print ("5. Nasi Ayam Katsu ------- Rp. 8000")
  nomor = int(input("Masukkan pilihan"))
  porsi = int(input("Berapa porsi: "))
  
  
  if nomor == 1:
    totalmkn = porsi*5000
    mkn = "Pisang keju"
  elif nomor == 2:
    totalmkn = porsi*5000
    mkn = "Sandwich"
  elif nomor == 3:
    totalmkn = porsi*7000
    mkn = "Burger"
  elif nomor == 4:
    totalmkn = porsi*8000
    mkn = "Cheese Burger"
  elif nomor == 5:
    totalmkn = porsi*8000
    mkn = "Nasi Ayam Katsu"
  else:
    print ("Pilihan tidak ada, silahkan masukkan lagi!")
    fungsimakanan()
    
  print(porsi, mkn, "= Rp", totalmkn)

  print ("--------------- MENU MINUMAN MAWAR -------------")
  print ("1. Es krim ----- Rp. 5000")
  print ("2. Es krim roti ----- Rp. 6000")
  print ("3. Pop Ice polos ----- Rp. 3000")
  print ("4. Pop Ice & topping ----- Rp. 4000")
  print ("5. Pop Ice & Es krim ----- Rp. 5000")
  print ("6. Pop Ice & cococrunch ----- Rp. 5000")
  print ("7. Milo ----- Rp. 6000")
  print ("8. Milo & topping ----- Rp. 7000")
  print ("9. Hilo ----- Rp. 4000")
  print ("10. Hilo & topping ----- Rp. 7000")
  print ("11. Chocolatos ----- Rp. 5000")
  print ("12. Chocolatos + topping ----- Rp. 6000")
  print ("13. Drink Bengbeng ----- Rp. 4000")
  print ("14. Drink Bengbeng & topping ----- Rp. 5000")
  print ("15. Jus Mangga -------- Rp. 6000")
  print ("16. Jus Jambu -------- Rp. 6000")
  print ("17. Jus Sirsak -------- Rp. 6000")
  print ("18. Jus Alpukat -------- Rp. 7000")
  print ("19. Jus Strawberry ------- Rp. 7000")
  print ("20. Jus Melon -------- Rp. 6000")
  print ("21. Jus Buah Naga -------- Rp. 6000")
  print ("22. Es Jeruk ------- Rp. 6000")
  nomor = int(input("\nMasukkan Pilihan: "))
  gelas = int(input("Berapa Gelas: "))

  if nomor == 1:
    totalmnum = gelas*5000
    mnum = "Es krim"
  elif nomor == 2:
    totalmnum = gelas*6000
    mnum = "Es krim roti"
  elif nomor == 3:
    totalmnum = gelas*3000
    mnum = "Pop Ice polos"
  elif nomor == 4:
    totalmnum = gelas*4000
    mnum = "Pop Ice & topping"
  elif nomor == 5:
    totalmnum = gelas*5000
    mnum = "Pop Ice & Es krim"
  elif nomor == 6:
    totalmnum = gelas*5000
    mnum = "Pop Ice & cococrunch"
  elif nomor == 7:
    totalmnum = gelas*6000
    mnum = "Milo"
  elif nomor == 8:
    totalmnum = gelas*7000
    mnum = "Milo & topping"
  elif nomor == 9:
    totalmnum = gelas*4000
    mnum = "Hilo"
  elif nomor == 10:
    totalmnum = gelas*7000
    mnum = "Hilo & topping"
  elif nomor == 11:
    totalmnum = gelas*5000
    mnum = "Chocolatos"
  elif nomor == 12:
    totalmnum = gelas*6000
    mnum = "Chocolatos & topping"
  elif nomor == 13:
    totalmnum = gelas*4000
    mnum = "Drink Bengbeng"
  elif nomor == 14:
    totalmnum = gelas*5000
    mnum = "Drink Bengbeng & topping"
  elif nomor == 15:
    totalmnum = porsi*6000
    mnum = "Jus Mangga"
  elif nomor == 16:
    totalmnum = porsi*6000
    mnum = "Jus Jambu"
  elif nomor == 17:
    totalmnum = porsi*6000
    mnum = "Jus Sirsak"
  elif nomor == 18:
    totalmnum = porsi*7000
    mnum = "Jus Alpukat"
  elif nomor == 19:
    totalmnum = porsi*7000
    mnum = "Jus Strawberry"
  elif nomor == 20:
    totalmnum = porsi*6000
    mnum = "Jus Melon"
  elif nomor == 21:
    totalmnum = porsi*6000
    mnum = "Jus Buah Naga"
  elif nomor == 22:
    totalmnum = porsi*6000
    mnum = "Es Jeruk"
  else:
    print ("Pilihan tidak ada, silahkan masukkan lagi!")
    fungsiminuman()

  print(gelas, mnum, "= Rp", totalmnum)

fungsimakanan()
fungsiminuman()

totalsemua = totalmkn + totalmnum

print("\nTotal harus Dibayar: Rp", totalsemua)
uang = int(input("Uang tunai pembeli: Rp"))
kembalian = uang - totalsemua
print("Kembalian:", kembalian)

print("======================================")
print("========= STRUK BELI ==========")
print("======================================")
print("Nama\t\t:", pembeli)
print("Beli\t\t:", porsi, mkn, "(Rp", totalmkn, ")")
print("\t\t", gelas, mnum, "(Rp", totalmnum, ")")
print("Tagihan\t\t: Rp", totalsemua)
print("Dibayar\t\t: Rp", uang)
print("Kembalian\t: Rp", kembalian)
print("========================================")
print("========================================")
