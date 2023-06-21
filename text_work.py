file = open('123.txt', 'r', encoding='utf-8')
print(file)
r = file.read()
print(r)
file.close()

print('****************************')

file = open('123.txt', 'r', encoding='utf-8')
r = file.read(25)
r1 = file.readline()
print('r =', r)
print('r1 =', r1)
file.close()

file = open('123.txt', 'r', encoding='utf-8')
file2 = open('456.txt', 'w', encoding='utf-8')
r = file.read()
file2.write(r)

file.close()
file2.close()


# name = input('Ваше имя?\n')
# film = input('Фильм?\n')
# food = input('Еда?\n')
#
# file = open('789.txt', 'w', encoding='utf-8')
# text = 'Имя: ' + name + '\n' + 'Фильм: ' + film + '\n' + 'Еда: ' + food
# file.write(text)
# file.close()

print('###########################################################################')

file = open('123.txt', 'r', encoding='utf-8')

books = []
for line in file:
    a = line.find('#')
    srez = line[a + 1:].replace('\n', '')
    books.append(srez)
print(books)

print('###########################################################################')

file = open('gubka.txt', 'r', encoding='utf-8')
file2 = open('ivan.txt', 'w', encoding='utf-8')
info = open('info.txt', 'r', encoding='utf-8')
old = info.readline().replace('\n', '')
new = info.readline().replace('\n', '')
print('old =', old, ', new =', new)
text = file.read()
text1 =text.replace(old, new)
file2.write(text1)

file.close()
file2.close()
info.close()





















