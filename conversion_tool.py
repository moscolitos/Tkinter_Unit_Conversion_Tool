# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 19:58:03 2023

@author: Mosco
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ConversionTool(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Unit Conversion Tool')

        self.conversion_fns = {
            'Length': self.length_conversion,
            'Weight': self.weight_conversion,
            'Temperature': self.temperature_conversion
        }

        self.setup_ui()

    def length_conversion(self, from_unit, to_unit, value):
        length_dict = {'km': 1000.0, 'm': 1.0, 'cm': 0.01, 'mm': 0.001, 
                       'mi': 1609.34, 'yd': 0.9144, 'ft': 0.3048, 'in': 0.0254}
        return (value * length_dict[from_unit]) / length_dict[to_unit]

    def weight_conversion(self, from_unit, to_unit, value):
        weight_dict = {'kg': 1.0, 'g': 0.001, 'lb': 0.453592, 'oz': 0.0283495}
        return (value * weight_dict[from_unit]) / weight_dict[to_unit]

    def temperature_conversion(self, from_unit, to_unit, value):
        if from_unit == 'C':
            if to_unit == 'F':
                return (value * 9/5) + 32
            elif to_unit == 'K':
                return value + 273.15
        elif from_unit == 'F':
            if to_unit == 'C':
                return (value - 32) * 5/9
            elif to_unit == 'K':
                return (value + 459.67) * 5/9
        elif from_unit == 'K':
            if to_unit == 'C':
                return value - 273.15
            elif to_unit == 'F':
                return (value * 9/5) - 459.67
        return value

    def calculate(self):
        for name, entry, result, from_, to_ in self.entries:
            value = entry.get()
            if not value:  # Skip if the entry is empty
                continue
            try:
                value = float(value)
                conversion_fn = self.conversion_fns[name]
                result['text'] = conversion_fn(from_.get(), to_.get(), value)
            except ValueError:
                tk.messagebox.showerror('Error', f'Invalid input for {name} conversion')

    def setup_ui(self):
        options = {
            'Length': ['km', 'm', 'cm', 'mm', 'mi', 'yd', 'ft', 'in'],
            'Weight': ['kg', 'g', 'lb', 'oz'],
            'Temperature': ['C', 'F', 'K']
        }

        self.entries = []

        for i, (name, option_values) in enumerate(options.items()):
            tk.Label(self, text=f'{name} Conversion').grid(column=i, row=0, sticky='W')

            from_ = ttk.Combobox(self, values=option_values)
            from_.grid(column=i, row=1, sticky='W')
            from_.current(0)

            to_ = ttk.Combobox(self, values=option_values)
            to_.grid(column=i, row=2, sticky='W')
            to_.current(1)

            entry = tk.Entry(self)
            entry.grid(column=i, row=3, sticky='W')

            result = tk.Label(self, text='')
            result.grid(column=i, row=4, sticky='W')

            self.entries.append((name, entry, result, from_, to_))

        tk.Button(self, text='Calculate', command=self.calculate).grid(column=0, row=5, sticky='W')

if __name__ == '__main__':
    app = ConversionTool()
    app.mainloop()
