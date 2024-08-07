import os
'''
自动将.\OtherFunnyThings文件夹中的项目内容生成html文件
'''
directory = './OtherFunnyThings'
html_content = '<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Other Funny Things</title>\n</head>\n<body>\n    <h1>一些有趣的东西</h1>\n    <ul>\n'

for item in os.listdir(directory):
    item_path = os.path.join(directory, item)
    if os.path.isfile(item_path):
        html_content += f'        <li><a href="./{item}">{item}</a></li>\n'
    elif os.path.isdir(item_path):
        html_content += f'        <li><a href="./{item}/">{item}</a></li>\n'

html_content += '    </ul>\n</body>\n</html>'

with open('./list.html', 'w', encoding='utf-8') as file:
    file.write(html_content)
    