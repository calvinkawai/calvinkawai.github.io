#!/usr/bin/env python3
from jinja2 import Environment, FileSystemLoader
import markdown
import yaml
from datetime import datetime
import os
from pathlib import Path

enviroment = Environment(loader=FileSystemLoader('templates'))

def md_parser():
    md = markdown.Markdown(
        extensions=["fenced_code", "full_yaml_metadata"],
        extension_configs={
            "full_yaml_metadata": {
                "yaml_loader": yaml.SafeLoader,
            }
        },
    )
    return md

def get_template(template_name):
    return enviroment.get_template(template_name)

class NoteLinkDTO:

    def __init__(self, href, timestamp, title, file_path):
        self.text = f"{timestamp} {self._parse_title(title)}"
        self.file_path = file_path
        self.href = f"{title}.html"
        self.title = self._parse_title(title)
        self.timestamp = timestamp

    def _parse_title(self, title):
        # Remove file extension and replace hyphens/underscores with spaces
        # Capitalize first letter of each word
        title_clean = title.replace('-', ' ').replace('_', ' ')
        return title_clean.title()

def get_file_modification_date(file_path):
    """Get file modification date in yyyy-mm-dd format"""
    mtime = os.path.getmtime(file_path)
    return datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")

def build_nav_links():
    """Read all markdown files from blogs/ folder and construct NoteLinkDTO objects"""
    blogs_dir = Path('blogs')
    note_links = []
    
    # Check if blogs directory exists
    if not blogs_dir.exists():
        print(f"Warning: {blogs_dir} directory does not exist")
        return note_links
    
    # Iterate through all files in blogs directory
    for file_path in blogs_dir.iterdir():
        # Skip directories and non-markdown files
        if file_path.is_file() and file_path.suffix.lower() == '.md':
            # Get filename without extension
            title = file_path.stem
            
            # Get modification date
            timestamp = get_file_modification_date(file_path)
            
            # Create NoteLinkDTO object
            note_link = NoteLinkDTO(
                href=f"{title}.html",
                title=title,
                timestamp=timestamp,
                file_path=str(file_path)
            )
            
            note_links.append(note_link)
    
    # Sort by modification date (newest first)
    note_links.sort(key=lambda x: x.text, reverse=True)
    
    return note_links

def render_index(note_links):
    template = get_template("index.html")
    with open("docs/index.html", "w") as fp:
        fp.write(template.render(notes=note_links))

def render_blog(note_link, note_links):
    template = get_template("base.html")
    with open(note_link.file_path, "r") as fp:
        content = fp.read()
        content = md_parser().convert(content)
    with open(f"docs/{note_link.href}", "w") as fp:
        fp.write(template.render({
            "content": content,
            "notes": note_links,
            "title": note_link.title,
            "updated_on": note_link.timestamp,
            "note_link": note_link
        }))

def render_all_blogs(note_links):
    for note_link in note_links:
        render_blog(note_link, note_links)


if __name__ == "__main__":
    nav_links = build_nav_links()
    render_index(nav_links)
    render_all_blogs(nav_links)
