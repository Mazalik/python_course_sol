import sys
from Bio import Entrez
#from datetime import datetime
#import csv
import functions_ncbi

def main():
    Entrez.email = "faratj.mazal@gmail.com"

    #get user input
    termx,number = functions_ncbi.user_input(sys.argv)

    #search for specified protein in the NCBI DB
    record, search_date = functions_ncbi.ncbi_protein_search(termx, number)

    #add search to search history in csv file
    functions_ncbi.search_history_update(search_date, termx, number, record)

    #search data fetch and save
    functions_ncbi.data_fetch(record, termx)

if __name__ == "__main__":
    main()








