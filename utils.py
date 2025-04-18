import random


def read_inputs(filepath):
    # filepath is relative to 'data' folder
    with open(f"./data/{filepath}", "r") as f:
        inputs = f.read().splitlines() 
    
    if len(inputs) == 1:
        return inputs[0]
    
    return inputs

def generate_random_dna_sequence(n):
    nucleotides = random.choices("AGTC", k=n)
    
    return "".join(nucleotides)
