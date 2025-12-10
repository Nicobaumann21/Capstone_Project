import os

def generate_tree(path, prefix=""):
    entries = sorted(os.listdir(path))
    tree = ""
    for i, entry in enumerate(entries):
        full_path = os.path.join(path, entry)
        connector = "├── " if i < len(entries)-1 else "└── "
        tree += prefix + connector + entry + "\n"
        if os.path.isdir(full_path) and entry not in ['.git', 'venv']:
            extension = "│   " if i < len(entries)-1 else "    "
            tree += generate_tree(full_path, prefix + extension)
    return tree

project_path = "."  # Repository-Wurzel
tree = generate_tree(project_path)

with open("README.md", "w", encoding="utf-8") as f:
    f.write("# Capstone Project – Projektmanagement Datenbank\n\n")
    f.write("Dieses Projekt entstand im Fach Datenbanken und DB-Programmierung: Relational, NoSQL, New SQL\n\n")
    f.write("Notion-Link: [Hier klicken](https://www.notion.so/Portfolio-Schenk-2be53dc6cef980239683e799d5455edd?source=copy_link)\n\n")
    f.write("## Projektstruktur\n\n```\n")
    f.write(tree)
    f.write("```\n")
