class Completion():

    def __init__(self, response):
        self.response = response

    def completion(self):
        completion = self.response["choices"][0]["text"].encode()
        return f"{completion.decode()}"

