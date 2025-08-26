import pandas as pd
class Oil():
    def __init__(self):
        self.Crude = pd.read_csv('crude-oil-price.csv')