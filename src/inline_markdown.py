from textnode import TextType, TextNode

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
                
