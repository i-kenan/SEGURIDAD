alf = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóúÁÉÍÓÚ0123456789 ,.:!-¿?()'
codedmsg = 'ihJACM?NM?IXCÑÚí2ZoAóx¿eyK1(íiv7ctw!q2,whCX-x!5Éqñ¿a¿3CkO?gDsvNOQZEBÍÉtbIÚGTEa-rMmj¿wwpwhN6sJíXbldcÑzZw)XhS hñ7Zr8U11YThAó8Ó5éjíú¿toyI.ÚqétÁÍMáTk3MsMpT?,ÍÚMñDaIU9¿FÚdKMcHB!!4:cIéTtB.á5-8Hcéí9T'

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(a, b):
    x = 0
    y = 1
    lx = 1
    ly = 0
    oa = a  
    ob = b  
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob
    if ly < 0:
        ly += oa 
    return lx

n = 62439738695706104201747
e = 356812573 
p = 249879448303
q = 249879448349


t = (p-1)*(q-1)

d = multiplicative_inverse(e, t)

k = 0 
s = True 
while s:
    if len(alf)**k <= n and n <= len(alf)**(k+1):
        s = False
    else :
        k+=1
print(k)

C = []
temp = k
sol = 0
counter = 0
for letter in codedmsg:
    sol += alf.index(letter)*((len(alf)**(temp)))
    temp -=1
    if temp == 0 and counter < 15:
        print(counter)
    counter+=1
    
    if temp == -1 :
        temp = k
        C.append(sol)
        sol = 0


M = []
for c in C:
    M.append(pow(c,d,n))

sol = ''
for m in M:
    temp = k
    while m!=0: 
        
        sol+=(alf[m%len(alf)])
        m = int(m/len(alf))

        temp-=1
        if temp == 0:
            m = 0
        


    



print(len(codedmsg)/12)
print(huff)

