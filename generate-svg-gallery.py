import os
import re
import argparse
from jinja2 import Environment, FileSystemLoader


def natural_sort_key(s):
    """Sort key for natural sorting of filenames."""
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]


def main():
    # Setup argparse to read command-line arguments
    parser = argparse.ArgumentParser(description="Generate an HTML gallery for SVG files in a specified directory.")
    parser.add_argument('-d', '--directory', type=str, required=True, help='The directory containing SVG files.')
    parser.add_argument('-t', '--template', type=str, required=True, help='The location of the template HTML file.')
    args = parser.parse_args()

    # Directory containing SVG files
    svg_directory = os.path.abspath(args.directory)
    print(f"SVG directory: {svg_directory}")

    # Verify the SVG directory exists
    if not os.path.isdir(svg_directory):
        print(f"The directory {svg_directory} does not exist.")
        return

    # Verify the template file exists
    template_path = os.path.abspath(args.template)
    if not os.path.isfile(template_path):
        print(f"The template file {template_path} does not exist.")
        return

    # List all SVG files in the directory and sort them naturally
    svg_files = sorted([f for f in os.listdir(svg_directory) if f.endswith('.svg')], key=natural_sort_key)
    print(f"SVG files found: {svg_files}")

    # Set up the Jinja2 environment
    template_dir = os.path.dirname(template_path)
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(os.path.basename(template_path))

    # Calculate relative paths for SVG files
    relative_svg_directory = os.path.relpath(svg_directory, os.getcwd())
    print(f"Relative SVG directory: {relative_svg_directory}")

    # Render the template with the list of SVG files
    html_content = template.render(svg_files=svg_files, svg_directory=relative_svg_directory)
    print(f"Generated HTML content: {html_content[:500]}...")  # Print first 500 chars for debugging

    # Write the HTML content to a file
    output_path = os.path.join(os.getcwd(), 'index.html')
    with open(output_path, 'w') as f:
        f.write(html_content)

    print(f"HTML file 'index.html' has been created at {output_path}")

if __name__ == "__main__":
    main()

