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

UPPER_PRIME_BOUND = 10000
LOWER_PRIME_BOUND = 55

key = namedtuple('Key', 'mod public private')
def splitList(lst, count=2, default=None, padFront=False):
    deficit = len(lst) % count
    if not deficit == 0 and default:
        for _ in range(deficit + 1):
            lst.append(default)
    return [lst[i:i+count] for i in range(0, len(lst), count)]
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
        #return 127, 9721
        return p, q

    def getCoprime(λn):
        """Get a number coprime to, and less than λn"""
        candidate = getPrime(λn)
        #candidate = 751
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

    ords = [ord(x) - ord('A') for x in plaintext.upper()]
    zeroPrefixed = [('0' if x < 10 else '') + str(x) for x in ords]
    grouped = [int(a+b+c) for a,b,c in splitList(zeroPrefixed, 3, '23')] # Pad with 'X'
    crypts = [(x**pubkey) % mod for x in grouped]
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

    result = []
    for x in ciphertext.split(' '):
        decrypted_chunk = str((int(x)**privkey) % mod)
        if len(decrypted_chunk) < 6:
            decrypted_chunk = '0'+decrypted_chunk
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
    import requests
    wordlist_url = 'http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain'
    words = requests.get(wordlist_url).content.decode('utf-8').splitlines()

    def simplify(string):
        """Take out all non-alpha text for punctuation insensitive comparison"""
        return ''.join([x for x in string if ord(x) in range(ord('A'), ord('Z') + 1)])

    for i in range(10000):
        test_key = gen_key(True)

        message = ' '.join([random.choice(words) for _ in range(5)]).upper()
        ciphertext = encrypt(True, test_key.public, test_key.mod, message)
        plaintext = decrypt(True, test_key.private, test_key.mod, ciphertext)

        if simplify(plaintext) != simplify(message):
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
