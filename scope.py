#global scope
a=1
def f():
    b=2
    print(a,b)

def ff():
    a='asdf'
    print(a)

i=-1
print(i)
i=[print(i) for i in range(10)]

s=[1,2,3,4,5]
d=(1,2,3,4,5)
dd={1,2,3,4,5}
ss={'a':1,'b':2}

def f(x):
    x.pop()
    return x
print(s)
s2=f(s)
print(s,s2)
s2[0]='123'
print(s,s2)

print(dd)
dd2=f(dd)
print(dd,dd2)
dd2=dd2.difference({4})
print(dd,dd2)

def f(x):
    x['a']='sdaf'
    return x
print(ss)
ss2=f(ss)
print(ss,ss2)
ss2['b']='123'
print(ss,ss2)

