#!/usr/bin/env python
# A japanese highlighter of different japanese letter formats
import tkinter as tk
import os

JAPANINPUT = "失せろ、くそオーストラリア人め。誰が貴様を払うかよ　(⁠-⁠_⁠-⁠メ⁠)"

hiragana = set([
    "あ", "い", "う", "え", "お",
    "か", "き", "く", "け", "こ",
    "さ", "し", "す", "せ", "そ",
    "た", "ち", "つ", "て", "と",
    "な", "に", "ぬ", "ね", "の",
    "は", "ひ", "ふ", "へ", "ほ",
    "ま", "み", "む", "め", "も",
    "や", "ゆ", "よ",
    "ら", "り", "る", "れ", "ろ",
    "わ", "を", "ん"
])

katakana = set([
    "ア", "イ", "ウ", "エ", "オ",
    "カ", "キ", "ク", "ケ", "コ",
    "サ", "シ", "ス", "セ", "ソ",
    "タ", "チ", "ツ", "テ", "ト",
    "ナ", "ニ", "ヌ", "ネ", "ノ",
    "ハ", "ヒ", "フ", "ヘ", "ホ",
    "マ", "ミ", "ム", "メ", "モ",
    "ヤ", "ユ", "ヨ",
    "ラ", "リ", "ル", "レ", "ロ",
    "ワ", "ヲ", "ン"
])

numberOfData = {
    "kanji": 0,
    "hiragana": 0,
    "katakana": 0,
    "other": 0
}

def Rounder(number, total):
    return f"{round((number / total) * 100)}%"

def main():
    root = tk.Tk()
    root.title("Japanese Text Highlighter")
    #root.geometry('650x650')
    #root.iconbitmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), "japanese-highlighter-logo.ico"))

    # Japanese Text Input
    textInput = tk.Text(root, wrap=tk.WORD, font=("Arial", 12), height = 5, width = 52)
    textInput.insert(tk.END, JAPANINPUT)
    textInput.pack()

    # Japanese Text Highlight
    textHighlight = tk.Text(root, wrap=tk.WORD, font=("Arial", 14), height=10, width = 52)
    textHighlight.tag_configure("hiragana", foreground="blue")
    textHighlight.tag_configure("katakana", foreground="green")
    textHighlight.tag_configure("kanji", foreground="red")
    #buttonInput = tk.Button(root, text="Enter", command=highlight_text(textHighlight, textInput.get(1.0, "end-1c")))

    def highlight_text():
        numberOfData = {
            "kanji": 0,
            "hiragana": 0,
            "katakana": 0,
            "other": 0,
            "total": 0,
        }
        text = textInput.get(1.0, "end-1c")
        textHighlight.delete(1.0, tk.END)
        textHighlight.insert(tk.END, text)
        print("Highlighting...")

        start_index = 1.0
        for char in text:
            if char in hiragana:
                tag = "hiragana"
                numberOfData["hiragana"] = numberOfData["hiragana"] + 1
                numberOfData["total"] = numberOfData["total"] + 1
            elif char in katakana:
                tag = "katakana"
                numberOfData["katakana"] = numberOfData["katakana"] + 1
                numberOfData["total"] = numberOfData["total"] + 1
            elif char.isascii() or char.isspace():
                start_index = textHighlight.index(f"{start_index} + 1 chars")
                numberOfData["other"] = numberOfData["other"] + 1
                numberOfData["total"] = numberOfData["total"] + 1
                continue
            else:
                tag = "kanji"
                numberOfData["kanji"] = numberOfData["kanji"] + 1
                numberOfData["total"] = numberOfData["total"] + 1

            end_index = textHighlight.index(f"{start_index} + 1 chars")
            textHighlight.tag_add(tag, start_index, end_index)
            start_index = end_index
        print(numberOfData)

        total = numberOfData["total"]
        kanjiLabel.config(text=f"Kanji: {Rounder(numberOfData['kanji'], total)}")
        hiraganaLabel.config(text=f"Hiragana: {Rounder(numberOfData['hiragana'], total)}")
        katakanaLabel.config(text=f"Katakana: {Rounder(numberOfData['katakana'], total)}")
        otherLabel.config(text=f"Other: {Rounder(numberOfData['other'], total)}")
        
    buttonInput = tk.Button(root, text="Highlight!", command=highlight_text)
    buttonInput.pack()
    textHighlight.pack(expand=1, fill=tk.BOTH)
    kanjiLabel = tk.Label(root, text = f"Kanji: {numberOfData['kanji']}")
    kanjiLabel.pack()
    hiraganaLabel = tk.Label(root, text = f"Hiragana: {numberOfData['hiragana']}")
    hiraganaLabel.pack()
    katakanaLabel = tk.Label(root, text = f"Katakana: {numberOfData['katakana']}")
    katakanaLabel.pack()
    otherLabel = tk.Label(root, text = f"Other: {numberOfData['other']}")
    otherLabel.pack()

    # Instructions
    Instructions = tk.Text(root, height = 5, width = 52)
    l = tk.Label(root, text = "Instructions")
    l.config(font =("Courier", 14), )

    instructionsText = """Red is for kanji
Blue is for hiragana
Green is for Katakana"""

    l.pack()
    Instructions.pack()

    Instructions.insert(tk.END, instructionsText)
    Instructions.config(state=tk.DISABLED)

    root.mainloop()

if __name__ == "__main__":
    main()
