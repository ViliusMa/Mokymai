# Pirma uzduotis

# import datetime

# pradzios_data = input("Įveskite pradžios datą (pvz. 2000-02-02 02:02:02): ")
# data1 = datetime.datetime.strptime(pradzios_data, "%Y-%m-%d %H:%M:%S")
# pabaigos_data = input("Įveskite pabaigos datą (pvz. 2000-02-02 02:02:02): ")
# data2 = datetime.datetime.strptime(pabaigos_data, "%Y-%m-%d %H:%M:%S")
# skirtumas = data1 - data2
# print("Praėjo sekundžių tarp įvestų datų: ", round(skirtumas.total_seconds()))
#
# Antra uzduotis
#
# import datetime
#
# now = datetime.datetime.now()
# print(now)
# five_days_before = now - datetime.timedelta(days=5)
# print(five_days_before)
# eight_hours_ahead = now + datetime.timedelta(hours=8)
# print(eight_hours_ahead)
# print(now.strftime("%Y %m %d, %H:%M:%S"))
#
#
# Trecia uzduotis
#
# import datetime
#
# data = input("Įveskite savo gimimo datą ir laiką (pvz. 2000-02-02 02:02:02): ")
# data1 = datetime.datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
# print(data1)
# skirtumas = datetime.datetime.now() - data1
# skirtumas_metuose = (skirtumas.days + skirtumas.seconds / 86400) / 365
# print("Praėjo metų: ", round(skirtumas_metuose))
# skirtumas_menesiuose = ((skirtumas.days + skirtumas.seconds / 86400) / 365) * 12
# print("Praėjo mėnesių: ", round(skirtumas_menesiuose))
# print("Praėjo dienų: ", skirtumas.days)
# print("Praėjo valandų: ", round(skirtumas.days) * 24)
# print("Praėjo minučių: ", round(skirtumas.days) * 24 * 60)
# print("Praėjo sekundžių: ", skirtumas.total_seconds())
#
#
# Ketvirta uzduotis 1dalis
#
# import datetime
#
# while True:
#    try:
#        pradzios_data = input("Įveskite pradžios datą (pvz. 2000-02-02 02:02:02): ")
#        data1 = datetime.datetime.strptime(pradzios_data, "%Y-%m-%d %H:%M:%S")
#        break
#    except ValueError:
#        print("Įvedėte klaidingai, bandykite dar kartą")
#
# while True:
#    try:
#        pabaigos_data = input("Įveskite pabaigos datą (pvz. 2000-02-02 02:02:02): ")
#        data2 = datetime.datetime.strptime(pabaigos_data, "%Y-%m-%d %H:%M:%S")
#        break
#    except ValueError:
#        print("Įvedėte klaidingai, bandykite dar kartą")
#
# skirtumas = data1 - data2
# print("Praėjo sekundžių tarp įvestų datų: ", round(skirtumas.total_seconds()))
#
#
#
# Ketvirta uzduotis antra dalis
#
# import datetime
#
# while True:
#    try:
#        data = input("Įveskite savo gimimo datą ir laiką (pvz. 2000-02-02 02:02:02): ")
#        data1 = datetime.datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
#        break
#    except ValueError:
#        print("Įvedėte klaidingai, bandykite dar kartą")
#
# print(data1)
# skirtumas = datetime.datetime.now() - data1
# skirtumas_metuose = (skirtumas.days + skirtumas.seconds / 86400) / 365
# print("Praėjo metų: ", round(skirtumas_metuose))
# skirtumas_menesiuose = ((skirtumas.days + skirtumas.seconds / 86400) / 365) * 12
# print("Praėjo mėnesių: ", round(skirtumas_menesiuose))
# print("Praėjo dienų: ", skirtumas.days)
# print("Praėjo valandų: ", round(skirtumas.days) * 24)
# print("Praėjo minučių: ", round(skirtumas.days) * 24 * 60)
# print("Praėjo sekundžių: ", skirtumas.total_seconds())
#
#
# Penkta uzduotis


# import datetime

# while True:
#    try:
#        time = input("Įveskite x sekundę/es: ")
#        time1 = datetime.datetime.strptime(time, "%S")
#        break
#    except ValueError:
#            print("Įvedėte klaidingai, bandykite dar kartą")
# y = input("Įveskite žodį: ")
# print("Jūsų žodis: ", y)


