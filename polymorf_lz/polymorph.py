import pandas as pd
class DF():
    def __init__(self):
        self.name = pd.read_csv('polymorf_lz/var9.csv')

    def divide(self):
        self.filtered_df_CB_true = self.name[self.name['Cash-back'] == "да" ]
        self.filtered_df_CB_false = self.name[self.name['Cash-back'] == "нет"]
        self.filtered_df_CB_true.to_csv('polymorf_lz/df_CB_true.csv', index=False)
        self.filtered_df_CB_false.to_csv('polymorf_lz/df_CB_false.csv', index=False) 


    def __invert__(self):
        self.df_no_duplicates = self.name.drop_duplicates()
        self.a = len(self.name)
        self.b = len(self.df_no_duplicates)
        self.duplicates = self.a - self.b
        print("Кол-во дубликатов - ",self.duplicates )
        self.df_no_duplicates.to_csv('polymorf_lz/df_no_duplicates.csv', index=False) 


    def __del__(self):
        print("del")

def main():
    a = DF()
    a.divide()
    ~a
        
if __name__ == "__main__":
    main()