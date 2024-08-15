table_head = r"""\begin{longtable}{
>{\raggedright\arraybackslash}p{0.1\textwidth}
>{\raggedright\arraybackslash}p{0.1\textwidth}
>{\raggedright\arraybackslash}p{0.1\textwidth}
>{\raggedright\arraybackslash}p{0.5\textwidth}
>{\raggedright\arraybackslash}p{0.2\textwidth}
}
\textbf{Outlined} & \textbf{Rounded} &\textbf{Sharp} & \textbf{Command} & \textbf{Codepoint} \\
\endfirsthead
\textbf{Outlined} & \textbf{Rounded} &\textbf{Sharp} & \textbf{Command} & \textbf{Codepoint} \\
\endhead
"""
table_tail = r"""
\end{longtable}
"""

codepoint_file_name = "./symbols-codepoints.txt"
output_file_name = "./symbols-table.txt"

lines = open(codepoint_file_name, encoding="utf-8").readlines()
entries_lines = [table_head]
for line in lines:
    name, codepoint = line.strip().split()
    name = name.replace("_", "-")
    entry_line = (
        "\\mSymbol[outlined]{%s} \\mSymbol[outlined-filled]{%s} & \\mSymbol[rounded]{%s} \\mSymbol[rounded-filled]{%s} & \\mSymbol[sharp]{%s} \\mSymbol[sharp-filled]{%s} & \\texttt{\\textbackslash mSymbol\\{%s\\}} & \\texttt{%s}\\\\\n"
        % (name, name, name, name, name, name, name, codepoint.upper())
    )
    entries_lines.append(entry_line)
entries_lines.append(table_tail)

with open(output_file_name, "w", encoding="utf-8") as f:
    f.writelines(entries_lines)
    f.close()
