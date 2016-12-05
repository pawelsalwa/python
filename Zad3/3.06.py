
a = input("a=?(liczba naturalna)? ")
b = input("b=?(liczba naturalna)? ")

figura = ""

i =0

while(i<a):
	figura = figura +  "+---" * b + "+\n"
	i = i+1
	figura = figura + "|   "*b+"|\n"

figura = figura + "+---"*b + "+\n"

print figura