# Ketvirta paskaita

# Pirma uzduotis
# 1
# def suma():
#    a = 1
#    b = 2
#    c = 3
#    d = a + b + c
#    print(d)
# suma()

# 2

# def saraso_suma(skaicius1=1, skaicius2=2, skaicius3=3):
#    suma = skaicius1 + skaicius2 + skaicius3
#    print(suma)
# saraso_suma()

# 3

# def didziausias_skaicius(*args):
#    return max(args)
#
# print(didziausias_skaicius(1, 2, 3))

# 4

# def zodis_atbulai(zodis):
#    return zodis[::-1]
# print(zodis_atbulai("Labas"))

# 5

# def kiekis(zodis):
#    zodziu_kiekis = len(zodis.split())
#    didziosios = sum(1 for x in zodis if x.isupper())
#    mazosios = sum(1 for x in zodis if x.islower())
#    skaiciai = sum(1 for x in zodis if x.isdigit())
#    return zodziu_kiekis, didziosios, mazosios, skaiciai
# zodis = "Labas Rytas 526"
# zodziu_kiekis, didziosios, mazosios, skaiciai = kiekis(zodis)
# print(zodis)
# print(f"Žodžių kiekis sakinyje: {zodziu_kiekis}\nDidžiųjų raidžių kiekis sakinyje: {didziosios}\nMažųjų raidžių kiekis sakinyje: {mazosios}\nSkaičių kiekis sakinyje: {skaiciai}")


# 6

# sarasas = [1, 2, 2, 3, 1, 1, 3, 3, 2]
# def unikalus_elementai(sarasas):
#    unikalus = []
#    for elementas in sarasas:
#        if elementas in unikalus:
#            continue
#        else:
#            unikalus.append(elementas)
#    return unikalus
#
# print(unikalus_elementai(sarasas))
#
#
# 7

# skaicius = int(input("Įrašykite skaičių: "))
# if skaicius > 1:
#    for x in range(2, skaicius):
#        if (skaicius % x) == 0:
#            print(skaicius, "nėra pirminis skaičius")
#            break
#    else:
#        print(skaicius, "yra pirminis skaičius")
# else:
#    print(skaicius, "nėra pirminis skaičius")
#
#
# 8
#
#
# def is_kito_galo(sakinys):
#    zodziai = sakinys.split()
#    return " ".join(zodziai[::-1])
#
#
# print(is_kito_galo("Laba diena visiems"))
#
#
# 9

# def keliamieji_metai(metai):
#    return metai % 4 == 0 and (metai % 100 != 0 or metai % 400 == 0)
#
#
# print(keliamieji_metai(2000))

# 10
#
# import datetime
#
# def skirtumas():
# dabartis = datetime.datetime.now()
# praeitis = datetime.datetime(1999, 8, 21, 9, 2, 29)
# skirtumas1 = dabartis - praeitis
# metai = skirtumas1.days // 365
# menesiai = (skirtumas1.days % 365) // 30
# dienos = (skirtumas1.days % 365) % 30
# valandos = skirtumas1.seconds // 3600         totaal.seconds
# minutes = (skirtumas1.seconds % 3600) // 60
# sekundes = (skirtumas1.seconds % 3600) % 60
# print(praeitis)
# print(f"Praėjo: \n{metai} metų\n{menesiai} mėnesių\n{dienos} dienų\n{valandos} valandų\n{minutes} minučių\n{sekundes} sekundžių")
#
# skirtumas()

# 2uzduotis
# 1
# def patikrinti(skaicius):
#    x = str(skaicius)
#    y = len(x)
#    if y % 2 == 0:
#        pirma_puse = x[:y // 2]
#        antra_puse = x[y // 2:]
#        if pirma_puse == antra_puse:
#            return True
#    return False
#
# print(patikrinti(1212))
#
# 2

# from datetime import datetime
#
#
# def generate_personal_code(gender, birthdate, order_number):
#    if gender.lower() == "vyras":
#        gender_number = 3
#    elif gender.lower() == "moteris":
#        gender_number = 4
#    else:
#        raise ValueError("Neteisinga lytis")
#
#    birthdate_obj = datetime.strptime(birthdate, "%Y-%m-%d")
#    year = birthdate_obj.year % 100
#    month = birthdate_obj.month
#    day = birthdate_obj.day
#
#    order_number_str = str(order_number).zfill(4)
#
#    base_code = f"{gender_number}{year:02d}{month:02d}{day:02d}{order_number_str}"
#    factors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
#    checksum = sum([int(base_code[i]) * factors[i] for i in range(10)]) % 11
#    if checksum == 10:
#        base_code += "0"
#    else:
#        base_code += str(checksum)
#
#    return base_code
#
#
# print(generate_personal_code("vyras", "1993-08-21", 1489))


