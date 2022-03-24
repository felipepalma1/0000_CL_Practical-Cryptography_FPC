import hashlib

'''MD5 Blanco'''
md5hasher = hashlib.md5()
print(md5hasher.hexdigest())


'''Es posible actualizar paso por paso un hash MD5'''
md5hasher.update(b'a')
md5hasher.update(b'l')
md5hasher.update(b'i')
md5hasher.update(b'c')
print(md5hasher.hexdigest())
md5hasher.update(b'e')
print(md5hasher.hexdigest())
