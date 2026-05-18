# Evaluation set: Chinese (Simplified)

A pre-aligned evaluation set for the EAMT 2026 tutorial *Translation Evaluation Tools for Everyone*. All files are UTF-8 plain text, one sentence per line, with line *N* corresponding to the same segment across files.

## Files

| File | Contents |
|---|---|
| `source_zh.txt` | English source sentences |
| `reference_zh.txt` | Professional human translation into German |
| `system_1_zh.txt` | Output from a leading commercial NMT engine |
| `system_2_zh.txt` | Output from a local NMT engine |
| `system_3_zh.txt` | Output from an open-weight LLM (large) |
| `system_4_zh.txt` | Output from an open-weight LLM (medium / small) |

Size: ~300 sentences. Line counts in every file are identical; verify with Notepad++ or Sublime.

## Source

Excerpted from the [**Reeve Foundation Multilingual Corpus (RFMC)**](https://github.com/YuriBalashov/reeve-mftc), a real medical-domain translation dataset based on the materials published with permission from the [Christopher & Dana Reeve Foundation](https://www.christopherreeve.org/) and aligned for research and educational use only by the project team. See Balashov et al. (2026) for the full description.

## How to use with MATEO

1. Open <https://mateo.ivdnt.org> or <https://huggingface.co/spaces/BramVanroy/mateo-demo> → **Evaluate**.
2. Upload `reference.txt` as the reference file.
3. Upload `system_1.txt` … `system_4.txt` as system outputs (up to four).
4. Upload `source.txt` (needed for COMET-22).
5. Tick **BLEU**, **chrF**, **TER**, **COMET-22**.
6. In the BLEU options expand *tokenize* and select `zh`.
7. In the TER options, select `normalized` and `asian_support`.
8. Click **Evaluate MT**.
9. Download the bar charts (PNG), the score tables (`mateo-evaluation.xlsx` and `mateo-evaluation-ci.xlsx`), and the sentence-level COMET file (`mateo-sentences.xlsx`) — we'll work through them together in Part 3.

## Citation

If you use this data in published work, please cite:

> Balashov, Yuri, Rex VanHorn, Austin Downes, and Mingxi Xu. 2026. Translation Analytics for Freelancers: II. Benchmarking Local LLMs for Confidential Translation Workflows. In *Proceedings of EAMT 2026*, forthcoming.
