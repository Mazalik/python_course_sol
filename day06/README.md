# Bacterial Growth Plotter

This program allows users to upload an Excel table containing data on time, measured turbidity, and dilution factors collected during bacterial growth in a fermentor. Using this data, the program generates a growth plot that reflects the real turbidity after accounting for the dilution factors. The resulting plot is both displayed to the user and saved for future reference.

## Features
- Upload an Excel table with time, measured turbidity, and dilution factor data.
- Calculate the real turbidity by considering the dilution factor.
- Generate and display a growth plot based on the provided data.
- Save the generated plot for future use.

## Installation
You might need to install a few libraries before using this code. You can use the requirements text file to install all necessary dependencies:

```bash
pip install -r requirements.txt
```

## Usage
1. Prepare an Excel table with the following columns:
   - Time - 'time_hr'
   - Measured Turbidity - 'raw_turbidity_OD600'
   - Dilution Factor - 'dilution_factor'
2. Run the program and upload the Excel file when prompted.
3. View the generated growth plot displayed by the program.
4. Find the saved plot in the designated directory for future reference.
