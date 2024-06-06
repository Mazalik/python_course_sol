# NCBI Protein Search Utility

This program allows users to search for proteins in the NCBI database, fetch data about the specified proteins, and save the search results. It also maintains a search history in a CSV file.

## Features

- Accepts user input for the search term and the number of records to retrieve.
- Searches for specified proteins in the NCBI database.
- Fetches detailed information about the found proteins.
- Saves the search history, including the search term, number of records, and the total count of results.
- Stores the fetched protein data in text files for easy access.

## Installation

To use this program, you need to install a few libraries. Use the provided `requirements.txt` file to install all necessary dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Ensure that you have the following setup in your working directory:
   - A folder named `search_downloads` where the fetched protein data will be saved.
   - An empty `search_history.csv` file to store the search history.

2. Run the program with the search term and the number of records to retrieve as command-line arguments.
   ```bash
   python script_name.py TERM NUMBER
   ```
   Replace `script_name.py` with the actual name of your Python script, `TERM` with the search term, and `NUMBER` with the number of records you want to retrieve.

3. The program will search the NCBI protein database for the specified term and fetch the specified number of records.

4. The search results and metadata will be saved in the following locations:
   - Search history: `search_history.csv`
   - Fetched protein data: `search_downloads/` directory

5. The program will also display the filenames of the saved data in the console.