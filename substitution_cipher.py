cipher_text = 'AKALBIELCK CFJ LDNSMBAI AFQEFAAIG JAUAKDS CFJ LIACBA ' \
              'SIDJMLBG BHCB LHCFQA BHA ODIKJ CFJ NCVA DMI KEUAG ACGEAI ' \
              'BHA LAKK SHDFAG OA JASAFJ DF BHA LDNSMBAIG MGAJ EF FCBEDFCK ' \
              'GALMIEBR CFJ BHA AKALBIELCK GRGBANG BHCB NCVA DMI LCIG ' \
              'DSAICBA OAIA CKK LIACBAJ TR AKALBIELCK CFJ LDNSMBAI AFQEFAAIG ' \
              'CB OSE OA VAAS BHCB SIDQIAGG NDUEFQ PDIOCIJ OEBH DMI EFFDUCBEUA ' \
              'IAGACILH CFJ DMB DP BHA TDY CSSIDCLHAG BHA JASCIBNAFB DP AKALBIELCK ' \
              'CFJ LDNSMBAI AFQEFAAIEFQ CB OSE LHCKKAFQAG GBMJAFBG BD SMGH ' \
              'BHANGAKUAG BD MFJAIGBCFJ GDLEABRG CFJ BALHFDKDQRG LDNSKAY EGGMAG ' \
              'EF C TIDCJAI LDFBAYB BHCF OHCBG EF PIDFB DP BHAN OA OCFB DMI ' \
              'GBMJAFBG OHABHAI BHAR CIA ACIFEFQ CF MFJAIQICJMCBA NEFDI DI C ' \
              'JDLBDICBA BD BCLVKA GDLEABRG NDGB SIAGGEFQ SIDTKANG CFJ MFLDUAI ' \
              'FAO OCRG DP GDKUEFQ BHAN OHABHAI EBG JAUAKDSEFQ GRGBANG BHCB LCF ' \
              'KDLCBA PEIAPEQHBAIG EF BHA NEJJKA DP C TMIFEFQ TMEKJEFQ DI LIACBEFQ ' \
              'FAMIDSIDGBHABELG BHCB KDDV CFJ PMFLBEDF KEVA FCBMICK KENTG DMI PCLMKBR ' \
              'CFJ GBMJAFBG CIA CB BHA PIDFB AJQA DP IANCIVCTKA EFFDUCBEDF OHEKA ' \
              'CJUCFLEFQ BALHFDKDQEAG EG CB DMI LDIA OA CKGD BCVA HMNCF LDFFALBEDFG ' \
              'UAIR GAIEDMGKR EF ALA OA SIEJA DMIGAKUAG DF BHA PCNEKR KEVA CBNDGSHAIA ' \
              'OA LMKBEUCBA PCLMKBR GBMJAFBG CFJ GBCPP AFLDMICQA ACLH DBHAIG AUAIR ' \
              'GMLLAGG CFJ CIA BHAIA PDI BHA LHCKKAFQAG TDBH EF BHA LKCGGIDDN CFJ EF KEPA'

alphabet = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0,
            'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0,
            'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
words = []
[words.append(list(cipher_text.split()[idx])) for idx in range(len(cipher_text.split()))]
count=0 # total number of letters in the text
for word in words:
    for letter in word:
        alphabet[letter] += 1
        count += 1
for letter in alphabet:
    alphabet[letter] = round(alphabet[letter]/count, 5)
# alphabet is now a dictionary of (letter : relative frequency value) pairs.
print(alphabet)

# a.	Provide the relative frequency of all letters A...Z in the ciphertext.********
# Output: {'A': 0.13928, 'B': 0.09285, 'C': 0.07985, 'D': 0.07057, 'E': 0.05385, 'F': 0.07707,
# 'G': 0.065, 'H': 0.04178, 'I': 0.06964, 'J': 0.03714, 'K': 0.04364, 'L': 0.04643, 'M': 0.03435,
# 'N': 0.02228, 'O': 0.01764, 'P': 0.01764, 'Q': 0.02136, 'R': 0.01393, 'S': 0.02228,
# 'T': 0.00836, 'U': 0.01393, 'V': 0.00836, 'W': 0.0, 'X': 0.0, 'Y': 0.00279, 'Z': 0.0}


