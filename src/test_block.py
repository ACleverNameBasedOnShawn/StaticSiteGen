import unittest

from block import (
    block_to_block_type,
    markdown_to_blocks,
    paragraph_type_ordered_list,
    paragraph_type_paragraph,
    paragraph_type_unorderedlist,
    paragraph_type_quote,
    paragraph_type_code,
    paragraph_type_heading,
)
class TestExtractMarkdown(unittest.TestCase):
    def test_block_to_inline(self):
        markdown = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
""" 
        self.assertEqual(markdown_to_blocks(markdown), [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ]
                         )

    def test_block_to_inline_blankspace(self):
        markdown = f"\n\n\n   \n"
        self.assertEqual(markdown_to_blocks(markdown), [])
        
    def test_block_to_block_type_header(self):
        blocks = [
            "# Main Header",
            "## Sub Header 1",
            "### Sub Header 2",
            "#### Sub Header 3",
            "##### Sub Header 4",
            "###### Sub Header 5",
        ]
        for block in blocks:
            self.assertEqual(paragraph_type_heading, block_to_block_type(block))

    def test_block_to_block_type(self):
        block = "```This is a code snippet:\nprint('hello world')```"
        self.assertEqual(paragraph_type_code, block_to_block_type(block))

    def test_block_to_block_type_quote(self):
        block = ">sleepy\n>can't sleep\n>what do?"
        self.assertEqual(paragraph_type_quote, block_to_block_type(block))

    def test_block_to_block_type_unorderedlist(self):
        block = "* this is a list\n* an unordered list\n- it is absolute chaos"
        self.assertEqual(paragraph_type_unorderedlist, block_to_block_type(block))

    def test_block_to_block_type_orderedlist(self):
        block = "1. Make a list\n2. Look at the list\n3. Realize the list was pointless\n4. Start over"
        self.assertEqual(paragraph_type_ordered_list, block_to_block_type(block))
if __name__ == "__main__":
    unittest.main()
