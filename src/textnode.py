from enum import Enum

class TextType(Enum):
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


