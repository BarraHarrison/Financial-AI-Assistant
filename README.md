# Financial Assistant in Python
Python-based chatbot which helps users manage and analyze their financial portfolios.
The assistant can add, remove and display the user's portfolio.
The assistant uses the 'neuralintents' to map the user input to the the predefined JSON file.

# Challenges Faced
- The GenericAssistant class was depreciated so we had to try using the BasicAssistant class.
- The BasicAssistant class seemed to be missing the train_model method as it kept throwing errors in the terminal.
- There was also issues integrating the JSON 'assistant_intents' with the mappings function in the main Python code.
