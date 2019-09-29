# 日本語の先生

# Importing Translation Module
import goslate

# Creating A Goslate Object
translation = goslate.Goslate()

# Taking Input From User
english_text = input("Enter Your English Text: ")

# Detecting The Japanese Language Code
# print(translation.detect('日本語')): ja

# Translating English Text To Japanese
translated_text = translation.traslate(english_text, "ja")

print("Japanese Translation: ", translated_text)