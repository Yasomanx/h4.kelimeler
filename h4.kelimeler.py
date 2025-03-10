import string
g="""Süper Ligin 27. haftasında sahasında ağırladığı Hatayspora 2-1
   mağlup olan Trabzonsporda bu yenilginin yankıları sürüyor. Bordo-Mavililer,
    beklenen performansın sergilenememesi sonrası hoca değişikliğine hazırlanıyor

Bordo-Mavililer, Hatayspor karşısında bu sezon rakip ceza sahasında
en fazla topla buluştuğu (47 kez) ve en fazla orta yaptığı (38) maçı kaybetti.
3 net pozisyon kaçıran, 1 defa da direğe takılan Trabzonspor,
son 5 lig maçını kazandığı evinde bu kez yenildi. Hataysporun Trabzonda kazanmasıyla,
Süper Ligde dış sahada galibiyeti bulunmayan tek takım olarak Trabzonspor kaldı"""
kelimeler=g.split()
def donustur(a):
  sayac=[]
  x = a.split()
  sayac=0
  for harf in range(len(x)):
    sayac+=1
    print(sayac)
  sayac.append(sayac)
  return sayac
b=donustur
