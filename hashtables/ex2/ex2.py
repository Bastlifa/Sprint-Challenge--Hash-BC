#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for t in tickets:
        hash_table_insert(hashtable, t.source, t.destination)

    
    start = hash_table_retrieve(hashtable, 'NONE')
    cur = start
    route[0] = cur
    i=0
    while cur != "NONE":
        cur = hash_table_retrieve(hashtable, cur)
        i += 1
        route[i] = cur
    
    return route
