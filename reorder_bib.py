#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""重新排列.bib文件，使参考文献按引用顺序编号"""

import re

# 读取引用顺序
with open('citation_order.txt', 'r', encoding='utf-8') as f:
    citation_order = [line.strip() for line in f if line.strip()]

print(f"Found {len(citation_order)} citations in order")

# 读取原始.bib文件
with open('reference/mybib.bib', 'r', encoding='utf-8') as f:
    bib_content = f.read()

# 解析所有条目
entry_pattern = r'(@\w+\{[^@]+)'
entries = re.findall(entry_pattern, bib_content, re.DOTALL)

print(f"Found {len(entries)} entries in bib file")

# 构建key到条目的映射
entry_dict = {}
for entry in entries:
    # 提取citation key
    key_match = re.match(r'@\w+\{([^,\s]+)', entry)
    if key_match:
        key = key_match.group(1)
        entry_dict[key] = entry

# 按引用顺序重新排列
ordered_entries = []
for key in citation_order:
    if key in entry_dict:
        ordered_entries.append(entry_dict[key])
        del entry_dict[key]
    else:
        print(f"Warning: Citation key '{key}' not found in bib file")

# 添加未被引用的条目
for key, entry in entry_dict.items():
    ordered_entries.append(entry)

# 写入新文件
with open('reference/mybib_reordered.bib', 'w', encoding='utf-8') as f:
    f.write('\n\n'.join(ordered_entries))

print(f"Reordered bib file saved to reference/mybib_reordered.bib")
print(f"Ordered entries: {len(ordered_entries)}")
