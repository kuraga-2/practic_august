import pandas as pd
class Excepts:
    def __init__(self):
        try:
            self.df = pd.read_csv('except_lz/var9.csv')
        except FileNotFoundError:
            print("Файл var9.csv отсутсвует либо назавн иначе")
        except pd.errors.EmptyDataError:
            print("Файл var9.csv пуст")
        except pd.errors.ParserError:
            print("Файл var9.csv не соответствует структуре csv")
        
    def check(self):
        self.column_names = self.df.columns.values
        self.column_example = ('Участники гражданского оборота,Тип операции,Сумма операции,Вид расчета,Место оплаты,Терминал оплаты,Дата оплаты,Время оплаты,Результат операции,Cash-back,Сумма cash-back')
        for i in range(0, len(self.column_example)):
            if self.column_example[i] != self.column_names[i]:
                print("Назвния столбцов не совпадают с ожидаемыми")
                print("Фактические название",self.column_names[i])
                print("Ожидаемые название",self.column_example[i])
                raise IndexError(f'Структура датафрейма var9.csv не соответсвует ожидаемой')
        
        
def main():   
    df = Excepts()
    df.check()


if __name__ == "__main__":
    main()