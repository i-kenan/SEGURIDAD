import math
import huffman
import freq
import numpy as np


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

def roundd(something):
    d = 5
    return round(something,5)
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

def probabilitiesFROMfrequencies(frequencies):
    values = 0
    for freqq in frequencies:
        values += freqq
    probabilities = []
    for freqq in frequencies:
        probabilities.append(freqq/values)
    return probabilities

def insertDummyIndexes(probabilities):
    values = 0
    dummIndex = []
    for prob in probabilities:
        dummIndex.append(values)
        values+=1
    return dummIndex

def getprobabilitiesFROMsquaremsges(m):


    dvaeska = 1
    _ = 0
    Probs = []
    print(occurences)
    for a in m :
        dvaeska*=occurences[int(a)]
        print(a + '  ' + str(dvaeska))
        if _ == 1:
            Probs.append(dvaeska)
            dvaeska = 1
            _ = 0
        else:
            _+=1
    return Probs

def getsquaredMSGES(uniqueLetters):

    uniq = []
    for a in uniqueLetters:
        for b in uniqueLetters:
            uniq.append(str(str(a) + str(b)))
    return uniq

def ternaryFilldct(uniqueletter):
    bits = math.ceil(math.log(len(uniqueletter),3))
    dct = {}
    for letter in uniqueletter:
        index = uniqueletter.index(letter)
        tempArray = []
        for _ in range(bits):
            if index == 0:
                tempArray.insert(0, 0)
            else:
                tempArray.insert(0,index%3)
                index = int(index/3)
        s = {letter:tempArray}
        dct.update(s)
    return dct

def probabilityDistributionR(E, A):
    return E.dot(A)

def probabilityDistributionER(E, A):
    e = np.diag(E)
    return e.dot(A)

def probabilityDistributionERbj(E,A):

    e = np.diag(E)
    S = probabilityDistributionR(E,A)
    s = np.diag(S)
    s_ = np.linalg.inv(s)
    ex = e.dot(A)
    return ex.dot(s_)

def transmissionRate(codelength, nmbOfCodes,q):
    return math.log(nmbOfCodes,q)/codelength

def relativeDistance(codelength):

    #Note d(C) is counted as one
    d = 1 
    return d/codelength

def compareTwoarrays(v1,v2):


    for _ in range(len(v1)):
        if v1[_] != v2[_]:
            return 0
    return 1


def decodingwithoutNoise(lista, dct):


    temp = []
    loca = []
    for _ in range(len(lista)):
        if _ % 24 < 3 or (_%24 >= 12 and _%24 < 15):
            temp.append(lista[_])
    temp2 = []
    for _ in range(len(temp)):
        temp2.append(temp[_])
        if _%5 == 4:
            loca.append(temp2)  
            temp2 = []  
    stringic = ''
    for a in loca:
        for k,v in dct.items():
            if compareTwoarrays(a,v):
                stringic += k
    return stringic


    