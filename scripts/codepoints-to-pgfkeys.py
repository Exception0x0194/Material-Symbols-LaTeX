codepoint_file_name = "./symbols-codepoints.txt"
pgf_file_name = "./symbols-pgf.txt"

pgf_head = r"""
\pgfkeys{
  /mSymbols/.cd
"""
pgf_tail = r"""
 ,others/.initial=E000
  }
"""

lines = open(codepoint_file_name, encoding="utf-8").readlines()
entries_lines = [pgf_head]
for line in lines:
    name, codepoint = line.strip().split()
    name = name.replace("_", "-")
    entry_line = " ,%s/.initial=%s\n" % (name, codepoint.upper())
    entries_lines.append(entry_line)
entries_lines.append(pgf_tail)

with open(pgf_file_name, "w", encoding="utf-8") as f:
    f.writelines(entries_lines)
    f.close()
