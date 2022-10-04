import io
import re

with io.open("komediya.txt", encoding='utf-8') as file:
    komediya = file.read()

komediya = re.sub("[^А-Яа-я ]", "", komediya)   # видаляємо всі символи крім зазначених
komediya = re.sub(" +", " ", komediya)          # виадаляємо повторні пробіли
komediya = komediya.lower()                     # переводимо всі символи в нижній регістр


f = open('komediya_clear.txt', 'w')
f.write(komediya)
f.close()


alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя "
file2 = open('symbols_frequency.txt', 'w')
all_symbols_count = len(komediya)
for a in alphabet:
    symbol_frequency = komediya.count(a)/all_symbols_count
    file2.writelines(["Частота символа '", str(a), "' :", str(symbol_frequency), "\n"])
file2.close()
