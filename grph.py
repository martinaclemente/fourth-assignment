def parse_fasta(fasta_strings):
    sequences = {}
    label = None
    for line in fasta_strings.strip().split("\n"):
        if line.startswith(">"):
            label = line[1:].strip()
            sequences[label] = ""
        else:
            sequences[label] += line.strip()
    return sequences

def build_overlap_graph(sequences, k):
    adjacency_list = []
    labels = list(sequences.keys())
    for i in range(len(labels)):
        for j in range(len(labels)):
            if i != j:
                s, t = sequences[labels[i]], sequences[labels[j]]
                if s[-k:] == t[:k]:
                    adjacency_list.append((labels[i], labels[j]))
    return adjacency_list

def main(file_name, k=3):
    with open(file_name, 'r') as f:
        fasta_input = f.read()
   
    sequences = parse_fasta(fasta_input)
    adjacency_list = build_overlap_graph(sequences, k)
    for edge in adjacency_list:
        print(f"{edge[0]} {edge[1]}")

file_name = "rosalind_grph.txt"
main(file_name)
