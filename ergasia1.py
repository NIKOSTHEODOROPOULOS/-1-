#ergasia1
#python 3.7.1
print("--------------------------------------")
print("ΕΡΓΑΣΙΑ.1")
print("--------------------------------------")
def sumIntervals(x):
    a=[]
    mikos=[]
    noumera=[]
    for i in range(len(x)):
        mikos.append(x[i][1]-x[i][0])
        k= x[i][0]
        for j in range(mikos[i]+1):
            noumera.append(k)
            a.extend(noumera)
            k= k + 1
        a.sort()
        result = 0
    if type(a)== list:
            for i in range(len(a)):
                if a[i]-a[i-1]==1:
                    result=result+1

    print("Το αποτελεσμα ειναι",result)


