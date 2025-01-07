# Financial AI Assistant in Python
from neuralintents import GenericAssistant
import matplotlib.pyplot as plt 
import pandas as pd 
import pandas_datareader as web
import mplfinance as mpf 

import pickle
import sys
import datetime as dt 

def greetings_function():
    pass

# Mappings Dictionary
mappings = {
    "greetings": greetings_function
}

assistant = GenericAssistant("assistant_intents.json", intent_methods = mappings)

assistant.train_model()
assistant.request("Hello, I want to see the latest stock prices")