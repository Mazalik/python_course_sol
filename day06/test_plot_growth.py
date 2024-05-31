import functions_plot_growth
import pandas as pd

#def test_read_data():
#    assert functions_plot_growth.read_data('test_a.xlsx') == False
#    assert isinstance(functions_plot_growth.read_data('test_b.xlsx'), pd.DataFrame) 

def test_calculate_real_turbidity():
    assert functions_plot_growth.calculate_real_turbidity('test_c.xlsx') == pd.read_excel('test_d.xlsx')
