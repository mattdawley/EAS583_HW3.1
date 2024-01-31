import hashlib
import os
import string
import random

def hash_collision(k):
    print("k =", k)
    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )
    if k > 5:
        print( "too long right now" )
        return( b'\x00',b'\x00' )
   
    #Generate random 'X'
    x_str = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=k))
    x = hashlib.sha256(x_str.encode('utf-8')).hexdigest()
    x_b = x.encode('utf-8')

    #Find 'Y' that matches final k bits
    found = False
    while not found:
        #Generate random 'Y' to test
        y_str = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=1000))
        y = hashlib.sha256(y_str.encode('utf-8')).hexdigest()
        y_b = y.encode('utf-8')

        #Compare final k bits of 'X' and 'Y'
        if x_b[-k:] == y_b[-k:]:
            found = True
    
    return(x,y)


print(hash_collision(5))

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


str = "Bitcoin"
m = hashlib.sha256()
for c in str:
  m.update(c.encode('utf-8'))
  #print(m.hexdigest())
m.hexdigest()
"""