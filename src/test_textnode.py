import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
         node = TextNode("This is a text node", TextType.BOLD)
         node2 = TextNode("This is a text node", TextType.ITALIC)
         self.assertNotEqual(node, node2)
    
    def test_url(self):
        node = TextNode("this is a text node", TextType.BOLD, "www.google.com")
        node2 = TextNode("this is a text node", TextType.TEXT, "www.google.com")
        self.assertEqual(node.url, node2.url)
    
    def test_txt(self):
        node = TextNode("this is a text node", TextType.BOLD, "www.google.com")
        node2 = TextNode("this is a text de", TextType.TEXT, "www.google.com")
        self.assertNotEqual(node.text, node2.text)
if __name__ == "__main__":
    unittest.main()
