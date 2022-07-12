#!/usr/bin/env python
import re

TODO_file = "C:\\SGZ_Pro\\Hobbys\\Writing\\Org\\todo.org"

with open(TODO_file) as f:
    text = f.read()

find = re.findall("\*.+?TODO",text)
print(len(find))
