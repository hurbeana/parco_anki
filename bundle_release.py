from pathlib import Path

basic_outpath = Path.cwd() / "basic.txt"
cloze_outpath = Path.cwd() / "cloze.txt"
basic = []
cloze = []
for b_f in Path.cwd().glob("*_basic.txt"):
    b_t = b_f.read_text(encoding="utf-8")
    if b_t:
        basic.append(b_t)
for c_f in Path.cwd().glob("*_cloze.txt"):
    c_t = c_f.read_text(encoding="utf-8")
    if c_t:
        cloze.append(c_t)
basic_outpath.write_text("\n".join(basic))
cloze_outpath.write_text("\n".join(cloze))
