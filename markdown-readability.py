# SPDX-License-Identifier: CC0-1.0
# SPDX-FileCopyrightText: 2024 The Foundation for Public Code <info@publiccode.net>
# markdown-readability.py: experiment in checking readability of jekyll text

import io
import os
import re
import sys

import markdown
import textstat

# remove links
def unmark_element(element, stream=None):
	if stream is None:
		stream = io.StringIO()
	if element.text:
		stream.write(element.text)
	for sub in element:
		unmark_element(sub, stream)
	if element.tail:
		stream.write(element.tail)
	return stream.getvalue()

# patch Markdown to add plaintext as an output format
markdown.Markdown.output_formats["plain"] = unmark_element
__md = markdown.Markdown(output_format="plain")
__md.stripTopLevelTags = False

def unmark(text):
	return __md.convert(text)

# jekyll markdown has YAML "frontmatter" which precedes the actual markdown
def strip_frontmatter(filepath):
	with open(filepath) as x:
		raw_lines = x.readlines()

		# strip "frontmatter"
		front_matter_markers = 0
		md_lines = []
		for line in raw_lines:
			if front_matter_markers < 2:
				if line == "---\n":
					front_matter_markers += 1
			else:
				md_lines.append(line)
		md_text = ''.join(md_lines)
		return md_text


def score_readability(filepath):
	md_text = strip_frontmatter(filepath)
	text = unmark(md_text)
	# print(text)

	print(filepath)
	print("flesch_kincaid_grade: ", textstat.flesch_kincaid_grade(text))
	print("gunning_fog:          ", textstat.gunning_fog(text))
	print("text_standard:        ", textstat.text_standard(text))

	# print("flesch_reading_ease: ", textstat.flesch_reading_ease(text))
	# print("smog_index: ", textstat.smog_index(text))
	# print("coleman_liau_index: ", textstat.coleman_liau_index(text))
	# print("automated_readability_index: ", textstat.automated_readability_index(text))
	# print("dale_chall_readability_score: ", textstat.dale_chall_readability_score(text))
	# print("difficult_words: ", textstat.difficult_words(text))
	# print("linsear_write_formula: ", textstat.linsear_write_formula(text))
	# print("fernandez_huerta: ", textstat.fernandez_huerta(text))
	# print("szigriszt_pazos: ", textstat.szigriszt_pazos(text))
	# print("gutierrez_polini: ", textstat.gutierrez_polini(text))
	# print("crawford: ", textstat.crawford(text))
	# print("gulpease_index: ", textstat.gulpease_index(text))
	# print("osman: ", textstat.osman(text))


markdown_dir = sys.argv[1];

if not os.path.isdir(markdown_dir):
	print(f"usage: {sys.argv[0]} path/to/markdown/dir")
	exit(1)

filelist = []
for f in os.listdir(markdown_dir):
	if f.endswith(".md"):
		filelist.append(markdown_dir + "/" + f)

for filepath in filelist:
	print("\n")
	score_readability(filepath)
