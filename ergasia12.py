#ergasia12
#python 3.7.1
print("--------------------------------------")
print("ΕΡΓΑΣΙΑ.12")
print("--------------------------------------")
print("Δυστυχως η εμφανιση του κειμενου γινεται καθετα,ελπιζω να μην ειναι μεγαλο λαθος")
letters= [0]

alpha =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alpha2=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for x in range(len(alpha)):
    letters.insert(x,0)
f = open('VVV.txt')
while True:
    line=f.readline()
    for x in range(len(line)):
            for i  in range(len(alpha)):
                if line[x]== alpha[i] or line[x]==alpha2[i]:
                    letters[i]=letters[i]+1
    if len(line) == 0:
        break

print ("αυτος ειναι ο αριθμος στα περισσοτερα εμφανιζομενα γραμματα:",max(letters))        
maxgramma=letters.index(max(letters))
print("το περισσοτερο εμφανιζομενο γραμμα ειναι το:",alpha2[maxgramma])

MIN=max(letters)
for x in range(len(alpha)):
    if letters[i]<MIN and letters[x]!=0:
        min = letters[x]

Mingramma=letters.index(min)
print("Το λιγοτερο εμφανιζομενο γραμμα ειναι το",alpha2[Mingramma])
f.close()

f = open('VVV.txt')

while True:
    line=f.readline()
    keimeno=[]
    for x in range(len(line)):
                if line[x]== alpha[maxgramma] or line[x]==alpha2[maxgramma]:
                    keimeno.insert(x,alpha2[Mingramma])
                elif line[x] == alpha[Mingramma] or line[x]==alpha2[Mingramma]:
                    keimeno.insert(x,alpha2[maxgramma])
                else:
                        keimeno.insert(x,line[x].upper())
    
    for x in range(len(keimeno)):
        print (keimeno[x])

    if len(line) == 0:
        break


f.close()

