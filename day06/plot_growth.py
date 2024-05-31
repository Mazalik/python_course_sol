import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import functions_plot_growth

def main():
    x = input("Please enter the full name of the excel file you would like to work on")

    turbidity_data = functions_plot_growth.read_data(x)
    print(turbidity_data)
    #if not turbidity_data:
    #    exit
    
    ##turbidity_data = functions_plot_growth.calculate_real_turbidity(turbidity_data)
    
    #turbidity_data['turbidity_OD600'] = turbidity_data.raw_turbidity_OD600 * turbidity_data.dilution_factor

    ##turbidity_data.plot.scatter(x='time_hr', y='turbidity_OD600')
    ##plt.savefig('growth_plot.png')
    ##plt.show()

if __name__ == "__main__":
    main()





