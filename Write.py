a=3
b=5
with open ('example.txt', 'w') as f:
    c = str(float(a)+float(b))+ '\b'

    f.write(c)
    f.close()

with open('example.txt') as rt:

    d=rt.read()
    print(d)