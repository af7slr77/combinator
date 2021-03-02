import itertools
import time
from file_saver import save
from get_adress import get_address


def get_all_permutations(sid, addr):
    words = sid.split()
    for i in itertools.permutations(words, len(words)):
        combined_words = ' '.join(i)
        list_of_addr = get_address(combined_words, 1)
        print(i)
        if addr in list_of_addr:
            save(combined_words)
            break


if __name__ == '__main__':
    SID = 'corn company frozen torch home tank oil move father dream liberty chest'
    start_time = time.time()
    get_all_permutations(SID, '8a7b422674e5936dfbcb5bf61d126eb35b243d5c')

    print("--- %s seconds ---" % (time.time() - start_time))
