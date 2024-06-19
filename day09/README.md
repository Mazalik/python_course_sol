# Sequence analyzer

This Python script performs simple analysis on DNA sequences, including duplication analysis and base frequency calculation. It reads DNA sequences from a FASTA file and allows the user to choose which analyses to perform.

## Installation

To use this program, you need to install a few libraries. Use the provided `requirements.txt` file to install all necessary dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To run the script, use the following command in the terminal:

```bash
python your_script_name.py FILENAME Duplicate(y/n) Frequency(y/n)
```

- `FILENAME`: Path to the FASTA file containing the DNA sequence.
- `Duplicate(y/n)`: Specify 'y' to perform duplication analysis or 'n' to skip it.
- `Frequency(y/n)`: Specify 'y' to perform base frequency analysis or 'n' to skip it.

## Notes
- Ensure the FASTA file does not contain any invalid characters and follows the proper format.

