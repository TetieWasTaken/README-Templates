import os
from urllib.parse import quote
import re


def regexReplace(string, search, replacement):
    return re.compile(search).sub(replacement, string)


templateCount = 0
templatesText = ""

root_dir = "EN"

for directory in sorted(os.listdir(os.path.join(root_dir))):
    if not (directory == '.' or directory == '..' or directory[0] == '.'
            or os.path.isfile(directory)):
        templateSubdir = directory
        subdirTemplatesText = ""
        for filename in sorted(os.listdir(os.path.join(root_dir, directory)), key=lambda s: s.lower()):
            if os.path.isfile(os.path.join(root_dir, directory, filename)):
                template = (os.path.splitext(filename)[0].replace(
                    "-", "-").replace("∕", "/").replace("＼", "\\").replace(
                        "˸", ":").replace("∗", "*").replace("？",                "?").replace("＂",
                            "\"").replace("﹤",
                                          "<").replace("﹥",
                                                       ">").replace("❘", "|"))
                file_path = os.path.join(root_dir, directory, filename)
                subdirTemplatesText += f'* [{template}]({quote(file_path)})\n'
                templateCount += 1
        templatesText += f'## [{templateSubdir}]({quote(os.path.join(root_dir, directory))})\n{subdirTemplatesText}'

result = f"""<!--Templates start-->
# Templates ({templateCount} total)
{templatesText}<!--Templates end-->"""

readmeContents = open('README.md', 'r', encoding="utf-8").read()

open('README.md', 'w', encoding="utf-8").write(
    regexReplace(readmeContents,
                 r"<!--Templates start-->(.|\n)*<!--Templates end-->", result))

