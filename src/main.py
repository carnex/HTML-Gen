
import os
import shutil
from textnode import TextType, TextNode
from htmlnode import HTMLNode, ParentNode, LeafNode
from markdown_blocks import markdown_to_blocks, BlockType, block_to_block_type, markdown_to_html_node, paragraph_block_to_html, Olist_block_to_html, Ulist_block_to_html, quote_block_to_html, code_block_to_html, heading_block_to_html, text_to_children, extract_title


def main():
    file_prep("public")
    file_copy("static", "public")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as f:
        template = f.read()
    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    page = template.replace("{{ Title }}", title)
    page = template.replace("{{ Content }}", content)
    dirpath = os.path.dirname(dest_path)
    if dirpath != "":
        os.makedirs(dirpath, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(page)

def file_prep(dest_path):
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)
    os.mkdir(dest_path)

def file_copy(source_path, dest_path):
    if os.path.exists(source_path) and os.path.exists(dest_path):
        for name in os.listdir(source_path):
            src_item = os.path.join(source_path, name)
            dst_item = os.path.join(dest_path, name)
            if os.path.isfile(src_item):
                shutil.copy(src_item, dst_item)
            else:
                os.mkdir(dst_item)
                file_copy(src_item,dst_item)
    else:
        raise Exception("one or more directorys missing.")
    

main()

    