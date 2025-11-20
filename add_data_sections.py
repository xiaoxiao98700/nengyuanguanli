# -*- coding: utf-8 -*-
"""
为每个功能模块的业务规则后面添加：
1. 数据处理逻辑说明
2. 数据限制要求
3. 数据来源说明
"""

# 读取文件
with open('智慧能源管理系统需求规格说明书.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 用于存储需要插入的内容的字典
# 格式：模块编号 -> [处理逻辑, 限制要求, 数据来源]
sections_to_add = {}

# 由于模块太多，我们先手动为每个模块准备内容
# 这里先定义几个示例模块的内容

result = []
i = 0
skip_count = 0

while i < len(lines):
    line = lines[i]
    result.append(line)
    
    # 检查是否是业务规则结尾（包含"（6）"或其他编号的结尾，且下一行是空行或新章节）
    if line.strip().startswith('（') and (')' in line or '）' in line):
        # 检查下一行是否是空行或新章节标题
        if i + 1 < len(lines):
            next_line = lines[i + 1].strip()
            # 如果下一行是空行，再检查下下行是否是新的章节或模块
            if next_line == '':
                if i + 2 < len(lines):
                    next_next_line = lines[i + 2].strip()
                    # 如果是新章节标题，需要插入三个新部分
                    if next_next_line.startswith('####') or next_next_line.startswith('###') or next_next_line.startswith('##'):
                        # 找到当前模块编号
                        # 向上查找章节编号
                        j = i
                        module_num = None
                        while j >= 0:
                            if lines[j].strip().startswith('####') and '业务规则' in lines[j]:
                                # 提取模块编号，如 "5.2.2.4"
                                parts = lines[j].strip().split()
                                if len(parts) > 0:
                                    module_num = parts[0]
                                break
                            j -= 1
                        
                        # 如果找到模块编号，添加三个新部分
                        if module_num:
                            # 确定下一个章节的编号
                            base_num = module_num.rsplit('.', 1)[0]  # 如 "5.2.2"
                            next_num = str(int(module_num.split('.')[-1]) + 1)  # 下一个编号
                            
                            # 插入三个新部分
                            result.append('\n')
                            result.append(f'##### {base_num}.{next_num} 数据处理逻辑说明\n')
                            result.append('（1）数据处理逻辑待补充\n')
                            result.append('（2）数据处理逻辑待补充\n')
                            result.append('（3）数据处理逻辑待补充\n')
                            result.append('\n')
                            result.append(f'##### {base_num}.{str(int(next_num)+1)} 数据限制要求\n')
                            result.append('（1）数据限制要求待补充\n')
                            result.append('（2）数据限制要求待补充\n')
                            result.append('\n')
                            result.append(f'##### {base_num}.{str(int(next_num)+2)} 数据来源说明\n')
                            result.append('（1）数据来源说明待补充\n')
                            result.append('（2）数据来源说明待补充\n')
                            skip_count += 3
    
    i += 1

# 由于这种方式可能不够精确，我们改为手动添加每个模块
# 先写回文件
with open('智慧能源管理系统需求规格说明书.md', 'w', encoding='utf-8') as f:
    f.writelines(result)

print(f'处理完成，跳过了 {skip_count} 个插入点')

