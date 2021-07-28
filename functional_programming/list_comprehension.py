'''такая конструкция'''

for x in range(5, 10):
    if x % 2 == 0:
        x *= 2

'''приводится к виду
[statement FOR var IN iterable IF predicate]
'''
print([x * 2 for x in range(5, 10) if x % 2 == 0])

'''если необходимо ELSE - ставим вначале'''
for x in range(5, 10):
    if x % 2 == 0:
        x *= 2
    else:
        x += 1

print([x * 2 if x % 2 == 0 else x + 1 for x in range(5, 10)])
    
'''Генератор списков - способ построить новый список, 
применяя выражение к каждому элементу последовательности. '''

my_list = [2, 5, 1, 4]

result_list = [c * 2 for c in my_list]
print(result_list)