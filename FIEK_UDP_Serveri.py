import socket
import datetime
import random
from datetime import date

serverName = 'localhost'
serverPort = 14000

serverS = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverS.bind((serverName,serverPort))
print('\n')
print('====================================================================================================================')
print('FIEK-UDP Serveri')
print('====================================================================================================================')
print("Ne pritje te kerkeses suaj...")

#M1 -> IP-adresa e klientit
def IP():
    hostname = socket.gethostname()
    x = socket.gethostbyname(hostname)
    return ("IP Adresa e klientit është: "+ str(x))


#M2 -> Porti i klientit
def NRPORTIT():
    return ("Klienti është duke përdorur portin "+str(address[1]))


#M3 -> Numrimi i zanoreve dhe bashketingelloreve
def NUMERO(teksti):
   
    zanore = 0
    bashketingellore = 0

    for i in range(0, len(teksti)):  
          
        s = teksti[i]  
  
        if (s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u' or s == 'y' 
            or s == 'A' or s == 'E' or s == 'I' or s == 'O' or s == 'U' or s == 'Y' ): 
            zanore += 1
               
        elif (s >= 'a' and s <= 'z') or (s >= 'A' and s <= 'Z' ): #Me i evitu hapesirat
            bashketingellore += 1 
    return (' Teksti i pranuar përmban: ' + str(zanore) + ' zanore' + ' dhe ' + str(bashketingellore) + ' bashkëtingëllore')



#M4 -> Serveri kthen Tekstin e anasjelltë (reversë)
def ANASJELLTAS(teksti):
    t=teksti[::-1]
    return t



#M5 -> Serveri duhet te tregoj se a është fjala e dhënë palindrome
def PALINDROM(teksti):
    t=teksti[::-1]
    if teksti == t:
        return 'Teksti i dhënë është palindrome'
    else:
        return 'Teksti i dhënë nuk është palindrome'
   


#M6 -> Koha aktuale e serverit(formati: 10.04.2020 11:00:00 PM)
def KOHA():
    x=datetime.datetime.now()
    y=x.strftime("%d" + "." +"%m" + "." + "%Y" + " " + "%I:%M:%S %p")
    return( y )



#M7 -> Kthen 5 numra nga rangu [1,35]-rezultati duhet te jete i sortuar
def LOJA():
    v = set() #Inicializimi i nje seti bosh 
    for x in range(5):  
        rangu = random.randint(1, 35) #I marrim 5 numra random (1 deri 35) dhe i ruajme ne variablen rangu
        v.add(rangu) #Numrat qe caktohen prej random i shtojme ne variablen v
        y=sorted(v)  #Sortojme 
    return y



#M8 ->Faktori me i madh i perbashket i dy numrave
def GCF(x,y):
    if x > y:
       nrVogel = y
    else:
        nrVogel = x
    for i in range(1, nrVogel+1):
        if((x % i == 0) and (y % i == 0)):
            faktoriM = i
              
    return faktoriM



#M9 -> Konverton cmNeInch(1cm=0.39inch), inchNeCm(1inch=2.54cm), kmNeMiles(1km=0.62miles), mileNeKm(1mile=1.6km)
def KONVERTO(opsioni, x):
    if (opsioni == "CMNEINCH"):
        return str(x * 3.94/10) + ' inch'
    elif (opsioni == "INCHNECM"):
        return str(x * 2.54) + ' cm'
    elif (opsioni == "KMNEMILES"):
        return str(x * 0.62) + ' mile'
    elif (opsioni == "MILENEKM"):
        return str(x * 1.6) + ' km'
    else:
        return 'Komande e gabuar.Menyra sesi duhet shkruar KONVERTO Opsioni(cmNeInch,inchNeCm,kmNeMiles,mileNeKm) Vlera'

#MSH2 -> Gjen factorielin e nje numri
def SYP(width, height):
        Area = width * height
        return Area

