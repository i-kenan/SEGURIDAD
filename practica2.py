import functions06 as f6

alf = "Existe una cosa muy misteriosa, pero muy cotidiana. Todo el mundo participa de ella,  todo el mundo la conoce, pero muy pocos se paran a pensar en ella.  Casi todos se limitan a tomarla como viene, sin hacer preguntas.  Esta cosa es el tiempo."



uniqueLetters = ''
for letter in alf:
    if letter not in uniqueLetters:
        uniqueLetters+=letter
probabilities = {}
temp = 0
for letter in uniqueLetters:
    probabilities.update({letter:0.00})
for letter in alf:
    probabilities[letter]+=1/len(alf)
    
P = []
for v in probabilities.values():
    P.append(v)

huff = f6.huffmanize(probabilities)

L = []
for k in huff.huffman.keys():
    L.append(len(k))

print(huff.huffman)
entropy = f6.H_Entropy(P)
print("Entropy = " + str(entropy))
longitud = f6.l_averagelength(L,P)
print("Longitud = " + str(int(longitud*len(alf))))
print("Longitud media = " + str(longitud))
efficacy = f6.N_efficacy(entropy, longitud, 2)
print("Efficacy = " + str(efficacy))
