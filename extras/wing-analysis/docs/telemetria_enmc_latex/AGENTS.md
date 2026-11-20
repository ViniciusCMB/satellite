# AGENTS.md

## What this is

LaTeX academic paper for the XXIX ENMC / XVII ECTM conference (2026, Bento Gonçalves). Language is Brazilian Portuguese with an English abstract/keywords block at the end of `main.tex`.

## Build

No Makefile or latexmk config exists. Build manually:

```bash
pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
```

All four passes are needed: first pass writes `.aux`, `bibtex` resolves citations, third pass inserts bibliography, fourth pass fixes cross-references.

Output: `main.pdf` in the repo root.

## File layout

| Path | Role |
|---|---|
| `main.tex` | Document entry point. Preamble, abstract, header/footer, `\input`s, bibliography, English abstract. |
| `sec-introducao.tex` | §1 INTRODUÇÃO + §2 DA NATUREZA À PLATAFORMA |
| `sec-metodologia.tex` | §3 METODOLOGIA (all subsections, equations, tables) |
| `sec-resultados.tex` | §4 RESULTADOS E DISCUSSÃO (all subsections, tables, figures) |
| `sec-conclusoes.tex` | §5 CONCLUSÕES + acknowledgements |
| `setup/config.sty` | Custom style: margins, section formatting, abstract/keywords environments, `\maketitle` override. |
| `bib/references.bib` | Bibliography (natbib + apalike). |
| `figures/` | Images. Referenced by filename only (no path prefix) because `\graphicspath{{figures/}}` is set in `main.tex`. |

## Conventions agents must follow

- **Figure references use bare filenames.** e.g. `\includegraphics{fig_test3_lrr.png}`, NOT `\includegraphics{figures/fig_test3_lrr.png}`. The `\graphicspath` directive handles the prefix.
- **Citations use `\citet` / `\citep`** (natbib), not raw `\cite`.
- **Section titles are UPPERCASE** in the source. Keep this convention when adding or editing sections.
- **Decimal separator is comma** in the body text (e.g. `12,90~m/s`). Math contexts use dots. Do not change existing numbers.
- **Non-breaking spaces before units** use `~` (e.g. `12,90~m/s`, `200~g`). Always include them.
- **Tables use `\begin{tabular*}{\textwidth}`** with `@{\extracolsep{\fill}}` to stretch across the page. Follow this pattern for new tables.
- **`\pretolerance=10000`** is set at document start — this relaxes line-breaking to avoid overfull warnings. Do not remove.
- **`\fontsize{11}{0}\selectfont`** is used before `\bibliography` to shrink the reference list. Follow this if adding post-bibliography content.

## Style quirks to know

- `config.sty` redefines `\maketitle`, `\section`, `\subsection`, and `\subsubsection` with custom spacing. Section numbering uses trailing dots (`1.`, `1.1`). Do not fight these — they are intentional for the ENMC template.
- The `keywords` environment is custom-defined in `config.sty` (not a standard LaTeX environment).
- The document ends with `\selectlanguage{english}` for the translated abstract, then switches back to `\selectlanguage{brazil}`.
- Header/footer uses `fancyhdr` with conference info. The first page has a special pagestyle (`firstpagestyle`).
- Some packages are loaded twice (e.g. `inputenc` in both `main.tex` and `config.sty`). This is harmless for pdflatex but do not add duplicates intentionally.
