'''Presentacion del concepto de digest en hashing'''

'''Se importa la biblioteca hashlib'''
import hashlib

'''Se almacena en una variable el valor del digest MD5 que tiene la biblioteca hashlib importada en linea 4'''
md5hasher = hashlib.md5()

'''Se expresa por pantalla el valor del digest'''
print(md5hasher.hexdigest())