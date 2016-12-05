line = 'asd\n		asd \n asd'

nowy = line.split()

print nowy

print len(nowy)

print len([litera for litera in line if litera.isalpha()])
# dla kazdego elementu w lini jezeli jest on litera

