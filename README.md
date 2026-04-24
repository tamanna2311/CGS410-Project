# Empirical Properties of DAGs in Natural Languages

[![Python Analysis](https://img.shields.io/badge/Python-3.x-blue.svg)](https://python.org)
[![Universal Dependencies](https://img.shields.io/badge/Universal-Dependencies-green.svg)](https://universaldependencies.org)

This repository serves as the official codebase and analytical pipeline for the **CGS410: Language in the Mind and Machines** course project by **Tamanna Meena (Roll No: 221119)** under Professor Himanshu Yadav. 

## 🧠 Project Objective
This project experimentally observes the structural topological bounds of organic syntactic dependencies compared against random, purely generative baseline graphs. We test human "working memory" limitations—specifically examining **Dependency Length Minimization (DLM)** structures—by isolating three core network metrics: 
1. **Tree Depth (Longest parsed paths)**
2. **Graph Density (Connectivity saturation)** 
3. **Maximal Arity (Branching out-degrees upon Central Heads)**

## 📊 Data Sources
To ensure the bounds detected are universal cognitive constants rather than language-specific quirks, the empirical pipeline dynamically parses 5,400 test sentences from typologically diverse language families sourced from exactly five Universal Dependency (`.conllu`) test treebanks:
* **English (`en_ewt`)** - Indo-European (SVO)
* **French (`fr_gsd`)** - Romance (SVO)
* **Hindi (`hi_hdtb`)** - Indo-Aryan (SOV)
* **Japanese (`ja_gsd`)** - Japonic (SOV)
* **Arabic (`ar_padt`)** - Afroasiatic (VSO)

## 🗂 Repository Structure
* `data/`: Raw `.conllu` dependency arrays tested across the evaluating language sets.
* `src/data_loader.py`: Cleans UDPipe/Universal Dependency fragments and reliably converts isolated sentences into structurally identical acyclic `networkx` graphs.
* `src/tree_generator.py`: Maps completely uniform baseline computational models mirroring strict $N$ node boundaries to generate random DAG comparisons securely drawn without evolutionary pressures.
* `src/metrics.py`: The quantitative algorithmic analyzer measuring depth limits, mean/max out-degree distributions, and overall standard edge densities.
* `main.py`: The executable pipeline orchestrating evaluation, matching geometries, building statistical DataFrames, and visualizing outputs via Seaborn architectures.

## 🚀 How to Run Locally

If you intend to test novel typological families, drop the `.conllu` banks securely in the `data/` volume and execute the environment natively:

```bash
# 1. Source the python environment securely
source venv/bin/activate
pip install -r requirements.txt

# 2. Automatically launch the pipeline orchestrator
python main.py
```
> The architecture will iteratively scale across all contained repositories returning absolute topological metrics directly in standard outputs, and generating evaluation distribution `.png` charts statically in `/results/`.

## 📈 Key Findings
Findings conclusively indicate robust architectural bounding pressures mitigating deep path extensions native to uniform structures securely. 
* Mathematical graph capacities universally penalize deep chain networks in natural speech architectures (**Human $\mu$ 5.10 < Random $\mu$ 7.88**).
* Syntactic networks overwhelmingly favor heavy central semantic roots (high arity) drastically condensing tree footprints directly contrasting with non-weighted random structures.

*See `term_paper.html` for complete methodological evaluation metrics and cognitive implications.*
