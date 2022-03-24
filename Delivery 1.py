import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pdpip

### DATA IMPORT ###

Excel_file = 'Desktop/Delivery1/Data/my_shop_data.xlsx'
EmployeesSale = pd.read_excel(Excel_file, "EmployeesSale")
CategorySale = pd.read_excel(Excel_file, "CategorySale")
Top5Products = pd.read_excel(Excel_file, "Top5Products")
Top5Customers = pd.read_excel(Excel_file, "Top5Customers")


