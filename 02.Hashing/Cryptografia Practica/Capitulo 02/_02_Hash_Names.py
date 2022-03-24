'''El presente archivo python recibe un valor que sera transformado a un hash MD5'''

'''Importa biblioteca hashlib'''
import hashlib

'''Ingresado el valor Alice, el hasher MD5 entrega un digest'''
md5hasher = hashlib.md5(b'Alice')
print(md5hasher.hexdigest())

'''Ingresado el valor Bob, el hasher MD5 entrega un digest'''
md5hasher = hashlib.md5(b'Bob')
print(md5hasher.hexdigest())
