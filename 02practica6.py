import functions06 as f6
line = '----------------------------------------'
LINE = '________________________________________'
SKIP = '\n'
#2.a
print('\n2.a')
print(LINE)
L = [13,56,22]
occurences = f6.probabilitiesFROMfrequencies(L)

F2 = f6.sourceSquared(occurences)

dummIndexes = f6.insertDummyIndexes(F2)
dct = f6.getdctOfunqLettersANDprobabilities(F2, dummIndexes)
Huff = f6.huffmanize(dct, 2)
print(SKIP)
codelength = f6.codelengthsFROMhuffman(Huff, dummIndexes)
averageLength = f6.l_averagelength(codelength,F2)
print('Average Length - ' + str(round(averageLength,5)))



entropy = f6.H_Entropy(F2)
efficacy = f6.N_efficacy(entropy, averageLength, 2)

print('Efficacy - ' + str(round(efficacy,5)))

print(line)

m = '2020'

uniq = f6.insertDummyIndexes(occurences)
uniq = f6.getsquaredMSGES(uniq)
dct = f6.getdctOfunqLettersANDprobabilities(F2,uniq)

media = 0
nextt = False
msg = list()
txt = ''
for _ in range(len(m)):
    txt = txt + m[_]
    if nextt == True:
        msg.append(txt)
        txt = ''
        nextt =False
    else :
        nextt = True


mediaLenghth = 0
for mess in msg:
    for k,v in dct.items():
        if mess == k:
            mediaLenghth+=f6.I_AmountofInfoSingle(v)
print('\n2.b\n')

print("Media - " + str(round(mediaLenghth,5)))
print(LINE)





        

