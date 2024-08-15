codepoint_file_name = "./symbols-codepoints.txt"
output_file_name = "./symbols-dense.txt"

head = r"""\documentclass{article}
\usepackage[
	a4paper,
	left=1.2cm,
	right=1.2cm,
	top=1.5cm,
	bottom=1cm,
	nohead
]{geometry}
\usepackage{material-symbols}
\begin{document}
\pagestyle{empty}
\noindent
"""
tail = r"\end{document}"


lines = open(codepoint_file_name, encoding="utf-8").readlines()
entries_lines = [head]
for line in lines:
    name, codepoint = line.strip().split()
    name = name.replace("_", "-")
    entry_line = "\\mSymbol[outlined]{%s}\n" % (name)
    entries_lines.append(entry_line)
entries_lines.append(tail)

with open(output_file_name, "w", encoding="utf-8") as f:
    f.writelines(entries_lines)
    f.close()
