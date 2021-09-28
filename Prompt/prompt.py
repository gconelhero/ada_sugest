from .openKey import OpenKey
from .accessApi import Access
from .contentFilter import ContentFilter
from .mongo import Database
from .completion import Completion
import os, sys

class Prompt():

    def __init__(self, prompt):
        self.api_key = OpenKey().openKey()
        self.prompt = prompt #input("\nWrite to GPT-3:\n")
        self.tokens = 64 #int(input("\nHow many tokes:\n"))
        self.response = Access(self.api_key, self.prompt, self.tokens).openai()
        content_filter = ContentFilter(self.api_key, self.response).contentFilter()
        self.filter_label = content_filter[0]
        self.filter_response = content_filter[1]

    def filtered(self):
        if self.filter_label == "0" or self.filter_label == "1":
            response = Completion(self.response)
            return response.completion()

        else:
            not_sec = input("**INSECURE COMPLETION**\nCONTINUE? [Y/n]: ")
            if not_sec == "y" or not_sec == "Y":
                response = Completion(self.response)
                return response.completion()
        

    def insertMongo(self):
        try:    
            filter_insert = Database("filter")
            completion_insert = Database("completion")
            filter_insert.insert(self.prompt, self.filter_response)
            completion_insert.insert(self.prompt, self.response)
        
        except Exception as error:
            print("ERROR > ", str(error))
            raise error

def main(prompt):
    while True: 
        try:
            start_prompt = Prompt(prompt)
            completion = start_prompt.filtered()
            start_prompt.insertMongo()
            print(completion)
            return completion
        
        except Exception as error:
            print("CRASH", str(error))
            raise error

        finally:
            prompt_continue = input("\nContiue? [Y/n] ").upper()
            if prompt_continue != "Y":
                break
            else:
                pass

if __name__ == "__main__":
    main()
