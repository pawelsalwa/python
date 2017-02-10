def myBubbSort(L): #nieuzyta, zostala po pierwszej wersji programu
    for i in range( len(L) ):
        for j in range( len(L) -1 ):
            if L[j] > L[j+1]:
                tmp = L[j]
                L[j] = L[j+1]
                L[j+1] = tmp
    return L
 
def mediana_sort(M, left, right):
    M = sorted(M[left:right]) #poprawione- nie uzywam juz mojej funkcji
    if (right - left ) % 2 == 0: #nieparzysta 
	print 'nieparzysta ilosc elementow'
        index = (right - left) / 2
        return M[left + index -1]

    else:  #parzysta- mediana jako srednia arytmetyczna srodkowych wyrazow:
        print 'parzysta ilosc elementow'
 
        lewySrodek = left + int(float(right - left) / 2.0 - 0.5)
        prawySrodek = left + int(float(right - left) / 2.0 + 0.5)
 
        return (float(M[lewySrodek]) + float(M[prawySrodek])) /2.0 #srednia


N = [1,3,2,5,4,6]
print N

print 'mediana = ' + repr( mediana_sort(N, 0, len(N)-1) )

print N
