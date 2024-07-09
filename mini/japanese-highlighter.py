#!/usr/bin/env python
# A japanese highlighter of different japanese letter formats
import tkinter as tk

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


def main():
    root = tk.Tk()
    root.title("Japanese Text Highlighter")

    # Japanese Text Input
    text_widget = tk.Text(root, wrap=tk.WORD, font=("Arial", 14))
    text_widget.pack(expand=1, fill=tk.BOTH)

    text_widget.tag_configure("hiragana", foreground="blue")
    text_widget.tag_configure("katakana", foreground="green")
    text_widget.tag_configure("kanji", foreground="red")
    text_widget.insert(tk.END, JAPANINPUT)

    japanText = ""
    text = "what"

    def highlight_text(event):
        print("h")
        text = text_widget.get(1.0, "end-1c")
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, japanText)
        #print("f" + JAPANINPUT)

        start_index = 1.0
        for char in japanText:
            if char in hiragana:
                tag = "hiragana"
            elif char in katakana:
                tag = "katakana"
            elif char.isascii() or char.isspace():
                start_index = text_widget.index(f"{start_index} + 1 chars")
                continue
            else:
                tag = "kanji"

            end_index = text_widget.index(f"{start_index} + 1 chars")
            text_widget.tag_add(tag, start_index, end_index)
            start_index = end_index

        japanText = japanText + text[-1]
        print(japanText)
    #highlight_text(text_widget, JAPANINPUT)
    highlight_text(text_widget)
    text_widget.bind('<KeyRelease>', highlight_text)

    Instructions = tk.Text(root, height = 5, width = 52)

    # Instructions
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