# 5 paskaita
#
# 1 uzduotis
#
# class Sakinys:
#    def __init__(self, tekstas):
#        self.tekstas = tekstas
##
#    def atbulai(self):
#        return self.tekstas[::-1]
#
#    def mazosios_raides(self):
#        return self.tekstas.lower()
#
#    def didziosios_raides(self):
#        return self.tekstas.upper()
#
#    def zodis(self, numeris):
#        zodziai = self.tekstas.split()
#        if numeris > len(zodziai):
#            return "Sakinyje nėra tiek žodžių."
#        return zodziai[numeris - 1]
#
#    def zodziu_kiekis(self):
#        return len(self.tekstas.split())
#
#    def simboliu_kiekis(self):
#        return len(self.tekstas)
#
#    def zodziu_keitimas(self, senas_zodis, naujas_zodis):
#        return self.tekstas.replace(senas_zodis, naujas_zodis)
#
#    def didziuju_kiekis(self):
#        return sum(1 for didzioji in self.tekstas if didzioji.isupper())
#
#    def mazuju_kiekis(self):
#       return sum(1 for mazoji in self.tekstas if mazoji.islower())
#
#    def kiekis(self):
#        print(f"Sakinys: {self.tekstas}\nŽodžių kiekis: {self.zodziu_kiekis()}\nSimbolių kiekis: {self.simboliu_kiekis()}\nDidžiųjų raidžių kiekis: {self.didziuju_kiekis()}\nMažųjų raidžių kiekis: {self.mazuju_kiekis()}")

# sakinys1 = Sakinys("Labas rytas visiems")
# sakinys2 = Sakinys("Viso gero")
# sakiniai = [sakinys1, sakinys2]
# print(sakinys1.tekstas)
# print(sakinys1.atbulai())
# print(sakinys1.mazosios_raides())
# print(sakinys1.didziosios_raides())
# print(sakinys1.zodis(2))
# print(sakinys1.zodziu_kiekis())
# print(sakinys1.simboliu_kiekis())
# print(sakinys1.zodziu_keitimas("rytas", "vakaras"))
# sakinys1.kiekis()

# 2uzduotis

# import datetime
# class Sukaktis:
#    def __init__(self, year: int, month: int, day: int):
#        self.date = datetime.datetime(year=year, month=month, day=day)
#
#    def praejo_metu(self):
#        today = datetime.datetime.today()
#        return today.year - self.date.year
#
#    def praejo_menesiu(self):
#        today = datetime.datetime.today()
#        return (today - self.date).days // 7
#
#    def praejo_dienu(self):
#        today = datetime.datetime.today()
#        return (today - self.date).days
#
#    def praejo_valandu(self):
#        today = datetime.datetime.today()
#        return int((today - self.date).total_seconds() // 3600)
#
#    def praejo_minuciu(self):
#        today = datetime.datetime.today()
#        return int((today - self.date).total_seconds() // 60)

#    def praejo_sekudziu(self):
#        today = datetime.datetime.today()
#        return int((today - self.date).total_seconds())
#
#    def keliamieji_metai(self):
#        a = False
#        if self.date.year % 4 == 0:
#            if self.date.year % 100 == 0:
#                if self.date.year % 400 == 0:
#                    a = True
#        return a

#    def atimti_dienas(self, days: int):
#        nauja_data = self.date - datetime.timedelta(days=days)
#        return nauja_data.strftime('%Y-%m-%d')
#
#    def prideti_dienas(self, days: int):
#        nauja_data = self.date + datetime.timedelta(days=days)
#        return nauja_data.strftime('%Y-%m-%d')
#
#
# sukaktis = Sukaktis(1995, 5, 12)
# print(sukaktis.praejo_metu())
# print(sukaktis.praejo_menesiu())
# print(sukaktis.praejo_dienu())
# print(sukaktis.praejo_valandu())
# print(sukaktis.praejo_minuciu())
# print(sukaktis.praejo_sekudziu())
# print(sukaktis.keliamieji_metai())
# print(sukaktis.atimti_dienas(100))
# print(sukaktis.prideti_dienas(100))


