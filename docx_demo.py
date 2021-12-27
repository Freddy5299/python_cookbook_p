import docx2txt
import os
from docx import Document
from collections import namedtuple

'''
获取所有的style paragraph
确定一级标题，二级标题，三级标题的格式， file的格式，可能需要字体
    paragraphs.style.font
    paragraphs.style.name
    在遇到正文之前所有内容都是可以丢掉的
    文本数据格式：
    file_content_list = [{head1:['xxx',{head2:{}},text,head]]
    文本的前缀和后缀数据格式:
    file_style = namedtuple('file_style', ['start_switch', 'end_switch'])
    file_style_list = {head1:file_style('### ','\n')}
    如何遍历文本内容
    已写好
    标题数字取名
    title_number = [1,2,3],只是临时变量没必要定义三个参数
    
如何确定代码块
页眉页脚可以去掉吗
table处理
图像处理

'''


# extract text and write images in /tmp/img_dir
def get_image(_image_path=r"E:\program\python\tools\docx_parse\image"):
    if os.path.exists(_image_path):
        for _fname in os.listdir(_image_path):
            os.remove(os.path.join(_image_path, _fname))
        os.rmdir(_image_path)
        os.mkdir(_image_path)
    docx2txt.process("1_test.docx", _image_path)
    id = 0
    for _fname in os.listdir(_image_path):
        _, extension = os.path.splitext(_fname)
        if extension in [".jpg", ".jpeg", ".png", ".bmp"]:
            id += 1
    return id


def read_docx_file(_file_path='3_test.docx'):
    path = '3_test.docx'  # 文件路径
    wordfile = Document(path)  # 读入文件
    paragraphs = wordfile.paragraphs
    return paragraphs


def open_file_look_style(paragraphs):
    # for paragraph in paragraphs:
    #     with open('1.txt', 'at', encoding='utf-8') as f:
    #         print(paragraph.style.name, file=f)
    #         print(paragraph.style.font.name, file=f)
    #         print(paragraph.style.font.size, file=f)
    #         print(paragraph.style.font.cs_bold, file=f)
    #         print(paragraph.text, file=f)
    style_head_list = ['Heading 1', 'Heading 7', 'Heading 9', 'List Paragraph']
    style_font_all_compare_list = [{'font': 'Arial', 'size': '177800', 'title': 'Overview'},
                                   {'font': 'Arial', 'size': '139700'},
                                   {'font': 'Arial', 'size': '127000'},
                                   {'font': 'Times New Roman', 'size': None}]

    return style_head_list, style_font_all_compare_list


def title_text_parse(style_head, text, title_number):
    file_style = namedtuple('file_style', ['start_switch', 'end_switch'])
    file_style_list = {'Heading 1': file_style('# ', '\n'), 'Heading 7': file_style('## ', '\n'),
                       'Heading 9': file_style('### ', '\n'), 'List Paragraph': file_style('### ', '\n'),
                       'text_code': file_style("```verilog", '```')}
    text_result = file_style_list[style_head][0] + '.'.join(title_number) + " " + text
    return text_result


def add_file_list(paragraphs, style_head_list, style_font_all_compare_list):
    # file_content_list = [{head1:['xxx',{head2:{}},text,head]]
    file_content_list = []
    title_number = {0: [0, ''], 1: [0, ''], 2: [0, ''], 3: [0, '']}
    for paragraph in paragraphs:
        if paragraph.style.name in style_head_list:
            index = style_head_list.index(paragraph.style.name)
            if index == 0 and style_font_all_compare_list[0]['title'] == paragraph.text:
                title_number[0][0] = 1
                title1 = title_text_parse(paragraph.style.name, paragraph.text, title_number)
                file_content_list.append({paragraph.style.name: []})
            elif style_font_all_compare_list[index]['font'] == paragraph.style.font.name and \
                    style_font_all_compare_list[index]['size'] == paragraph.style.font.size:
                title_number[index][0] += 1
                title_number[index][1] = paragraph.style.name
                title1 = title_text_parse(paragraph.style.name, paragraph.text, title_number)
                if index == 0:
                    file_content_list.append({title1: []})
                elif index == 1:
                    for _k, _v in title_number.items():
                        file_content_list.append({title1: []})
    else:
        pass


if __name__ == '__main__':
    # x = get_image(r"E:\program\python\tools\docx_parse\image2")
    open_file_look_style()
    # Body Text 正文 Times New Roman 127000
    # Normal 代码
