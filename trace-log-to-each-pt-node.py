import os
import sys

# Input data
data = sys.stdin.read()

# Split the input data by the separator lines
sections = data.split('##########################################################################################')

# Create output directory if it doesn't exist
output_dir = 'parser_trees'
os.makedirs(output_dir, exist_ok=True)
os.makedirs(output_dir + '/svg', exist_ok=True)

# Write each section to a separate file
for i, section in enumerate(sections[1:]):
    file_name = os.path.join(output_dir, f'parser_tree_{i + 1}.txt')
    with open(file_name, 'w') as file:
        file.write(section.strip() + '\n')

print(f'Successfully extracted {len(sections)} sections into the {output_dir} directory.')

