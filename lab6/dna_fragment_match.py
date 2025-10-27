def best_alignment(genome, sequence):
    seq_length = len(sequence)
    best_index = -1
    fewest_mismatches = float('inf')

    for i in range(len(genome) - seq_length + 1):
        window = genome[i:i+seq_length]
        mismatches = 0
        for j, char in enumerate(window):
            if char != sequence[j]:
                mismatches += 1
        if mismatches < fewest_mismatches:
            fewest_mismatches = mismatches
            best_index = i
    return best_index

def best_alignment_to_file(path, sequence):
    with open(path,"r") as f:
        content = f.read()
    return best_alignment(content, sequence)

