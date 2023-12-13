from collections import Counter
from typing import List

from build_homepage_md import *


def save_lines(lines, output_dir, output_name):
    full_path = os.path.join(output_dir, output_name)
    with open(full_path, "w") as f:
        f.writelines(lines)
        print("".join(lines))
        print(f"Save at {full_path}")


def change_md_href_to_text_href(md: str) -> str:
    for text, link in re.findall(r"\[(.+?)\]\((.+?)\)", md):
        tex_link = f"\\href{{{link}}}{{{text}}}"
        md_link = f"[{text}]({link})"
        md = md.replace(md_link, tex_link)
    return md


def _build_about_text(sheet: Spreadsheet, sheet_path_list: List[str], tab_name: str):
    tab = get_tab_df(sheet, sheet_path_list, tab_name)
    lines = [rf"\cvsection{{{tab_name.title()}}}", "\n" * 2, r"{\small", "\n" * 2]
    for i, r in tab.iterrows():
        tex_text = change_md_href_to_text_href(r.text)
        lines += [tex_text, "\n" * 2]
    lines += ["}", "\n" * 2, r"\hfill \break"]
    return lines


def _build_cventry(sheet: Spreadsheet, sheet_path_list: List[str], tab_name: str,
                   keys: List[str], out_date_format):
    # education
    tab = get_tab_df(sheet, sheet_path_list, tab_name)

    lines = [rf"\cvsection{{{tab_name.title()}}}", "\n" * 2]
    lines += [r"\begin{cventries}", "\n" * 2]

    for i, r in tab.iterrows():
        lines += [" " * 2, r"\cventry", "\n"]
        for ik, k in enumerate(keys):
            if ik < 3:
                _l = f"{{{getattr(r, k)}}} % {k}"
            if ik == 3:  # date
                _d = datetime.strptime(getattr(r, k), "%Y-%m-%d").strftime(out_date_format)
                _l = f"{{{_d}}} % {k}"
            else:  # bullets
                _l = f"{{{getattr(r, k)}}} % {k}" if getattr(r, k) != "" else r"{}\vspace{-1em}"
            lines += [" " * 4, _l, "\n"]

        lines.append("\n")

    lines += [r"\end{cventries}"]
    return lines


def _build_cvpubs(sheet: Spreadsheet, sheet_path_list: List[str], tab_name: str, me="Dongkwan Kim"):
    # publications, services, talks, teaching
    def _publications(df: pd.DataFrame, lines, subsec_key: str):
        subsec_counter = Counter(getattr(r, subsec_key) for i, r in df.iterrows())
        for subsec, counts in sorted(subsec_counter.items(), key=lambda kv: kv[0]):
            # sort [conference, workshop]
            lines += [rf"\cvsubsection{{{subsec.title()}}}", "\n" * 2]
            lines += [r"\begin{cvpubs}", "\n" * 2]
            for i, r in sorted(df.iterrows(), key=lambda _ir: _ir[1].date, reverse=True):

                if subsec != r.type:
                    continue

                _prefix = f"{r.type[0].upper()}{subsec_counter[r.type]}"
                subsec_counter[r.type] -= 1

                _authors = r.authors.replace(me, rf"\textbf{{{me}}}")
                _year = datetime.strptime(r.date, "%Y-%m-%d").strftime("%Y")
                url = r.paperurl or r.arxivurl
                _pub = rf'[{_prefix}] {_authors}. \href{{{url}}}{{``{r.title}."}} \textit{{{r.venue}}}. {_year}'
                lines += [rf"  \cvpub{{{_pub}}}", "\n" * 2]
            lines += [r"\end{cvpubs}", "\n" * 2]

    def _talks(df: pd.DataFrame, lines, *args):
        lines += [r"\begin{cvpubs}", "\n" * 2]
        for i, r in sorted(df.iterrows(), key=lambda _ir: _ir[1].date, reverse=True):
            _presenters = r.presenters.replace(me, rf"\textbf{{{me}}}")
            _date = datetime.strptime(r.date, "%Y-%m-%d").strftime("%d %b %Y")
            _venue = rf'\href{{{r.venueurl}}}{{{r.venue}}}'
            _talk = rf'{_presenters}. \href{{{r.slideurl}}}{{``{r.title}."}} \textit{{{_venue}}}. {_date}'
            lines += [rf"  \cvpub{{{_talk}}}", "\n" * 2]
        lines += [r"\end{cvpubs}"]

    def _academic_services(df: pd.DataFrame, lines, *args):
        position_and_org_to_rs = defaultdict(lambda: defaultdict(list))
        for i, r in df.iterrows():
            position_and_org_to_rs[r.position][r.organization].append(r)
        lines += [r"\begin{cvpubs}", "\n" * 2]
        for p, o_to_rs in position_and_org_to_rs.items():
            _o_ys = []
            for o, rs in o_to_rs.items():
                _years = [f"{r.year}" if r.url == "" else rf"\href{{{r.url}}}{{{r.year}}}" for r in rs]
                _years = [y.replace("#", "\#") for y in _years]
                _o_ys.append(f"{o} ({', '.join(_years)})")
            one_line = rf"\textbf{{{p}:}} {', '.join(_o_ys)}"
            lines.append(rf"  \cvpub{{{one_line}}}" + "\n" * 2)
        lines += [r"\end{cvpubs}"]

    def _teaching_experiences(df: pd.DataFrame, lines, *args):
        course_to_rs = defaultdict(list)
        for i, r in df.iterrows():
            course_to_rs[r.course].append(r)
        lines += [r"\begin{cvpubs}", "\n" * 2]
        for c, rs in course_to_rs.items():
            positions = [r.position for r in rs]
            positions = set(positions) if len(set(positions)) == 1 else positions
            head = rf'\textbf{{{", ".join(positions)}:}}'
            semesters = ", ".join(f"{r.semester}" if r.url == ""
                                  else rf"\href{{{r.url}}}{{{r.semester}}}" for r in rs)
            notes = ", ".join(r.note for r in rs if r.note != "")
            if notes == "":
                lines += [rf"  \cvpub{{{head} {c} ({semesters})}}", "\n" * 2]
            else:
                lines += [rf"  \cvpub{{{head} {c} ({semesters}), \textit{{{notes}}}}}", "\n" * 2]
        lines += [r"\end{cvpubs}"]

    tab = get_tab_df(sheet, sheet_path_list, tab_name)
    func_name = "_" + tab_name.replace(" ", "_")

    lines = [rf"\cvsection{{{tab_name.title()}}}", "\n" * 2]
    locals()[func_name](tab, lines, "type")
    return lines


