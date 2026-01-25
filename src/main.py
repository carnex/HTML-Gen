from textnode import TextType, TextNode

def main():
    node = TextNode("This is me", TextType.BOLD, "https://github.com/carnex/HTML-Gen")
    print(node)

main()