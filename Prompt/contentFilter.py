import openai

class ContentFilter():

    def  __init__(self, key, completion):
        openai.api_key = key
        self.completion = completion
        self.response = None
        self.response_flag = False
        self.response = openai.Completion.create(
                    engine="content-filter-alpha-c4",
                    prompt=f"""
                    <|endoftext|>
                    {self.completion["choices"][0]["text"]}
                    \n--\nLabel:""",
                    temperature=0,
                    max_tokens=1,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0,
                    logprobs=10
                )
    
    def contentFilter(self):
        output_label = ""
        while output_label == "":
            output_label = self.response["choices"][0]["text"]
        #output_label = self.response["choices"][0]["text"]
        toxic_threshold = -0.355

        if output_label == "2":
            logprobs = self.response["choices"][0]["logprobs"]["top_logprobs"][0]

            if logprobs["2"] < toxic_threshold:
                logprob_0 = logprobs.get("0", None)
                logprob_1 = logprobs.get("1", None)

                if logprob_0 is not None and logprob_1 is not None:
                    if logprob_0 >= logprob_1:
                        output_label = "0"
                    else:
                        output_label = "1"
                elif logprob_0 is not None:
                    output_label = "0"
                elif logprob_1 is not None:
                    output_label = "1"

        if output_label not in ["0", "1", "2"]:
            output_label = "2"

        return output_label, self.response