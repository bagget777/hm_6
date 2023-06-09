import re


class Data():
    def __init__(self, full_name, email, file_name, color):
        self.__full_name = full_name
        self.__email = email
        self.__file_name = file_name
        self.__color = color

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value


    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        self.__file_name = value


    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

with open("D:\Desktop\python_2\month_2\MOCK_DATA.txt", "r", encoding='utf-8') as file:
    content = file.read()

    full_name_list = re.findall(r"[A-Za-z'\-]+\s[A-Za-z'\-]+", content)
    print(full_name_list)

    email_list = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+", content)

    file_list = re.findall(r"[A-Z]\w+\.\w+", content)

    color_list = re.findall(r"[#]\w+", content)

fails = [Data(full_name="Nurlan uulu Beksultan", email="beka@gmail.com", file_name="beka.py", color="#046220"),
         Data(full_name="IYAsiudy", email="tguysrc@ehow.com", file_name="UtTellus.tiff", color="#e8a767"),
         Data(full_name="AKDHKAHSKD", email="Josadfasd@nyu.edu", file_name="PlateaDictumst.txt", color="#ddc1be"),
         Data(full_name="ASKDHhAKSD", email="rigonetqasd@mysql.com", file_name="DolorQuis.jpeg", color="aa422c"),
         Data(full_name="ASKHDJAHSD", email="mkillockq6@sourceforge.net", file_name="SodalesScelerisque.mov", color="#012499")]

for data in fails:
    if data.full_name in full_name_list:
        with open("D:\Desktop\python_2\month_2\FIO.txt", "w") as f:
            f.write(data.full_name)
    if data.email in email_list:
        with open("D:\Desktop\python_2\month_2\email.txt", "w") as f:
            f.write(data.email)
    if data.file_name in file_list:
        with open("D:\Desktop\python_2\month_2\philename.txt", "w") as f:
            f.write(data.file_name)
    if data.color in color_list:
        with open("D:\Desktop\python_2\month_2\color.txt", "w") as f:
            f.write(data.color)
