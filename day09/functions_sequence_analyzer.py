import re

def user_input(sys_argv):
    if len(sys_argv) != 4:
        exit(f"The correct usage is: {sys_argv[0]} FILENAME Duplicate(y/n) Frequency(y/n)")
    filename = sys_argv[1]
    duplicate = sys_argv[2] #"y" or "n"
    frequency = sys_argv[3] #"y" or "n"
    return(filename, duplicate, frequency)

def read_fasta(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        sequence = ''
        for line in lines:
            if not line.startswith('>'):
                sequence += line.strip()  
    return sequence

def duplications(dna):
    match = re.search(r"([GATC]+).*\1", dna)
    if match:
        print(match.group(1))
    length = 1
    result = ''
    while True:
        regex = r'([GATC]{' + str(length) + r'}).*\1'
        m = re.search(regex, dna)
        if m:
            result = m.group(1)
            length += 1
        else:
            break
    print(result)
    print(len(result))
    return result

def frequency(dna):
    base_counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    dna = dna.upper()
    for base in dna:
        base_counts[base] += 1
    total_bases = len(dna) 
    base_frequencies = {}
    if total_bases != 0: #avoid division by zero
        for base in base_counts:
            frequency_percentage = (base_counts[base] / total_bases) * 100
            base_frequencies[base] = round(frequency_percentage, 2)
        return base_frequencies
    else:
        return {'A': 0, 'T': 0, 'G': 0, 'C': 0}
