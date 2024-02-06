import matplotlib.pyplot as plt

cipher = """OBRGXIMYAZZAWCATBNMUYYHAZNVGFCXPVVSIJSVLKIFAVGBIECAZSBWGRGRQWUCHMMOCYE
FLGQQNKFSHQMGYALNKCIJQVEKVWXNFOYFYQBESGOYTXMAYTXSISNBPMSGOJBKFWRUTTMLS
BNQMLLRGFNZUAWHZLBRVZGHUVZMCKJEHSLSWGXCNZYEXRIMLPXRIXNUXRNSNRPHFDHBMAY
WKHTKNGNUXRNJUVGMYNYEYNLYYGPGYFSBNQQWUCHMMSLRWTFDYQRNOJUEWNLVUZIDHWXLH
TLKNEXMALBRQGUMMGXCUFXLHTLLLRTROJYFIDHLIGADLUBVXENSCALVCDFFIQCFAHISILU
XXZXNUAMZAWISRNOJYKMQYECGRSBWHAHLUFBBPDPWLJBRYOCYEAYSVYXSISPRKSNZYPHMM
WKHXMWWMGAZNEOFMDHKORMGOKNUHTAZQRAZPWBRTQXGZFMTJAXUTRNWCAPZLUFRODLFYFL
GUKHRODLTYRGRYWHNLRIUCNMDXOCGAKIFAQXKUQMVGZFDBVLSIJSGADLWCFGNCFMGTMWWI
STBIMHGKXBSPVGFVWHRYHNWXSKNGHLBENHYYQPZLXUEXNHDSBGDQZIXGNQKNUXCCKUFMQI
MMRYEYUNFHEUDIAZVUJWNGQYSFVSDNZYFNOLWGRBLJGLGTMWWISKZJAXVMXCFVEBMAAHTB
SNGUPENMWCGBRIFFLHMYOBBBRNZIEHTAZFLTBKMUVGSYVQVMGNZYROHFKISPZLOBBVZHLB
BKNOYBYRTHVYELSUFXGADJJISBSUTFRPZSGZPTQLQCAZHNGHGADMCCYEEODARGDLSFQHDM
FIGKZCKYNLDWGHQEDPQHRBSBWLNKDBAMFNOJDSJTFIFMYHZXWXZHQYLBNGSQAWRHMWWQNK
HMVYPEZLWXUXVCDFAHSQSMGXOLWWVHTMLCZXHHOUVMHHYZBKQYAHSHQWWGRGSMFIEPHFDB
RMTLFBVLZLESOTBEXIEYQYKBFNOJDCRLAOLWEHRMWMGADYFYZRRZJIAMHYJQVMGIMNQXKU
QNUXUUDORHENAGRMGULCFUDCFANEHNLFRTGYSXBYXIMLBIOIFYAMGUKWBNMNWXSHQGGLRM
GUFYVMGYJHHFDLAWNEROHYEBNLANLHQNZYABBYKNPTKWMFNMHIFMJBSBJYTTQXLIPHLGAM
FTQCSN"""
cipher = cipher.replace('\n','') #Remove return characters
print("Length: ", len(cipher))


relativeFreq = { "A": .08167, "B": .01492, "C": .02782, "D": .04253, "E": .12702, "F": .02228,
"G": .02015, "H": .06094, "I": .06966, "J": .00153, "K": .00772, "L": .04025,
"M": .02406, "N": .06749, "O": .07507, "P": .01929, "Q": .00095, "R": .05987,
"S": .06327, "T": .09056, "U": .02758, "V": .00978, "W": .02360, "X": .00150,
"Y": .01974, "Z": .00074 }
#Display frequency for comparison point
# plt.bar(range(len(relativeFreq)), list(relativeFreq.values()), align='center')
# plt.xticks(range(len(relativeFreq)), list(relativeFreq.keys()))
# plt.show()

#Isolate into parts and determine cipher (shift of each part)

parts = [{},{},{},{},{},{}]
shift = [18, 20, 13, 19, 25, 20]
newList = []
for i in range(len(cipher)):
    dict = parts[i%6]
    curChar = cipher[i]
    charInt = ord(curChar) + (26-shift[i%6]) #To decipher use opposite shift
    if(charInt>90):
        charInt = (charInt%90) + 64
    newList.append(chr(charInt))
    if curChar not in dict.keys():
        dict[curChar] = 1
    else:
        dict[curChar] += 1
print(''.join(newList))



alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for D in parts:
    for letter in alphabet:
        if letter not in D.keys():
            D[letter] = 0
    lists = sorted(D.items())
    x, y = zip(*lists)

    plt.bar(x, y)
    plt.show()
    print(D)

# print(parts)
#Find candidate string lengths
candidates = []
#Cycle over the text to find repeats
for i in range(len(cipher)-2):
    cur = cipher[i:i+3]
    #Check rest of the string
    # print(cur)
    for j in range(i+1, len(cipher)-2):
        check = cipher[j:j+3]
        if(cur==check):
            candidates.append(j-i)
            # print(j-i)
print(len(candidates))
candidates.sort()
divisible = 0
keyLength = 6
total = len(candidates)
for cand in candidates:
    if(cand/keyLength % 1.0 ==0.0):
        divisible += 1
print("Total divisible by", keyLength, " is ", divisible/total)
print(candidates)
