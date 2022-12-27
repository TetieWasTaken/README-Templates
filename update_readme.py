import os
from urllib.parse import quote
import re


def regexReplace(string, search, replacement):
    return re.compile(search).sub(replacement, string)


languageCount = 0
languagesText = ""

root_dir = "EN"

# Iterate over the language directories
for directory in sorted(os.listdir(os.path.join(root_dir))):
    if not (directory == '.' or directory == '..' or directory[0] == '.'
            or os.path.isfile(directory)):
        # Store the current language subdirectory name
        languageSubdir = directory
        # Initialize a variable to store the language files for the current subdirectory
        subdirLanguagesText = ""
        # Iterate over the files within the language directories
        for filename in sorted(os.listdir(os.path.join(root_dir, directory)), key=lambda s: s.lower()):
            if os.path.isfile(os.path.join(root_dir, directory, filename)):
                # Generate the language name and file path
                language = (os.path.splitext(filename)[0].replace(
                    "-", "-").replace("∕", "/").replace("＼", "\\").replace(
                        "˸", ":").replace("∗", "*").replace("？",                "?").replace("＂",
                            "\"").replace("﹤",
                                          "<").replace("﹥",
                                                       ">").replace("❘", "|"))
                file_path = os.path.join(root_dir, directory, filename)
                # Add the language file to the list of language files for the current subdirectory
                subdirLanguagesText += f'* [{language}]({quote(file_path)})\n'
                # Increment the language count
                languageCount += 1
        # Add the language subdirectory name and list of language files for the current subdirectory to the overall language list
        languagesText += f'## [{languageSubdir}]({quote(os.path.join(root_dir, directory))})\n{subdirLanguagesText}'

# Generate the result string with the desired formatting for the language list
result = f"""<!--Templates start-->
# Languages ({languageCount} total)
{languagesText}<!--Templates end-->"""

# Read the contents of the README file
readmeContents = open('README.md', 'r', encoding="utf-8").read()

# Replace the language list section in the README file with the updated language list
open('README.md', 'w', encoding="utf-8").write(
    regexReplace(readmeContents,
                 r"<!--Templates start-->(.|\n)*<!--Templates end-->", result))