# English letter frequency [Wikipedia https://en.wikipedia.org/wiki/Letter_frequency ]:
D = {'A': 0.08167, 'B': 0.01492, 'C': 0.02782, 'D': 0.04253, 'E': 0.12702, 'F': 0.02228, 'G': 0.02015, 'H': 0.06094,
     'I': 0.06966, 'J': 0.00153, 'K': 0.00772, 'L': 0.04025, 'M': 0.02406, 'N': 0.06749, 'O': 0.07507, 'P': 0.01929,
     'Q': 0.00095, 'R': 0.05987, 'S': 0.06327, 'T': 0.09056, 'U': 0.02758, 'V': 0.00978, 'W': 0.02360, 'X': 0.00150,
     'Y': 0.01974, 'Z': 0.00074}
plain=1
for letter in alphabet:
    for key in D:
        if abs(alphabet[letter]-D[key])< plain:
            target = key
            plain = abs(alphabet[letter]-D[key])
    alphabet[letter] = target
    plain = 1
print(alphabet)
# Output:
#{'A': 'E', 'B': 'T', 'C': 'A', 'D': 'I', 'E': 'R', 'F': 'O', 'G': 'S', 'H': 'D', 'I': 'I',
# 'J': 'L', 'K': 'D', 'L': 'D', 'M': 'L', 'N': 'F', 'O': 'P', 'P': 'P', 'Q': 'F', 'R': 'B',
# 'S': 'F', 'T': 'K', 'U': 'B', 'V': 'K', 'W': 'Z', 'X': 'Z', 'Y': 'J', 'Z': 'Z'}

#c.	Find the Plaintext/Ciphertext letter pairs, alphabetized by plaintext.****
# Modify substitution until a reasonable plaintext
alphabet = {'A': 'E', 'B': 'T', 'C': 'A', 'D': 'O', 'E': 'I', 'F': 'N', 'G': 'S', 'H': 'H', 'I': 'R', 'J': 'D',
            'K': 'L', 'L': 'C', 'M': 'U', 'N': 'M', 'O': 'W', 'P': 'F', 'Q': 'G', 'R': 'Y', 'S': 'P', 'T': 'B',
            'U': 'V', 'V': 'K', 'W': 'Z', 'X': 'Z', 'Y': 'X', 'Z': 'Z'}


for word in words:
    for i,letter in enumerate(word):
        word[i]=alphabet[letter]
temp = []
plainText = []
[temp.append(''.join(word)) for word in words]
[plainText.append(' '.join(temp))]
print(plainText)
# Output before modifying the substitution:
# ['EDEDTIRDAD AOL DIFFLTEI EOFROEEIS LEBEDIF AOL DIEATE FIILLDTS TDAT DDAOFE TDE PIIDL AOL
# FAKE ILI DRBES EASREI TDE DEDD FDIOES PE LEFEOL IO TDE DIFFLTEIS LSEL RO OATRIOAD SEDLIRTB
# AOL TDE EDEDTIRDAD SBSTEFS TDAT FAKE ILI DAIS IFEIATE PEIE ADD DIEATEL KB EDEDTIRDAD AOL
# DIFFLTEI EOFROEEIS AT PFR PE KEEF TDAT FIIFIESS FIBROF PIIPAIL PRTD ILI ROOIBATRBE IESEAIDD
# AOL ILT IP TDE KIJ AFFIIADDES TDE LEFAITFEOT IP EDEDTIRDAD AOL DIFFLTEI EOFROEEIROF AT PFR
# DDADDEOFES STLLEOTS TI FLSD TDEFSEDBES TI LOLEISTAOL SIDRETBS AOL TEDDOIDIFBS DIFFDEJ RSSLES
# RO A KIIALEI DIOTEJT TDAO PDATS RO PIIOT IP TDEF PE PAOT ILI STLLEOTS PDETDEI TDEB AIE EAIOROF
# AO LOLEIFIALLATE FROII II A LIDTIIATE TI TADKDE SIDRETBS FIST FIESSROF FIIKDEFS AOL LODIBEI
# OEP PABS IP SIDBROF TDEF PDETDEI RTS LEBEDIFROF SBSTEFS TDAT DAO DIDATE PRIEPRFDTEIS RO TDE
# FRLLDE IP A KLIOROF KLRDLROF II DIEATROF OELIIFIISTDETRDS TDAT DIIK AOL PLODTRIO DRKE OATLIAD
# DRFKS ILI PADLDTB AOL STLLEOTS AIE AT TDE PIIOT ELFE IP IEFAIKAKDE ROOIBATRIO PDRDE ALBAODROF
# TEDDOIDIFRES RS AT ILI DIIE PE ADSI TAKE DLFAO DIOOEDTRIOS BEIB SEIRILSDB RO EDE PE FIRLE ILISEDBES
# IO TDE PAFRDB DRKE ATFISFDEIE PE DLDTRBATE PADLDTB STLLEOTS AOL STAPP EODILIAFE EADD ITDEIS EBEIB
# SLDDESS AOL AIE TDEIE PII TDE DDADDEOFES KITD RO TDE DDASSIIIF AOL RO DRPE'

