# Run this script using:
#
# python single_run.py

from spacy_llm.util import assemble

nlp = assemble("config.cfg")
doc = nlp("You look gorgeous!")
print(doc.cats)
