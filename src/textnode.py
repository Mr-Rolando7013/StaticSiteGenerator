from enum import Enum
from htmlnode import HTMLNode, LeafNode

class TextType(Enum):
    TEXT = '"'
    BOLD = "**"
    ITALIC = "_"
    CODE = "`"
    LINK = "[anchor text](url)"
    IMAGES = "![alt text](url)"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, otherObject):
        if self.text == otherObject.text and self.text_type == otherObject.text_type and self.url == otherObject.url:
            return True
        if self.text != otherObject.text and self.text_type == otherObject.text_type:
            print(f"Text is different!")
            return False
        if self.text == otherObject.text and self.text_type != otherObject.text_type:
            print(f"Text type is different")
            return False
        if self.url != otherObject.url:
            return False
        else:
            return False
        #if self.text == otherObject.text and self.text_type == otherObject.text_type and self.url == otherObject.url:
            #return True
        #else:
            #return  False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    match(text_node.text_type):
        case(text_node.text_type.TEXT):
            print("text: ", text_node.text)
            return LeafNode(text_node.text)
        case(text_node.text_type.BOLD):
            print("bold", text_node.text)
            return LeafNode(text_node.text, "b")
        case(text_node.text_type.ITALIC):
            print("italic", text_node.text)
            return LeafNode(text_node.text, "i")
        case(text_node.text_type.CODE):
            return LeafNode(text_node.text, "code")
        case(text_node.text_type.LINK):
            return HTMLNode("a", text_node.text, None, {"href": text_node.url})
        case(text_node.text_type.IMAGES):
            print("image", text_node.text)
            return HTMLNode("img", None, None, {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception
