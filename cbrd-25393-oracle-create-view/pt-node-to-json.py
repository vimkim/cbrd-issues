import json
import sys
import re


def parse_node(lines):


    def get_indent_level(line):
        return len(re.match(r"^-*", line).group(0)) // 4

    def get_node_info(line):
        parts = line.strip().split()
        return parts[0], parts[-1]

    def get_name_info(line):
        parts = line.strip().split("[")
        name = parts[1].split("]")[0].strip()
        address = parts[-1].split()[-1]
        return name, address

    root = {}
    current_node = root
    node_stack = [(current_node, -1)]  # Stack to maintain (node, indent level)


    isStackTrace = 'vimkim' in lines[0]


    for line in lines:
        if isStackTrace and '----------------------------------' in line:
            isStackTrace = False
            continue

        if isStackTrace:
            continue

        if line.strip() == "":
            continue

        if "At" in line:
            continue

        indent_level = get_indent_level(line)
        node_type, address = get_node_info(line.strip('- '))

        new_node = {node_type: {"address": address}}
        if "PT_NAME" in line:
            name, name_address = get_name_info(line)
            new_node[node_type]["name"] = name
            new_node[node_type]["name_address"] = name_address

        while node_stack and node_stack[-1][1] >= indent_level:
            node_stack.pop()

        parent_node = node_stack[-1][0]
        parent_node.setdefault("children", []).append(new_node)

        node_stack.append((new_node[node_type], indent_level))

    return root

def main():
    input_lines = sys.stdin.read().strip().split("\n")
    parsed_output = parse_node(input_lines)
    print(json.dumps(parsed_output, indent=4))

if __name__ == "__main__":
    main()

