import openai

class Access():
    
    def __init__(self, key, prompt, tokens):
        self.key = key
        self.prompt = prompt
        self.tokens = tokens
    
    def openai(self):
        openai.api_key = self.key
        response = openai.Completion.create(
                    engine='ada',
                    prompt=f'{self.prompt}',
                    max_tokens=self.tokens,
                    temperature=0.5,
                    top_p=1,
                    frequency_penalty=0.5,
                    stop='\n'
                    
                )
        
        return response
