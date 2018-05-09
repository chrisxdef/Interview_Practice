from random import shuffle

def find_pairs( int_array ):
    pairs   = []
    loners  = []
    for i in range( len(int_array) ):
        v = int_array[i]

        pair = None
        for j in loners:
            if v + int_array[j] == 10:
                pair = (j, i)

        if pair == None:
            loners.append(i)
        else:
            pairs.append(pair)

    return pairs

if __name__ == '__main__':
    int_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    shuffle(int_array)

    print find_pairs(int_array)
