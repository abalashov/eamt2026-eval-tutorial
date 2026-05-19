# Translation Evaluation Tools for Everyone

**A Hands-On Tutorial for Freelance Translators and Smaller LSPs**

EAMT 2026 · Yuri Balashov · University of Georgia, USA

---

This repository accompanies the half-day tutorial *Translation Evaluation Tools
for Everyone* to be presented at EAMT 2026.
Everything you need to follow along and to keep practicing afterward is here:
the slide deck, four pre-aligned evaluation sets in different language pairs, worked
examples in Excel and Python, a reading list, and templates you can adapt for your own projects.

The tutorial is aimed at practicing translators and small language-service
providers. No programming experience is assumed; familiarity with Excel and a
modern web browser is enough.

---

## $\color{red}{\text{IMPORTANT NOTES}}$

1. **May 18, 2026 update: most of the content and the links in this README.md are complete; sample evaluation sets are ready; slides and bibliography may be updated between now and June 15; worked examples, Excel templates and a sample script will be posted soon. Please pardon our progress.**
2. **You are welcome (and encouraged) to use your own evaluation set of 200-300 sentences, in any domain and language pair, in lieu of the sets in this repository. But please make sure to read the MATEO paper linked below as well as the instructions on the MATEO site. You might also want to check out this brief [freelancer-oriented introduction to MATEO](https://mailchi.mp/slator/tool-box-january-2024#mctoc7) on Slator.**
3. **As of May 18, 2026, the main MATEO-hosting site is not operational: "On May 5, 2026, the [Institute for the Dutch Language (INT)](https://ivdnt.org/) became the target of a hack... It is currently unclear when the websites and services will be back online" (from the May 13,  2026 update). Accordingly: until this issue is resolved, the [HuggingFace mirror space](https://huggingface.co/spaces/BramVanroy/mateo-demo) is the only available option. You can use this space directly or clone it on your own (free) HuggingFace account by clicking [here](https://huggingface.co/spaces/BramVanroy/mateo-demo?duplicate=true). Further details are available on [Bram Vanroy's MATEO GitHub repository](https://github.com/BramVanroy/mateo-demo).**
4. **Due to these unfortunate circumstances, and to the likely memory limitations set by HuggingFace, we strongly recommend that you perform the Quick start steps (below) in advance of the tutorial and download all the Excel and PNG outputs on your laptop. Doing this during the tutorial, even assuming good Internet connection, may be impractical. On-site debugging would not be possible due to time constraints. In the worst-case scenario, the MATEO evaluation outputs for all four evaluation sets will be provided shortly before the tutorial. While that might deprive you of the opportunity to practice MATEO directly, we will go over some of the outputs in Parts 3 and 4 in any case.**

---

## What you'll learn

By the end of the session you should be able to:

1. Choose appropriate metrics (BLEU, chrF, TER, COMET, BLEURT, BERTScore) for a
   given evaluation task and explain their strengths and limitations.
2. Run a complete evaluation on your own data using the **MATEO** browser
   toolkit, with no installation and no GPU.
3. Read MATEO's output — bar charts, score tables with confidence intervals,
   and the sentence-level Excel export — with a critical eye.
4. Apply a small but rigorous statistical toolkit (mean, variance, standard
   deviation, confidence intervals, p-values, and Pearson/Spearman/Kendall
   correlation) to interpret your results.
5. Pair automatic scores with your own human grades (if available) to produce
   defensible quality assessments for your clients.

---

## Tutorial structure

The session is organized in four parts plus a final Q&A:

| Part | Title | Length |
|---|---|---|
| 1 | Introduction to Translation Evaluation Methods | 45 min |
| 2 | Hands-On with MATEO | 45 min |
| ☕ | Coffee break | 30 min |
| 3 | Interpreting Evaluation Results | 30 min |
| 4 | Lightweight Statistical Analysis | 45 min |
| Q&A | Final wrap-up | 10–15 min |


---

## Repository layout

```
.
├── README.md                                  ← this file
├── bibliography.bib                           ← reading list / citations
├── bibliography.pdf                           ← reading list / citations
├── slides/
│   └── Translation-Evaluation-Tools-for-Everyone.pdf
├── evaluation_sets/                           ← four parallel test sets
│   ├── en-de/
│   ├── en-ru/
│   ├── en-ja/
│   └── en-zh/
├── MATEO_outputs/   ← worst-case scenario outputs from MATEO
│   ├── 300_en-de/
│   ├── 300_en-ru/
│   ├── 300_en-ja/
│   └── 300_en-zh/
├── COMET-human-correlations/   ← addendum with excel calculations for 90-100_en-{de,ru,zh}
├── sample script/
│   └── python/                                ← bootstrap CIs
└── figures/                                   ← extra charts and diagrams from the deck
```

Each `evaluation_sets/<pair>/` directory contains:

- `source.txt` — the English source, one sentence per line, UTF-8.
- `reference.txt` — the professional human translation in the target language.
- `system_1.txt` … `system_4.txt` — outputs from commercial NMT engines and
  open-weight LLMs.
- `README.md` — the source of the data, line counts, and any
  language-specific notes (setting the BLEU tokenizer to `ja-mecab` for Japanese or `zh` for Chinese; and TER settings for both these languages to `asian_support` and `norm`).

All files are line-aligned: line *N* of every file corresponds to the same
segment.

---

## Prerequisites

- A modern web browser (Chrome, Firefox, Safari, Edge — anything from the
  last two years is fine).
- A working installation of **Excel** 2019 or newer: compatible alternatives (LibreOffice Calc, Google Sheets, Apple Numbers) may work too; but you'd need to figure out the details on your own.
- The four evaluation-set zip files from this repository, downloaded ahead of
  time.
- A text editor with explicit UTF-8 support (Notepad++ for Windows, Sublime or a similar app for Mac OS).
- MATEO evaluation outputs for your chosen set — strongly recommended, see in **boldface** above and below.

Entirely optional:

- Python 3.10+ if you want to run the optional `sample_script/python/` example. An LLM assistant (Claude, GPT, Gemini) can write and adapt this script for you in seconds, or write other simple scripts — you do not need to be a programmer.

The tutorial materials were prepared with **MATEO** version 1.8.4:

**Vanroy, Bram, Arda Tezcan, and Lieve Macken. 2023. [MATEO: MAchine Translation Evaluation Online](https://aclanthology.org/2023.eamt-1.52/).** In *Proceedings of the 24th Annual Conference of the European Association for Machine Translation*, Tampere, Finland: European Association for Machine Translation, 499–500.

MATEO is hosted by CLARIN B at the Instituut voor de Nederlandse Taal:
- Primary: <https://mateo.ivdnt.org>
- Mirror:  <https://huggingface.co/spaces/BramVanroy/mateo-demo>
- Source: <https://github.com/BramVanroy/mateo-demo>

The CLARIN instance has a 1 MB upload limit per file. The evaluation sets in this repository are sized to fit comfortably within that limit. **Unfortunately, "on May 5, 2026, the [Institute for the Dutch Language (INT)](https://ivdnt.org/) became the target of a hack... It is currently unclear when the websites and services will be back online" (from the May 13,  2026 update).** Accordingly: unless this issue is resolved soon, the [HuggingFace mirror space](https://huggingface.co/spaces/BramVanroy/mateo-demo) is the only available option. You can use this space directly, or clone it on your own (free) HuggingFace account by clicking [here](https://huggingface.co/spaces/BramVanroy/mateo-demo?duplicate=true). Further details are available on [Bram Vanroy's MATEO GitHub repository](https://github.com/BramVanroy/mateo-demo).

**Due to these unfortunate circumstances, and to the likely memory limitations set by HuggingFace, we strongly recommend that you perform the Quick start steps (below) in advance of the tutorial and download all the Excel and PNG outputs on your laptop. Doing this during the tutorial, even assuming good Internet connection, may be impractical. On-site debugging would not be possible due to time constraints. In the worst-case scenario, the MATEO evaluation outputs for all four evaluation sets will be provided at the tutorial. While that might deprive you of the opportunity to practice MATEO directly, we will go over some of the outputs in Parts 3 and 4 in any case.**

---

## Quick start (before the tutorial)

1. Clone or download this repository.
2. Pick the language pair you want to work on and download
   `evaluation_sets/<pair>/`.
3. Open <https://mateo.ivdnt.org> or <https://huggingface.co/spaces/BramVanroy/mateo-demo> in your browser, navigate to
   **Evaluate**.
4. Upload `reference.txt`, then `system_1.txt` through `system_4.txt`. Upload `source.txt` as well — COMET-22 will use it.
5. Tick **BLEU**, **chrF**, **TER**, **COMET-22**.
6. For Japanese: in the BLEU options expand *tokenize* and select `ja-mecab`. For Chinese: select `zh`.
7. For Japanese and Chinese: in the TER options, select `normalized` and `asian_support`.
8. Click **Evaluate MT**, hold your breath...
9. Download the bar charts (PNG), the score tables (`mateo-evaluation.xlsx` and `mateo-evaluation-ci.xlsx`), and the
   sentence-level COMET file (`mateo-sentences.xlsx`) — we'll work through them together in Part 3.

---

## MATEO outputs

The four "worst-case scenario" subdirectories in `MATEO_outputs/` are reserved for the MATEO outputs for our evaluation sets. These outputs will be provided shortly before the tutorial as a back-up for those who encounter any issues with the MATEO web interface, for any reason.

---

## COMET-human-correlations
`COMET-human-correlations` contains three additional excel workbooks calculating sentence-level correlations between COMET and human evaluation scores for about 12 outputs x 100 sentences in `en-{de,ru,zh}`. We will do over them if time permits.

---

## Sample script

`sample script/python/` contains a short Python script (`bootstrap_ci.py`) that reproduces the confidence intervals from the sentence-level data in the sample `sentence_level_comet.xlsx`.

---



## Citing this tutorial

If you use the materials, the evaluation sets, or the analysis pipeline,
please cite:

> Balashov, Y. (2026). [*Translation Evaluation Tools for Everyone: A
> Hands-On Tutorial for Freelance Translators and Smaller LSPs.*](https://github.com/YuriBalashov/eamt2026-eval-tutorial)
> Tutorial at the 26th Annual Conference of the European Association for
> Machine Translation (EAMT 2026).

A BibTeX entry is included in `bibliography.bib`.

The evaluation data is derived from the [**Reeve Foundation Multilingual Corpus (RFMC)**](https://github.com/YuriBalashov/reeve-mftc). If you use it in published work, please cite the corresponding
papers:

> Balashov, Yuri, Alex Balashov, and Shiho Fukuda Koski. 2025. [Translation Analytics for Freelancers: I. Introduction, Data Preparation, Baseline Evaluations](https://aclanthology.org/2025.mtsummit-1.42/).
> In *Proceedings of Machine Translation Summit XX, Volume 1*, Geneva, Switzerland: European Association for Machine Translation, 538–65

> Balashov, Yuri, Rex VanHorn, Austin Downes, and Mingxi Xu. 2026. Translation Analytics for Freelancers: II. Benchmarking Local LLMs for Confidential Translation Workflows. In *Proceedings of EAMT 2026*, forthcoming.

---

## License

- **Tutorial materials** are licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/), for non-commercial/academic use only, with attribution.
- **Evaluation data**: derived from the Reeve Foundation Trilingual /
  Multilingual Corpus, used with permission for research and educational
  purposes. Please consult the per-pair `README.md` files for specific
  redistribution terms.
- The MATEO toolkit itself is licensed independently (Apache-2.0); see
  <https://github.com/BramVanroy/mateo-demo>.

---

## Acknowledgments

This tutorial draws on research supported by the U.S. National Science
Foundation under Award **SES-2336713**. Any opinions, findings, and
conclusions expressed here are those of the author and do not necessarily
reflect the views of the National Science Foundation.

Thanks to the Christopher & Dana Reeve Foundation for permission to use
multilingual professional translations from their published materials; to
Bram Vanroy and the LT3 group at Ghent University for building and
maintaining MATEO; to Rex VanHorn for collaboration on the underlying analytics work;
and to Felix do Carmo and Diptesh Kanojia, whose AMTA-2024 tutorial
*Editing Distance Metrics for Machine Translation Evaluation* was a model
for how to teach evaluation methods to working translators.

---

## Contact

**Yuri Balashov**, Department of Philosophy & Institute for Artificial Intelligence
University of Georgia, Athens, GA, USA · <yuri@uga.edu> · <https://www.yuribalashov.com>
