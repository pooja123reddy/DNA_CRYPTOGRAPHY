f=open('protein.txt','r')



protein_map = dict()

i = 0
for line in f:
    if i % 2 == 0:
        tRNA = line.strip()
    else:
        protein = line.strip()  # Removed [2:] because proteins don't need to be trimmed
        print(tRNA + " " + protein)
        protein_map[tRNA] = protein
    i += 1

f.close()



f = open('ascii.txt', 'r')
char_map = dict()

for line in f:
    line = line.strip()  # Remove any leading/trailing whitespace
    if not line:  # Skip empty lines
        continue
    parts = line.split()  # Split by whitespace (spaces)
    if len(parts) >= 2:  # Ensure there are at least two parts
        # Check if the character is already in the map and handle duplicates
        if parts[0] in char_map:
            print(f"Warning: Duplicate entry for '{parts[0]}'. Overwriting value '{char_map[parts[0]]}' with '{parts[1]}'.")
        char_map[parts[0]] = parts[1]
        print(parts[0] + "\t" + parts[1])

f.close()

# Print out the character map for verification
print("\nCharacter Map Loaded:")
for key, value in char_map.items():
    print(f"'{key}': '{value}'")





def complement(DNA):
    _DNA=""
    for char in DNA:
        if char == 'A':
            _DNA+='T'
        elif char == 'T':
            _DNA+='A'
        elif char == 'C':
            _DNA+='G'
        elif char == 'G':
            _DNA+='C'

    return _DNA




def complement_tRNA(tRNA):
    mRNA=""
    for char in tRNA:
        if char == 'A':
            mRNA+='U'
        elif char == 'U':
            mRNA+='A'
        elif char == 'C':
            mRNA+='G'
        elif char == 'G':
            mRNA+='C'

    return mRNA




def translate(seq):
     
    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                 
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }



def compl(DNA,p1):
    f=open('ascii2.txt','w')
    f.write(p1)
    f.write("\n")
    f.write(DNA)
    f.close()



def DNA2Binary(DNA):
    binary=""
    for ch in DNA:
        if ch=='A':
            binary+="00"
        elif ch=='T':
            binary+="01"
        elif ch=="C":
            binary+="10"
        else:
            binary+="11"

    return binary
        





##def convert(plain):
##
##    dict1={'B':'AAGG','A':'ACAT','N':'GCTT','K':'GAGG'}
##    
##    DNA=""
##
##    for char in plain:
##        DNA+=dict1[char]
##
##    return DNA
        

def convert(plain):
    DNA = ""
    for ch in plain:
        if ch in char_map:
            DNA += char_map[ch]
        else:
            print(f"Character '{ch}' not found in char_map, skipping it.")
    return DNA





def convert2mRNA(DNA):
    _mRNA=DNA.replace("T","U")
    return _mRNA
   

def convert2DNA(mRNA):
    DNA=mRNA.replace("U","T")
    return DNA
   


def rightShift(DNA):
    return DNA[-1:] + DNA[:-1]   


def XNOR_and_convert2DNA(binary,_intron):
    dict1={'00':'A', '01':'T', '10':'C', '11':'G'}

    _intron=""
    for i in range(len(binary)//4):
        _intron+=intron

    print(binary)

    print(_intron )  

    xnor=""
    
    for i in range(len(binary)):
        
        if binary[i] == _intron[i]:
           xnor+="1"
        else:
            xnor+="0"

    print(xnor)

    DNA=""
    
    for i in range(len(xnor)//2):
        DNA+=dict1[xnor[i*2:i*2+2]]

    print(DNA)
    return DNA
    




plain=input("\n\nEnter plain text: ")
intron=input("\n\nEnter intron sequence: ")
n = int(input("Enter the number of iterations: "))  # Ensure n is an integer


intron1=intron[:4]
intron2=intron[4:]

print("\nintron1 :" + intron1)
print("intron2 :" + intron2)



print("\nPLAIN TEXT\n")

if len(plain)%2==0:
    plain1=plain[:len(plain)//2]
    plain2=plain[len(plain)//2:]
else:
    plain1=plain[:len(plain)//2 + 1]
    plain2=plain[len(plain)//2+1:] + "#"

print(plain1)
print(plain2)
    

print("\nDNA\n")
DNA1=convert(plain1)
print(DNA1)
DNA2=convert(plain2)
print(DNA2)

##print("\n_DNA\n")
_DNA1 =compl(intron,plain)
##print _DNA1
##_DNA2 =complement(DNA2)
##print _DNA2


binary1 = DNA2Binary(DNA1)
binary2 = DNA2Binary(DNA2)
print("\nbinary sequence1 : "+ binary1)
print("binary sequence2 : "+ binary2)


DNA1=XNOR_and_convert2DNA(binary1,intron1)
DNA2=XNOR_and_convert2DNA(binary2,intron2)



for i in range(n):

    print("\n\nIteration : "+str(i))

    print("\nmRNA:")
    mRNA1 = convert2mRNA(DNA1)
    print(mRNA1)
    mRNA2 = convert2mRNA(DNA2)
    print(mRNA2)

    print("\ntRNA:")
    tRNA1 = complement_tRNA(mRNA1)
    print(tRNA1)
    tRNA2 = complement_tRNA(mRNA2)
    print(tRNA2)


    print("\nDNA:")
    DNA1 = convert2DNA(tRNA1)
    print(DNA1)
    DNA2 = convert2DNA(tRNA2)
    print(DNA2)


    print("\nR-Shift:")
    DNA1 = rightShift(DNA1)
    print(DNA1)
    DNA2 = rightShift(DNA2)
    print(DNA2)




_CT=DNA1+DNA2
_CT=convert2mRNA(_CT)
_CT=complement_tRNA(_CT)




print ("\n\nIntermediate result : " + (_CT))


CT=""

# Check for the presence of the protein mapping
CT = ""
for i in range(len(_CT) // 4):
    segment = _CT[i * 4:i * 4 + 4]
    if segment in protein_map:
        CT += protein_map[segment]
    else:
        print(f"Warning: '{segment}' not found in protein_map, skipping.")

print("\n\nCIPHER TEXT : " + CT)