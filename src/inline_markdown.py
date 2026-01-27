from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    output = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            output.append(node)
        else:
            if delimiter not in node.text:
                output.append(node)
                continue
            parts = node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise Exception("End delimiter missing please check input file.")   
            for i, part in enumerate(parts):
                if part == "":
                    continue
                if i % 2 == 0:
                    output.append(TextNode(part, TextType.TEXT))
                else:
                    output.append(TextNode(part, text_type))
    return output
                
def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    output = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            output.append(node)
            continue
        matchs = extract_markdown_images(node.text)
        if len(matchs) == 0:
             output.append(node)
        else:
            current_text = node.text
            for match in matchs:
                parts = current_text.split(f"![{match[0]}]({match[1]})",1)
                if len(parts[0]) > 0:
                    output.append(TextNode(parts[0], TextType.TEXT))
                output.append(TextNode(match[0], TextType.IMAGE, match[1]))
                current_text = parts[1]
            if len(current_text) != 0:
                output.append(TextNode(current_text, TextType.TEXT))
    return output                   

def split_nodes_link(old_nodes):
    output = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            output.append(node)
            continue
        matchs = extract_markdown_links(node.text)
        if len(matchs) == 0:
            output.append(node)
        else:
            current_text = node.text
            for match in matchs:
                parts = current_text.split(f"[{match[0]}]({match[1]})",1)
                if len(parts[0]) > 0:
                    output.append(TextNode(parts[0], TextType.TEXT))
                output.append(TextNode(match[0], TextType.LINK, match[1]))
                current_text = parts[1]
            if len(current_text) != 0:
                output.append(TextNode(current_text, TextType.TEXT))
    return output

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes