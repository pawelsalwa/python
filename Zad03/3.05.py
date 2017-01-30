
x = raw_input("jaka dlugosc(liczba naturalna)? ")
if x.isdigit():
	dlugosc = int(x)

ramka = "|...." * dlugosc

print ramka + "|"

i =0

liczby =""

while(i<=dlugosc):
	liczby = liczby + repr(i) + "   "
	if i<9:
		liczby = liczby + " "
	i = i+1

print liczby
