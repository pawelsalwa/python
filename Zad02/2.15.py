L = [1,2,3,4,5]

nowy = "".join(map(repr,L)) #map wykonuje fuunkcje na kilku elementach

import string

print nowy
print isinstance(nowy, str)
