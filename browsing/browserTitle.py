from ctypes import *
import Regex
from Prompt import prompt


class BrowserTitle():
    def __init__(self):
        self.browser_title = ""
        self.window_list = []
        self.count = 0
        self.buffer = ""

    
    def handlerTitle(self):
        while True:
            hwnd = windll.user32.GetForegroundWindow()
            
            window_title = create_string_buffer(b"\x00" * 512)
            length = windll.user32.GetWindowTextA(hwnd, byref(window_title), 512)
            
            window_title = window_title.value.decode('latin-1')
            windll.kernel32.CloseHandle(hwnd)

            window_title = window_title.split(" - ")
            if window_title[-1] == 'Google Chrome':
                window_title = ' '.join(map(str, window_title[:-1]))
                title_lenght = window_title.split(" ")
                print(Regex.pidRe(window_title))
                return Regex.pidRe(window_title)


    def title(self):
        while True:            
            handler = BrowserTitle()
            if self.browser_title !=  handler.handlerTitle():
                self.browser_title = handler.handlerTitle()
                if (self.browser_title != None and 
                    self.browser_title != 'test Pesquisa Google' and 
                    self.browser_title != 'Nova guia' and 
                    self.browser_title not in self.window_list and
                    self.browser_title != 'Sem título' and
                    self.browser_title != 'Google' and
                    self.browser_title != 'Nova guia'
                    ):
                    if len(self.window_list) == 5:
                        self.window_list.pop(0)
                        self.window_list.append(self.browser_title)
                    else:
                        self.window_list.append(self.browser_title)
                if self.browser_title == 'stop Pesquisa Google':
                    return "stop"
                if self.browser_title == 'test Pesquisa Google':
                    for i in self.window_list:
                        self.count += 1
                        self.buffer += f"{str(self.count)}.{i}\n"
                    
                    self.buffer = f"""Create titles to search the web\n{self.buffer}"""
                   # print(f"\nPROMPT:::\n{self.buffer}\n\n")
                    completion = prompt.Prompt(self.buffer)
                    return completion.filtered()
                self.count = 0
                self.buffer = ""



