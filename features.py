from forex_python.converter import CurrencyRates
from googletrans import Translator
import requests


def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    try:
        result = c.convert(from_currency, to_currency, amount)
        return f"{amount} {from_currency} is approximately {result:.2f} {to_currency}."
    except Exception as e:
        return "Sorry, I couldn't perform the conversion. Please try again."

def translate_text(text, target_language):
    translator = Translator()
    try:
        translation = translator.translate(text, dest=target_language)
        return f"The translation is: {translation.text}"
    except Exception as e:
        print(e)  # Print the error for debugging purposes
        return "Sorry, I couldn't perform the translation. Please try again."
    
# Add this function to track asteroids



