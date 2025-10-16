import tkinter as tk

root = tk.Tk()
root.title("메모장 프로그램")
root.geometry("400x400")

text_area = tk.Text(root, wrap='word')
text_area.pack(expand=True, fill='both')

def save_memo():
    memo = text_area.get("1.0", tk.END)
    with open("memo.txt", "w", encoding="utf-8") as f:
        f.write(memo)

save_btn = tk.Button(root, text="저장", command=save_memo)
save_btn.pack()

root.mainloop()
