import pandas as pd
class DF():
    def __init__(self):
        self.name = pd.read_csv('polymorf_lz/var9.csv')

    def divide(self):
        self.filtered_df_1 = self.name[self.name['Место оплаты'] == "Брест" ]
        self.filtered_df_2 = self.name[self.name['Место оплаты'] == "Витебск" ]
        self.filtered_df_3 = self.name[self.name['Место оплаты'] == "Гомель" ]
        self.filtered_df_4 = self.name[self.name['Место оплаты'] == "Гродно" ]
        self.filtered_df_5 = self.name[self.name['Место оплаты'] == "Минск" ]
        self.filtered_df_6 = self.name[self.name['Место оплаты'] == "Могилев" ]
        

        self.filtered_df_1.to_csv('polymorf_lz/df_1.csv', index=False)
        self.filtered_df_2.to_csv('polymorf_lz/df_1.csv', index=False)
        self.filtered_df_3.to_csv('polymorf_lz/df_1.csv', index=False)
        self.filtered_df_4.to_csv('polymorf_lz/df_1.csv', index=False)
        self.filtered_df_5.to_csv('polymorf_lz/df_1.csv', index=False)
        self.filtered_df_6.to_csv('polymorf_lz/df_1.csv', index=False)


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