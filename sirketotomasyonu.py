class Sirket():
    def __init__(self,ad):
        self.ad = ad
        self.calisma= True
    def butceGir(self):
        with open("butce.txt", "r+") as dosya:
            butceCheck=dosya.readline()
            if len(butceCheck) == 0 :
               butce= (input("Bütçenizi giriniz: "))
               dosya.write(butce)  
    def program(self):
        self.butceGir()
        secim = self.menuSecim()
        if secim ==1:
            self.calisanEkle()
        if secim ==2:
            self.calisanCikar()
        if secim ==3:
            ay_yil_secim=input("Yillik bazda görmek ister misiniz?()e/h:")
            if ay_yil_secim == "e":
                self.verilecekMaasGoster(hesap="y")
            else:
                self.verilecekMaasGoster()
        if secim ==4:
            self.maaslariVer()
        if secim ==5:
            self.masrafGir()
        if secim ==6:
            self.gelirGir()
    def menuSecim(self):
        secim= int(input("****{} Otomasyonuna hoş geldiniz **** \n\n 1-Çalışan Ekle\n 2-Çalışan Çıkar\n 3-Verilecek Maaş Göster\n 4-Maaslari Ver\n 5-Masraf Gir\n 6-Gelir Gir\n Seçiminizi giriniz:".format(self.ad)))
        while secim < 1 or  secim >6:
            secim = int(input("Lütfen 1-6 arasında belirtilen seçeneklerden birini giriniz!"))
        return secim
    def calisanEkle(self):
        id=1
        ad= input("Çalışanın adını giriniz:")
        soyad= input("Çalışanın soyadını giriniz:")
        yas= input("Çalışanın yasini giriniz:")
        cinsiyet= input("Çalışanın cinsiyetini giriniz:")
        maas= input("Çalışanın maaşını giriniz:")
        with open("calisanlar.txt","r") as dosya:
           calisanListesi= dosya.readlines()
        if len(calisanListesi) == 0:
            id=1
        else:
            with open("calisanlar.txt","r") as dosya:
                      id=int(dosya.readlines()[-1].split(")")[0]) + 1
        with open("calisanlar.txt","a+") as dosya:
            dosya.write("{})-{}-{}-{}-{}-{}\n".format(id,ad,soyad,yas,cinsiyet,maas))
                   
    def calisanCikar(self):
        with open("calisanlar.txt","r") as dosya:
            calisanlar=dosya.readlines()
        gCalisanlar=[]
        for calisan in calisanlar:
            gCalisanlar.append(" ".join (calisan[:-1].split("-")))
        for calisan in gCalisanlar:
            print(calisan)
        secim= int(input("Lütfen çıkarmak istediğiniz çalışanın numarasını giriniz(1-{}:").format(len(gCalisanlar)))
        while secim<1 or secim> len(gCalisanlar):
            secim= int(input("Lütfen(1-{}):arasında numara giriniz:").format(len(gCalisanlar)))
        calisanlar.pop(secim-1)
        msayi=len(calisanlar)
        sayac=1
        dCalisanlar=[]
        for calisan in calisanlar:
            dCalisanlar.append(str(sayac)+")"+ calisan.split(")")[1])
            sayac+=1
        with open("calisanlar.txt", "w") as dosya:
            dosya.writelines(dCalisanlar)    
    def verilecekMaasGoster(self,hesap="a"):
        "hesap a ise aylık y ise yillik hesap"
        with open("calisanlar.txt", "r") as dosya:
             calisanlar=dosya.readlines()
        maaslar = []
        for calisan in calisanlar:
                 maaslar.append(int(calisan.split("-")[-1]))
        if hesap=="a":
            print("Bu ay toplam vermeniz gereken maaş : {}".format(sum(maaslar)))
        else: 
            print("Bu yıl toplam vermeniz gereken maaş:  {}".format(sum(maaslar)*12))
    
    def maaslariVer(self):
        with open("calisanlar.txt", "r") as dosya:
             calisanlar=dosya.readlines()
        maaslar = []
        for calisan in calisanlar:
                 maaslar.append(int(calisan.split("-")[-1]))
        toplamMaas=sum(maaslar)
        #### bütceden maasi alma ####
        with open("butce.txt", "r") as dosya:
            tbutce=int(dosya.readlines()[0])
        tbutce=tbutce-toplamMaas
        with open("butce.txt", "w") as dosya:
            dosya.write(str(tbutce))
    def masrafGir(self):
        with open("masraflar.txt", "r") as dosya:
            masraflar=dosya.readlines()
        masrafs= input("Masrafınız ne kadar:")
        masrafint=int(masrafs)
        masrafDescription=input(" Masraf açıklamasını giriniz:")
        with open("masraflar.txt","a+")as dosya:
            """dosya.write(str(masrafs +(" ")+ masrafDescription))"""
            dosya.write("masraf:{} aciklama: {} \n".format(masrafs,masrafDescription))
        with open("butce.txt", "r")  as dosya:
            butce=int(dosya.readlines()[0])
        newbutce=butce-masrafint
        print("Masraf Açıklaması: {} ---- Masraf: {}".format(masrafDescription,masrafs))
        print("Yeni Butceniz:" + str(newbutce))
        with open("butce.txt", "w") as dosya:
            dosya.write(str(newbutce))
    def gelirGir(self):
        with open("gelirler.txt", "r") as dosya:
            gelirler=dosya.readlines()
        gelirs= input("Geliriniz ne kadar:")
        gelirint=int(gelirs)
        gelirDescription=input(" Gelir açıklamasını giriniz:")
        with open("gelirler.txt", "a+") as dosya:
            dosya.write("gelir:{} aciklama: {} \n".format(gelirs,gelirDescription))
        with open("butce.txt", "r")  as dosya:
            butce=int(dosya.readlines()[0])
        newbutce=butce+gelirint
        print("Gelir Açıklaması: {} ---- Gelir: {}".format(gelirDescription,gelirs))
        print("Yeni Butceniz:" + str(newbutce))
        with open("butce.txt", "w") as dosya:
            dosya.write(str(newbutce))
        
sirket = Sirket("Rigel")

while sirket.calisma:
    sirket.program()