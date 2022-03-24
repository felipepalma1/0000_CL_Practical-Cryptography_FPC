'''El siguiente ejercicio tiene como objetivo transformar entradas tipo cadenas de texto en formato MD5'''

import hashlib

md5hasher = hashlib.md5(b'alice')
print(md5hasher.hexdigest())

md5hasher = hashlib.md5(b'bob')
print(md5hasher.hexdigest())

md5hasher = hashlib.md5(b'balice')
print(md5hasher.hexdigest())

md5hasher = hashlib.md5(b'cob')
print(md5hasher.hexdigest())

md5hasher = hashlib.md5(b'a')
print(md5hasher.hexdigest())

md5hasher = hashlib.md5(b'aa')
print(md5hasher.hexdigest())

'''10 copias del caracter a'''
md5hasher = hashlib.md5(b'a'*10)
print(md5hasher.hexdigest())

'''100000 copias de caracter a'''
md5hasher = hashlib.md5(b'a'*100000)
print(md5hasher.hexdigest())