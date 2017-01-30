def myBubbSort(L):
    for i in range( len(L) ):
        for j in range( len(L) -1 ):
            if L[j] > L[j+1]:
                tmp = L[j]
                L[j] = L[j+1]
                L[j+1] = tmp
    return L
 
def mediana_sort(L, left, right):
    L = myBubbSort(L)
    if (right - left ) % 2 == 0: #nieparzysta 
	print 'nieparzysta ilosc elementow'
        index = (right - left) / 2
        return L[left + index -1]

    else:  #parzysta- mediana jako srednia arytmetyczna srodkowych wyrazow:
        print 'parzysta ilosc elementow'
 
        lewySrodek = left + int(float(right - left) / 2.0 - 0.5)
        prawySrodek = left + int(float(right - left) / 2.0 + 0.5)
 
        return (float(L[lewySrodek]) + float(L[prawySrodek])) /2.0 #srednia
 
L = [1,2,3,4,5,6]

print 'mediana = ' + repr( mediana_sort(L, 0, len(L)-1) )


