num1 = int(input('Ingrese un numero> '))
num2 = int(input('Ingrese un numero> '))

for i in range(num1,num2+1,1):
    if i % 2 == 0 :    
        print(i)

if num2<num1:
    for i in range(num2,num1+1,1):
        if i % 2 == 0 :    
            print(i)