#!/usr/bin/env python3
import os
import glob
import markdown
import yaml
import datetime
from full_yaml_metadata import makeExtension

index_template = "templates/index.html"
blog_template = "templates/blog.html"
homepage_template = '<nav><ul><li><a href="{path}" class="contrast"><strong>Home</strong></a></li></ul></nav>'
style_link = '<link href="{path}" rel="stylesheet"></link>'

index_section = {
    "about": "index/about.md",
    "passionate": "index/passionate.md",
    "working_with": "index/working_with.md",
    "thinking_about": "index/thinking_about.md",
}
awesome_md = "index/003 Awesome.md"
blog_dir = "blogs/"
seeds_dir = "seed/"

extension = "html"

makeExtension()


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


md = md_parser()


def get_template(template_file):
    with open(template_file, "r") as index_fp:
        template = index_fp.read()
    return template


def output_path(pattern):
    return "docs" + "/" + pattern + "." + extension


def format_index(blog_list):
    index_html = get_template(index_template)

    with open(output_path("index"), "w") as out:

        # blog section list
        blog_list_content = ""
        blog_list = sorted(blog_list, key=lambda x: x[0], reverse=True)
        for blog in blog_list:
            blog_list_content += "<article><a href='blogs/{title}.html' class='contrast'>{title}</a></article>".format(
                title=blog[1]
            )

        index_html = index_html.replace("{{body}}", blog_list_content)

        out.write(index_html)

    index_html = get_template(index_template)
    with open(output_path("about"), "w") as out:
        # about me
        about_me_md = index_section["about"]
        with open(about_me_md, "r") as section_fp:
            raw = section_fp.read()
            content = md.convert(raw)
            index_html = index_html.replace("{{body}}", content)

        out.write(index_html)


# def format_awesome(template):
#     with open(output_path("awesome"), "w") as out:
#         with open(awesome_md, "r") as input:
#             raw = input.read()
#             content = md.convert(raw)
#             template = template.replace("{{title}}", "awesome")
#             template = template.replace("{{body}}", content)
#             template = template.replace("{{home}}", homepage_template.format(path="index.html"))
#             template = template.replace("{{style_link}}", style_link.format(path="retro.css"))
#         out.write(template)


def format_blog(template, blog_file):
    with open(blog_file, "r") as input:
        raw = input.read()
        content = md.convert(raw)
        template = template.replace("{{title}}", md.Meta.get("title"))
        template = template.replace("{{body}}", content)
        template = template.replace("{{home}}", homepage_template.format(path="../index.html"))
        template = template.replace("{{style_link}}", style_link.format(path="../retro.css"))
        with open(output_path(f"blogs/{md.Meta.get("title")}"), "w") as out:
            out.write(template)
    return md.Meta.get("created"), md.Meta.get("title")


if __name__ == "__main__":
    if not os.path.exists("docs"):
        os.mkdir("docs")

    blog_template = get_template(blog_template)

    blog_list = []
    for f in glob.iglob("blogs/*.md"):
        blog_list.append(format_blog(blog_template, f))

    format_index(blog_list)
    # format_awesome(blog_template)
