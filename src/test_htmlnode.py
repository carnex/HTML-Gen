import unittest

from htmlnode import HTMLNode, LeafNode

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
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_b(self):
        node = LeafNode("b", "I am important!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<b href="https://www.google.com">I am important!</b>')
        
if __name__ == "__main__":
    unittest.main()