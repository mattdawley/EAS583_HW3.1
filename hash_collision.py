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

    #seed X and Y
    x = random.randint(0,100)
    y = 1

    while True:

        # Convert X and Y to hash
        x_hash = hashlib.sha256(str(x).encode('utf-8')).hexdigest()
        y_hash = hashlib.sha256(str(y).encode('utf-8')).hexdigest()

        # Convert hash to bytes
        x_small = str(int(x_hash[-16], 16)).encode('utf-8')
        x_chunk = int.from_bytes(x_small, 'big') & mask

        y_small = str(int(y_hash[-16], 16)).encode('utf-8')
        y_chunk = int.from_bytes(y_small, 'big') & mask

        if x_chunk == y_chunk:
            return x, y

        x += 0
        y += 1
