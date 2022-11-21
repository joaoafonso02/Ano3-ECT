#!/bin/python
import sys
from cryptography.hazmat.primitives import hashes

def main():
    if len(sys.argv) != 3:
        print("Usage: %s file algorithm" % (sys.argv[0]), file=sys.stderr)
        sys.exit(1)

    # ALGORITHM in argv[2]
    alg_name = 'hashes.' + sys.argv[2] + '()'
    alg_f = hashes.Hash( eval(alg_name) )

    # FILE in argv[1]
    with open( sys.argv[1] , 'rb' ) as in_file:
        while True:
            block = in_file.read( 8192 ) # ler 8k
            if len(block) == 0:
                digest = alg_f.finalize()
                in_file.close()
                break
            else:
                alg_f.update( block )
        print( digest.hex() )

if __name__ == "__main__":
    main()