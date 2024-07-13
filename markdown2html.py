#!/usr/bin/env python3

import sys
import os
import markdown

def main():
    # Check if the number of arguments is less than 2
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Check if the input Markdown file exists
    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)
    
    # Read the Markdown file
    with open(input_file, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()
    
    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content)
    
    # Write the HTML content to the output file
    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)
    
    # Exit with code 0
    sys.exit(0)

if __name__ == "__main__":
    main()
