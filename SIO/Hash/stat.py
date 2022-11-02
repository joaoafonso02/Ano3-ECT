#!/bin/python
import sys
import os
from cryptography.hazmat.primitives import hashes

# analisador estatísitico - quantos bits a 1 tem cada número até 256
def main():
    if len(sys.argv) != 2:
        print("Usage: %s file algorithm" % (sys.argv[0]), file=sys.stderr)
        sys.exit(1)

    alg_name = 'hashes.' + sys.argv[1] + '()'
    buffer = bytearray(os.urandom( 1024 )) # 10240

    ones_dict = [0] * 256 # cada byte pode ter 256 valores possíveis 
    for i in range(0, 256):
        for j in range(0, 8):
            if (1 << j) & i != 0:
                ones_dict[i] += 1
        #print('%d %d' % (i, ones_dict[i]))

    bin_dict = [0] * (eval(alg_name).digest_size * 8 + 1)
    for i in range(0, len( buffer ) * 8):
        byte = i // 8
        bit = i % 8

        alg_f = hashes.Hash( eval(alg_name) )
        alg_f.update( buffer )
        d1 = alg_f.finalize()

        saved_byte = buffer[byte]

        buffer[byte] ^= 1 << bit

        alg_f = hashes.Hash( eval(alg_name) )
        alg_f.update( buffer )
        d2 = alg_f.finalize()

        buffer[byte] = saved_byte

        ones = 0
        for j in range(0, len(d1)):
            delta = d1[j] ^ d2[j]
            ones += ones_dict[delta]

        bin_dict[ones] += 1

    for i in range(0, len(bin_dict)):
        print('%3d %d' % (i, bin_dict[i]))

if __name__ == "__main__":
    main()