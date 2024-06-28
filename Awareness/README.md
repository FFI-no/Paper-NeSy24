# LLMs and ASP for situational awareness

This directory contains the code related to experiment 2
## How to run the reasoner
1. Run the telingo file:
```bash
telingo file.lp
```

## How to run the NL -> LTL converter:
1. Install the required packages 
```bash
pip install nl2ltl
```

2. Set your openAI API key
```bash 
export OPENAI_API_KEY=<your_api_key>
```

3. Run the translator
```bash
python3 generate_attack_pattern.py
```

## Citation
The implementation of `generate_attack_pattern.py` is based on code from [nl2ltl](https://github.com/IBM/nl2ltl)

>Fuggitti, Francesco, and Tathagata Chakraborti. "NL2LTL–a python package for converting natural language (NL) instructions to linear temporal logic (LTL) formulas." In Proceedings of the AAAI Conference on Artificial Intelligence, vol. 37, no. 13, pp. 16428-16430. 2023.
