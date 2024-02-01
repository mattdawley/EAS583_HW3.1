import hashlib

a = 99
b = str(a).encode('utf-8')
print(b)
print(int.from_bytes(b, 'big'))
x_hash = hashlib.sha256(str(a).encode('utf-8')).hexdigest()
i = int(x_hash, 16)
b = bin(i)
mask = (1 << 2) - 1
print(mask)
print(bin(mask & i))