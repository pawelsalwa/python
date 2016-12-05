x = 2 ; y = 3 ;
if (x > y):
    result = x;
else:
    result = y;

#for i in "qwerty": if ord(i) < 100: print i 
#powyzsza linijka nie skompiluje sie, poniewaz if oraz print wymagaja tutaj nowej linii i wciecia

for i in "axby": print ord(i) if ord(i) < 100 else i

