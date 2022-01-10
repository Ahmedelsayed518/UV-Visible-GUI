from tkinter import *
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg




class graph(Frame):
    def __init__(self, parent, contoller, root, master):
        Frame.__init__(self, parent)
        self.root = root
        self.controller = contoller
        data1 = {'Country': ['US','CA','GER','UK','FR'],
         'GDP_Per_Capita': [45000,42000,52000,49000,47000]
        }
        df1 = DataFrame(data1,columns=['Country','GDP_Per_Capita'])


        data2 = {'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
                'Unemployment_Rate': [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
                }
        df2 = DataFrame(data2,columns=['Year','Unemployment_Rate'])


        data3 = {'Interest_Rate': [5,5.5,6,5.5,5.25,6.5,7,8,7.5,8.5],
                'Stock_Index_Price': [1500,1520,1525,1523,1515,1540,1545,1560,1555,1565]
                }  
        df3 = DataFrame(data3,columns=['Interest_Rate','Stock_Index_Price'])
        figure1 = plt.Figure(figsize=(7,4))
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, master)
        bar1.get_tk_widget().grid(column=0, row=1, rowspan=20, sticky="w")
        df1 = df1[['Country','GDP_Per_Capita']].groupby('Country').sum()
        df1.plot(legend=True, ax=ax1)
        ax1.set_title('Country Vs. GDP Per Capita')