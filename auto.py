import os

def find_index_or_readme(directory):
    """
    在指定目录中查找 index.html 或 README.md 文件，并返回其内容。
    """
    index_path = os.path.join(directory, 'index.html')
    readme_path = os.path.join(directory, 'README.md')
    
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as file:
            return file.read()
    elif os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as file:
            return file.read()
    else:
        return None

def generate_html_list(directory):
    """
    生成一个包含指定目录中所有文件和文件夹的 HTML 列表。
    """
    html_content = '<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Other Funny Things</title>\n</head>\n<body>\n    <h1>一些有趣的东西</h1>\n    <ul>\n'

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            html_content += f'        <li><a href="{directory+item}">{item}</a></li>\n'
        elif os.path.isdir(item_path):
            html_content += f'        <li><a href="{directory+item}/">{item}</a></li>\n'

    html_content += '    </ul>\n</body>\n</html>'
    return html_content

def main():
    directory = './OtherFunnyThings'
    
    # 尝试查找 index.html 或 README.md
    content = find_index_or_readme(directory)
    
    if content is None:
        # 如果没有找到 index.html 或 README.md，则生成一个 HTML 列表
        content = generate_html_list(directory)
    
    # 将内容写入 list.html 文件
    with open('./list.html', 'w', encoding='utf-8') as file:
        file.write(content)

if __name__ == "__main__":
    main()
    
    
    
#     <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Other Funny Things</title>
# </head>
# <body>
#     <h1>一些有趣的东西</h1>
#     <ul>
#         <li><a href="./OtherFunnyThings/ascii-art-converter/index.html">ascii-art-converter</a></li>
#         <li><a href="./OtherFunnyThings/game.html">game.html</a></li>
#         <li><a href="./OtherFunnyThings/StudyWithMiku-main/StudyWithMiku-main/index.html">StudyWithMiku-main</a></li>
#         <li><a href="./OtherFunnyThings/video2chars-0.3/README.md">video2chars-0.3</a></li>
#     </ul>
# </body>
# </html>