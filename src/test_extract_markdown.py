import unittest

from markdown import extract_markdown_links, extract_markdown_images, split_nodes_link, split_nodes_image
from textnode import (
    TextNode,
    text_type_text,
    text_type_image,
    text_type_link
)
    
class TestExtractMarkdown(unittest.TestCase):
    def test_extract_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        self.assertEqual(extract_markdown_images(text), [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")])
        
    def test_extract_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        self.assertEqual(extract_markdown_links(text), [("link", "https://www.example.com"), ("another", "https://www.example.com/another")])

    def test_split_images(self):
        node = TextNode(
    "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
    text_type_text,
)
        self.assertEqual(split_nodes_image([node]), [
    TextNode("This is text with an ", text_type_text),
    TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
    TextNode(" and another ", text_type_text),
    TextNode(
        "second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
    ),
]
                         )
        
    def test_split_link(self):
        node = TextNode(
            "This is text with a [link](https://google.com) and another [second link](https://bing.com)",
    text_type_text,
)
        self.assertEqual(split_nodes_link([node]), [
    TextNode("This is text with a ", text_type_text),
    TextNode("link", text_type_link, "https://google.com"),
    TextNode(" and another ", text_type_text),
    TextNode("second link", text_type_link, "https://bing.com"
    ),
]
                         )
        
if __name__ == "__main__":
    unittest.main()

