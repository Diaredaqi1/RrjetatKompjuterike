import socket
import time 
import sys
print('\n')
print('====================================================================================================================')
print('FIEK-UDP Klienti')
print('====================================================================================================================')
x = input('\nKeni mundesi te nderroni emrin e serverit dhe portin, nese doni t\'i nderroni shtypni Y perndryshe N:  ')

if x == 'Y' or x == 'y':
  serverName=input('Emri i serverit: ')
  serverPort=int(input('Porti i serverit: ')) #Kufizojme me int vetem nje vlere numerike
else:
  serverName = 'localhost' #formati i IP: 127.0.0.1
  serverPort = 14000
try:
     sClienti= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     sClienti.connect((serverName,serverPort))
except Exception:
    print("Nuk eshte realizuar lidhja mes klientit dhe serverit.")
    time.sleep(60)
         


while True:
   print('\n====================================================================================================================')
   print('Ky program permbane keto operacione: \n-IP \n-NRPORTIT \n-NUMERO teksti \n-ANASJELLTAS teksti \n-PALINDROM teksti \n-KOHA \n-LOJA \n-GCF Nr1 Nr2 \n-KONVERTO Opsioni(cmNeInch,inchNeCm,kmNeMiles,mileNeKm) Nr \n-SYP Nr1 Nr2 \n-FAKTORIEL Nr \n-VITIBRISHTE Nr')
   print('\n====================================================================================================================')
   print('\n---Nese doni te dilni nga programi shkruani FUND!')
   print('---Nese kerkesa juaj eshte e zbrazet poashtu programi mbyllet\n')
   k=input('Shkruani kerkesen tuaj ketu: ').upper()
   print("\n")
   pergjigjja = ''
   sClienti.sendto(k.encode(),(serverName,serverPort))
   data, address = sClienti.recvfrom(128)
   pergjigjja += data.decode("utf-8")
   print('Pergjigjja: ' + pergjigjja)
sClienti.close()
