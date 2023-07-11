#!/usr/bin/python3
import sys
import os.path
import markdown
"""
A script that takes an argument 2 strings:

    First argument is the name of the Markdown file
    Second argument is the output file name

"""

def convert_markdown_to_html(markdown_file, output_file):
    if not os.path.isfile(markdown_file):
        sys.stderr.write(f"Missing {markdown_file}\n")
        sys.exit(1)

    with open(markdown_file, 'r') as f:
        markdown_content = f.read()

    html_content = markdown.markdown(markdown_content)

    with open(output_file, 'w') as f:
        f.write(html_content)


if __name__ == "__main__":

    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py <markdown_file> <output_file>\n")
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(markdown_file, output_file)

    sys.exit(0)
