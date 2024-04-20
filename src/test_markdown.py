import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_code,
    text_type_italic,
    text_type_link,
    text_type_image
)

from markdown import split_nodes_delimiter, text_to_textnodes
    
class TestMarkdown(unittest.TestCase):
    def test_type_bold(self):
        node = TextNode("This is text with a *bold* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_bold)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" word", text_type_text),
        ])

    def test_type_italic(self):
        node = TextNode("This is text with a **italicized** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_italic)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", text_type_text),
            TextNode("italicized", text_type_italic),
            TextNode(" word", text_type_text),
        ])

    def test_type_code(self):
        node = TextNode("This is text with a **code** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_code)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", text_type_text),
            TextNode("code", text_type_code),
            TextNode(" word", text_type_text),
        ])

    def test_type_double_bold(self):
        node = TextNode("This is *text* with a *bold* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_bold)
        self.assertEqual(new_nodes, [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with a ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" word", text_type_text),
        ])

    def test_text_to_textnode2(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        self.assertEqual(text_to_textnodes(text), [
    TextNode("This is ", text_type_text),
    TextNode("text", text_type_bold),
    TextNode(" with an ", text_type_text),
    TextNode("italic", text_type_italic),
    TextNode(" word and a ", text_type_text),
    TextNode("code block", text_type_code),
    TextNode(" and an ", text_type_text),
    TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
    TextNode(" and a ", text_type_text),
    TextNode("link", text_type_link, "https://boot.dev"),
] 
                         )
if __name__ == "__main__":
    unittest.main()

