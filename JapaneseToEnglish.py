import tkinter as tk
import requests
from tkinter import *
from settings_secret import *

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master.title("Translate Japanese to English (DeepL)")
        self.master.geometry('1150x400+0+0')

        self.translatedText = tk.StringVar()
        self.translatedText.set("")

        self.create_textbox()

    def create_textbox(self):
        original_textbox = tk.Frame(self.master, width=400, height=200)
        label1 = tk.Label(original_textbox, text="原文")
        entry = tk.Text(original_textbox)
        def getValue():
            tval = entry.get("1.0","end")
            items = requests.get("https://api-free.deepl.com/v2/translate", params={"auth_key": API_KEY, "source_lang": "JA", "target_lang": "EN-GB", "text": tval, }, )
            items = items.json()["translations"][0]["text"]
            self.translatedText.set(items)
            label3.delete(1.0, "end")
            label3.insert(1.0, self.translatedText.get())

        translated_textbox = tk.Frame(self.master, width=400, height=200)
        label2 = tk.Label(translated_textbox, text="translated")
        label3 = tk.Text(translated_textbox)
        button = tk.Button(original_textbox, text='翻訳', command=getValue)
        label3.insert(1.0, self.translatedText.get())
        label2.pack(pady=(20,0))
        label3.pack()
        label1.pack(pady=(20,0))
        entry.pack(expand=True)
        button.pack(pady=(5,0))
        original_textbox.pack(side=tk.LEFT, anchor=tk.N, padx=(10,5))
        translated_textbox.pack(side=tk.LEFT, anchor=tk.N, padx=(5, 10))

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()