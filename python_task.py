#CHINGIZ ZAIDOV
#659.22S

SPRINT 3_A
1)
x = input("X dəyərini daxil edin: ")

## Ilk once user herf de daxil ede biler . Ona gorede yoxlayiriq
if x.replace('.', '', 1).isdigit() or (x.startswith('-') and x[1:].replace('.', '', 1).isdigit()):
    x = float(x)
    if x > 0:
        print("müsbət")
    elif x < 0:
        print("mənfi")
    else:
        print("sıfır")
else:
    print("Yalniz reqem daxil ede bilersiz...")


2)
n = input("Bir ədəd daxil edin: ")

###Reqemdirse davam etsin
if n.isdigit():
    n = int(n)
    if n % 2 == 0:
        print("cüt")
    else:
        print("tək")
else:
    print("Yalniz reqem daxil ede bilersiz...")


3)
a = input("A dəyərini daxil edin: ")
b = input("B dəyərini daxil edin: ")
c = input("C dəyərini daxil edin: ")

###Reqemdirmi
if a.isdigit() and b.isdigit() and c.isdigit():
    a, b, c = int(a), int(b), int(c)
    print("Ən böyük rəqəm:", max(a, b, c))
else:
    print("Yalniz reqem daxil ede bilersiz...")



4)
day = input("Həftə gününü (1-7) daxil edin: ")

if day.isdigit():
    day = int(day)
    if 1 <= day <= 7:
        days = ["Bazar ertəsi", "Çərşənbə axşamı", "Çərşənbə", "Cümə axşamı", "Cümə", "Şənbə", "Bazar"]
        print(days[day-1])##Cunki index 0dan baslayir
    else:
        print("Yanlış gün - 1 ilə 7 arasında bir rəqəm daxil edin.")
else:
    print("Yalniz reqem daxil ede bilersiz...")


5)
temp = input("Temperaturu daxil edin: ")

if temp.replace('.', '', 1).isdigit() or (temp.startswith('-') and temp[1:].replace('.', '', 1).isdigit()):
    temp = float(temp)
    if temp < 0:
        print("soyuq")
    elif 0 <= temp <= 20:
        print("normal")
    else:
        print("isti")
else:
    print("Yalniz reqem daxil ede bilersiz...")


6)
password = input("Şifrəni daxil edin: ")

if len(password) < 8:
    print("qısa")
elif 8 <= len(password) <= 12:
    print("orta")
else:
    print("uzun")


7)
x = input("Bir ədəd daxil edin: ")

if x.isdigit():
    x = int(x)
    if x % 3 == 0 and x % 5 == 0:
        print("3 və 5")
    elif x % 3 == 0:
        print("3")
    elif x % 5 == 0:
        print("5")
    else:
        print("heç biri")
else:
    print("Yalniz reqem daxil ede bilersiz...")


8)
##range 0-20 arasindaki ededleri 2-2 cap edir
for i in range(0, 21, 2):
    print(i, end=" ")


9)
##end funksiyasi indexleri ayirir,veridyimiz category -e esasen mes: ","
string = "Bağda ərik var idi …"
for char in string:
    print(char, end=" ")


10)
for i in range(1, 11):
    if i != 3:
        print(i, end=" ")


11)
i = 1
while True:
    if i % 5 == 0:
        print(i)
        break
    i += 1


12)
##Burada istediyimiz eded ola biler listde olan
numbers = [1, 3, 5, 7, 9]
for index, value in enumerate(numbers):
    if value == 5:
        print(f"5-in indeksi: {index}")
        break






SPRINT 3_B
1)
def sayHello():
  print("Salam, Dünya!")


sayHello()



2)
def kub_hesabla(n):
  if isinstance(n, (int, float)):
    return n ** 3
  else:
    return "Error : Yalniz reqem daxil ede bilersiniz..."

print(kub_hesabla(2))

3)
def birlesdir(soz1, soz2):
  if all(isinstance(s, str) for s in [soz1, soz2]):
    return f"{soz1} {soz2}"
  else:
    return "Error : Yalniz string tipinde melumat daxil edin..."


print(birlesdir("Menim adim", "Cingizdir."))




4)
def cap_et(lst):
  if isinstance(lst, list):
    for i in lst:
      print(f"{i}) : {i}")
  else:
    print("Error : Yalniz list daxil etmelisiniz...")

cap_et([1, 2, 3, 4])



