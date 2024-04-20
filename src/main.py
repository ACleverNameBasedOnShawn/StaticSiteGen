import os
import shutil

from copydir import copy_files_recursive
from block import markdown_to_html_node
dir_path_static = "./static"
dir_path_public = "./public"

def main():
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("copying files...")
    copy_files_recursive(dir_path_public, dir_path_public)

def extract_title(markdown):
    for block in markdown.split("\n"):
        if block.startswith("# "):
            return block.split("#")[1].strip()
        else:
            raise Exception("markdown file has no header")
            
def generate_page(from_path, template_path, dest_path):
    print(f"Generating path from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path) as f:
        source_contents = f.read()
    f.close()
    
    with open(template_path) as f:
        template_copy = f.read()
    f.close()

    title = extract_title(source_contents)
    nodes = markdown_to_html_node(source_contents)
    html = nodes.to_html()
    template_copy = template_copy.replace("{{ Title }}", f"{title}")
    template_copy = template_copy.replace("{{ Content }}", f"{html}")
    

    f = open(dest_path, mode = 'a')
    f.write(template_copy)
    f.close()

generate_page("content/index.md", "template.html", "private/index.html")

main()
