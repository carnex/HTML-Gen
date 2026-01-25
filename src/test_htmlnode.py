import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag="a",value="this is a value")
        node2 = HTMLNode(tag="a",value="this is a value")
        self.assertEqual(node, node2)
    
    def test_noteq(self):
        node = HTMLNode(tag="p",value="this is a value")
        node2 = HTMLNode(tag="a",value="this is a value")
        self.assertNotEqual(node, node2)

    def test_propseq(self):
        node = HTMLNode(props={"href": "https://www.google.com","target": "_blank",})
        node2 = HTMLNode(props={"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node, node2)

    def test_propsnoteq(self):
        node = HTMLNode(props={"href": "https://www.google.com","target": "_blank",})
        node2 = HTMLNode(props={"href": "https://www.dog.com","target": "_blank",})
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()