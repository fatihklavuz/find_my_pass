arn=input("Kullandığın paraolayı gir :").strip()
f=open("a.csv","r",encoding="utf8")
strn=0
blgstrsy=0
for x in f:
    blgstrsy+=1*2
    strn+=1*2
    iyicebibakbakim=f.readline().find(arn)
    if iyicebibakbakim !=-1:
        print("parolan olan " ,arn,"kelimesi",strn,"satır içinde bulundu")
print("Belge içinde toplam ",blgstrsy," adet parola vardır")
f.close()


