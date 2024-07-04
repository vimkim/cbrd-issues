import json
import sys
from graphviz import Digraph

def parse_node(node, dot, parent_id=None):
    for child in node.get('children', []):
        for key, value in child.items():
            node_id = f"{key}_{value['address']}"
            label = key
            if 'name' in value:
                label += f" [ {value['name']} ]"
            
            dot.node(node_id, label)
            
            if parent_id:
                dot.edge(parent_id, node_id)
            
            parse_node(value, dot, node_id)

def main():
    input_data = sys.stdin.read().strip()
    json_data = json.loads(input_data)
    
    dot = Digraph()
    dot.attr()

    parse_node(json_data, dot)
    
    print(dot.source)

if __name__ == "__main__":
    main()

