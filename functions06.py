import math
import huffman
import freq
import numpy

#TO USE THIS, functions06, huffman and freq must be in the same folder as your CODE 
#install numpy if you don't have it


#Function that returns unique letters
#EXAMPLE 
#Input - > txt = 'abcdbca' 
#Output - > 'abcd'
def getUniqueLettersFROMtext(txt):
    uniqueLetters = ''
    for letter in txt:
        if letter not in uniqueLetters:
            uniqueLetters+=letter
    return uniqueLetters

#Function that returns the probabilities of each letter
#EXAMPLE
#Input -> txt = 'abcdbcdcdd' 
#         uniqueletters = 'abcd'
#Output -> returns [0.1,0.2,0.3,0.4]
def getProbabilitiesFROMuniquelettersANDtext(uniqueletters, txt):
    P = []
    lentxt = len(txt)
    for letter in uniqueletters:
        P.append(txt.count(letter)/lentxt)
    return P

#Same as the getProbabilitiesFROMuniquelettersANDtext except it returns a dictionary
#Output -> {a:0.1,b:0.2,c:0.3,d:0.4}
def getdctOfprobabilitiesANDunqLetters(probabilities, uniqueLetters):
    dct = dict()
    for _ in range(len):
        s = {probabilities[_] : uniqueLetters[_]}
        dct.update(s)
    return dct

#Same as the getProbabilitiesFROMuniquelettersANDtext except it returns a dictionary
#Dictionary is reversed where probabilities are keys
#Output -> {0.1:a, 0.2:b,0.3:c,0.4:d}
def getdctOfunqLettersANDprobabilities(probabilities, uniqueLetters):
    dct = dict()
    for _ in range(len(probabilities)):
        s = {uniqueLetters[_] : probabilities[_]}
        dct.update(s)
    return dct

#Amount of info for a singular probability
#BINARY CASE, switch q to 3 if you want TERNARY
def I_AmountofInfoSingle(probability):
    q = 2
    if probability == 0 :
        print('p == 0 !!!')
        return
    return math.log(1/probability,q)

#Entropy of all probabilities in a list
def H_Entropy(probabilities):
    value = 0
    for prob in probabilities:
        value += prob*I_AmountofInfoSingle(prob)
    return value

#Medium Length of a q-ary code, MUST huffmanize a dct and then codelengthsFROMhuffman
def l_averagelength(lengths, probabilities):

    if not lengths or not probabilities:
        print('Empty L or P for average length')
        return
    value = 0
    for _ in range(len(lengths)):
        value += lengths[_]*probabilities[_]
    return value

#creates a huffman object, object.encode() to code, object.decode() to decode
#to get a dict of huffman -> object.huffman without () as it's an attribute of class
def huffmanize(dct,q):

    freqs = list(dct.items())
    huff = huffman.HuffmanCode(freqs,2)
    return huff

#returs codelengths of each uniqueletter 
def codelengthsFROMhuffman(huff, uniqueLetters):

    codelengths = []
    for letter in uniqueLetters:
        for key,values in huff.huffman.items():
            if letter == values:
                codelengths.append(len(key))
    return codelengths

#optimum efficacy of a code
def N_efficacy(entropy, averagelength,q):
    return entropy/(math.log(2,q)*averagelength)

#returns FxF ... {0.1, 0.9} -> {0.01, 0.09, 0.9, 0.81}
def sourceSquared(probabilities):
    squaredProbabilities = []
    for p1 in probabilities:
        for p2 in probabilities:
            squaredProbabilities.append(p1*p2)
    return squaredProbabilities
    