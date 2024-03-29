import sys
sys.setrecursionlimit(1000000)  # long type,32bit OS 4B,64bit OS 8B(1bit for sign)
from Crypto.PublicKey import RSA

n = 0x00d546aa825cf61de97765f464fbfe4889ad8bf2f25a2175d02c8b6f2ac0c5c27b67035aec192b3741dd1f4d127531b07ab012eb86241c09c081499e69ef5aeac78dc6230d475da7ee17f02f63b6f09a2d381df9b6928e8d9e0747feba248bffdff89cdfaf4771658919b6981c9e1428e9a53425ca2a310aa6d760833118ee0d71
p = 11807485231629132025602991324007150366908229752508016230400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001
q = n//p
e = 65537


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n

phi = (p-1)*(q-1)
d = mulinv(e, phi)
key = RSA.construct([n, e, d])
print(key.exportKey().decode("utf-8"))
