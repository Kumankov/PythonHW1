# Напишите программу для. проверки истинности 
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для 
# всех значений предикат.

q=[0]*8
i=0
sum=0
# result = 10 % 2 == 0
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            q[i] = not(x or y or z) == (not (x) and not (y) and not (z))
            print (f'X = {x}, Y = {y}, Z = {z} - {q[i]}')            
            sum=sum+q[i]           
            i+=1              
if sum==0:
    print('Выражение тождественно ложно') 
elif sum==8:
    print('Выражение тождественно истинно') 
else: 
    print('Выражение не является ни тождественно истинным ни тождественно ложным')