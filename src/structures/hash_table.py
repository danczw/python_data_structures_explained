class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size

    def custom_hash(self, key):
        """ custom function for hashing keys """
        hash_value = 0

        for i in key:
            hash_value += ord(i)
            # add randomness to decrease likelihood of same hash values for different keys (collision)
            hash_value = (hash_value * ord(i)) % self.table_size
        
        return hash_value

    def add_key_value(self, key, value):
        """ add key, value pair to hash table by hashing key """
        hashed_key = self.custom_hash(key)

        if self.hash_table[hashed_key] is None:
            self.hash_table[hashed_key] = Node(Data(key, value), None)
        else:
            node = self.hash_table[hashed_key]
            while node.next_node:
                node = node.next_node

            node.next_node = Node(Data(key, value), None)
    
    def get_value(self, key):
        """ return value of a key """
        hashed_key = self.custom_hash(key)

        if self.hash_table[hashed_key] is not None:
            node = self.hash_table[hashed_key]

            if node.next_node is None:
                return node.data.value
            
            while node.next_node:
                if key == node.data.key:
                    return node.data.value
                node = node.next_node
            
            if key == node.data.key:
                return node.data.value
        
        return None

    def print_table(self):
        """ display hash table """
        print("{")
        for i, val in enumerate(self.hash_table):
            if val is not None:
                llist_string = ""
                node = val

                if node.next_node:
                    while node.next_node:
                        llist_string += (
                            str(node.data.key + " : " + str(node.data.value) + " -> ")
                        )
                        node = node.next_node
                    
                    llist_string += (
                        str(node.data.key + " : " + str(node.data.value) + " -> None")
                    )
                    print(f"    [{i}] {llist_string}")
                else:
                    print(f"    [{i}] {val.data.key} : {val.data.value}")
            else:
                print(f"    [{i}] {val}")

# testing
# ht = HashTable(4)
# ht.add_key_value("hi", "there")
# ht.add_key_value("hi", "there")
# ht.add_key_value("hello", "you")
# ht.add_key_value("dog", "wuff")
# ht.print_table()