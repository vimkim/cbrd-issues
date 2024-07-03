python trace-log-to-each-pt-node.py < trace_log.txt
find parser_trees/* -type f -name '*.txt' | parallel 'python pt-node-to-json.py < {} | python json-to-dot.py | python dot-to-svg.py --output parser_trees/svg/{/.}.svg'
python generate-svg-gallery.py -d parser_trees/svg
