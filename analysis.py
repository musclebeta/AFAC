import json
import matplotlib.pyplot as plt


def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def analyze_json(data):
    data_list = {}
    for item in data:
        if item['产品名'] not in data_list:
            data_list[item['产品名']] = 1
        else:
            data_list[item['产品名']] += 1

    data_list = dict(sorted(data_list.items(), key=lambda x: x[1], reverse=True))
    return data_list

def plot_bar(data_list):
    plt.bar(range(len(data_list)), list(data_list.values()), align='center')
    plt.xticks(range(len(data_list)), list(data_list.keys()))
    plt.show()


def save_json(data_list, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    file_paths = ['round1_training_data/train.json', 'round1_training_data/dev.json', 'round1_training_data/test.json']
    for i in range(len(file_paths)):
        file_path = file_paths[i]
        data = read_json(file_path)
        data_list = analyze_json(data)
        save_json(data_list, f'{file_path[:-5]}_data_analysis.json')

