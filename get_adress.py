from mnemonic import Mnemonic
from bip32 import BIP32, HARDENED_INDEX
from pyzil.crypto import zilkey
import time
import math


def get_address(words, strange=10):
    address_list = []
    mnemo = Mnemonic("english")
    seed = mnemo.to_seed(words, passphrase="")
    bip32 = BIP32.from_seed(seed)
    for i in range(0, strange):
        path = "m/44'/313'/0'/0/%i" % i
        pab_key = bip32.get_pubkey_from_path(path)
        key = zilkey.ZilKey(public_key=pab_key.hex())
        address_list.append(key.address)
    return address_list


if __name__ == '__main__':
    WORDS = 'home company frozen torch corn tank oil move father dream liberty chest'
    start_time = time.time()
    print(get_address(WORDS))
    print("--- %s seconds ---" % ((time.time() - start_time) * math.factorial(12)/60))
