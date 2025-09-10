import hashlib
import random

# Hàm hash SHA-1 rút gọn còn m-bit
def hash_id(value, m=6):
    return int(hashlib.sha1(value.encode()).hexdigest(), 16) % (2 ** m)

class Node:
    def __init__(self, identifier, m=6):
        self.id = identifier
        self.m = m
        self.successor = self
        self.predecessor = None
        self.finger = [None] * m

    def __repr__(self):
        return f"Node({self.id})"

    # Tìm successor của 1 key
    def find_successor(self, key):
        if self == self.successor:
            return self
        if self.id < key <= self.successor.id or \
           (self.id > self.successor.id and (key > self.id or key <= self.successor.id)):
            return self.successor
        node = self.closest_preceding_node(key)
        return node.find_successor(key)

    # Tìm node gần key nhất trong finger table
    def closest_preceding_node(self, key):
        for finger in reversed(self.finger):
            if finger and self.id < finger.id < key:
                return finger
        return self

    # Join vòng từ node có sẵn
    def join(self, existing_node):
        if existing_node:
            self.init_finger_table(existing_node)
        else:
            self.successor = self
            for i in range(self.m):
                self.finger[i] = self

    def init_finger_table(self, existing_node):
        self.successor = existing_node.find_successor(self.id)
        self.finger[0] = self.successor
        for i in range(1, self.m):
            start = (self.id + 2 ** i) % (2 ** self.m)
            self.finger[i] = existing_node.find_successor(start)

# Demo tạo vòng
def create_chord_ring(num_nodes=5, m=6):
    nodes = []
    for i in range(num_nodes):
        node_id = hash_id(f"node{i}", m)
        node = Node(node_id, m)
        if nodes:
            node.join(nodes[0])
        else:
            node.join(None)
        nodes.append(node)
    return nodes
