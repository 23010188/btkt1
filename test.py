import unittest

class TestChord(unittest.TestCase):
    def setUp(self):
        self.nodes = create_chord_ring(4, m=4)  

    def test_ring_successors(self):
      
        for node in self.nodes:
            self.assertIsNotNone(node.successor)
            print(node, "-> successor:", node.successor)

    def test_lookup_single_key(self):
       
        start_node = self.nodes[0]
        key = 7
        responsible = start_node.find_successor(key)
        self.assertIsNotNone(responsible)
        print(f"Key {key} được lưu tại {responsible}")

    def test_lookup_multiple_keys(self):
  
        keys = [2, 5, 10, 13]
        for k in keys:
            res = self.nodes[0].find_successor(k)
            self.assertIsNotNone(res)
            print(f"Key {k} -> Node {res.id}")

unittest.main(argv=[''], exit=False)

