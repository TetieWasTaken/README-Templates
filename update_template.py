import re
import os
import subprocess

template_content = """
This template is licensed under the [MIT license](https://choosealicense.com/licenses/mit/). Feel free to use it in your own projects without any limitations.
"""

def regexReplace(string, search, replacement):
    return re.compile(search).sub(replacement, string)

for root, _, files in os.walk('EN'):
    for file in files:
        if not file.endswith('.md'):
            continue
        if file == 'README.md':
            continue

        templateFile = file[0].upper() + file[1:]
        templateFile = templateFile.replace('_', ' ')

        size = len(templateFile)

        template_text = f"""<!--Title start-->

# {templateFile[:size-3]} template
{template_content}
<!--Title end-->"""

        file_path = os.path.join(root, file)
        with open(file_path, 'r') as f:
            contents = f.read()

        # Replace the template text in the .md file
        open(file_path, 'w', encoding="utf-8").write(regexReplace(contents, r"<!--Title start-->(.|\n)*<!--Title end-->", template_text))