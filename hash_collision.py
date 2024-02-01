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
        if y == x:
            y += 1

        # Convert X and Y to hash
        x_hash = hashlib.sha256(str(x).encode('utf-8')).hexdigest()
        y_hash = hashlib.sha256(str(y).encode('utf-8')).hexdigest()

        # Convert hash to bytes
        """
        x_small = str(int(x_hash[-4:], 16)).encode('utf-8')
        zz = int(x_hash[-4:], 16)
        print("zz:", zz)
        print(bin(zz & mask))
        print("x_small:", x_small)
        """
        x_masked = bin(int(x_hash,16) & mask)

        """
        print(type(int.from_bytes(x_small, 'big')))
        print(type(mask))
        print(bin(int.from_bytes(x_small, 'big')))
        print(bin(int.from_bytes(x_small, 'big') & mask))
        print(int.from_bytes(x_small, 'big'))
        print("Full X:", x_hash)
        print("Small X:", x_hash[-4:])
        print("Small X Int:", int(x_hash[-4],16))
        print("Small X Binary:", bin(int(x_hash[-4],16)))
        print("X_Masked:", x_masked)
        y_small = str(int(y_hash[-4:], 16)).encode('utf-8')
        """
        y_masked = bin(int(y_hash, 16) & mask)
        """
        print("Full Y:", y_hash)
        print("Small Y:", y_hash[-4:])
        print("Small Y Int:", int(y_hash[-4],16))
        print("Small Y Binary:", bin(int(y_hash[-4],16)))
        print("Y_Chunk:", y_masked)
        """
        if x_masked == y_masked:
            return str(x).encode('utf-8'), str(y).encode('utf-8')

        y += 1

#print(hash_collision(20))