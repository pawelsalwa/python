
while(1):
	x = raw_input("wpisz liczbe")
	if x.isdigit():
		
		print "%s %s" % (int(x)*2 , int(x)*int(x))
	elif (x == "stop") :
		break
	else :
		print "cos zle wpisales"		
		continue


