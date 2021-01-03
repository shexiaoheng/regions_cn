from util.write_util import write_json


class TestWriteUtil:
    # 测试把字典转为json格式并写入文件保存
    def test_write_util(self):
        test_content = [{'name': '佘小恒', 'sex': '男'}, {'name': 'shexiaoheng', 'sex': 'man'}]
        write_json(test_content, '../json_data/test.json')
