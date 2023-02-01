#colors = ['red', 'green', 'blue']
#data = open('file.txt', 'a') #дописывает к старой информации новую
#data = open('file.txt', 'w') #Старые данные удаляются, а новые дописываются
#data.writelines(colors) #разделителей не будет
#data.write('\nLINE22\n')
#data.write('\nLINE13\n')
#data.close()
#exit()

#with open('file.txt', 'w') as data:
#    data.write('line 1\n')
#    data.write('line 2\n')
#path = 'file.txt'

#data = open(path, 'r') # режим чтения
#for line in data:
#    print(line)
#data.close()
#exit()

#Функции и модули

#import hello
#print(hello.f(1))
#import hello as h # h - псевдоним hello
#print(h.f(1))

#Функции

#def new_string(symbol, count):
#    return symbol * count
#print(new_string('!', 5)) # Результат !!!!!
#print(new_string('!')) #Результат !!!(count раз)
#print(new_string(4)) # Результат 12

#def concatenatio(*parms):
    #res: int = 0
    #res = 0
#    res: str = ""
#    for item in parms:
#        res += item
#    return res

#print(concatenatio('a', 's', 'd', 'w')) #asdw
#print(concatenatio('a', '1')) #a1
#print(concatenatio(1, 2, 3, 4)) #для int

#Рекурсия (вызывает сама себя)

#def fib(n):
#    if n in [1, 2]:
#        return 1
#    else:
#        return fib(n-1) + fib(n-2)
#list = []
#for e in range(1, 10):
#    list.append(fib(e))
#print(list) #Результат 1 1 2 3 5 8 13 21 34

#Кортежи - неизменяемый список, изменять значения нельзя

#(a, b) = (3, 4) #кортеж
#a = (3, 4) #кортеж
#print(a)
#print(a[-1])

#a = (3,1, 41, 2, 4)
#print(a)
#print(a[-2])
#a = (3,) #кортеж из 1 элемента

# t = tuple(['red', 'green', 'blue'])
# print(t[0]) #red
# print(t[2]) #blue
# print(t[-2]) #green
# for e in t:
#     print(e) #red green blue
#t[0] = 'black' #Error нельзя изменить элемент на black
#print(t[10]) #Error нет такого индекса

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}' .format(red, green, blue)) 
# #r:red g:green b:blue

# a = (3, 4, 7)
# print(a)
# print(a[0])

# for item in a:
#     print(a)

#Словари

# dictionary = {}
# dictionary = \
#     {
#         'up': 'вверх',
#         'left': 'влево',
#         'down': 'вниз',
#         'right': 'вправо'
#     }

# print(dictionary) #('up': 'вверх' 'left': 'влево' 'down': 'вниз' 'right': 'вправо')
# print(dictionary['left']) #типы ключей могут отличаться

# for k in dictionary.keys():
#     print(k) #получить названия кейсов
# for v in dictionary.values():
#      print(v) #получить только значения

# print(  dictionary['up'])
# dictionary['up'] = 'up'
# print( dictionary['up'])

#Множества

# colors = {'red', 'green', 'blue'}
# print(type(colors)) #тип данных 'set'
# exit() #чтобы код, кторый ниже не читал

# colors = {'red', 'green', 'blue'}
# print(colors) #{'red', 'green', 'blue'}
# colors.add('red') 
# print(colors) #{'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) #{'red', 'green', 'blue', 'gray'}
# colors.remove('red')
# print(colors) #{'green', 'blue', 'gray }
# colors.discard('red')
# print(colors) #{'green', 'blue', 'gray'}
# colors.clear() #{}
# print(colors) #set

#Изменяемые множества

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()            #c = {1, 2, 3, 5, 8}
# u = a.union(b)          #u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b)   #i = {8, 2, 5}
# dl = a.difference(b)    #dl = {1, 3}
# dr = b.difference(a)    #dr = {13, 21}

# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
# #{1, 21, 3, 13}

#Неизменяемые множества

#s = frozenset(a)

#Списки

# list1 = [1, 2, 3, 4, 5]
# list2 = list1
# list1[0] = 123
# list1[0] = 123
# list2[1] = 333

# for e in list1:
#     print(e)

# for e in list2:
#     print(e)
# list1 = [1, 2, 3, 4, 5]

# print(len(list1))
# print(list1.pop())
# print(len(list1))

