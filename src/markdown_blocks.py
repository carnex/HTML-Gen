from enum import Enum
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextNode, text_node_to_html_node
from inline_markdown import text_to_textnodes

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    OLIST = "ordered_list"
    ULIST = "unordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    children = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) ==  "heading":
            children.append(heading_block_to_html(block))
        if block_to_block_type(block) == "code":
            children.append(code_block_to_html(block))
        if block_to_block_type(block) == "quote":
            children.append(quote_block_to_html(block))
        if block_to_block_type(block) =="unordered_list":
            children.append(Ulist_block_to_html(block))
        if block_to_block_type(block) == "ordered_list":
            children.append(Olist_block_to_html(block))
        if block_to_block_type(block) == "paragraph":
            children.append(paragraph_block_to_html(block))
    return HTMLNode("div", children=children)

def paragraph_block_to_html(block):
        lines = block.split("\n")
        joined_parts = []
        for line in lines:
            stripped = line.strip()
            if stripped != "":
                joined_parts.append(stripped)
        joined = " ".join(joined_parts)
        children = text_to_children(joined)
        return HTMLNode("p", children=children)

def Olist_block_to_html(block):
    child_nodes = []
    lines = block.split("\n")
    for line in lines:
        dot_index = line.find(".")
        stripped = line[dot_index + 1:].lstrip()
        child_nodes.append(HTMLNode("li", children=text_to_children(stripped)))
        return HTMLNode("ol", children=child_nodes)

def Ulist_block_to_html(block):
    child_nodes = []
    lines = block.split("\n")
    for line in lines:
        if line.startswith("- ") or line.startswith("* "):
            stripped = line[2:].lstrip()
            child_nodes.append(HTMLNode("li", children=text_to_children(stripped)))
    return HTMLNode("ul", children=child_nodes)
        
def quote_block_to_html(block):
    formatted = []
    lines = block.split("\n")
    for line in lines:
        formatted.append(line[1:].lstrip())
    text = " ".join(formatted)
    children = text_to_children(text)
    node = HTMLNode("blockquote", children=children)
    return node

def code_block_to_html(block):
    lines = block.split("\n")
    inner_lines = lines[1:-1]
    code_text = "\n".join(inner_lines) + "\n"
    code_leaf = TextNode(code_text, "code")
    code_child = text_node_to_html_node(code_leaf) 
    pre_node = HTMLNode("pre", children=[code_child])
    return pre_node

def heading_block_to_html(block):
    level = 0
    lines = block.split("\n")
    first_line = lines[0]
    for ch in first_line:
        if ch == "#":
            level += 1
        else:
            break
    prepped = first_line.lstrip("#").strip()
    tag = "h" + str(level)
    child = text_to_children(prepped)
    return HTMLNode(tag,children=child)
        
def text_to_children(text):
    children = []
    text_nodes = text_to_textnodes(text)
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    return children

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    raise Exception("h1 header not found")