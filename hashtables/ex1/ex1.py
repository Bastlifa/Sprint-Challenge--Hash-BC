#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    a = []
    # for i in range(len(weights)):
    #     if hash_table_retrieve(ht, weights[i]):
    #         b = hash_table_retrieve(ht, weights[i])
    #         c = []
    #         c.append(b)
    #         c.append(i)
    #         hash_table_insert(ht, weights[i], c)
    #     else:
    #         hash_table_insert(ht, weights[i], i)

    # for i in weights:
    #     if hash_table_retrieve(ht, limit - i):
    #         try:
    #             # len(hash_table_retrieve(ht, limit - i))
    #             return f'aadfasdf, {hash_table_retrieve(ht, limit - i)}'
    #             # b = hash_table_retrieve(ht, limit - i)
    #             # a.append(b[:len(b) - 1])
    #             # a.append(b[:len(b) - 2])
    #         except:
    #             a.append(hash_table_retrieve(ht, limit - i))
    #             # hash_table_remove(ht, limit - i)
    #             a.append(hash_table_retrieve(ht, i))
    #             return a

    for i in range(len(weights)):
        if hash_table_retrieve(ht, weights[i]) is not None:
            if weights[i]*2 == limit:
                return [i, hash_table_retrieve(ht, weights[i])]
        else:
            hash_table_insert(ht, weights[i], i)

        
    for j in weights:
        if hash_table_retrieve(ht, limit - j):
            a.append(hash_table_retrieve(ht, limit - j))
            a.append(hash_table_retrieve(ht, j))
            return a

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

# weights_2 = [4, 4]
# answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
# # for i in range(len(answer_2)):
# #     answer_2[i] = str(answer_2[i])
# print_answer(answer_2)