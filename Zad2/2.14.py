line = 'asd\n		asd \n asdf'

nowy = line.split()

dlugosc = 0
najdluzszy = ""

for word in nowy:
        if dlugosc<len(word):
		dlugosc = len(word)
		najdlozszy = word

print dlugosc
print najdlozszy