# b.	Decrypt the ciphertext with help of the relative letter frequency of the
# English language (e.g., search Wikipedia for letter frequency analysis).
# Note that the text is relatively short and might not completely fulfill the
# given frequencies from the table.

# After modifying the alphabet
# 'ELECTRICAL AND COMPUTER ENGINEERS DEVELOP AND CREATE PRODUCTS THAT CHANGE THE WORLD AND MAKE
# OUR LIVES EASIER THE CELL PHONES WE DEPEND ON THE COMPUTERS USED IN NATIONAL SECURITY AND THE
# ELECTRICAL SYSTEMS THAT MAKE OUR CARS OPERATE WERE ALL CREATED BY ELECTRICAL AND COMPUTER ENGINEERS
# AT WPI WE KEEP THAT PROGRESS MOVING FORWARD WITH OUR INNOVATIVE RESEARCH AND OUT OF THE BOX APPROACHES
# THE DEPARTMENT OF ELECTRICAL AND COMPUTER ENGINEERING AT WPI CHALLENGES STUDENTS TO PUSH THEMSELVES
# TO UNDERSTAND SOCIETYS AND TECHNOLOGYS COMPLEX ISSUES IN A BROADER CONTEXT THAN WHATS IN FRONT OF THEM
# WE WANT OUR STUDENTS WHETHER THEY ARE EARNING AN UNDERGRADUATE MINOR OR A DOCTORATE TO TACKLE SOCIETYS
# MOST PRESSING PROBLEMS AND UNCOVER NEW WAYS OF SOLVING THEM WHETHER ITS DEVELOPING SYSTEMS THAT CAN LOCATE
# FIREFIGHTERS IN THE MIDDLE OF A BURNING BUILDING OR CREATING NEUROPROSTHETICS THAT LOOK AND FUNCTION LIKE
# NATURAL LIMBS OUR FACULTY AND STUDENTS ARE AT THE FRONT EDGE OF REMARKABLE INNOVATION WHILE ADVANCING TECHNOLOGIES
# IS AT OUR CORE WE ALSO TAKE HUMAN CONNECTIONS VERY SERIOUSLY IN ECE WE PRIDE OURSELVES ON THE FAMILY LIKE
# ATMOSPHERE WE CULTIVATE FACULTY STUDENTS AND STAFF ENCOURAGE EACH OTHERS EVERY SUCCESS AND ARE THERE FOR THE
# CHALLENGES BOTH IN THE CLASSROOM AND IN LIFE'


# Letter frequency analysis for the plaintext
p_alphabet = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0,
            'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0,
            'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
count=0 # total number of letters in the text
for word in words:
    for letter in word:
        p_alphabet[letter] += 1
        count += 1
for letter in p_alphabet:
    p_alphabet[letter] = round(p_alphabet[letter]/count, 5)

print(p_alphabet)

#d.	Provide letter frequency for the given plaintext.********
# Output:
# {'A': 0.07985, 'B': 0.00836, 'C': 0.04643, 'D': 0.03714, 'E': 0.13928, 'F': 0.01764,
# 'G': 0.02136, 'H': 0.04178, 'I': 0.05385, 'J': 0.0, 'K': 0.00836, 'L': 0.04364,
# 'M': 0.02228, 'N': 0.07707, 'O': 0.07057, 'P': 0.02228, 'Q': 0.0, 'R': 0.06964,
# 'S': 0.065, 'T': 0.09285, 'U': 0.03435, 'V': 0.01393, 'W': 0.01764, 'X': 0.00279,
# 'Y': 0.01393, 'Z': 0.0}

