"""Check the published external confusion matrices with Python's standard library."""
import csv
from math import isclose
from pathlib import Path

with Path(__file__).with_name("external_validation.csv").open(encoding="utf-8-sig") as table:
    for row in csv.DictReader(table):
        tn, fp, fn, tp = (int(row[key]) for key in ("TN", "FP", "FN", "TP"))
        total = tn + fp + fn + tp
        accuracy = (tn + tp) / total
        assert total == int(row["N_external"])
        assert isclose(accuracy, float(row["Accuracy"]), abs_tol=0.0001)
        print(f"{row['Model']:20} {total} genomes | accuracy {accuracy:.4f} | reported ROC-AUC {row['ROC-AUC']}")
