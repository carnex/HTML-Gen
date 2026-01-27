import unittest
import re
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import extract_markdown_images, extract_markdown_links, split_nodes_delimiter, split_nodes_image, split_nodes_link

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

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")
        
    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        
if __name__ == "__main__":
    unittest.main()
