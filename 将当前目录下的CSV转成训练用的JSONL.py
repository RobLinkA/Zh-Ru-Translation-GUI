import pandas as pd
import json
import glob

# 步骤1: 查找当前目录下的所有.csv文件
csv_files = glob.glob('*.csv')

# 预定义的系统消息内容
system_content = "严复是一名资深翻译家，将汉语的政治文献翻译成俄语。"

for file in csv_files:
    # 步骤2: 读取CSV文件内容
    df = pd.read_csv(file, header=None)
    
    # 准备一个列表来存储所有转换后的数据
    data_to_save = []
    
    for index, row in df.iterrows():
        # 步骤3: 转换格式
        entry = {
            "messages": [
                {"role": "system", "content": system_content},
                {"role": "user", "content": f"将以下文本翻译成俄语：{row[0]}"},
                {"role": "assistant", "content": row[1]}
            ]
        }
        
        data_to_save.append(entry)
    
    # 将数据保存为.jsonl文件
    jsonl_file_name = file.replace('.csv', '.jsonl')
    with open(jsonl_file_name, 'w', encoding='utf-8') as jsonl_file:
        for item in data_to_save:
            jsonl_file.write(json.dumps(item, ensure_ascii=False) + '\n')

print("所有CSV文件已成功转换为JSONL格式。")
