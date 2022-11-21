#!/usr/bin/env python3.10

import json, sys, os
from rdflib import Graph

g = Graph()

g.parse("result.rdf")
print(type(g))

for subj, pred, obj in g:
    # Check if there is at least one triple in the Graph
    print(subj,"\t",pred,"\t",obj)
    if (subj, pred, obj) not in g:
       raise Exception("It better be!")

# Print the number of "triples" in the Graph
print(f"Graph g has {len(g)} statements.")
# Prints: Graph g has 86 statements.
sys.exit()
# Print out the entire Graph in the RDF Turtle format
print(g.serialize(format="turtle"))
