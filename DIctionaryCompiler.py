import os
import json

class DictOfWords:
    using System;
using System.Windows.Forms;

namespace DZ
{
    public partial class Form1 : Form
    {

        public Form1()
        {
            InitializeComponent();
            comboBox1.Items.AddRange(new string[] { "Сложение", "Вычитание", "Умножение", "Деление", "Целочисленное деление", "Остаток от деления" });
            comboBox1.SelectedIndex = 0; // Устанавливаем значение по умолчанию
        }

        private void buttonEquals_Click(object sender, EventArgs e)
        {
            try
            {
                string result = Calculator.Calculate(comboBox1.SelectedItem.ToString(), textBoxNumber1.Text, textBoxNumber2.Text).ToString();
                textBoxResult.Text = result;
            }
            catch (Exception ex)
            {
                MessageBox.Show("Ошибка: " + ex.Message);
            }
        }

        private void buttonClear_Click(object sender, EventArgs e)
        {
            textBoxNumber1.Clear();
            textBoxNumber2.Clear();
            textBoxResult.Clear();
            comboBox1.SelectedIndex = -1;
        }
    }

    // Класс калькулятора
    public class Calculator
    {
        // Метод для выполнения арифметических операций
        public static decimal Calculate(string operation, string number1Text, string number2Text)
        {
            // Удаляем пробелы из введенных чисел
            number1Text = number1Text.Replace(" ", "");
            number2Text = number2Text.Replace(" ", "");

            // Проверка наличия чисел
            if (string.IsNullOrWhiteSpace(number1Text) || string.IsNullOrWhiteSpace(number2Text))
            {
                throw new ArgumentException("Пожалуйста, введите оба числа.");
            }

            // Проверка, является ли первое число 25-значным
            if (number1Text.Length != 25)
            {
                throw new ArgumentException("Первое число должно быть 25-значным.");
            }

            // Преобразование строк в числа
            BigInt number1 = new BigInt(number1Text);
            BigInt number2 = new BigInt(number2Text);
            decimal result = 0;

            // Выбор операции и выполнение соответствующего алгоритма
            switch (operation)
            {
                case "Сложение":
                    result = number1.Add(number2);
                    break;
                case "Вычитание":
                    result = number1.Subtract(number2);
                    break;
                case "Умножение":
                    result = number1.Multiply(number2);
                    break;
                case "Деление":
                    result = number1.Divide(number2);
                    break;
                case "Целочисленное деление":
                    result = number1.IntegerDivide(number2);
                    break;
                case "Остаток от деления":
                    result = number1.Modulo(number2);
                    break;
                default:
                    throw new ArgumentException("Неизвестная операция.");
            }

            return result;
        }
    }

    // Пользовательский класс для работы с большими числами
    public class BigInt
    {
        private decimal value;

        // Конструктор класса, принимающий строку и преобразующий её в decimal
        public BigInt(string number)
        {
            if (!decimal.TryParse(number, out value))
            {
                throw new ArgumentException("Неверный формат числа");
            }
        }

        // Методы для выполнения арифметических операций
        public decimal Add(BigInt other)
        {
            return value + other.value;
        }

        public decimal Subtract(BigInt other)
        {
            return value - other.value;
        }

        public decimal Multiply(BigInt other)
        {
            return value * other.value;
        }

        public decimal Divide(BigInt other)
        {
            if (other.value == 0)
                throw new DivideByZeroException("Деление на ноль");
            return value / other.value;
        }

        public decimal IntegerDivide(BigInt other)
        {
            if (other.value == 0)
                throw new DivideByZeroException("Деление на ноль");
            return Math.Truncate(value / other.value);
        }

        public decimal Modulo(BigInt other)
        {
            if (other.value == 0)
                throw new DivideByZeroException("Деление на ноль");
            return value % other.value;
        }
    }
}


    def __init__(self):
        self.dictionary = {}
        # self.amountOfWords = 0
    
    def saveDict(self, pathToFile="dict.json"):
        '''saves dictionary to json file in specified directory'''
        with open(pathToFile, "w") as wf:
            json.dump(self.dictionary, wf)
    
    def loadDict(self, pathToFile="dict.json"):
        '''loads json dictionary from specified directory'''
        try:
            with open(pathToFile) as rf:
                stepDictionary = json.load(rf)
                self.dictionary = self.__combineDict(self.dictionary, stepDictionary)
                # self.amountOfWords = sum(self.dictionary.values())
        except: 
            print("No such file or directory")

    def eatText(self, someText:str):
        '''collects statistics from semeText'''
        someText = someText.lower()
        someText = "".join(c for c in someText if c.isalpha() or c==" ")
        wordsList = someText.split()
        stepDictionary = dict.fromkeys(wordsList, 0)
        for word in wordsList:
            stepDictionary[word] += 1
        self.dictionary = self.__combineDict(self.dictionary, stepDictionary)
        # self.amountOfWords = sum(self.dictionary.values())

    def eatFileTXT(self, pathToFile):
        '''collects statistics from .txt file in the specified directory'''
        try:
            with open(pathToFile) as file:
                someText = file.read().replace('\n', ' ')
            self.eatText(someText)
        except:
            print("No such file or directory")

    def eatDir(self, pathToDir=""):
        '''collects statistics from all .txt files in the specified directory'''
        if pathToDir != "":
            pathToDir += "/"
        listOfNames = self.__listFiles(pathToDir)
        for name in listOfNames:
            self.eatFileTXT(f"{pathToDir}{name}")
    
    def __listFiles(self, pathToDir):
        '''creates a list of all file names in a directory with a .txt extension'''
        listOfNames = []
        for file in os.listdir(pathToDir):
            if file.endswith(".txt"):
                listOfNames.append(file)
        return listOfNames

    def __combineDict(self, dict1, dict2):
        '''creates a dictionary with keys from dict1 and dict2 and sum their values'''
        for key in dict1:
            if key in dict2:
                dict1[key] += dict2[key]
                dict2.pop(key)
        dict1.update(dict2)
        return dict1

    def __repr__(self):
        return repr(self.dictionary)
     
def main():
    dict1 = DictOfWords()
    dict1.eatText("hello my dear, my pleasent DND - WORLD!")
    print(dict1.dictionary)
    # print(max(dict1.dictionary, key=dict1.dictionary.get))

if __name__ == "__main__":
    main()
