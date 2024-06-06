from Bio import Entrez
from datetime import datetime
import csv

#get user input
def user_input(sys_argv):
    if len(sys_argv) != 3:
        exit(f"The correct usage is: {sys_argv[0]} TERM NUMBER")
    termx = sys_argv[1]
    number = sys_argv[2]
    return(termx, number)

#search for specified protein in the NCBI DB
def ncbi_protein_search(termx, number):
    handle = Entrez.esearch(db="protein", term=termx, idtype="acc", retmax=number)
    record = Entrez.read(handle)
    handle.close()
    search_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return(record, search_date)

#add search to search history in csv file
def search_history_update(search_date, termx, number, record):
    csv_file = "search_history.csv"
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([search_date, termx, number, record["Count"]])

#search data fetch and save
def data_fetch(record, termx):
        for id in record["IdList"]:
            fetch_handle = Entrez.efetch(db="protein", id=record["IdList"], rettype="gb", retmode="text")
            protein_info = fetch_handle.read()
            file_name = f"search_downloads/{termx}_{id}.txt"
            print(f"The file: {termx}_{id}.txt was created and saved in search_downloads folder")
            with open(file_name, "w") as file:
                file.write(protein_info)
        fetch_handle.close()

