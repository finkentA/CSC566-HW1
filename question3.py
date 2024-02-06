plainText = """ethicslawanduniversitypolicieswarningtodefendasystemyouneedtobeabletot
hinklikeanattackerandthatincludesunderstandingtechniquesthatcanbeusedt
ocompromisesecurityhoweverusingthosetechniquesintherealworldmayviolate
thelawortheuniversitysrulesanditmaybeunethicalundersomecircumstancesev
enprobingforweaknessesmayresultinseverepenaltiesuptoandincludingexpuls
ioncivilfinesandjailtimeourpolicyineecsisthatyoumustrespecttheprivacya
ndpropertyrightsofothersatalltimesorelseyouwillfailthecourseactinglawf
ullyandethicallyisyourresponsibilitycarefullyreadthecomputerfraudandab
useactcfaaafederalstatutethatbroadlycriminalizescomputerintrusionthisi
soneofseverallawsthatgovernhackingunderstandwhatthelawprohibitsifindou
btwecanreferyoutoanattorneypleasereviewitsspoliciesonresponsibleuseoft
echnologyresourcesandcaenspolicydocumentsforguidelinesconcerningproper"""

relativeFreq = { "A": .08167, "B": .01492, "C": .02782, "D": .04253, "E": .12702, "F": .02228,
"G": .02015, "H": .06094, "I": .06966, "J": .00153, "K": .00772, "L": .04025,
"M": .02406, "N": .06749, "O": .07507, "P": .01929, "Q": .00095, "R": .05987,
"S": .06327, "T": .09056, "U": .02758, "V": .00978, "W": .02360, "X": .00150,
"Y": .01974, "Z": .00074 }

def calculateVariance(dictionary):
    #Calculate the variance of a given frequency table
    # in the form of python dictionary, all columns sum to 1
    mean = 0
    total = 0
    #Calculate mean from dictionary
    for letter in dictionary.keys():
        value = ord(letter)
        freq = dictionary[letter]
        mean += freq
        total += 1
    mean /= total
    # print("Mean = ", mean)
    variance = 0
    #Then calculate the variance with each letter's distance to the mean
    for letter in dictionary.keys():
        value = dictionary[letter]
        diff = value - mean 
        # if diff > 13:
        #     diff = 26 - diff
        squared = diff * diff 
        variance += squared 
    # print("Var = ", variance)
    variance /= total
    return variance

def calculateFrequency(text):
    baseFreq = { "A": .08167, "B": .01492, "C": .02782, "D": .04253, "E": .12702, "F": .02228,
        "G": .02015, "H": .06094, "I": .06966, "J": .00153, "K": .00772, "L": .04025,
        "M": .02406, "N": .06749, "O": .07507, "P": .01929, "Q": .00095, "R": .05987,
        "S": .06327, "T": .09056, "U": .02758, "V": .00978, "W": .02360, "X": .00150,
        "Y": .01974, "Z": .00074 }
    length = len(text)
    for letter in baseFreq.keys():
        baseFreq[letter] = 0 #Reset
    for letter in text:
        baseFreq[letter] += 1
    for letter in relativeFreq.keys():
        baseFreq[letter] /= length #Turn into percentages
    return baseFreq

def encrypt(text, key):
    shift = []
    keyLength = len(key)
    for letter in key:
        shift.append(ord(letter)-65) #Get shift value where A=0,B=1...
    newList = []
    for i in range(len(text)):
        curChar = text[i]
        charInt = ord(curChar) + (shift[i%keyLength]) #To decipher use opposite shift
        if(charInt>90):
            charInt = (charInt%90) + 64
        newList.append(chr(charInt))
    return "".join(newList)

def pullParts(text, keyLength):
    #Function which pulls characters from text based on length
    parts = []
    for i in range(keyLength):
        parts.append([])
    for i in range(len(text)):
        parts[i%keyLength].append(text[i])
    textParts = []
    for charList in parts:
        textParts.append("".join(charList))
    return textParts

var = calculateVariance(relativeFreq)
print("a) Variance in English text = ", var*1000)
plainText = plainText.replace('\n','') #Remove return characters
plainText = plainText.upper()
length = len(plainText)
# print("Length: ", length)
relativeFreq = calculateFrequency(plainText)
var2 = calculateVariance(relativeFreq)
print("b) Variance in given plaintext =", var2*1000)
for key in ["yz","xyz","wxyz","vwxyz","uvwxyz"]:
    key = key.upper()
    cipher = encrypt(plainText, key)
    cipherFreq = calculateFrequency(cipher)
    print("For key = ", key)
    var3 = calculateVariance(cipherFreq)
    print("Key Variance =", var3*1000)

for key in ["yz","xyz","wxyz","vwxyz","uvwxyz"]:
    key = key.upper()
    cipher = encrypt(plainText, key)
    pulledParts = pullParts(cipher, len(key))
    count = 1
    varMean = 0
    print("For key = ", key)
    for part in pulledParts:
        # print("For part ", count)
        count += 1
        cipherFreq = calculateFrequency(part)

        var3 = calculateVariance(cipherFreq)
        varMean += var3
    varMean /= len(key)
    print("Key Mean Variance = ", varMean*1000)

key = "UVWXYZ"
cipher = encrypt(plainText, key)
for i in range(2,6):
    pulledParts = pullParts(cipher, i)
    count = 1
    varMean = 0
    print("For key length = ", i)
    for part in pulledParts:
        # print("For part ", count)
        count += 1
        cipherFreq = calculateFrequency(part)

        var3 = calculateVariance(cipherFreq)
        varMean += var3
    varMean /= i
    print("Mean Variance = ", varMean*1000)