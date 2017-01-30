def odwracanie_iteracyjne(L, left, right):
	tmp = 0
	while(right != left):
		tmp = L[left]
		L[left] = L[right]
		L[right] = tmp
		right = right - 1
		left = left +1
	return L

L = [1,2,3,4,5]
print L
print odwracanie_iteracyjne(L , 0 , len(L) - 1)
#====================================================
def odwracanie_rekurencyjne(L,left , right):
	tmp = 0
	if left != right:
		tmp = L[left]
		L[left] = L[right]
		L[right] = tmp
		L = odwracanie_rekurencyjne(L,left+1,right-1)
	return L
L = [1,2,3,4,5]
print L
print odwracanie_rekurencyjne(L , 0 , len(L) - 1)
