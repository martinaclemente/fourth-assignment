import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

def read_fasta(file_name):
    sequences = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        current_seq = ""
        for line in lines:
            line = line.strip()
            if line.startswith(">"): 
                if current_seq:
                    sequences.append(current_seq)
                current_seq = ""
            else:
                current_seq += line
        if current_seq:
            sequences.append(current_seq)
    return sequences

def overlap(s1, s2):
    max_overlap = 0
    merged_string = s1 + s2 
    for i in range(1, len(s1)):
        if s1[-i:] == s2[:i]: 
            max_overlap = i
            merged_string = s1 + s2[i:]
    
    return max_overlap, merged_string

def shortest_superstring(sequences):
    while len(sequences) > 1:
        max_overlap = -1
        merge_a, merge_b = None, None
        merged_result = None
        
        for i in range(len(sequences)):
            for j in range(len(sequences)):
                if i != j:
                    ov_length, merged = overlap(sequences[i], sequences[j])
                    if ov_length > max_overlap:
                        max_overlap = ov_length
                        merge_a, merge_b = i, j
                        merged_result = merged
        
        sequences.pop(max(merge_a, merge_b))
        sequences.pop(min(merge_a, merge_b))
        sequences.append(merged_result)
    
    return sequences[0]

def main(file_name):
    sequences = read_fasta(file_name)
    result = shortest_superstring(sequences)
    print(result)

file_name = "rosalind_long.txt" 
if __name__ == "__main__":
    main(file_name)
