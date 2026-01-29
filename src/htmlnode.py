class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("Child classes will override this method to render themselves as HTML")
    
    def props_to_html(self):
        output = ""
        if self.props == None or len(self.props) == 0:
            return ""
        for prop in self.props:
            value = self.props[prop]
            output = output + f' {prop}="{value}"'
        return output

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

    def __eq__(self, other):
        if self.tag != other.tag:
            return False
        if self.value != other.value:
            return False
        if self.children != other.children:
            return False
        if self.props != other.props:
            return False
        return True

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>" 

    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        output =""
        if not self.tag:
            raise ValueError("Object does not have tag")
        if self.children is None:
            raise ValueError("Child node has no value")
        for child in self.children:
             output = output + child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{output}</{self.tag}>" 
 