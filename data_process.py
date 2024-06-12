import json


def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data
 
def data_convert(data):
    data_processed = []
    for item in data:
        # 创建一个全新的template字典副本
        template = {
            "type": "chatml",
            "messages": [
                {
                    "role": "system",
                    "content": "你是一个非常棒的保险从业者，你要尽可能的使用我给你的保险条款以及你的知识和经验，来回答我的问题。"
                },
                {
                    "role": "user",
                    "content": ""
                },
                {
                    "role": "assistant",
                    "content": ""
                }
            ],
            "source": "unknown"
        }
        template["messages"][1]["content"] = (item.get("产品名", "") + 
                                               item.get("条款", "") + 
                                               item.get("问题", ""))
        template["messages"][2]["content"] = item.get("答案", "")
        data_processed.append(template)
    return data_processed

if __name__ == '__main__':
    file_paths = ['round1_training_data/train.json', 'round1_training_data/dev.json']
    for file_path in file_paths:
        data = read_json(file_path)
        new_data = data_convert(data)
        with open(f'{file_path[:-5]}_processed.jsonl', 'w', encoding='utf-8') as f:
            for item in new_data:
                f.write(json.dumps(item, ensure_ascii=False) + '\n')
