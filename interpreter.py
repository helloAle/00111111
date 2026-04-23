#FEITO COM GPT

import customtkinter as ctk
from tkinter import messagebox

# ==============================
# Brainfuck Interpreter
# ==============================
class BrainfuckInterpreter:
    def __init__(self, code, input_stream=""):
        self.code = code
        self.input_stream = list(input_stream)
        self.output = ""
        self.cells = [0] * 30000
        self.ptr = 0
        self.pc = 0
        self.bracket_map = self.build_bracket_map()

    def build_bracket_map(self):
        stack = []
        bracket_map = {}
        for pos, cmd in enumerate(self.code):
            if cmd == '[':
                stack.append(pos)
            elif cmd == ']':
                start = stack.pop()
                bracket_map[start] = pos
                bracket_map[pos] = start
        return bracket_map

    def run(self):
        while self.pc < len(self.code):
            cmd = self.code[self.pc]

            if cmd == '>': self.ptr += 1
            elif cmd == '<': self.ptr -= 1
            elif cmd == '+': self.cells[self.ptr] = (self.cells[self.ptr] + 1) % 256
            elif cmd == '-': self.cells[self.ptr] = (self.cells[self.ptr] - 1) % 256
            elif cmd == '.': self.output += chr(self.cells[self.ptr])
            elif cmd == ',':
                self.cells[self.ptr] = ord(self.input_stream.pop(0)) if self.input_stream else 0
            elif cmd == '[' and self.cells[self.ptr] == 0:
                self.pc = self.bracket_map[self.pc]
            elif cmd == ']' and self.cells[self.ptr] != 0:
                self.pc = self.bracket_map[self.pc]

            self.pc += 1

        return self.output

# ==============================
# Text -> Brainfuck
# ==============================
def text_to_brainfuck(text):
    bf_code = ""
    current = 0
    for char in text:
        target = ord(char)
        diff = target - current
        bf_code += ("+" * diff) if diff > 0 else ("-" * (-diff))
        bf_code += "."
        current = target
    return bf_code

# ==============================
# Morse
# ==============================
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}
MORSE_DECODE = {v: k for k, v in MORSE_CODE.items()}

def text_to_morse(text):
    return ' '.join('/' if c==' ' else MORSE_CODE.get(c.upper(),'') for c in text if c==' ' or c.upper() in MORSE_CODE)

def morse_to_text(code):
    return ''.join(' ' if p=='/' else MORSE_DECODE.get(p,'') for p in code.split())

# ==============================
# Binary
# ==============================
def text_to_binary(text):
    return ' '.join(format(ord(c), '08b') for c in text)

def binary_to_text(binary):
    chars = []
    for b in binary.split():
        try:
            chars.append(chr(int(b, 2)))
        except:
            pass
    return ''.join(chars)

# ==============================
# App
# ==============================
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Translator Hub")
        self.geometry("500x500")
        self.minsize(400,400)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.current_frame=None
        self.show_main_menu()

    def clear_frame(self):
        if self.current_frame:
            self.current_frame.destroy()

    # MENU
    def show_main_menu(self):
        self.clear_frame()
        frame=ctk.CTkFrame(self)
        frame.grid(row=0,column=0,sticky="nsew")

        frame.grid_rowconfigure((0,1,2,3), weight=1)
        frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(frame,text="Escolha um modo",font=("Arial",20)).grid(row=0,column=0)
        ctk.CTkButton(frame,text="Morse",command=self.show_morse).grid(row=1,column=0)
        ctk.CTkButton(frame,text="Binário",command=self.show_binary).grid(row=2,column=0)
        ctk.CTkButton(frame,text="Brainfvck",command=self.show_brainfuck).grid(row=3,column=0)

        self.current_frame=frame

    # TEMPLATE SCREEN BUILDER
    def build_screen(self,title,translate_func):
        self.clear_frame()
        frame=ctk.CTkFrame(self)
        frame.grid(row=0,column=0,sticky="nsew")

        frame.grid_rowconfigure(0, weight=0)
        frame.grid_rowconfigure(1, weight=0)
        frame.grid_rowconfigure(2, weight=2)
        frame.grid_rowconfigure(3, weight=0)
        frame.grid_rowconfigure(4, weight=2)
        frame.grid_rowconfigure(5, weight=0)
        frame.grid_rowconfigure(6, weight=2)
        frame.grid_rowconfigure(7, weight=0)
        frame.grid_columnconfigure(0, weight=1)

        ctk.CTkButton(frame,text="← Voltar",command=self.show_main_menu).grid(row=0,column=0,sticky="w",padx=10)

        ctk.CTkLabel(frame,text="Texto").grid(row=1,column=0)
        text_input=ctk.CTkTextbox(frame)
        text_input.grid(row=2,column=0,sticky="nsew",padx=10)

        ctk.CTkLabel(frame,text=title).grid(row=3,column=0)
        code_input=ctk.CTkTextbox(frame)
        code_input.grid(row=4,column=0,sticky="nsew",padx=10)

        ctk.CTkLabel(frame,text="Resultado").grid(row=5,column=0)
        output=ctk.CTkTextbox(frame)
        output.grid(row=6,column=0,sticky="nsew",padx=10)

        def translate():
            t=text_input.get("1.0","end").strip()
            c=code_input.get("1.0","end").strip()
            try:
                result=translate_func(t,c)
                if result is None:
                    messagebox.showwarning("Aviso","Preencha um campo")
                    return
                output.delete("1.0","end")
                output.insert("1.0",result)
            except Exception as e:
                messagebox.showerror("Erro",str(e))

        def clear_all():
            text_input.delete("1.0","end")
            code_input.delete("1.0","end")
            output.delete("1.0","end")

        btn_frame=ctk.CTkFrame(frame)
        btn_frame.grid(row=7,column=0,pady=10,sticky="ew")
        btn_frame.grid_columnconfigure((0,1), weight=1)

        ctk.CTkButton(btn_frame,text="Traduzir",command=translate).grid(row=0,column=0,padx=5)
        ctk.CTkButton(btn_frame,text="Limpar",command=clear_all).grid(row=0,column=1,padx=5)

        self.current_frame=frame

    # MORSE SCREEN
    def show_morse(self):
        def logic(t,c):
            if t and not c:
                return text_to_morse(t)
            elif c and not t:
                return morse_to_text(c)
            elif t and c:
                return f"Texto → Morse:\n{text_to_morse(t)}\n\nMorse → Texto:\n{morse_to_text(c)}"
        self.build_screen("Morse",logic)

    # BINARY SCREEN
    def show_binary(self):
        def logic(t,c):
            if t and not c:
                return text_to_binary(t)
            elif c and not t:
                return binary_to_text(c)
            elif t and c:
                return f"Texto → Binário:\n{text_to_binary(t)}\n\nBinário → Texto:\n{binary_to_text(c)}"
        self.build_screen("Binário",logic)

    # BRAINFUCK SCREEN
    def show_brainfuck(self):
        def logic(t,c):
            if t and not c:
                return text_to_brainfuck(t)
            elif c and not t:
                return BrainfuckInterpreter(c).run()
            elif t and c:
                return f"Texto → Brainfuck:\n{text_to_brainfuck(t)}\n\nBrainfuck → Texto:\n{BrainfuckInterpreter(c).run()}"
        self.build_screen("Brainfvck",logic)

if __name__=="__main__":
    App().mainloop()
