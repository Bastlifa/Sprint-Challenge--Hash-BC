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
    for i in range(len(weights)):
        hash_table_insert(ht, weights[i], i)

    for i in weights:
        if hash_table_retrieve(ht, limit - i):
            a.append(hash_table_retrieve(ht, limit - i))
            hash_table_remove(ht, limit - i)
            a.append(hash_table_retrieve(ht, i))
            return a

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

# weights_2 = [4, 4]
# answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
# for i in range(len(answer_2)):
#     answer_2[i] = str(answer_2[i])
# print_answer(answer_2)