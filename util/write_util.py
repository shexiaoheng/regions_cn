import json


# 省/直辖市数据
def write_province(content):
    write_json(content, '../json_data/province.json')


# 地级市/市辖区数据
def write_city(content):
    write_json(content, '../json_data/city.json')


# 区/县数据
def write_county(content):
    write_json(content, '../json_data/county.json')


# 镇/街道数据
def write_town(content):
    write_json(content, '../json_data/town.json')


def write_json(content, filepath):
    # ensure_ascii=False 保留中文    indent=4 缩进为4个空格
    data = json.dumps(content, ensure_ascii=False, indent=4)
    file = open(filepath, 'w', encoding='utf-8')
    file.write(data)
    file.close()
