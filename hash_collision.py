import hashlib
import os
import random

def hash_collision(k):

    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )

    mask = (1 << k) - 1

    #seed X (randomly) and Y
    x = random.randint(2,100)
    y = 1

    while True:
        if y == x:
            y += 1

        # Convert X and Y to hash
        x_hash = hashlib.sha256(str(x).encode('utf-8')).hexdigest()
        y_hash = hashlib.sha256(str(y).encode('utf-8')).hexdigest()

        # Apply mask, convert to binary
        x_masked = bin(int(x_hash,16) & mask)
        y_masked = bin(int(y_hash, 16) & mask)

        if x_masked == y_masked:
            return str(x).encode('utf-8'), str(y).encode('utf-8')

        y += 1