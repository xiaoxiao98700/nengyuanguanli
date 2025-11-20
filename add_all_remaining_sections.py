# -*- coding: utf-8 -*-
"""
为所有剩余的模块添加：
1. 数据处理逻辑说明 (X.5)
2. 数据限制要求 (X.6)
3. 数据来源说明 (X.7)
"""

import re

# 需要补充的模块列表
modules_to_add = [
    ("5.5.1.4", "5.5.1"),
    ("5.5.2.4", "5.5.2"),
    ("5.5.3.4", "5.5.3"),
    ("5.5.4.4", "5.5.4"),
    ("5.5.5.4", "5.5.5"),
    ("5.5.6.4", "5.5.6"),
    ("5.5.7.4", "5.5.7"),
    ("5.5.8.4", "5.5.8"),
    ("5.5.9.4", "5.5.9"),
    ("5.5.10.4", "5.5.10"),
    ("5.6.1.4", "5.6.1"),
    ("5.6.2.4", "5.6.2"),
    ("5.6.3.4", "5.6.3"),
    ("5.7.1.4", "5.7.1"),
    ("5.7.2.4", "5.7.2"),
    ("5.7.3.4", "5.7.3"),
    ("5.7.4.4", "5.7.4"),
    ("5.8.1.4", "5.8.1"),
    ("5.8.2.4", "5.8.2"),
    ("5.8.3.4", "5.8.3"),
    ("5.8.4.4", "5.8.4"),
]

# 读取文件
with open('智慧能源管理系统需求规格说明书.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 每个模块添加的内容模板
template = """
##### {module}.5 数据处理逻辑说明
（1）**数据处理逻辑待补充**：根据模块业务特点补充数据处理逻辑说明
（2）**数据处理逻辑待补充**：根据模块业务特点补充数据处理逻辑说明
（3）**数据处理逻辑待补充**：根据模块业务特点补充数据处理逻辑说明

##### {module}.6 数据限制要求
（1）**数据限制要求待补充**：根据模块业务特点补充数据限制要求
（2）**数据限制要求待补充**：根据模块业务特点补充数据限制要求

##### {module}.7 数据来源说明
（1）**数据来源说明待补充**：根据模块业务特点补充数据来源说明
（2）**数据来源说明待补充**：根据模块业务特点补充数据来源说明
"""

# 查找所有业务规则的位置并添加内容
for rule_section, module_base in modules_to_add:
    # 查找业务规则部分
    pattern = rf'({re.escape(rule_section)} 业务规则.*?)(\n####|\n###|\n##)'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        # 提取业务规则内容和下一章节的开始
        rule_content = match.group(1)
        next_section = match.group(2)
        
        # 检查是否已经添加了这三个部分
        if f"{module_base}.5 数据处理逻辑说明" not in content:
            # 生成要添加的内容
            new_content = template.format(module=module_base)
            
            # 在业务规则后、下一章节前插入新内容
            content = content.replace(
                rule_content + next_section,
                rule_content + new_content + "\n" + next_section
            )
            print(f"已为 {rule_section} 添加三个部分")
        else:
            print(f"{rule_section} 已存在，跳过")
    else:
        print(f"未找到 {rule_section}")

# 写回文件
with open('智慧能源管理系统需求规格说明书.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("批量添加完成！")

