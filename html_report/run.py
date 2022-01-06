from jinja2 import Template

with open('base.html', 'r') as f:
    lines = f.read()
    TPL = lines

render_dict = {}
dict_table_data = [{'Name': 'Basketball', 'Type': 'Sports', 'Value': 5},
                   {'Name': 'Football', 'Type': 'Sports', 'Value': 4.5},
                   {'Name': 'Pencil', 'Type': 'Learning', 'Value': 5},
                   {'Name': 'Hat', 'Type': 'Wearing', 'Value': 2}]
test_content = [["项目名称", "状态", "运行时间", "最后执行时间"],
                ["F", "pass", "10s", "2022-01-06"],
                ["G", "fail", "12s", "2022-01-06"],
                ["H", "pass", "10s", "2022-01-06"], ]
render_dict.update({'Content': 'Hello reader, here is a table:',
                    'array_table_head': ['Name', 'Type', 'Value'],
                    'dict_table_data': dict_table_data,
                    'css_address': 'static/css/bootstrap.min.css',
                    'js_address': 'static/js/bootstrap.min.js',
                    'test_content': test_content})

content = Template(TPL).render(render_dict)
with open('out.html', "w", encoding='utf-8') as f:
    f.write(content)  # 写入文件
