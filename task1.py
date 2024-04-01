
"""
Посчитайте сумму чётных элементов от 1 до n исключая кратные e. 
Используйте while и if. 
Попробуйте разные значения e и n.
"""
n = int(input("введите n:"))
e = int(input("введите e:"))
count = 2
sum_p = 0
while count <= n:
    if count % e == 0:
        count +=2
        continue
    sum_p += count
    count += 2
    print(sum_p) 
print('')
print(sum_p) 