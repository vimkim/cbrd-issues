import os
import argparse

def main():
    # Setup argparse to read command-line arguments
    parser = argparse.ArgumentParser(description="Generate an HTML gallery for SVG files in a specified directory.")
    parser.add_argument('-d', '--directory', type=str, required=True, help='The directory containing SVG files.')
    args = parser.parse_args()

    # Directory containing SVG files
    svg_directory = args.directory

    # List all SVG files in the directory and sort them alphabetically
    svg_files = sorted([f for f in os.listdir(svg_directory) if f.endswith('.svg')])

    # HTML template
    html_template = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SVG Gallery</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
            }}
            .svg-container {{
                display: flex;
                flex-direction: column;
                align-items: center;
            }}
            .svg-item {{
                margin: 20px;
                border: 1px solid #ccc;
                padding: 10px;
                width: 80%;
            }}
            .svg-item img {{
                max-width: 100%;
                height: auto;
            }}
            .svg-title {{
                text-align: center;
                font-weight: bold;
                margin: 10px 0;
            }}
        </style>
    </head>
    <body>
        <h1>SVG Gallery</h1>
        <div class="svg-container">
            {}
        </div>
    </body>
    </html>
    '''

    # Generate the HTML content for SVG images with titles
    svg_items = '\n'.join([f'''
    <div class="svg-item">
        <div class="svg-title">{file}</div>
        <img src="{svg_directory}/{file}" alt="{file}">
    </div>
    ''' for file in svg_files])

    # Write the HTML content to a file
    with open('index.html', 'w') as f:
        f.write(html_template.format(svg_items))

    print("HTML file 'index.html' has been created.")

if __name__ == "__main__":
    main()

