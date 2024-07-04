import sys
import argparse
from graphviz import Source

def main():
    parser = argparse.ArgumentParser(description="Render a Graphviz DOT file to SVG.")
    parser.add_argument('--output', type=str, required=True, help='The output SVG file name.')
    args = parser.parse_args()
    
    dot_data = sys.stdin.read().strip()

    dot_graph = Source(dot_data)

    output_filename = args.output
    if output_filename.endswith('.svg'):
        output_filename = output_filename[:-4]

    dot_graph.format = 'svg'
    dot_graph.render(output_filename, format='svg', cleanup=True)
    print(f"SVG file '{output_filename}' has been created.")

if __name__ == "__main__":

    main()

