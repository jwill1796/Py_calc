import tkinter as tk
import math


class Calculator(tk.Tk):

    def __init__(self):
        
        super().__init__()
        self.config(bg="#2E2E2E")
        self.title('Simple Calculator')
        self.resizable(None, None)

        # Add a flag for each operator
        self.addition = False
        self.subtraction = False
        self.multiplication = False
        self.division = False
        self.equal = False

        # Create a global variable for the first number
        self.f_num = 0

        # Create a global variable for the currrent operator
        self.current_operator = 'add'
        self.last_operator = None
        self.running_total = 0
        self.equal_pressed = False

        # Add styles to the UI
        self.button_bg = '#4D4D4D'
        self.button_fg = '#FFFFFF'
        self.accent_color = '#FF5733'
        self.operator_bg = '#D3D3D3'
        self.operator_fg = '#4D4D4D'
        self.entry_bg = '#3E3E3E'
        self.entry_fg = "#FFFFFF"
        self.clicked_color = '#FF5733'
        self.equation_entry_font = ('Arial', 12)

        # Create the entry object
        self.equation_entry = tk.Entry(self, bd=5, justify='right', bg=self.entry_bg, fg=self.entry_fg,
                                       font=self.equation_entry_font)
        # Create the buttons
        num_1_btn = tk.Button(self, text="1", bg=self.button_bg, fg=self.button_fg, command=lambda: self.button_click(1))
        num_2_btn = tk.Button(self, text="2", bg=self.button_bg, fg=self.button_fg, command=lambda: self.button_click(2))
        num_3_btn = tk.Button(self, text="3", bg=self.button_bg, fg=self.button_fg, command=lambda: self.button_click(3))
        num_4_btn = tk.Button(self, text="4", bg=self.button_bg, fg=self.button_fg, command=lambda: self.button_click(4))
        num_5_btn = tk.Button(self, text="5", bg=self.button_bg, fg=self.button_fg, command=lambda: self.button_click(5))
        num_6_btn = tk.Button(self, text="6", bg=self.button_bg, fg=self.button_fg, command=lambda: self.button_click(6))
        num_7_btn = tk.Button(self, text="7", bg=self.button_bg, fg=self.button_fg, command=lambda: self.button_click(7))
        num_8_btn = tk.Button(self, text="8", bg=self.button_bg, fg=self.button_fg, command=lambda: self.button_click(8))
        num_9_btn = tk.Button(self, text="9", bg=self.button_bg, fg=self.button_fg, command=lambda: self.button_click(9))
        num_0_btn = tk.Button(self, text='0', bg=self.button_bg, fg=self.button_fg, command=lambda: self.button_click(0))

        # Create the operation buttons
        self.add_btn = tk.Button(self, text="+", bg=self.operator_bg, fg=self.operator_fg, command=lambda: self.clicked_operator('add', self.add_btn))
        self.sub_btn = tk.Button(self, text="-", bg=self.operator_bg, fg=self.operator_fg, command=lambda: self.clicked_operator('subtract', self.sub_btn))
        self.multi_btn = tk.Button(self, text="*", bg=self.operator_bg, fg=self.operator_fg, command=lambda: self.clicked_operator('multiply', self.multi_btn))
        self.div_btn = tk.Button(self, text="÷", bg=self.operator_bg, fg=self.operator_fg, command=lambda: self.clicked_operator('divide', self.div_btn))
        self.clear_btn = tk.Button(self, text="Clear", bg=self.accent_color, fg=self.button_fg, command=lambda: self.clear_entry(self.clear_btn))
        equal_btn = tk.Button(self, text="=", bg=self.operator_bg, fg=self.operator_fg, command=self.button_equal)

        # Add buttons and entry object to the screen
        opts = {'ipadx': 10, 'ipady': 10, 'sticky': 'nswe'}
        self.equation_entry.grid(row=0, column=1, columnspan=4, **opts)
        self.clear_btn.grid(row=1, column=1, columnspan=3, **opts)
        self.div_btn.grid(row=1, column=4, **opts)
        num_7_btn.grid(row=2, column=1, **opts)
        num_8_btn.grid(row=2, column=2, **opts)
        num_9_btn.grid(row=2, column=3, **opts)
        self.multi_btn.grid(row=2, column=4, **opts)
        num_4_btn.grid(row=3, column=1, **opts)
        num_5_btn.grid(row=3, column=2, **opts)
        num_6_btn.grid(row=3, column=3, **opts)
        self.sub_btn.grid(row=3, column=4, **opts)
        num_1_btn.grid(row=4, column=1, **opts)
        num_2_btn.grid(row=4, column=2, **opts)
        num_3_btn.grid(row=4, column=3, **opts)
        self.add_btn.grid(row=4, column=4, **opts)
        num_0_btn.grid(row=5, column=1, **opts)
        equal_btn.grid(row=5, column=2, columnspan=4, **opts)

        # Enter the numbers on the screen
    def button_click(self, number):
        if self.equal_pressed:
            self.equation_entry.delete(0, tk.END)
            self.equal_pressed = False
        self.equation_entry.insert(tk.END, str(number))

    def clicked_operator(self, operator, button):
        if self.current_operator:
            self.reset_operator_color()
        button.config(bg=self.clicked_color)
        self.last_operator = operator

        if operator == 'add':
            self.button_add()
        if operator == 'subtract':
            self.button_subtract()
        if operator == 'multiply':
            self.button_multiply()
        if operator == 'divide':
            self.button_divide()

    def reset_operator_color(self):
        if self.current_operator == 'add':
            self.add_btn.config(bg=self.operator_bg)
        elif self.current_operator == 'subtract':
            self.sub_btn.config(bg=self.operator_bg)
        elif self.current_operator == 'multiply':
            self.multi_btn.config(bg=self.operator_bg)
        elif self.current_operator == 'divide':
            self.div_btn.config(bg=self.operator_bg)

    def clear_entry(self, button):
        self.equation_entry.delete(0, tk.END)
        self.f_num = 0
        self.running_total = 0
        self.reset_operator_color()
        self.current_operator = 'add'
        self.clicked_operator('add', self.add_btn)

    def button_add(self):
        self.calculate_running_total()
        self.current_operator = 'add'
        self.equal_pressed = False
        self.equation_entry.delete(0,tk.END)

    def button_subtract(self):
        self.calculate_running_total()
        self.current_operator = 'subtract'
        self.equation_entry.delete(0, tk.END)

    def button_multiply(self):
        self.calculate_running_total()
        self.current_operator = 'multiply'
        self.equation_entry.delete(0, tk.END)

    def button_divide(self):
        self.calculate_running_total()
        self.current_operator = 'divide'
        self.equation_entry.delete(0, tk.END)

    def button_equal(self):
        self.equal_pressed = True
        self.calculate_running_total()
        self.equation_entry.delete(0, tk.END)
        self.equation_entry.insert(0, str(self.running_total))
        self.reset_operator_color()
        self.current_operator = None


    def calculate_running_total(self):
        current_value = self.equation_entry.get()
        if current_value == '':
            current_value = 0
        else:
            current_value = float(current_value)
        if self.current_operator == 'add':
            self.running_total += current_value
        elif self.current_operator == 'subtract':
            self.running_total -= current_value
        elif self.current_operator == 'multiply':
            self.running_total *= current_value
        elif self.current_operator == 'divide':
            if current_value != 0:
                self.running_total /= current_value
            else:
                self.running_total = 0

        else:
            self.running_total = current_value

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
