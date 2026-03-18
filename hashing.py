import hashlib

class ConsistentHashing:

    def get_node(self, key, nodes):

        hash_key = int(hashlib.md5(key.encode()).hexdigest(), 16)
        return nodes[hash_key % len(nodes)]
