# A Program that can convert a number to a descriptive string
# Use Case : Banking Application when amount is also written in words

from num2words import *

number = int(input("Enter A Number: "))

number_to_words_ENGLISH = num2words(number, lang="en")
number_to_words_JAPANESE = num2words(number, lang="ja")

# If there is a '-', then replacing it to a ' ' instead
result = number_to_words_ENGLISH.translate(
    {
        ord('-') : ' '
    }
)

# Making the first charater of the string to UPPERCASE
print(result.capitalize())

print(number_to_words_JAPANESE)