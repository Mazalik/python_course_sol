import functions_plot_growth
import pandas as pd

def test_read_data():
    #test using excel in the wrong tamplate:
    assert functions_plot_growth.read_data('test_a.xlsx') == False
    #test using excel in the correct tamplate:
    assert isinstance(functions_plot_growth.read_data('test_b.xlsx'), pd.DataFrame) 

def test_calculate_real_turbidity():
    #test real turbidity calculation:
    test_c = functions_plot_growth.calculate_real_turbidity(pd.read_excel('test_c.xlsx'))
    test_d = pd.read_excel('test_d.xlsx')
    assert test_c.equals(test_d)





 