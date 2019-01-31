#! /usr/bin/env python3

import sys
fasta = {}
sequence = ''
with open("SHH.fa") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            active_sequence_name = line[1:]
            if active_sequence_name not in fasta:
                fasta[active_sequence_name] = []
            continue
        sequence = sequence + line
fasta[active_sequence_name].append(sequence)
print(fasta)