5)
def toplam(*args):
  if all(isinstance(i, (int, float)) for i in args):
    return sum(args)
  else:
    return "Error : Yalniz reqem daxil etmlisiniz..."


print(toplam(1, 2, 3, 4))


6)
def ortalama(*args):
  if not args:
    return "Rəqəm yoxdur"
  elif all(isinstance(i, (int, float)) for i in args):
    return sum(args) / len(args)
  else:
    return "Error : Yalniz reqm daxil etmelisiniz"


print(ortalama(10, 20, 53))


7)
def adlar_rəqəmlər(**kwargs):
  if not kwargs:
    print("Heleki cut daxil etmemisiniz...")
  else:
    for ad, reqem in kwargs.items():
      print(f"ad: {ad}, reqem: {reqem}")


adlar_rəqəmlər(Murad=79.43, Chingiz=89.21, Kaha=82.4)


8)Burada butun tipleri yazmaq olar , sadece kod uzunlugudur.Lazim olarsa yazmaq olar
def tip_yoxla(deyer):
  if isinstance(deyer, str):
    print("Tip: metn")
  elif isinstance(deyer, (int, float)):
    print("Tip: reqem")
  elif isinstance(deyer , list):
    print("Tip: list")
  else:
    print("Tip: other type")

tip_yoxla("salam")
tip_yoxla(42)
tip_yoxla([1, 2])



9)Burada orta yasli, qoca falan da yazmaq olar ,yeni istediyimiz qeder conditon qoya bilerik
def yas_kateqoriya():
  yas = input("Yashinizi daxil edin:")
  if yas.isdigit():
    yas = int(yas)
    if yas < 18:
      print("Genc")
    else:
      print("Yetkin")
  else:
    print("Error : Yalniz reqem daxil edilmelidir...")

yas_kateqoriya()




10)
def soz_uzunluq():
  soz = input("Bir soz daixl edin: ")
  if soz.isalpha():
    print(f"Soz uzunlugu : {len(soz)}")
  else:
    print("Error : Yalniz herf daxil etmelisiniz...")

soz_uzunluq()







SPRINT 4_A
1)
def kalkulyator():
  try:
    a = float(input("Ilk ededi daxil edin :"))
    b = float(input("Ikinci ededi daxl edin : "))
    operation = input("Emeliyyat daxil edin (+, -, *, /): ")

    if operation == "+":
      print("Netice:", a + b)
    elif operation == "-":
      print("Netice:", a - b)
    elif operation == "*":
      print("Netice:", a * b)
    elif operation == "/":
      if b == 0:
        print("Error : 0-a bolmek olmaz...")
      else:
        print("Netice:", a / b)
    else:
      print("Error : Duzgun emeliyyat daxil etmemisiniz ...")

  except ValueError:
    print("Error : Reqem evezine basqa ddyer daxil etmisiniz ...")
  except TypeError:
    print("Error : Deyer uygunsuzlugu...")
  finally:
    print("Hesablama bitti...")

kalkulyator()



2)
def bolunenler():
  return [i for i in range(1, 51) if i % 11 == 0]

print(bolunenler())  # [11, 22, 33, 44]




3)
def ilk_herfler(sozler):
  return [soz[0] for soz in sozler if isinstance(soz, str) and soz]

print(ilk_herfler(["Chingiz", "Mobile", "developer", "olmaq", "isteyir..."]))



4)
def seher_kodlar(seherler, kodlar):
  if len(seherler) == len(kodlar):
    return dict(zip(seherler, kodlar))
  else:
    return "Error : SIyahilarin uzunluqlari ferqlidir.Zehmet olmasa seher ve kod eyni sayda olsun!"

print(seher_kodlar(["Quba", "Baki", "Gence"], [40, 90, 20]))





5)
km_to_mil = lambda km: round(km * 0.621371, 3)
print([km_to_mil(km) for km in [1, 5, 10, 21, 100]])




6)
qiymetler = [100, 200, 300, 400]
vergi_ile = list(map(lambda x: round(x * 1.18, 2), qiymetler))
print(vergi_ile)




7)Burada istediyimiz condition vere bilerik
siyahi1 = [3, 7, 12]
siyahi2 = [2, 4, 6]

cem = list(map(lambda x, y: (x * 2) + (y * 2), siyahi1, siyahi2))
print(cem)




8)
from functools import reduce

qiymetler = [150, 80, 220, 45]
minimum = reduce(lambda x, y: x if x < y else y, qiymetler)

print("En kicik eded : ", minimum)