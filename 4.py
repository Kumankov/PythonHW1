# Напишите программу, которая по заданному номеру 
# четверти, показывает диапазон возможных координат 
# точек в этой четверти (x и y).

quarter= int(input('Введите номер четверти от 1 до 4 - '))
if quarter<1 or quarter>4:
    print ('Некорректный номер четверти')
elif quarter==1:
    print ('X > 0 и Y > 0')
elif quarter==2:
    print ('X > 0 и Y < 0')
elif quarter==3:
    print ('X < 0 и Y < 0')
else:
    print ('X < 0 и Y > 0')