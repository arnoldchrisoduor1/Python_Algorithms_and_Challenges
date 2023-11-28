def find_it(seq):
    counts = {}

    for i in range(len(seq)):
        if seq[i] not in counts:
            counts[seq[i]] = 1
        else:
            counts[seq[i]] += 1

    for key, value in counts.items():
        if value % 2 !=0:
            return key