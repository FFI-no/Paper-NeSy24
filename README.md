# On the use of neurosymbolic AI for defending against cyber attacks
Authors: Gudmund Grov, Jonas Halvorsen, Magnus Wiik Eckhoff, Bjørn Jervell Hansen, Martin Eian, and Vasileios Mavroeidis

Accepted by the International Conference on Neural-Symbolic Learning and Reasoning 2024 [(NeSy2024)](https://sites.google.com/view/nesy2024).

<!--- See the full paper on arxiv here [comming soon](arxiv.org) --->

<!---<img src="https://github.com/FFI-no/Paper-NeSy24/assets/145285395/22d22913-c1a2-465a-a412-5fd86afb6a7c" alt="Image of paper frontpage" width="300" height="auto">--->

## Abstract
It is generally accepted that all cyber attacks cannot be prevented, creating a need for the ability to detect and respond to cyber
attacks. Both connectionist and symbolic AI are currently being used to support such detection and response. In this paper, we make the case
for combining them using neurosymbolic AI. We identify a set of challenges when using AI today and propose a set of neurosymbolic use cases
we believe are both interesting research directions for the neurosymbolic AI community and can have an impact on the cyber security field. We
demonstrate feasibility through two proof-of-concept experiments.

## Structure
```
.
├── LTN       (experiment 1)
│   ├── Intrusion_detection.ipynb
│   ├── README.md
├── Awareness (experiment 2)
│   ├── telingo-example.py
│   ├── generate_attack_pattern.py
│   ├── README.md
└── README.md
```

## Running the provided code
Both experiments have a dedicated `README.md` with instructions on how to setup and run.

- [**Experiment 1: LTN for Knowledge-aware Intrusion Detection**](LTN)
- [**Experiment 2: LLMs and ASP for situational awareness**](Awareness)

<!--- 
## Citing this article
The paper is cited as:
> TODO

Bibtex entry:
```bib
TODO
```

--->
