import socket

print('\n')
print('====================================================================================================================')
print('FIEK-TCP Klienti')
print('====================================================================================================================')
x = input('\nKeni mundesi te nderroni emrin e serverit dhe portin, nese doni t\'i nderroni shtypni Y perndryshe N:  ')

if x == 'Y' or x == 'y':
  serverName=input('Emri i serverit: ')
  serverPort=int(input('Porti i serverit: ')) #Kufizojme me int vetem nje vlere numerike
else:
  serverName = 'localhost' #formati i IP: 127.0.0.1
  serverPort = 14000

soketiK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soketiK.connect((serverName,serverPort))


while True:
  print('\n====================================================================================================================')
  print('Ky program permbane keto operacione: \n-IP \n-NRPORTIT \n-NUMERO teksti \n-ANASJELLTAS teksti \n-PALINDROM teksti \n-KOHA \n-LOJA \n-GCF Nr1 Nr2 \n-KONVERTO Opsioni(cmNeInch,inchNeCm,kmNeMiles,mileNeKm) Nr \n-SYP Nr1 Nr2 \n-FAKTORIEL Nr \n-VITIBRISHTE Nr')
  print('\n====================================================================================================================')
  print('\n---Nese doni te dilni nga programi shkruani FUND!')
  print('---Nese kerkesa juaj eshte e zbrazet poashtu programi mbyllet\n')
  k=input('Shkruani kerkesen tuaj ketu: ').upper()
  print("\n")
  #Kerkesa nuk duhet te kete me teper se 128 karaktere
  a = len(k)
  if(a>128):
      print('Kerkesa permbane me teper se 128 karaktere')
      continue
    #validojme hyrjen e metodava me argumente
  if k == 'NUMERO':
      print('\n--Keni harruar argumentin! Duhet te shkruani NUMERO teksti.')
      continue
  elif k == 'ANASJELLTAS':
      print('\n--Keni harruar argumentin! Duhet te shkruani ANASJELLTAS teksti.')
      continue
  elif k == 'PALINDROM':
      print('\n--Keni harruar argumentin! Duhet te shkruani PALINDROM teksti.')
      continue
  elif k == 'GCF':
      print('\n--Keni harruar argumentin! Duhet te shkruani GCF Nr1 Nr2.')
      continue
  elif k == 'KONVERTO':
      print('\n--Keni harruar argumentin! Duhet te shkruani KONVERTO Opsioni(cmNeInch,inchNeCm,kmNeMiles,mileNeKm) Nr.')
      continue
  elif k == 'SYP':
      print('\n--Keni harruar argumentin! Duhet te shkruani SYP Nr1 Nr2.')
      continue
  elif k == 'VITIBRISHTE':
      print('\n--Keni harruar argumentin! Duhet te shkruani VITIBRISHTE Nr1 ')
      continue
  elif k == 'FIBONACI':
      print('\n--Keni harruar argumentin! Duhet te shkruani FIBONACI Nr1 ')
      continue

  elif k == 'FUND':
      break
  elif k=='':
    break
  
  soketiK.send(k.encode('utf-8'))
  pergjigjja = soketiK.recv(128)
  print("Përgjigjja: " + pergjigjja.decode('utf-8'))
  print('\n')

soketiK.close()