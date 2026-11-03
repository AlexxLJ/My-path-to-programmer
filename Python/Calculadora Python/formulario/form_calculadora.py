import tkinter as tk 
from tkinter import font
import util.util_ventana as util_ventana
from config import constantes as cons
import winsound

class FormularioCalculadora(tk.Tk):

    def __init__(self):
        super().__init__() 
        
        self.index_theme = 0
        self.current_theme = cons.LIST_THEMES[self.index_theme]
        self.config_window() 
    
        self.memory = 0.0
        self.mrc_pressed = False
        self.sound_ON = True  
        self.history = []

        self.construct_widget() 
        self.construct_music()
        self.construir_widget_toggle() 

    
    def config_window(self):
        
        self.title("Calculator SIGMA")
        self.configure(bg=self.current_theme["bg"]) 
        self.geometry("360x480")
        self.resizable(True, True)  
        util_ventana.centrar_ventana(self, 360, 480)

        for col in range(6):
            self.columnconfigure(col, weight=1, minsize=50)

        for col in [2, 3, 4]:
            self.columnconfigure(col, uniform="num_cols")

        self.grid_rowconfigure(0, weight=1, minsize=35)   
        self.grid_rowconfigure(1, weight=1, minsize=50)   
        
        for row in range(2, 7):
            self.grid_rowconfigure(row, weight=1, minsize=60)

    
    def construct_widget(self):
        
        self.operation_label = tk.Label(
            self, 
            text="", 
            font=('Arial', 16), 
            fg=self.current_theme["textarea"], 
            bg=self.current_theme["bg"], 
            justify='right',
            bd=6,
            relief="sunken",
            cursor="hand2"
            ) 

        self.operation_label.grid(row=0, column=3, columnspan=3, sticky="nsew", padx=10, pady=10)

        
        self.operation_label.bind("<Button-1>", self.show_history)
        
        
        self.entry = tk.Entry(
            self, 
            width=12, 
            font=('Arial', 40), 
            bd=1, 
            fg=self.current_theme["textarea"], 
            bg=self.current_theme["input_area"], 
            justify='right')

        self.entry.grid(row=1, column=0, columnspan=6, sticky="nsew", padx=10, pady=10 )  
        
        buttons = [
            ["%", "()", "MRC", "M-", "M+", "÷"],
            ["+/-", "7", "8", "9", "×"],
            ["➪", "4", "5", "6", "-"],
            ["C·CE", "1", "2", "3", "+"],
            ["0", "00", ".", "="]
        ]
        
        self.botones_creados = []

        for i, fila in enumerate(buttons):

            col_actual= 0

            for texto in fila:
               
                if texto == "C·CE":
                    bg = self.current_theme["SPECIAL_BUTTON"]
                    fg = self.current_theme["textarea"]

                elif texto in ["%", "()", "MRC", "M-", "M+", "÷", "×", "-", "+", "="]:
                    bg = self.current_theme["BUTTON_area"] 
                    fg = self.current_theme["textarea"]
                else:
                    bg = self.current_theme["Numbers"]
                    fg = self.current_theme["textarea"]

                
                ancho = 2 if texto in ["+/-", "➪", "C·CE", "0", "="] else 1

             
                if texto.isdigit() or texto in ["00"]:
                    fuente = ("Arial", 28)  
                else:
                    fuente = ("Arial", 14)
                
                btn = tk.Button(
                    self,
                    text=texto,
                    bg=bg,
                    fg=fg,
                    font=fuente,
                    command=lambda v=texto: self.on_button_click(v)
                )
                                 

                btn.grid(
                    row=2 + i,
                    column=col_actual,
                    columnspan=ancho,
                    sticky="nsew",
                    padx=4,
                    pady=4
                )

                self.botones_creados.append((btn, texto))

                col_actual += ancho


    def construir_widget_toggle(self):
            
            
            font_awesome = font.Font(family='FontAwesome', size=12)
           
            self.theme_button = tk.Button(self, text=f"Tema {self.index_theme}\uf186", width=13, font=font_awesome,  bd=0, borderwidth=0,
                                          highlightthickness=0, relief=tk.FLAT, command=self.toggle_theme, bg=self.current_theme["BUTTON_area"],fg=self.current_theme["textarea"])
            self.theme_button.grid(row=0, column=1, columnspan=2,
                                   pady=0, padx=0, sticky="nw")  
            

    def toggle_theme(self):
           
                self.index_theme = (self.index_theme + 1) % len(cons.LIST_THEMES)
                self.current_theme = cons.LIST_THEMES[self.index_theme]
    
                self.configure(bg=self.current_theme["bg"])
                self.entry.config(fg=self.current_theme["textarea"],
                                  bg=self.current_theme["input_area"])
                self.operation_label.config(
                    fg=self.current_theme["textarea"], bg=self.current_theme["bg"])
                self.theme_button.configure(
                    text=f"Tema {self.index_theme} \uf186", 
                    bg=self.current_theme["BUTTON_area"],
                    fg=self.current_theme["textarea"])
               
                self.theme_button.configure(
                    text=f"Tema {self.index_theme} \uf186", 
                    bg=self.current_theme["BUTTON_area"],
                    fg=self.current_theme["textarea"]
                )

                self.frame_brand.configure(bg=self.current_theme["bg"])
                self.lbl_sigma.configure(fg=self.current_theme["textarea"], bg=self.current_theme["bg"])
                self.lbl_sound_on.configure(bg=self.current_theme["bg"])
                if self.sound_ON:
                    self.lbl_sound_on.configure(fg=self.current_theme["ON_color"])

                for btn, texto in self.botones_creados:
                    if texto == "C·CE":
                        bg = self.current_theme["SPECIAL_BUTTON"]
                    elif texto in ["%", "()", "MRC", "M-", "M+", "÷", "×", "-", "+", "="]:
                        bg = self.current_theme["BUTTON_area"] 
                    else:
                        bg = self.current_theme["Numbers"]
            
                    btn.configure(bg=bg, fg=self.current_theme["textarea"])
                    

    def on_button_click(self, value):

        if self.sound_ON:
            winsound.Beep(440, 50);

        if value == "M+":
            try:
                numero = float(self.entry.get())
                self.memory += numero
            except:
                pass
            return
        
        if value == "M-":
            try:
                numero = float(self.entry.get())
                self.memory -= numero
            except:
                pass
            return
        
       
        if value == "MRC":
                if self.mrc_pressed:
                    self.memory = 0.0
                    self.mrc_pressed = False
                    self.operation_label.config(text="Memoria borrada")
                else:
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, str(self.memory))
                    self.mrc_pressed = True
                return
        
        if value == "()":
            texto = self.entry.get()

            abiertos = texto.count("(")
            cerrados = texto.count(")")

            if abiertos > cerrados:
                self.entry.insert(tk.END, ")")
            else:
                self.entry.insert(tk.END, "(")
            return

        if value == "+/-":
            texto = self.entry.get()

            if not texto:
                return

            try:
                numero = float(texto)
                numero = -numero
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(numero))
                return
            except:
                pass

        
            operators = ["+", "-", "×", "÷"]
            pos = -1
            for op in operators:
                p = texto.rfind(op)
                if p > pos:
                    pos = p

            if pos == -1:
                return

            inicio = texto[:pos+1]
            ultimo = texto[pos+1:]

            try:
                numero = float(ultimo)
                numero = -numero
                nuevo = inicio + str(numero)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, nuevo)
            except:
                pass

            return

        if value == '=':

            texto = self.entry.get()
                

            if hasattr(self, "last_operator") and self.last_operator is not None:
                self.operation_label.config(text="")
                if self.last_operator == '+':
                    self.last_result += self.last_number
                elif self.last_operator == '-':
                    self.last_result -= self.last_number
                elif self.last_operator == '*':
                    self.last_result *= self.last_number
                elif self.last_operator == '/':
                    self.last_result /= self.last_number

                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(self.last_result))
                return

           
            try:
                exp_original = texto
                expression = texto.replace('%', '/100') 
                expression = expression.replace('×', '*').replace('÷', '/') 

                result = eval(expression) 

               
                operators_eval = ["+", "-", "*", "/"]
                pos = -1
                for op in operators_eval:
                    p = expression.rfind(op)
                    if p > pos:
                        pos = p

                if pos != -1:
                    self.last_operator = expression[pos]
                    self.last_number = float(expression[pos+1:])
                else:
                    self.last_operator = None
                    self.last_number = None

                self.last_result = result

                self.entry.delete(0, tk.END) 
                self.entry.insert(tk.END, str(result)) 
               
                operation = expression + " " + value
                self.operation_label.config(text=operation)

                
                operacion_completa = f"{exp_original} = {result}"
                self.history.append(operacion_completa)
            except Exception as e:
                self.entry.delete(0, tk.END) 
                self.entry.insert(tk.END, "Error")
                self.operation_label.config(text="") 

        elif value == 'C·CE':
            self.entry.delete(0, tk.END)
            self.operation_label.config(text="")
            self.last_operator = None
            self.last_number = None
            self.last_result = None
        
        elif value == '➪':
            current_text = self.entry.get()
            if current_text:
                new_text = current_text[:-1]  
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, new_text)
               
                self.operation_label.config(text=new_text + " ")
        else:
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_text + value)
            
            if value == '=':
                self.operation_label.config(text="")

       
    def construct_music(self):
        
        self.frame_brand = tk.Frame(self, bg=self.current_theme["bg"], cursor="hand2")
        self.frame_brand.grid(row=0, column=0, columnspan=3, sticky="w", padx=10, pady=2)

        
        self.lbl_sound_on = tk.Label(
            self.frame_brand,
            text="ON",
            font=('Arial', 7, 'bold'),
            fg=self.current_theme["ON_color"], 
            bg=self.current_theme["bg"]
        )
        self.lbl_sound_on.pack(anchor="w", padx=2)

        
        self.lbl_sigma = tk.Label(
            self.frame_brand,
            text="SIGMA",
            font=('Arial', 14, 'bold'),
            fg=self.current_theme["textarea"],
            bg=self.current_theme["bg"]
        )
        self.lbl_sigma.pack(anchor="w")

        
        self.frame_brand.bind("<Button-1>", lambda e: self.toggle_sonido())
        self.lbl_sound_on.bind("<Button-1>", lambda e: self.toggle_sonido())
        self.lbl_sigma.bind("<Button-1>", lambda e: self.toggle_sonido())


    def toggle_sonido(self):
        """ Activa/Desactiva el sonido al hacer clic sobre SIGMA """
        self.sound_ON = not self.sound_ON
        if self.sound_ON:
            self.lbl_sound_on.config(text="ON", fg=self.current_theme["ON_color"])
            self.bell()  
        else:
            self.lbl_sound_on.config(text="", fg=self.current_theme["bg"])


    def show_history(self, event=None):
            """ Abre una ventana emergente que muestra la lista de operaciones realizadas """
            history_window = tk.Toplevel(self)
            history_window.title("Operation History")
            history_window.geometry("300x400")
            history_window.configure(bg=self.current_theme["bg"])

            
            lbl_titulo = tk.Label(
                history_window, 
                text="📜 History", 
                font=('Arial', 14, 'bold'),
                fg=self.current_theme["textarea"],
                bg=self.current_theme["bg"]
            )
            lbl_titulo.pack(pady=10)

            frame_lista = tk.Frame(history_window, bg=self.current_theme["bg"])
            frame_lista.pack(fill="both", expand=True, padx=15, pady=5)

            scrollbar = tk.Scrollbar(frame_lista)
            scrollbar.pack(side="right", fill="y")

            history_list = tk.Listbox(
                frame_lista,
                font=('Arial', 12),
                bg=self.current_theme["input_area"],
                fg=self.current_theme["textarea"],
                bd=0,
                yscrollcommand=scrollbar.set
            )
            history_list.pack(side="left", fill="both", expand=True)
            scrollbar.config(command= history_list.yview)

            if not self.history:
                history_list.insert(tk.END, " Sin operaciones aún.")
            else:
                for item in self.history:
                    history_list.insert(tk.END, f"  {item}")

            def clear_history():
                self.history.clear()
                history_list.delete(0, tk.END)
                history_list.insert(tk.END, " Deleted History.")

            btn_clear = tk.Button(
                history_window,
                text="Clear History",
                bg=self.current_theme["bg"], 
                fg=self.current_theme["SPECIAL_BUTTON"],
                font=('Arial', 10, 'bold'),
                command=clear_history
            )
            btn_clear.pack(pady=10)    

    
