from typing import List
import re

# Class to handle rhymes
class Rhyme:
    
    def __init__(self, triggers: List[str], ignore: str, answer: str):
        self.triggers = triggers # Word ending to rhyme.
        self.ignore = ignore # Words that must NOT rhyme
        self.answer = answer # Answer

    # Check if a word rhymes.
    def rhymeswith(self, word) -> bool:
        result = False
        # Check if the word is not the last word of the answer (you can't rhyme a word with the same word)
        # and if the word is not the ignored word 
        if word != self.answer.split()[-1].lower() and word != self.ignore:
            # Compare it with every trigger
            for trigger in self.triggers:
                if word.endswith(trigger):
                    result = True
        return result
    
    # Check if the word contains a mathematical operation whose result rhymes
    def resultrhymeswith(self, word) -> bool:
        result = False

        # Replace all ',' to '.' to avoid compatibility errors
        word = word.replace(",", ".")

        # Check if the word contains a mathematical operation
        if re.match(r".*[0-9.]+([+\-*/][0-9.]+)+$", word):

            # Calculate the result
            operationresult = "" + str(eval(word))

            # Remove '.0' if it's a float ended with 0 
            while operationresult.endswith("0") and operationresult.__contains__("."):
                operationresult = operationresult.rstrip("0")
            if (operationresult.endswith(".")):
                operationresult = operationresult.rstrip(".")

            # Compare the result with all triggers and the ignore
            for trigger in self.triggers:
                if operationresult.endswith(trigger) and \
                    not (self.ignore != "" and operationresult.endswith(self.ignore)):
                    result = True

        return result


