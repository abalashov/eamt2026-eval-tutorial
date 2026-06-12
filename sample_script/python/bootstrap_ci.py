"""
bootstrap_ci.py — compute 95% bootstrap confidence intervals for COMET scores.

Reads 'sentence_level_comet.xlsx' from the same directory as this script and
prints, for each system column, the mean score and a 95% CI obtained from
1000 bootstrap resamples (with replacement).

Usage (IDLE)
------------
    1. Place sentence_level_comet.xlsx in the same folder as this script.
    2. Open this script in IDLE.
    3. Press F5 (Run > Run Module). Output appears in the IDLE shell.

Dependencies
------------
    pip install pandas numpy openpyxl
"""

from pathlib import Path

import numpy as np
import pandas as pd

XLSX_PATH = Path.cwd() / "sentence_level_comet.xlsx"

def bootstrap_ci(scores: np.ndarray, n_resamples: int = 1000,
                 alpha: float = 0.05, rng: np.random.Generator | None = None
                 ) -> tuple[float, float, float]:
    """Return (mean, low, high) where (low, high) is the (1 - alpha) bootstrap CI."""
    if rng is None:
        rng = np.random.default_rng(seed=20260502)
    n = len(scores)
    means = np.empty(n_resamples)
    for i in range(n_resamples):
        sample = rng.choice(scores, size=n, replace=True)
        means[i] = sample.mean()
    low = np.quantile(means, alpha / 2)
    high = np.quantile(means, 1 - alpha / 2)
    return float(scores.mean()), float(low), float(high)


def main() -> None:
    if not XLSX_PATH.is_file():
        print(f"Could not find {XLSX_PATH.name} next to this script.")
        print(f"Expected location: {XLSX_PATH}")
        return

    df = pd.read_excel(XLSX_PATH)
    # Heuristic: any column whose name starts with "system_" or contains "COMET"
    # is treated as a system score column.
    score_cols = [
        c for c in df.columns
        if c.lower().startswith("system_") or "comet" in c.lower()
    ]
    if not score_cols:
        print("No score columns detected. The Excel file needs system_* "
              "or *COMET* columns.")
        return

    print(f"{'system':<24} {'mean':>8} {'95% CI low':>12} {'95% CI high':>12}")
    print("-" * 60)
    for col in score_cols:
        scores = df[col].dropna().to_numpy(dtype=float)
        mu, lo, hi = bootstrap_ci(scores)
        print(f"{col:<24} {mu:>8.3f} {lo:>12.3f} {hi:>12.3f}")


if __name__ == "__main__":
    main()