def _build_cvhonor(sheet: Spreadsheet, sheet_path_list: List[str], tab_name: str,
                   keys: List[str], out_date_format: str):
    # honors
    tab = get_tab_df(sheet, sheet_path_list, tab_name)

    lines = [rf"\cvsection{{{tab_name.title()}}}", "\n" * 2]
    lines += [r"\begin{cvhonors}", "\n" * 2]

    for i, r in tab.iterrows():
        lines += [" " * 2, r"\cvhonor", "\n"]
        for ik, k in enumerate(keys):
            if k is None:
                _l = "{} % None"
            elif ik < 3:
                if k == "title" and r.url != "":
                    tex_link = f"\\href{{{r.url}}}{{{getattr(r, k)}}}"
                    _l = f"{{{tex_link}}} % {k}"
                else:
                    _l = f"{{{getattr(r, k)}}} % {k}"
            else:  # date
                try:
                    _d = datetime.strptime(getattr(r, k), "%Y-%m-%d").strftime(out_date_format)
                    _l = f"{{{_d}}} % {k}"
                except ValueError:
                    _l = f"{{{getattr(r, k)}}} % {k}"  # date but not %Y-%m-%d
            lines += [" " * 4, _l, "\n"]

        lines.append("\n")

    lines += [r"\end{cvhonors}"]
    return lines


if __name__ == '__main__':

    __target__ = "all"
    __gsheet__ = "https://docs.google.com/spreadsheets/d/1QeeQhPYIeTiCTJNczKSfenHCYGMLf3a2vvzCor1Gd2A/"
    __dir__ = "./cv/"
    __path_1__ = "./Data for CV (Dongkwan Kim).xlsx"

    os.makedirs(__dir__, exist_ok=True)

    try:
        gc = gspread.oauth()
        sh = gc.open_by_url(__gsheet__)
    except:
        gc, sh = None, None

    if __target__ == "about" or __target__ == "all":
        tex = _build_about_text(sh, [__path_1__], "about")
        save_lines(tex, __dir__, "about.tex")

    if __target__ == "education" or __target__ == "all":
        tex = _build_cventry(sh, [__path_1__], "education",
                             keys=["degree", "institution", "location", "date", "bullets"],
                             out_date_format="%b %Y")
        save_lines(tex, __dir__, "education.tex")

    if __target__ == "publications" or __target__ == "all":
        tex = _build_cvpubs(sh, [__path_1__], "publications")
        save_lines(tex, __dir__, "publications.tex")

    if __target__ == "talks" or __target__ == "all":
        tex = _build_cvpubs(sh, [__path_1__], "talks")
        save_lines(tex, __dir__, "talks.tex")

    if __target__ == "services" or __target__ == "all":
        tex = _build_cvpubs(sh, [__path_1__], "academic services")
        save_lines(tex, __dir__, "services.tex")

    if __target__ == "teaching" or __target__ == "all":
        tex = _build_cvpubs(sh, [__path_1__], "teaching experiences")
        save_lines(tex, __dir__, "teaching.tex")

    if __target__ == "honors" or __target__ == "all":
        tex = _build_cvhonor(sh, [__path_1__], "honors",
                             keys=["title", "organization", None, "date"],
                             out_date_format="%Y")
        save_lines(tex, __dir__, "honors.tex")
