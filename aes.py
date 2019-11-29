input = [0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0,
         0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1,
         1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0,
         1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1]
S_box = [[0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
        [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
        [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
        [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
        [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
        [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
        [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
        [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
        [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
        [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
        [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
        [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
        [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
        [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
        [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
        [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]]
round_key = [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0,
             0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1,
             1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1,
             1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0]
round_key_hex=[[0x34, 0x09, 0xa6, 0xd6],
              [0x76, 0x93, 0x28, 0x43],
              [0xd5, 0x04, 0xc8, 0xcd],
              [0xf1, 0xb5, 0x72, 0x72]]
irreducable = [1,0,0,0,1,1,0,1,1]
def get_columns(matrix):
    columns = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return columns
def xor(list1,list2):
    assert len(list1)==len(list2)
    res=[]
    for k in range(len(list1)):
        res.append(list1[k]^list2[k])
    return res
def reduce_poly(result,irreducable):
    irr=irreducable[:]
    [irr.append([0]) for k in range(len(result)-9)]
    temp=result[:]
    for i in range(len(result)-8):
        temp = xor(temp,irr)
        irr.pop(len(irr)-1)
        irr.insert(0,0)
    return temp
def gal_mul(column,coefficient):
    out = [0]*8
    for idx, element in enumerate(column):
        c=[]
        c[:0] = format(int(element, 16),'08b')
        d = [int(k) for k in c ]
        c = bin(coefficient[idx])[2:]
        c = [int(k) for k in c]
        result = [0] * (len(d) + len(c) - 1)
        for o1, i1 in enumerate(d):
            for o2, i2 in enumerate(c):
                result[o1 + o2] += i1 * i2
        result=[x%2 for x in result]
        t = []
        flag = 0
        #remove zeros
        for k in range(len(result)):
            if len(result) < 9: break
            if flag == 0:
                if result[k] != 0:
                    t.append(result[k])
                    flag = 1
            else:
                t.append(result[k])

        if len(t)!=0: result=t[:]
        if len(result)>8:
            result = reduce_poly(result,irreducable)
        # pad zeros
        if len(result)<8:
            for k in range(8 - len(result)): result.insert(0,0)
        out=xor(result[len(result)-8:len(result)],out)
    return out
# 2a- Convert the given 128-bit input to Hexadecimal form.
inp=''.join(map(str, input))
input_h = hex(int(inp, 2))
print('Input in Hexadecimal form:\n',input_h)
'''
Output:
Input in Hexadecimal form: 
0x56e219b244b3db43811e9d3a9e85f34f
'''
r=''.join(map(str, round_key))
input_h = hex(int(r, 2))
print('key in Hexadecimal form:\n',input_h)
# 2b- Write the input in a state diagram (4 by 4 matrix).
input_hex = [[0x56, 0xe2, 0x19, 0xb2],
             [0x44, 0xb3, 0xdb, 0x43],
             [0x81, 0x1e, 0x9d, 0x3a],
             [0x9e, 0x85, 0xf3, 0x4f]]
# 2c- Apply SubBytes Step: use AES S-box to substitute the input.
SubBytes_out=[]
for x,r in enumerate(input_hex):
    out_row=[]
    for y,c in enumerate(r):
        column = int(c%16)
        row = int((c - column)/16)
        out_row.append(hex(S_box[row][column]))
    SubBytes_out.append(out_row)
print('\nAfter SubBytes Step:')
[print(row) for row in SubBytes_out]
'''
Output:
After SubBytes Step:

['0xb1', '0x98', '0xd4', '0x37']
['0x1b', '0x6d', '0xb9', '0x1a']
['0x0c', '0x72', '0x5e', '0x80']
['0x0b', '0x97', '0x0d', '0x84']
'''
# 2d- Apply ShiftRows Step.
ShiftRows_out = SubBytes_out[:]
for r,row in enumerate(ShiftRows_out):
    for k in range(r):
        temp = row.pop(0)
        row.append(temp)
    ShiftRows_out[r] = row
print('\nAfter ShiftRows Step:')
[print(row) for row in ShiftRows_out]
'''
Output:
After ShiftRows Step:

['0xb1', '0x98', '0xd4', '0x37']
['0x6d', '0xb9', '0x1a', '0x1b']
['0x5e', '0x80', '0xc', '0x72']
['0x84', '0x0b', '0x97', '0x0d']
'''

# 2e- Apply Mixcolumns Step: use Irreducible polynomial P(x)=x^8+x^4+x^3+x+1.
c_matrix = [[2, 3, 1, 1],
          [1, 2, 3, 1],
          [1, 1, 2, 3],
          [3, 1, 1, 2]]
columns = get_columns(ShiftRows_out)
Mixcolumns_out = ShiftRows_out[:]
temp=[]
for c, column in enumerate(columns):
    col=[]
    for j in range(4):
        col.append(gal_mul(column, c_matrix[j]))
    temp.append(col)
for k,r in enumerate(temp):
    for i,h in enumerate(r):
        h = ''.join(map(str, h))
        temp[k][i] = hex(int(h, 2))
Mixcolumns_out = get_columns(temp)
print('\nAfter MixColumns step:\n')
[print(row) for row in Mixcolumns_out]
'''
After MixColumns step:
Output:
['0x14', '0x70', '0x06', '0x3c']
['0x0d', '0x61', '0x63', '0x9a']
['0xf7', '0x27', '0x74', '0xdf']
['0xe8', '0x9c', '0x44', '0x2a']
'''

# 2f- Apply AddRoundKey Step: use the given round key
AddRoundKey_out=Mixcolumns_out[:]
for k,element in enumerate(Mixcolumns_out):
    row=[int(element[k], 16) for k in range(len(element))]
    AddRoundKey_out[k]= xor(round_key_hex[k],row)
for k,element in enumerate(AddRoundKey_out):
    row = [hex(element[k]) for k in range(len(element))]
    AddRoundKey_out[k]=row
print('\nAfter AddRoundKey step:\n')
[print(row) for row in AddRoundKey_out]
'''
Output:
After AddRoundKey step:

['0x20', '0x79', '0xa0', '0xea']
['0x7b', '0xf2', '0x4b', '0xd9']
['0x22', '0x23', '0xbc', '0x12']
['0x19', '0x29', '0x36', '0x58']
'''