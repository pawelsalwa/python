#========3.05.py:========

def f35():
	x = raw_input("jaka dlugosc(liczba naturalna)? ")
	if x.isdigit():
		dlugosc = int(x)
	
	ramka = "|...." * dlugosc
	
	i =0
	
	liczby =""
	
	while(i<=dlugosc):
		liczby = liczby + repr(i) + "   "
		if i<9:
			liczby = liczby + " "
		i = i+1
	return ramka + "\n" + liczby

string = f35()

print string
#========3.06.py:========
def f36():
	a = input("a=?(liczba naturalna)? ")
	b = input("b=?(liczba naturalna)? ")
	
	figura = ""
	
	i =0
	
	while(i<a):
		figura = figura +  "+---" * b + "+\n"
		i = i+1
		figura = figura + "|   "*b+"|\n"
	
	figura = figura + "+---"*b + "+\n"
	
	return figura

string = f36()
print string





