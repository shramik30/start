#list - apppend, extend, count ,insert, length 


from audioop import reverse
from pickle import TRUE
from platform import python_branch
from re import T


kiran=[1,21,2.2,'kiran', True]
print(type(kiran))

#append 

kiran.append(2)
print(kiran)

shramik=[5,3.5,'true']
shramik.append(65)
print(shramik)

kiran.append(22.5)
print(kiran)

#extend

shramik.extend([569,'kiran'])
print(shramik)

#insert

shramik.insert(1,'python')
print(shramik)

#count

print(shramik.count('python'))
print(kiran.count(1))

#length

print(len(shramik))
print(len(kiran))

for i in kiran:
    print(i)
soumya=[6,2,3,8,[25,56,45,2],12,32,3]
print(soumya)
print(soumya[4][0])
B='kiran'
for i in B:
    print(i)

#looping system - while, for, range

#while

c=0
while c<3:
    c=c+1
    print('while')
else: 
    print('op') 

#for

pavan=[1,2,3,4,5,6]
sum=0
for i in pavan:
    sum=sum+i
    print(sum)


#RANGE 

for i in range(1,10):
   print(i)

for a in range(1,10,2):
    print(a)

#TUPLE

t=()
print(type(t)) 

prashanth=(1,2,2,2,3)
harish=(19,12,12,12)
print(prashanth+harish)

a=(0x56)
print(a)

a=5.5+6j
b=2.5+10j
print(a*b)

a=5j
print(a.imag)

s=kiran

a=3e2
print(a,type(a),id(a))

s='python'
print(s[0:5:2])

a="10"
b=int(a)
print(b,type(b))

n=9
for i in range(1,21):

    print(n,"x",i,"=",n*i)