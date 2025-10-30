alphabet=[]
sentence=input("Enter your sentence here.").lower()
import string

for i in sentence:
    if i in string.ascii_lowercase:
        if i not in alphabet:
          alphabet.append(i)

print(alphabet)
if len(alphabet)==26:
    print("It is a pangram :)")
else:
    print("It is not a pangram :(")

al=[]
for i in string.ascii_lowercase:
    al.append(i)
for i in sentence:
    if i in al:
        al.remove(i)
if len(al)==0:
    print("It is a pangram :)")
print(al)

alpha={}
for i in string.ascii_lowercase:
    alpha[i]=0

print(alpha)
for i in sentence:
    if i in alpha:
        alpha[i]+=1

print(alpha)
count=0
for i in alpha:
    if alpha[i]>0:
        count+=1
if count==26:
    print("It is a pangram :)")
else:
    print("It is not a pangram :(")