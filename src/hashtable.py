# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f"{self.key} = {self.value}"

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        hashed_key = self._hash_mod(key)
        node = self.storage[hashed_key]

        if node is None:
            node = LinkedPair(key, value)
            self.storage[hashed_key] = node
        else: # collision
            new_head = LinkedPair(key, value)
            new_head.next = node
            self.storage[hashed_key] = new_head

    def remove(self, key):
        hashed_key = self._hash_mod(key)
        node = self.storage[hashed_key]

        if node is None:
            return print(f"{key} could not be found.")

        previous_node = None

        while node != None:
            if node.key == key:
                if previous_node:
                    previous_node.next = node.next
                else:
                    self.storage[hashed_key] = node.next
                
                return
            
            previous_node = node
            node = node.next
        
        print(f"{key} could not be found.")

    def retrieve(self, key):
        hashed_key = self._hash_mod(key)
        node = self.storage[hashed_key]

        while node:
            if node.key == key:
                return node.value

            node = node.next

        return None


    def resize(self):
        old_storage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity

        for node in old_storage:
            while node != None:
                self.insert(node.key, node.value)
                node = node.next



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
