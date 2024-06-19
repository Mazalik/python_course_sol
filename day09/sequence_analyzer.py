import functions_sequence_analyzer as fn
import sys

def main():
    filename, duplicate, frequency = fn.user_input(sys.argv)
    dna = fn.read_fasta(filename) ###from here
    print(dna)

    if duplicate == "y":
        fn.duplications(dna)
    elif duplicate == "n":
        print("Not performing duplication analysis")
    else:
        print(f"{sys.argv[2]} - Invalid input. Choose 'y' or 'n'")

    if frequency == "y":
        print(f"The bases frequencies (in [%]) are: {fn.frequency(dna)}")
    elif frequency == "n":
        print("Not performing frequency analysis")
    else:
        print(f"{sys.argv[3]} - Invalid input. Choose 'y' or 'n'")

if __name__ == "__main__":
    main()
