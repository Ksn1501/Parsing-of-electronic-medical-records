#"внедрение "программной библиотеки на языке Python для обработки и анализа данных
import os 
from pandas import *
from pprint import pprint #"красиво печатать" произвольные структуры данных на Python


class Predstavlenie:

    def init(self):
        self.df = self.open_file()
        self.structured_dict = {}
        self.receiving_part_of_the_patient()

#начало работы (открытие файла) 
    def open_file(self):
        file_path = os.path.abspath("..") + "\\honor\\proba\\med_recs_depers.pkl" #универсальный путь к нужному файлу
        dataframe = read_pickle(file_path)
        return dataframe
# = self.df["Статус"].ne('ПРЕДСТАВЛЕНИЕ О БОЛЬНОМ').idxmax()
#поиск нужной информации 
    def receiving_part_of_the_patient(self):
        #df.A.searchsorted('a', side='right')
        k = 0
        while True:
            n = self.df["Статус"].iloc[k]
            if n != "ПРЕДСТАВЛЕНИЕ О БОЛЬНОМ":
                k += 1
            else:
                break
        count = k
        g = k
        while True:
            n = self.df["Статус"].iloc[count]
            if n == "ПРЕДСТАВЛЕНИЕ О БОЛЬНОМ":
                self.structured(counter=g)
                count += 1
                g += 1
            else:
                break
        pprint(self.structured_dict)
        return self.structured_dict
    
#обработка и внесение нужной информации
    def structured(self, counter):
        if self.df["patient_ID"].iloc[counter] not in self.structured_dict.keys():
            self.structured_dict[self.df["patient_ID"].iloc[counter]] = {
                "Общее состояние": None,
                "Вес": None,
                "Рост": None,
                "Индекс массы тела": None,
                "Площадь поверхности тела": None,
                "Пищеварительная система": None,
                "Представление о больном (ост)": None
            }
            if "ОБЪЕКТИВНЫЙ ОСМОТР" in self.df["Данные"].iloc[counter]:
                
                if "Общее состояние" in self.df["Данные"].iloc[counter]:
                    self.structured_dict[self.df["patient_ID"].iloc[counter]]["Общее состояние"] = self.df["Данные"].iloc[counter]
                elif "Вес" in self.df["Данные"].iloc[counter]:
                    self.structured_dict[self.df["patient_ID"].iloc[counter]]["Вес"] = self.df["Данные"].iloc[counter]
                elif "Рост" in self.df["Данные"].iloc[counter]:
                    self.structured_dict[self.df["patient_ID"].iloc[counter]]["Рост"] = self.df["Данные"].iloc[counter]
                elif "индекс массы тела" in self.df["Данные"].iloc[counter]:
                    self.structured_dict[self.df["patient_ID"].iloc[counter]]["Индекс массы тела"] = self.df["Данные"].iloc[counter]
                elif "площадь поверхности тела" in self.df["Данные"].iloc[counter]:
                    self.structured_dict[self.df["patient_ID"].iloc[counter]]["Площадь поверхности тела"] = self.df["Данные"].iloc[counter]
                elif "Пищеварительная система" in self.df["Данные"].iloc[counter]:
                    self.structured_dict[self.df["patient_ID"].iloc[counter]]["Пищеварительная система"] = self.df["Данные"].iloc[counter]
                else:
                    self.structured_dict[self.df["patient_ID"].iloc[counter]]["Представление о больном (ост)"] = self.df["Данные"].iloc[counter]
            else:
                self.structured_dict[self.df["patient_ID"].iloc[counter]]["Представление о больном (ост)"] = self.df["Данные"].iloc[counter]
                  
        else:
            
            if "ОБЪЕКТИВНЫЙ ОСМОТР" in self.df["Данные"].iloc[counter]:
                if "Общее состояние" in self.df["Данные"].iloc[counter]:
                    self.structured_dict[self.df["patient_ID"].iloc[counter]]["Общее состояние"] = self.df["Данные"].iloc[counter]
                elif "Вес" in self.df["Данные"].iloc[counter]:
                    self.structured_dict[self.df["patient_ID"].iloc[counter]]["Вес"] = self.df["Данные"].iloc[counter]
                elif "Рост" in self.df["Данные"].iloc[counter]:
                    self.structured_dict[self.df["patient_ID"].iloc[counter]]["Рост"] = self.df["Данные"].iloc[counter]
                elif "индекс массы тела" in self.df["Данные"].iloc[counter]:
                    self.structured_dict[self.df["patient_ID"].iloc[counter]]["Индекс массы тела"] = self.df["Данные"].iloc[counter]
                elif "площадь поверхности тела" in self.df["Данные"].iloc[counter]:
                    self.structured_dict[self.df["patient_ID"].iloc[counter]]["Площадь поверхности тела"] = self.df["Данные"].iloc[counter]
                elif "Пищеварительная система" in self.df["Данные"].iloc[counter]:
                    self.structured_dict[self.df["patient_ID"].iloc[counter]]["Пищеварительная система"] = self.df["Данные"].iloc[counter]
                else:
                    self.structured_dict[self.df["patient_ID"].iloc[counter]]["Представление о больном (ост)"] = self.df["Данные"].iloc[counter]
            else:
               self.structured_dict[self.df["patient_ID"].iloc[counter]]["Представление о больном (ост)"] = self.df["Данные"].iloc[counter]


test = Predstavlenie()
"""
Проблема с счетчиком, отвечающим за индексацию
Понятно, что нужно считывать массив в поле Данные, опираясь на показатель ОБЪЕКТИВНЫЙ ОСМОТР по большей части, после него 
идёт несколько ключевых маркеров, например, Вес, Рост, Пищеварительная система и т.д.
Однако цикл, который отвечает за соответсвие поля Статус, т.к. почему-то некорректно считываются строки и, соответственно, 
нет возможности узнать конкретное значение индекса первого вхождения статуса ПРЕДСТАВЛЕНИЕ О БОЛЬНОМ,
выходит за рамки нужной строки и не читает те самые маркеры в заданную аннотацию поля ID пациента 
Если есть возможнсть получить комментарий касательно ошибки и переделать код, работу с блоком представления удастся завершить
Сейчас файл отправляется в таком виде
"""