#MSH2 -> Gjen factorielin e nje numri
def FAKTORIEL(n):
    if n == 1:
        return n
    elif n < 1:
        return ("Numer negativ")
    else:
        return n*FAKTORIEL(n-1)
    print (FAKTORIEL(int(num)))

#MSH3 -> Tregon nese viti i futur si input eshte i brishte 
def VITIBRISHTE(year):
        if (year % 4) == 0:
          if (year % 100) == 0:
              if (year % 400) == 0:
                  return str("{0} eshte vit i brishte".format(year))
              else:  
                  return str("{0} nuk eshte vit i brishte".format(year))
          else:
             return str("{0} eshte vit i brishte".format(year))
        else:  return str("{0} nuk eshte vit i brishte".format(year))


while True:
            kerkesa,address =serverS.recvfrom(128)
            kerkesa.upper()
            kerkesa = kerkesa.decode("utf-8")
            m = kerkesa.split(' ')
            print('Kerkesa nga klienti:' + kerkesa)

            #Thirrja e metodave
            if m[0] == "IP":
                pergjigjja=str(IP())
                serverS.sendto(str.encode(pergjigjja),address)
            elif m[0] == "NRPORTIT":
                pergjigjja = str(NRPORTIT())
                serverS.sendto(str.encode(pergjigjja),address)
            elif m[0] == "KOHA":
                pergjigjja = str(KOHA())
                serverS.sendto(str.encode(pergjigjja),address)
            elif m[0] == "LOJA":
                pergjigjja = str(LOJA())
                serverS.sendto(str.encode(pergjigjja),address)
            elif m[0] == "NUMERO":
                pergjigjja = str(NUMERO(kerkesa[len(m[0]):len(kerkesa)]))
                serverS.sendto(str.encode(pergjigjja),address)
            elif m[0] == "ANASJELLTAS":
                pergjigjja = str(ANASJELLTAS(kerkesa[len(m[0]):len(kerkesa)]))
                serverS.sendto(str.encode(pergjigjja),address)
            elif m[0] == "PALINDROM" :
                pergjigjja = str(PALINDROM(m[1]))      
                serverS.sendto(str.encode(pergjigjja),address)
                
            elif(m[0]=="GCF"):
             try:
              v1=int(m[1])
              v2=int(m[2])
              pergjigjja=str(GCF(v1,v2)) 
             except Exception:
                pergjigjja="Keni dhene ndonje karakter ne vend te vleres!"
             serverS.sendto(str.encode(pergjigjja),address)

            elif(m[0]=="SYP"):
             try:
              v1=float(m[1])
              v2=float(m[2])
              pergjigjja=str(SYP(v1,v2)) 
             except Exception:
                pergjigjja="Keni dhene ndonje karakter ne vend te vleres!"
             serverS.sendto(str.encode(pergjigjja),address)

            elif(m[0]=="FAKTORIEL"):
             try:
              v1=int(m[1])
              pergjigjja=str(FAKTORIEL(v1)) 
             except Exception:
                pergjigjja="Keni dhene ndonje karakter ne vend te vleres!"
             serverS.sendto(str.encode(pergjigjja),address)

            elif(m[0]=="VITIBRISHTE"):
             try:
              v1=int(m[1])
              pergjigjja=str(VITIBRISHTE(v1)) 
             except Exception:
                pergjigjja="Keni dhene ndonje karakter ne vend te vleres!"
             serverS.sendto(str.encode(pergjigjja),address)

            elif(m[0]=="KONVERTO"):
             try:
                vlera=float(m[2])
                pergjigjja=str(KONVERTO(m[1], vlera))
             except Exception:
                pergjigjja="Keni dhene shkronje ne vend te vleres!"
             serverS.sendto(str.encode(pergjigjja),address)
            else: 
                pergjigjja = "Kjo kerkese nuk eshte valide!/n"
                serverS.sendto(str.encode(pergjigjja),address)


                
