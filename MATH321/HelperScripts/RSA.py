"""
Cute lil kid RSA module for Discrete Structures

Beware the padding oracle
...and birthday paradox
...and literally every other attack against RSA ever

...(please don't use this for anything outside a maths course)
"""
# pylint: disable=C0103
# Because apparently λn is not a PEP8 approved name :(
import random
import argparse
from collections import namedtuple
from sympy import lcm as sp_lcm
from sympy import sieve as sp_sieve

UPPER_PRIME_BOUND = 1000
LOWER_PRIME_BOUND = 55
N_TEST_ITERATIONS = 1000

key = namedtuple('Key', 'mod public private')
def splitList(lst, count=2):
    return [lst[i:i+count] for i in range(0, len(lst), count)]
def block_length(mod):
    if mod < 252525:
        return 2
    elif mod < 25252525:
        return 3
    return 4
def gen_key(silent, *_):
    """Generate and print a new private/public keypair"""
    def getPrime(upperbound=UPPER_PRIME_BOUND, lowerbound=LOWER_PRIME_BOUND):
        """Get a prime number"""
        prime_list = list(sp_sieve.primerange(lowerbound, upperbound))
        return random.choice(prime_list)

    def getPrimePair():
        """Get a pair of unique primes"""
        p = getPrime()
        q = p
        while q == p:
            q = getPrime()
        return p, q

    def getCoprime(λn):
        """Get a number coprime to, and less than λn"""
        candidate = getPrime(λn)
        if λn % candidate != 0:
            return candidate
        return getCoprime(λn)

    def getMultModInv(e, λn):
        """Get a multiplicative modular inverse for the whatever"""
        candidates = [x for x in range(λn) if (e * x) % λn == 1]
        return random.choice(candidates)

    p, q = getPrimePair()
    n = p * q
    λn = sp_lcm(p - 1, q - 1)
    e = getCoprime(λn)
    d = getMultModInv(e, λn)

    if not silent:
        print('Modulus: ', n)
        print('Public Exponent: ', e)
        print('Private Exponent: ', d)
    return key(n, e, d)


def encrypt(silent, pubkey, mod, plaintext):
    """Take a user's pubkey and a plaintext, and encrypt it"""
    # Why can't assert be a function like everything else? Whyyyyyyyy
    assert pubkey, 'Public key is required for encryption'
    assert mod, 'Modulus is required for encryption'
    assert plaintext, 'Plaintext is required for encryption'

    CHARS_PER_BLOCK = block_length(mod)

    ords = [ord(x) - ord('A') for x in plaintext.upper()]
    zeroPrefixed = [str(x).zfill(2) for x in ords]
    while len(zeroPrefixed)%CHARS_PER_BLOCK:
        zeroPrefixed.append('23')
    grouped = [int(''.join(x)) for x in splitList(zeroPrefixed, CHARS_PER_BLOCK)]
    crypts = [pow(x, pubkey, mod) for x in grouped]
    alpha_crypts = [str(x) for x in crypts]
    ciphertext = ' '.join(alpha_crypts)

    if not silent:
        print('Encrypting "{}" with key {} and mod {}'.format(
            plaintext, pubkey, mod))
        print(ciphertext)
    return ciphertext


def decrypt(silent, privkey, mod, ciphertext):
    """Take a user's privkey and a ciphertext, and decrypt it"""
    assert privkey, 'Private key is required for decryption'
    assert mod, 'Modulus is required for decryption'
    assert ciphertext, 'Ciphertext is required for decryption'

    CHARS_PER_BLOCK = block_length(mod)

    result = []
    for x in ciphertext.split(' '):
        decrypted_chunk = str(pow(int(x), privkey, mod)).zfill(2*CHARS_PER_BLOCK)
        for char in splitList(decrypted_chunk, 2):
            result.append(chr(int(char) + ord('A')))
    plaintext = ''.join(result)

    if not silent:
        print('Decrypting "{}" with key {} and mod {}'.format(
            ciphertext, privkey, mod))
        print(plaintext)
    return plaintext


def test(*_):
    """Perform a whole bunch of full message exchanges"""
    with open('wordlist.txt', 'r') as myFile:
        words = [x.replace('\n','') for x in myFile.readlines() if '\'' not in x]

    def simplify(string):
        """Take out all non-alpha text for punctuation insensitive comparison"""
        return ''.join([x for x in string if ord(x) in range(ord('A'), ord('Z') + 1)])

    for i in range(N_TEST_ITERATIONS):
        test_key = gen_key(True)

        message = ''.join([random.choice(words) for _ in range(5)]).upper()
        ciphertext = encrypt(True, test_key.public, test_key.mod, message)
        plaintext = decrypt(True, test_key.private, test_key.mod, ciphertext)

        if simplify(plaintext)[:len(message)] != simplify(message):
            print(message)
            print(plaintext)
            response = input('Do these look similar? (y or n)')
            if response.lower() != 'y':
                print('{}x PASS'.format(i))
                print('Key: ', test_key)
                print('Message: ', message)
                print('Ciphertext: ', ciphertext)
                print('Plaintext: ', plaintext)
                print('FAILURE')
                return
    print('PASS')


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(description='Do some kid RSA')
    MODES = PARSER.add_mutually_exclusive_group(required=True)
    MODES.add_argument('--gen-key', dest='mode', action='store_const', const=gen_key,
                       help='Run in key generation mode')
    MODES.add_argument('--encrypt', dest='mode', action='store_const', const=encrypt,
                       help='Encrypt a message using the public key from --key/--mod')
    MODES.add_argument('--decrypt', dest='mode', action='store_const', const=decrypt,
                       help='Decrypt a message using the private key from --key/--mod')
    MODES.add_argument('--full-test', dest='mode', action='store_const', const=test,
                       help='Encrypt and decrypt messages to and from two parties for testing')
    PARSER.add_argument('--key', dest='key', action='store', type=int,
                        help='The key to use for encryption/decryption')
    PARSER.add_argument('--mod', dest='mod', action='store', type=int,
                        help='The modulus to use for encryption/decryption')
    PARSER.add_argument('text', action='store', nargs='?', default='',
                        help='The plain or ciphertext to encrypt/decrypt')
    ARGS = PARSER.parse_args()
    ARGS.mode(False, ARGS.key, ARGS.mod, ARGS.text)
