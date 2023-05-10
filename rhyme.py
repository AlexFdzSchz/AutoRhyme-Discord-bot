from typing import List
import re

# Class to handle rhimes
class Rhyme:
    
    def __init__(self, triggers: List[str], ignore: str, answer: str):
        self.triggers = triggers # Word ending to rhyme.
        self.ignore = ignore # Words that must NOT rhyme
        self.answer = answer # Answer

    # Check if a word rhymes.
    def rhymeswith(self, word) -> bool:
        result = False
        # Check if the word is not the last word of the answer (you can't rhime a word with the same word)
        # and if the word is not the ignored word 
        if word != self.answer.split()[-1].lower() and word != self.ignore:
            # Compare it with every trigger
            for trigger in self.triggers:
                if word.endswith(trigger):
                    result = True
        return result

    def resultrhymeswith(self, word) -> bool:
        result = False
        # Check if the word contains a mathematical operation
        if re.match(r".*[0-9]+([\+\-\*/][0-9]+)+$", word):
            # Calculate the result
            operationresult = "" + str(eval(word))
            # Compare the result with all triggers and the ignore
            for trigger in self.triggers:
                if operationresult.endswith(trigger) and not operationresult.endswith(self.ignore):
                    result = True
        return result


