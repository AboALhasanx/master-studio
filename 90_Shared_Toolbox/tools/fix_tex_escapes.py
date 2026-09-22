from pathlib import Path
import re
p = Path(r"G:\My Drive\Master-Studio\90_Shared_Toolbox\tools\build_w02_fuzzy_booklet.py")
src = p.read_text(encoding="utf-8")
cmds = r"varphi|varepsilon|tilde|text|to|ne|notin|in|mid|ldots|cdots|Rightarrow|mapsto|subseteq|supseteq|overline|bar|cap|cup|times|cdot|frac|sum|int|pm|le|ge|infty|mathbb|bmod|quad|qquad|left|right|langle|rangle|partial|forall|exists|mu|alpha|beta|gamma|delta|epsilon|lambda|sigma|omega|phi|psi"
pat = re.compile(r"(?<!\\)\\(" + cmds + r")\b")
new, n = pat.subn(lambda m: "\\\\" + m.group(1), src)
pat2 = re.compile(r"(?<!\\)\\([()\[\]])")
new, n2 = pat2.subn(lambda m: "\\\\" + m.group(1), new)
new = new.replace("\x0barphi", "\\\\varphi")
p.write_text(new, encoding="utf-8")
print("tex-command fixes", n, "delimiter fixes", n2)
for i,line in enumerate(new.splitlines(),1):
    if re.search(r"(?<!\\)\\[vtnrabf](?![a-zA-Z])", line):
        print("still-bad", i, line[:140])
print("done")
