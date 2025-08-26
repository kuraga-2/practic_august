
import pandas as pd
import matplotlib.pyplot as plt
class PlayerStats:
    def __init__(self):
        self.df = pd.read_csv("capsule_lz/playstation_players.csv")
        
    def diagramma(self):
        self.country_counts = self.df['country'].value_counts()
        #Диаграмма
        plt.figure(figsize=(8, 8))
        plt.pie(self.country_counts, labels=self.country_counts.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
        plt.title('Количество игроков PS')
        plt.axis('equal')  
        plt.show()
    
    def __del__():
        pass

def main():
    a = PlayerStats()
    a.diagramma()
        
if __name__ == "__main__":
    main()