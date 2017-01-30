X = "qwerty"

def func():
    print X

func() #wypisze poprawnie string X
#=======================
X = "qwerty1"

def func():
    X = "abc"

func()
print X #wypisze qwerty1 poniewaz X w func nie ma slowa kluczowego global
#=======================
X = "qwerty2"

def func():
    global X
    X = "abc"

func() 
print X #wypisze abc, poniewaz X ma w func slowo kluczowe global(ma dostep do zmiany globalnego X)

