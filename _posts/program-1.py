t = ['a' , 'b' , 'c' ]
t.append('d' )
print (t)
t1 = ['a' , 'b' , 'c' ]
t2 = ['d' , 'e' ]
t1.extend(t2)
print (t1)
t = ['d' , 'c' , 'e' , 'b' , 'a' ]
t.sort()
print (t)




cheeses = [' Cheddar' , ' Edam' , ' Gouda' ]
for cheese in cheeses:
    print (cheeses[cheese])

numbers = [17, 123]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print (numbers)