import re

from textnode import (
    text_node_to_html_node,
    TextNode,
    text_type_text,
    text_type_image,
    text_type_link,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

from htmlnode import (
    ParentNode,
)
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        split_sections = old_node.text.split(delimiter)
        if len(split_sections) % 2 == 0:
            raise ValueError("Invalid section; not correctly encapsulated")
        for i in range(len(split_sections)):
            if split_sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(split_sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(split_sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        copy_text = old_node.text
        images = extract_markdown_images(copy_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            split_sections = copy_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(split_sections) != 2:
                raise ValueError("Invalid section; not correctly encapsulated")
            if split_sections[0] != "":
                new_nodes.append(TextNode(split_sections[0], text_type_text))
            new_nodes.append(
                TextNode(
                    image[0],
                    text_type_image,
                    image[1],
                )
            )
            copy_text = split_sections[1]
        if copy_text != "":
            new_nodes.append(TextNode(copy_text, text_type_text))
    return new_nodes
            
def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        copy_text = old_node.text
        links = extract_markdown_links(copy_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            split_sections = copy_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(split_sections) != 2:
                raise ValueError("Invalid section; not correctly encapsulated")
            if split_sections[0] != "":
                new_nodes.append(TextNode(split_sections[0], text_type_text))
            new_nodes.append(
                TextNode(
                    link[0],
                    text_type_link,
                    link[1],
                )
            )
            copy_text = split_sections[1]
        if copy_text != "":
            new_nodes.append(TextNode(copy_text, text_type_text))
    return new_nodes

def text_to_textnodes(text):
    node_list = []
    node = TextNode(text, text_type_text)
    node_list.append(node)
    node_list = split_nodes_delimiter(node_list, "**", text_type_bold)
    node_list = split_nodes_delimiter(node_list, "*", text_type_italic)
    node_list = split_nodes_delimiter(node_list, "`", text_type_code)
    node_list = split_nodes_image(node_list)
    node_list = split_nodes_link(node_list)
    return node_list