# with open("Tekstas.txt", "w") as w_failas:
#     w_failas.write("Zen of Python\n" "Beautiful is better than ugly\n")
#
# with open("Tekstas.txt", "r") as r_failas:
#     print(r_failas.read())
#
# with open("Tekstas.txt", "a") as w_failas:
#     dabar = datetime.datetime.now()
#     str_data = dabar.strftime("%Y %m %d %H:%M:%S \n")
#     w_failas.write(str_data)
#
#
# with open('Tekstas.txt', 'r') as failas:
#     naujas = ""
#     skaicius = 1
#     for eilute in failas:
#         naujas += str(skaicius) + " " + eilute
#         skaicius += 1
#
# with open('Tekstas.txt', 'w') as failas:
#     failas.write(naujas)
#
#
# with open('Tekstas.txt', 'r') as r_failas:
#     a = ""
#     senas_tekstas = "Beutiful is better than ugly."
#     pakeistas_tekstas = "Grazu yra geriau nei bjauru."
#     for eilute1 in r_failas:
#         a += eilute1.replace(senas_tekstas, pakeistas_tekstas)

# 8 paskaita
# 1uzduotis

# tekstas = "Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex."
# print(tekstas)
# sakiniai = tekstas.split(". ")
# nauji_sakiniai = map(lambda x: x + "!", sakiniai)
# naujas_tekstas = " ".join(nauji_sakiniai)
# print(naujas_tekstas)
#
# 2uzduotis

# from statistics import mean, median
#
# sarasas = list(range(0, 51))
# print(sarasas)
#
# sarasas_daugyba = list(map(lambda x: x * 10, sarasas))
# print(sarasas_daugyba)
#
# sarasas_dalyba = list(filter(lambda x: x % 7 == 0, sarasas))
# print(sarasas_dalyba)
#
# sarasas_kvadratu = list(map(lambda x: x ** 2, sarasas))
# print(sarasas_kvadratu)
#
# suma = sum(sarasas_kvadratu)
# maziausias = min(sarasas_kvadratu)
# didziausias = max(sarasas_kvadratu)
# vidurkis = mean(sarasas_kvadratu)
# mediana = median(sarasas_kvadratu)
# print(f"Suma: {suma}, Mažiausias skaičius: {maziausias}, Didžiausias skaičius: {didziausias}, Vidurkis: {vidurkis}, Mediana: {mediana}")
#
# sarasas_kvadratu_atbulai = sorted(sarasas_kvadratu, reverse=True)
# print(sarasas_kvadratu_atbulai)
#
# 3uzduotis
#
# sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]
# skaiciai = []
# zodziai = []
# true_reiksmes = []
#
# for x in sarasas:
#     if type(x) is int or type(x) is float:
#         skaiciai.append(x)
#     elif type(x) is str:
#         zodziai.append(x)
#     elif type(x) is bool and x is True:
#         true_reiksmes.append(x)
#
# print(f"Skaičių suma: {sum(skaiciai)}")
# print(f"Visi žodžiai: {' '.join(zodziai)}")
# print(f"True reikšmių skaičius: {len(true_reiksmes)}")

# 4uzduotis

# from operator import attrgetter
#
#
# class Zmogus:
#     def __init__(self, vardas, amzius):
#         self.vardas = vardas
#         self.amzius = amzius
#
#     def __repr__(self):
#         return f"Vardas: {self.vardas}, Amžius: {self.amzius}"
#
#
# zmoniu_sarasas = [Zmogus('Saulius', 54), Zmogus('Paulius', 25), Zmogus('Gabija', 27)]
#
# print(sorted(zmoniu_sarasas, key=attrgetter('vardas')))
# print(sorted(zmoniu_sarasas, key=attrgetter('amzius')))
# print(sorted(zmoniu_sarasas, key=attrgetter('vardas'), reverse=True))
# print(sorted(zmoniu_sarasas, key=attrgetter('amzius'), reverse=True))


#1uzduotis

from datetime import datetime

print(datetime.now())
print(datetime.now().date())
print(datetime.now().time())

from datetime import date

print(date.today())

from datetime import date as data
print(data.today())


