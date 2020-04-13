import functions06

line = '----------------------------------------'
LINE = '________________________________________'
SKIP = '\n'
#-------------------------------------------------------------------------------------------------------------------------------
print(LINE)
#Text 
texto="Al pie del murallón los pasos se hundían ya  en la arena, y por el aire negro, tal vagos fantasmas,  surgieron las velas de las barcas pesqueras. Allí es-taba él: en lo oscuro, un lamento de gozo o de pena;  una voz insomne llamando nadie sabe qué o quién  en la vastedad sin nombre de la noche.  (OCNOS, Luis Cernuda, 1902-1963)"

#1.a
print('\n1.a\n')

#Length of Source F
uniqueLetters = functions06.getUniqueLettersFROMtext(texto)
print('Length of Source F - ' + str(len(uniqueLetters)))


occurences = functions06.getProbabilitiesFROMuniquelettersANDtext(uniqueLetters,texto)

#Entropy of F
Entropy = functions06.H_Entropy(occurences)
print('Entropy of F - ' + str(functions06.roundd(Entropy)))
print(SKIP)
print(line)
#1.b
print('\n1.b\n')


dct = functions06.getdctOfunqLettersANDprobabilities(occurences,uniqueLetters)
binary_huffman = functions06.huffmanize(dct,2)
codelengths = functions06.codelengthsFROMhuffman(binary_huffman,uniqueLetters)

#Average Length
averageLength = functions06.l_averagelength(codelengths,occurences)
print('Average binary length - ' + str(round(averageLength,5)))

#Efficacy
Efficacy = functions06.N_efficacy(Entropy,averageLength,2)
print('Efficacy - ' + str(round(Efficacy,5)))

#-----------------------------------------------------------------------------------------------------------------------------
print(LINE)

