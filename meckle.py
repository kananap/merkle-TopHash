import os
import hashlib


#storing pathnames and values in a list
hash = []  
os.getcwd()
for file in os.listdir("file"):
    if file.endswith(".txt"):
        with open(os.path.join("file", file), 'rb') as f:
            variables= f.read()
            hashData=hashlib.md5(variables).hexdigest()
            hash.append(hashData)



print("The hash values of L1, L2, L3, L4:")
# Outputs all the hashed values of L1, L2, L3 and L4
print(hash)
if(len(hash)%2!=0):
        hash.append(hash[-1])
while(len(hash)>1):
    j=0
    for i in range(0, len(hash)-1):
        f = str(hash[i]+hash[i+1])
        hash[j]=hashlib.md5(f.encode()).hexdigest()
        
        i+=2
        j+=1
    del hash[j:]

if (len(hash)==1):
    print("Top Hash:") 
    print(hash)