from fpdf import FPDF
import pandas

df = pandas.read_csv("articles.csv")

class Article:
    pass

class Buy:
    pass




""" Printing the dataframe without the index """
print(df.to_string(index=False))
