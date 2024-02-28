
import pandas as pd

class DataProcess:
    def __init__(self):
        print("Access Data and Grouping")
        product = self.access()

    def access(self):
        product = pd.read_csv('../data/产品主档.xlsx')
#        ads = pd.read_csv('../data/广告')
        return product