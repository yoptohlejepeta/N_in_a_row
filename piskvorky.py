import string
import random
import copy

def pole():
  nradku = int(input('Zadej počet řádků: '))
  nsloupcu = int(input('Zadej počet sloupců: '))
  matice = [['_' for j in range(nsloupcu)] for i in range(nradku)]
  return matice, nradku, nsloupcu

def players():
  hráči = {}
  počet_hráčů = int(input('Kolik hraje hráčů?: '))
  počet_AI = int(input('Kolik hraje počítačů?: '))
  znaky_pro_AI = list(string.ascii_lowercase)
  for i in range(počet_hráčů):
    hrac_jmeno = input('Zadej své jméno: ')
    hrac_znak = input('Jaký chceš mít znak?: ')
    if hrac_znak in znaky_pro_AI:
      znaky_pro_AI.remove(hrac_znak)
    elif hrac_znak in hráči.values():
      hrac_znak = input('Tento znak je již obsazený! Zadej jiný znak: ')
    hráči[hrac_jmeno] = hrac_znak
  for i in range(počet_AI):
    znak_pocitac = random.choice(znaky_pro_AI)
    hráči[f'počítač{i+1}'] = znak_pocitac
    znaky_pro_AI.remove(znak_pocitac)
  return hráči

def kola(slovník, matice, kolo, nradku, nsloupcu):
  počet_hráčů = len(slovník.keys())
  rada = kolo % počet_hráčů
  hrajici_hrac = list(slovník.keys())[rada]
  print(f'Na řadě je {hrajici_hrac}.')
  if hrajici_hrac.startswith('počítač'):
    radek, sloupec = random.randint(1,nradku),random.randint(1,nsloupcu)
    while matice[radek-1][sloupec-1] != '_':
      radek, sloupec = random.randint(1,nradku),random.randint(1,nsloupcu)
    matice[radek-1][sloupec-1] = slovník.get(hrajici_hrac)
  else:
    radek, sloupec = map(int, input('Do jakého řádku a sloupce chceš umístit svůj znak? ').split(','))
    while matice[radek-1][sloupec-1] != '_':
      radek, sloupec = map(int, input('Trumbero! Do tohoto pole už někdo psal. Zkus jiné: ').split(','))
    matice[radek-1][sloupec-1] = slovník.get(hrajici_hrac)
  return matice, hrajici_hrac

def výhra(matice, hráči, konec):
  for radek in matice:
    for znak in hráči.values():
      if (radek.count(znak) > 2):
        a = radek.index(znak)
        if radek[a+1] == znak and radek[a+2] == znak:
             konec = True 
  return konec

def transponovana_matice(matice):
  transponovanamatice = list(map(list, zip(*matice)))
  return transponovanamatice

def doplneni_diagonal1(matice):
  matice2 = copy.deepcopy(matice)
  for radek in matice2:
    for i in range(len(radek)- matice2.index(radek)):
      radek.insert(0,'_')
    for i in range(matice2.index(radek)):
      radek.append('_')
  matice2 = list(map(list, zip(*matice2)))
  return matice2

def doplneni_diagonal2(matice):
  matice3 = copy.deepcopy(matice)
  for radek in matice3:
    for i in range(matice3.index(radek) + len(radek)):
      radek.insert(0,'_')
    for i in range(matice3.index(radek)):
      radek.append('_')
  matice3 = list(map(list, zip(*matice3)))
  return matice3

def piskvorky():
  konec = False
  hráči = players()
  matice, nradku, nsloupcu = pole()
  kolo = 0
  while not konec:
    for radek in matice:
      print(radek)
    matice, hrajici_hrac = kola(hráči, matice, kolo, nradku, nsloupcu)
    transponovanamatice = transponovana_matice(matice)
    matice2 = doplneni_diagonal1(matice)
    matice3 = doplneni_diagonal2(matice)                              
    konec = výhra(matice, hráči,konec)
    konec = výhra(transponovanamatice, hráči, konec)
    konec = výhra(matice2, hráči, konec)
    konec = výhra(matice3, hráči, konec)
    kolo += 1
  if konec == True:
    for radek in matice:
      print(radek)
    print(f'Vyhrává {hrajici_hrac}! ')

piskvorky()