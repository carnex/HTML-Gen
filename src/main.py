
import os
import shutil
from textnode import TextType, TextNode
from htmlnode import HTMLNode, ParentNode, LeafNode
from markdown_blocks import markdown_to_blocks, BlockType, block_to_block_type, markdown_to_html_node, paragraph_block_to_html, Olist_block_to_html, Ulist_block_to_html, quote_block_to_html, code_block_to_html, heading_block_to_html, text_to_children, extract_title


def main():
    file_prep("public")
    file_copy("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")
    dir_list = get_directory_list("content", "public")
    for src, dst in dir_list:
        generate_page(src, "template.html", dst)


def get_directory_list(src_dir, dst_dir):
    src_path = []
    for name in os.listdir(src_dir):
        src = os.path.join(src_dir, name)
        dst = os.path.join(dst_dir, name)
        if os.path.isfile(src):
            if src.endswith(".md"):
                new_dst = dst[:-3] + ".html"
                src_path.append((src,new_dst))
        if os.path.isdir(src):
            src_path.extend(get_directory_list(src, dst)) 
    return src_path



def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as f:
        template = f.read()
    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    page = template.replace("{{ Title }}", title)
    page = page.replace("{{ Content }}", content)
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
    if not os.path.exists(source_path):
        raise Exception(F"{source_path} does not exist")
    if not os.path.exists(dest_path):
        os.makedirs(dest_path, exist_ok=True)
    for name in os.listdir(source_path):
        src_item = os.path.join(source_path, name)
        dst_item = os.path.join(dest_path, name)
        if os.path.isfile(src_item):
            shutil.copy(src_item, dst_item)
        else:
            file_copy(src_item,dst_item)

    

main()

    