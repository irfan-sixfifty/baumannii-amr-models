# Predicting carbapenem resistance in Acinetobacter baumannii

How well does a model trained on one set of bacterial genomes predict resistance on another? This repository contains two benchmark workflows from my [Frontiers in Bioinformatics paper](https://doi.org/10.3389/fbinf.2026.1885813). I developed the computational pipeline under the mentorship of Morteza Sarmadi, PhD.

The internal modeling cohort comprised 2,448 genomes. Random forest reached an internal ROC-AUC of 0.965. On 2,500 independent genomes its ROC-AUC was 0.8392. The drop matters when interpreting performance outside the training cohort.

## Start with the external results

Run `python check_external_results.py` from a local copy. It checks cohort size and recomputes accuracy from the four confusion matrices in the published Supplementary Table S6. ROC-AUC is read from the table because recomputing it requires per-genome prediction scores.

## Read the experiments

- [Classical models](classical_benchmark.ipynb) trains random forest and logistic regression on 5,606 gene features. Follow the feature checks, five seeds, stratified folds, and saved held-out predictions.
- [Graph model](graph_benchmark.ipynb) trains a fresh graph convolutional network in each fold and assembles one prediction per genome. Follow the graph manifest checks, training loop, and fold-level comparisons.

These are selected workflows from the study's revision notebook. Notebook outputs were cleared and the original Drive mount was replaced with a relative input directory. The results check runs with standard Python. Full training requires the prepared feature matrix, labels, graphs and reference artifacts listed in each notebook, plus the Python scientific stack and PyTorch Geometric for the graph run. The paper describes data and code availability.

Source for the included aggregate results: Shaik et al., 2026, [article and supplementary materials](https://doi.org/10.3389/fbinf.2026.1885813), Supplementary Table S6.
