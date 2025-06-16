class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        result = ""
        for key in self.props:
            result = result + f"{key}={self.props[key]} "
        return result[:-1]

    def __repr__(self):
        return f"Tag: {self.tag} Value: {self.value} Children: {self.children} Props: {self.props}"


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None):
        super().__init__(tag=tag, value=value, children=None, props=None)

    def to_html(self):
        if self.value == None:
            raise ValueError("value is none")

        if self.tag == None:
            return self.value

        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        print("CHILDRENNN!", self.children)
        if self.tag is None:
            raise ValueError("error, no tag")
        if self.children is None:
            raise ValueError("error, no children")
        child_value = ''.join(child.to_html() for child in self.children)
        print("Child value: ", child_value)
        attrs = ''
        if self.props:
            attrs = ' ' + ' '.join(f'{key}="{value}"' for key, value in self.props.items())

        return f"<{self.tag}{attrs}>{child_value}</{self.tag}>"

