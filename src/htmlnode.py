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

