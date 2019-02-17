#ergasia3
#python 3.7.1
print("--------------------------------------")
print("ΕΡΓΑΣΙΑ.3")
print("--------------------------------------")

li = ["'",'"']
a=0
f=open("test.py",'r')
fn=open("test2.py",'w')
while True:
    text2=""   
    text=f.readline()
    if text == "" : break
    for i in text:
        if i in li: a+=1
        if i == "#" and a%2==0: break
        else: text2= text2 + i
    fn.write(text2)           
f.close()
fn.close()




