from textnode import TextType, TextNode
from htmlnode import HTMLNode

def main():
    node = TextNode("This is me", TextType.BOLD, "https://github.com/carnex/HTML-Gen")
    print(node)

main()
