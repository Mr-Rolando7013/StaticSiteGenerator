from textnode import TextNode

def main():
    test = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    print(test.__repr__())


main()
