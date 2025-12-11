import os

IGNORE = ['.git', 'venv', '.github']

def generate_tree(path, prefix=""):
    entries = sorted(os.listdir(path))
    tree = ""
    for i, entry in enumerate(entries):
        if entry in IGNORE:
            continue
        full_path = os.path.join(path, entry)
        connector = "├── " if i < len(entries)-1 else "└── "
        tree += prefix + connector + entry + "\n"
        if os.path.isdir(full_path):
            extension = "│   " if i < len(entries)-1 else "    "
            tree += generate_tree(full_path, prefix + extension)
    return tree

project_path = "."
tree = generate_tree(project_path)

with open("README.md", "w", encoding="utf-8") as f:
    f.write("# Capstone Project – Projektmanagement Datenbank\n\n")
    f.write("Dieses Projekt entstand im Fach Datenbanken und DB-Programmierung: Relational, NoSQL, New SQL\n\n")
    f.write("Dieser Link ist für eine Notion-Seite, auf der alle relevanten Schritte, Queries und sonstige step-by-step aufgeführt sind:\n")
    f.write("[Notion-Link](https://www.notion.so/Portfolio-Schenk-2be53dc6cef980239683e799d5455edd?source=copy_link)\n\n")
    f.write("## Projektstruktur\n\n```\n")
    f.write(tree)
    f.write("```\n")
