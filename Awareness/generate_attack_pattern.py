from nl2ltl import translate
from nl2ltl.engines.gpt.core import GPTEngine, Models
from nl2ltl.filters.simple_filters import BasicFilter
from nl2ltl.engines.utils import pretty

engine = GPTEngine(model=Models.GPT4.value, prompt="new-prompt.json")
filter = BasicFilter()


with open("attack_description.txt", "r") as f:
    attack_description = f.read()
    utterances = attack_description.split("\n")
    for i in range(len(utterances) - 1):
        utterance = utterances[i] + ". This leads to: " + utterances[i + 1]

    print("\n", utterance)
    ltlf_formulas = translate(utterance, engine, filter)
    pretty(ltlf_formulas)
