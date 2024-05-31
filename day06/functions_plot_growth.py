import pandas as pd

def read_data(x):
    turbidity_data = pd.read_excel(x)

    if not all(turbidity_data.columns == ['time_hr','raw_turbidity_OD600','dilution_factor']):
        print("make sure your file is in the correct tamplate")
        return 'bad'
    else:
        return turbidity_data

def calculate_real_turbidity(turbidity_data):
    turbidity_data['turbidity_OD600'] = turbidity_data.raw_turbidity_OD600 * turbidity_data.dilution_factor
    return turbidity_data

