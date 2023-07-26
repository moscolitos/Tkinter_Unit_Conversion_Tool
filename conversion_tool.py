# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 18:32:22 2023

@author: Mosco
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def length_conversion(from_unit, to_unit, value):
    # Conversion rates
    length_dict = {'km': 1000.0, 'm': 1.0, 'cm': 0.01, 'mm': 0.001, 
                   'mi': 1609.34, 'yd': 0.9144, 'ft': 0.3048, 'in': 0.0254}

    return (value * length_dict[from_unit]) / length_dict[to_unit]

def weight_conversion(from_unit, to_unit, value):
    # Conversion rates
    weight_dict = {'kg': 1.0, 'g': 0.001, 'lb': 0.453592, 'oz': 0.0283495}

    return (value * weight_dict[from_unit]) / weight_dict[to_unit]

def temperature_conversion(from_unit, to_unit, value):
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



def calculate():
    length_value = length_entry.get()
    weight_value = weight_entry.get()
    temp_value = temp_entry.get()

    # Check if all fields are empty
    if not length_value and not weight_value and not temp_value:
        tk.messagebox.showerror('Error', 'Please fill in at least one entry')
        return

    # Length conversion
    if length_value:
        try:
            length_value = float(length_value)
            length_result['text'] = length_conversion(length_from.get(), length_to.get(), length_value)
        except ValueError:
            tk.messagebox.showerror('Error', 'Invalid input for length conversion')

    # Weight conversion
    if weight_value:
        try:
            weight_value = float(weight_value)
            weight_result['text'] = weight_conversion(weight_from.get(), weight_to.get(), weight_value)
        except ValueError:
            tk.messagebox.showerror('Error', 'Invalid input for weight conversion')

    # Temperature conversion
    if temp_value:
        try:
            temp_value = float(temp_value)
            temp_result['text'] = temperature_conversion(temp_from.get(), temp_to.get(), temp_value)
        except ValueError:
            tk.messagebox.showerror('Error', 'Invalid input for temperature conversion')


root = tk.Tk()
root.title('Unit Conversion Tool')

# Length conversion
tk.Label(root, text='Length Conversion').grid(column=0, row=0, sticky='W')
length_options = ['km', 'm', 'cm', 'mm', 'mi', 'yd', 'ft', 'in']
length_from = ttk.Combobox(root, values=length_options)
length_from.current(0)
length_from.grid(column=0, row=1, sticky='W')
length_to = ttk.Combobox(root, values=length_options)
length_to.current(1)
length_to.grid(column=0, row=2, sticky='W')

# Weight conversion
tk.Label(root, text='Weight Conversion').grid(column=1, row=0, sticky='W')
weight_options = ['kg', 'g', 'lb', 'oz']
weight_from = ttk.Combobox(root, values=weight_options)
weight_from.current(0)
weight_from.grid(column=1, row=1, sticky='W')
weight_to = ttk.Combobox(root, values=weight_options)
weight_to.current(1)
weight_to.grid(column=1, row=2, sticky='W')

# Temperature conversion
tk.Label(root, text='Temperature Conversion').grid(column=2, row=0, sticky='W')
temp_options = ['C', 'F', 'K']
temp_from = ttk.Combobox(root, values=temp_options)
temp_from.current(0)
temp_from.grid(column=2, row=1, sticky='W')
temp_to = ttk.Combobox(root, values=temp_options)
temp_to.current(1)
temp_to.grid(column=2, row=2, sticky='W')

# Entries
length_entry = tk.Entry(root)
length_entry.grid(column=0, row=3, sticky='W')
weight_entry = tk.Entry(root)
weight_entry.grid(column=1, row=3, sticky='W')
temp_entry = tk.Entry(root)
temp_entry.grid(column=2, row=3, sticky='W')

# Result labels
length_result = tk.Label(root, text='')
length_result.grid(column=0, row=4, sticky='W')
weight_result = tk.Label(root, text='')
weight_result.grid(column=1, row=4, sticky='W')
temp_result = tk.Label(root, text='')
temp_result.grid(column=2, row=4, sticky='W')

# Calculate button
calc_button = tk.Button(root, text='Calculate', command=calculate)
calc_button.grid(column=0, row=5, sticky='W')

root.mainloop()
