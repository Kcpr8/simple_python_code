import msgpack
import numpy as np

with (open("4.msgpack", "rb") as file):
    data = msgpack.unpackb(file.read())

print(data[0].items())
print(data[0].keys())
print(data[0].values())
print('---------')

#zad1
def f_1(el):
    if el['had_asthma'] == True:
        return True
    else:
        return False

lista1 = list(filter(f_1, data))

asthma_patients = len(lista1)
print(asthma_patients)
print('---------')

#zad2
def f_2(el):
    if el['smoker_status'] == 'Current smoker - now smokes every day' or 'Current smoker - now smokes some day' and el['sex'] == 'Male' and el['age'] >= 40:
        return True
    else:
        return False

lista2 = list(filter(f_2, data))

def f_3(el):
    return el['weight_in_kilograms']

lista3 = sorted(list(map(f_3, lista2)))
median_weight_smoking_man = round(np.median(lista3), 3)
print(median_weight_smoking_man)

print('---------')

#zad3
def f_4(el):
    if el['alcohol_drinkers'] == True and el['sex'] == 'Female':
        return True
    else:
        return False

lista4 = list(filter(f_4, data))

def f_5(el):
    return el['height_in_meters']

lista5 = sorted(list(map(f_5, lista4)))

mean_height_alcohol_drinking_women = round(np.mean(lista5), 3)
print(mean_height_alcohol_drinking_women)

print('---------')

#zad4
def f_6(el):
    if el['sex'] == 'Male' and el['age'] < 25:
        return True
    else:
        return False

lista6 = list(filter(f_6, data))

def f_7(el):
    bmi = el['weight_in_kilograms'] / el['height_in_meters']**2
    return bmi

lista7 = sorted(list(map(f_7, lista6)))

bmi_men_under_25 = round(np.mean(lista7), 3)
print(bmi_men_under_25)

print('---------')

#zad5
def f_8(el):
    if el['sex'] == 'Female' and el['e_cigarrette_usage'] == 'Use them some day' or 'Use them every day':
        return True
    else:
        return False

lista8 = list(filter(f_8, data))

def f_9(el):
    return round(el['sleep_hours'], 3)

lista9 = sorted(list(map(f_9, lista8)))

least_sleep_women_e_cig = lista9[:10]
print(least_sleep_women_e_cig)

print('---------')


#utworzenie slownika z odpowiedziami
results = {
    'asthma_patients': asthma_patients,
    'median_weight_smoking_man': median_weight_smoking_man,
    'mean_height_alcohol_drinking_women': mean_height_alcohol_drinking_women,
    'bmi_men_under_25': bmi_men_under_25,
    'least_sleep_women_e_cig': least_sleep_women_e_cig
}

print (results)
#zapis slownika results do pliku lab_1.msgpack
with open("lab_1.msgpack", "wb") as file:
     file.write(msgpack.packb(results))


#sprawdzenie poprawnosci zapisu pliku
with (open("lab_1.msgpack", "rb") as file):
    data2 = msgpack.unpackb(file.read())

print(data2.values())


