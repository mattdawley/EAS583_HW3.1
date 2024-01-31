import hashlib
import os
import string
import random

def hash_collision2(k):
    print("k =", k)
    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )

    x_og = 0
    y_og = 1

    while True:
        x = hashlib.sha256(str(x_og).encode('utf-8')).hexdigest()
        x_b = x.encode('utf-8')

        y = hashlib.sha256(str(y_og).encode('utf-8')).hexdigest()
        y_b = y.encode('utf-8')

        #Compare final k bits of 'X' and 'Y'
        if x_b[-k:] == y_b[-k:]:
            return(x_og, y_og)
        x_og += 1
        y_og += 1

#print(hash_collision(7))
#(82228326, 82228327)

"""You can compute SHA256 hashes using hashlib, which works like this.
def produce_hash(word):
    h = hashlib.sha256(word.encode('utf-8')).hexdigest()
    return h

def test(word, k):
    x = produce_hash(word)
    found = False
    while not found:
        rando_word = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=10))
        y = produce_hash(rando_word)
        if x[-k:] == y[-k:]:
            found = True
    return (x, rando_word, y)

print('test', produce_hash('test'))
print(test('test', 5))
print()
"""

"""The function “hashlib.sha256” expects bytes, so we use the “encode” function 
to convert our string to bytes, before passing it to the function.

“hexdigest” gives you the hexadecimal output of the hash function.
Since SHA can process files of arbitrary length, it is sometimes useful to 
calculate the hash in smaller chunks. This is important when you’re hashing 
large files, but not necessary when the input to the hash fits easily in 
memory. The code below calculates the same hash one character at a time.

"""
"""str = "ab"
m = hashlib.sha256()
for c in str:
  m.update(c.encode('utf-8'))
  print(m.hexdigest())
m.hexdigest()
"""



def hash_collision(k, chunk_size=8):

    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )

    mask = (1 << k) - 1
    x = 0
    y = 1
    while True:
        print(x)
        x_hash = hashlib.sha256(str(x).encode('utf-8')).digest()
        y_hash = hashlib.sha256(str(y).encode('utf-8')).digest()
        """
        x_small = str(int(x_hash[-chunk_size], 16)).encode('utf-8')
        x_chunk = int.from_bytes(x_small, 'big') & mask

        y_small = str(int(y_hash[-chunk_size], 16)).encode('utf-8')
        y_chunk = int.from_bytes(y_small, 'big') & mask

        """
        x_chunk = int.from_bytes(x_hash[-chunk_size:], 'big') & mask
        y_chunk = int.from_bytes(y_hash[-chunk_size:], 'big') & mask

        if x_chunk == y_chunk:
            return x, y

        x += 1
        y += 1

"""
print(hash_collision2(7))
#(82228326, 82228327)
print()
x = hashlib.sha256(str(49).encode('utf-8')).hexdigest()
y = hashlib.sha256(str(50).encode('utf-8')).hexdigest()
print(x)
print(y)
print(x.encode('utf-8'))
print(y.encode('utf-8'))
str = "a"
by = str.encode('utf-8')
print(by)
"""