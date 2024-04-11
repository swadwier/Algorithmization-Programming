import os
import json

array_dir = os.listdir(path="C:\\Users\\semen\\Downloads\\Telegram Desktop\\transactions\\transactions")
# получаем названия файлов в папке

way = "C:\\Users\\semen\\Downloads\\Telegram Desktop\\transactions\\transactions\\"
# выносим путь в переменную для дальнейшего использования

rez = []
for i in array_dir:
    file = (open(way + i, 'r'))
    rez.append(json.loads(file.read()))

rez = sorted(rez, key=lambda item: item['index'])

rez_search_hash = None
for rez_dict in rez:
    if rez_dict['hash'].startswith("000") and rez_dict['hash'].endswith("000"):
        rez_search_hash = rez_dict

author = rez_search_hash['transactions'][-1]
print("1.", 'Автор блока: ', author['to'], "\nНомер блока: ", rez_search_hash['index'])

# print(*rez, sep="\n")
# print(type(rez))
# print(type(rez[0]))


all_indexes = []

for rez_dict in rez:
    # print(rez_dict['index'])
    all_indexes.append(rez_dict['index'])

uniq_numbers = []
for i in range(len(all_indexes) - 1):
    if all_indexes[i] == all_indexes[i + 1]:
        uniq_numbers.append(all_indexes[i])

print(uniq_numbers)
print(range(len(uniq_numbers)-1))

indexes_corteges = []
count = 0


for i in range(len(uniq_numbers) - 1):
    if uniq_numbers[i] + 1 == uniq_numbers[i + 1]:
        count += 1
    else:
        indexes_corteges.append((uniq_numbers[i - count], uniq_numbers[i], count + 1))
        count = 0

if count > 0:
    indexes_corteges.append((uniq_numbers[-count - 1], uniq_numbers[-1], count + 1))

# print(indexes_corteges)
first_elem = None
min_elem = indexes_corteges[0][2]
for elem in indexes_corteges:
    if elem[2] < min_elem:
        min_elem = elem[2]
        first_elem = elem[0]

# minimal_len = min(indexes_corteges, key=lambda elem: elem[2])
# first_block = indexes_corteges[min(indexes_corteges, key=lambda elem: elem[2])]

print("2.", f'Минимальный размер форка: {min_elem}')
print("3.", f'Номер первого блока в форке наименьшей длины: {first_elem}')

last_elem = None
max_elem = indexes_corteges[0][2]
for elem in indexes_corteges:
    if elem[2] > max_elem:
        max_elem = elem[2]
        last_elem = elem[1]
print("4.", f'Максимальный размер форка: {max_elem}')

last_elem_list = []

for i in range(len(rez) - 1):
    if rez[i]['index'] == last_elem:
        last_elem_list.append(rez[i])

# print(*last_elem_list, sep="\n")

for i in range(len(last_elem_list) - 1):
    if last_elem_list[i]['timestamp'] > last_elem_list[i+1]['timestamp']:
        last_elem = last_elem_list[i]
    else:
        last_elem = last_elem_list[i+1]

print("5.", f'Хэш последнего блока в отброшенной ветке форка наибольшей длины: {last_elem["hash"]}')
print("6.", f'В системе произошло {len(indexes_corteges)} форк(-а/-ов)')

value = None
for i in range(len(rez)):
    if rez[i]['index'] == 71:
        value = rez[i]['transactions'][-1]

# print(value)
print("7. Размер вознаграждения за создание 71 блока =", value['value'])

rez_for_8 = []
for i in range(len(rez)-1):
    if rez[i]['index'] == rez[i+1]['index'] - 1:
        rez_for_8.append(rez[i])
rez_for_8.append((rez[-1]))

value = None
value2 = None
counter = 0
summ = 0
for i in range(len(rez_for_8)-1):
    value = rez_for_8[i]['transactions'][-1]['value']
    value2 = rez_for_8[i+1]['transactions'][-1]['value']
    if value == value2:
        counter += 1
    else:
        if counter > summ:
            summ = counter
        counter = 0

print(f"8. Вознаграждение уменьшается в среднем раз в {summ+1} блоков")

rez_for_9 = []
for i in range(len(rez_for_8)-1):
    value = rez_for_8[i]['transactions'][-1]['value']
    value2 = rez_for_8[i+1]['transactions'][-1]['value']
    if value != value2:
        rez_for_9.append(rez_for_8[i])
rez_for_9.append(rez_for_8[-1])
rez_for_9.pop(0)

values = []
for i in range(len(rez_for_9)):
    # print(rez_for_9[i]['transactions'][-1])
    values.append(rez_for_9[i]['transactions'][-1]['value'])

# print(*values, sep="\n")
summa = 0
last_number = None
for i in range(len(values)-1):
    summa += values[i+1]/values[i]
    last_number = values[i+1]
summa = round(summa / (len(values)-1), 2)

print(f"9. Средний коэффицент сокращения вознаграждения за выработку блока равен {summa}")

count = 0
difference = 0
for i in range(len(rez_for_8)):
    if rez_for_8[i]['transactions'][-1]['value'] == last_number:
        count += 1
        if count != (summ+1):
            difference = (summ+1) - count

counter = 0  # умножать на 17
coeff = summa
number = 0.09

while round(last_number, 2) != number:
    last_number = last_number * coeff
    counter += 1

quantity_of_blocks = (counter * 17 - 17) + 99 + difference + 1
print(f"10. # блока, в котором в будущем разм ер вознаграждения впервые окажется равен 0,09 = {quantity_of_blocks}")

indexes_with_secret_info = []
secret_info = []
for i in range(len(rez_for_8)):
    if rez_for_8[i]['secret_info'] != '':
        indexes_with_secret_info.append(rez_for_8[i]['index'])
        secret_info.append(rez_for_8[i]['secret_info'])

print(f"11. {indexes_with_secret_info}  -  № блоков, в которых в поле secret_info встречается дополнительная информация")

print(f"12. {secret_info}  -  полученная информация в порядке ее появления в цепочке")

byte = ''
for i in secret_info:
    byte += i

# print(byte)

print(f"13. {bytes.fromhex(byte).decode('utf-8')}")


