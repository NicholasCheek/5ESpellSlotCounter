#!/usr/bin/env python
"""D20 Spell Slot Counter keeps track of spell slots for casters."""

# counter.py
# D20 Spell Slot Counter v 1.0.0
# Nicholas Cheek

# Copyright (C) 2020  Nicholas Cheek.
#
# This program is free software: you can redistibute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Imports
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("500x500")
window.title("Spell Slot Counter")

class_label = tk.Label(window, text="Class")
class_label.grid(column=0, row=0)

class_combo = ttk.Combobox(window, values=["Sorcerer", "Wizard"])
class_combo.grid(column=1, row=0)
class_combo.current(1)

level_label = tk.Label(window, text="Level")
level_label.grid(column=0, row=1)

level_combo = ttk.Combobox(
    window,
    # List 1-20
    values=list(range(1, 21)),
)
level_combo.grid(column=1, row=1)
level_combo.current(19)


def clicked():
    current_class = class_combo.get()
    current_level = level_combo.get()
    spell_window = tk.Toplevel(window)
    spell_window.geometry("500x500")
    top_label = tk.Label(
        spell_window, text=f"{current_class} level {current_level}"
    )
    top_label.grid(column=0, row=0)

    max_slots = []

    if current_class == "Wizard" or current_class == "Sorcerer":
        if current_level == "20":
            max_slots = [4, 3, 3, 3, 3, 2, 2, 1, 1]
        elif current_level == "19":
            max_slots = [4, 3, 3, 3, 3, 2, 1, 1, 1]
        elif current_level == "18":
            max_slots = [4, 3, 3, 3, 3, 1, 1, 1, 1]
        elif current_level == "17":
            max_slots = [4, 3, 3, 3, 2, 1, 1, 1, 1]
        elif current_level == "16":
            max_slots = [4, 3, 3, 3, 2, 1, 1, 1, 0]
        elif current_level == "15":
            max_slots = [4, 3, 3, 3, 2, 1, 1, 1, 0]
        elif current_level == "14":
            max_slots = [4, 3, 3, 3, 2, 1, 1, 0, 0]
        elif current_level == "13":
            max_slots = [4, 3, 3, 3, 2, 1, 1, 0, 0]
        elif current_level == "12":
            max_slots = [4, 3, 3, 3, 2, 1, 0, 0, 0]
        elif current_level == "11":
            max_slots = [4, 3, 3, 3, 2, 1, 0, 0, 0]
        elif current_level == "10":
            max_slots = [4, 3, 3, 3, 2, 0, 0, 0, 0]
        elif current_level == "9":
            max_slots = [4, 3, 3, 3, 1, 0, 0, 0, 0]
        elif current_level == "8":
            max_slots = [4, 3, 3, 2, 0, 0, 0, 0, 0]
        elif current_level == "7":
            max_slots = [4, 3, 3, 1, 0, 0, 0, 0, 0]
        elif current_level == "6":
            max_slots = [4, 3, 3, 0, 0, 0, 0, 0, 0]
        elif current_level == "5":
            max_slots = [4, 3, 2, 0, 0, 0, 0, 0, 0]
        elif current_level == "4":
            max_slots = [4, 3, 0, 0, 0, 0, 0, 0, 0]
        elif current_level == "3":
            max_slots = [4, 2, 0, 0, 0, 0, 0, 0, 0]
        elif current_level == "2":
            max_slots = [3, 0, 0, 0, 0, 0, 0, 0, 0]
        elif current_level == "1":
            max_slots = [2, 0, 0, 0, 0, 0, 0, 0, 0]

    def clone(max_slots):
        clone = max_slots[:]
        return clone

    current_slots = clone(max_slots)

    def click1():
        if current_slots[0] > 0:
            current_slots[0] = current_slots[0] - 1
        else:
            current_slots[0] = 0
        first_btn.configure(text=f"{current_slots[0]}/{max_slots[0]}")

    def click2():
        if current_slots[1] > 0:
            current_slots[1] = current_slots[1] - 1
        else:
            current_slots[1] = 0
        second_btn.configure(text=f"{current_slots[1]}/{max_slots[1]}")

    def click3():
        if current_slots[2] > 0:
            current_slots[2] = current_slots[2] - 1
        else:
            current_slots[2] = 0
        third_btn.configure(text=f"{current_slots[2]}/{max_slots[2]}")

    def click4():
        if current_slots[3] > 0:
            current_slots[3] = current_slots[3] - 1
        else:
            current_slots[3] = 0
        fourth_btn.configure(text=f"{current_slots[3]}/{max_slots[3]}")

    def click5():
        if current_slots[4] > 0:
            current_slots[4] = current_slots[4] - 1
        else:
            current_slots[4] = 0
        fifth_btn.configure(text=f"{current_slots[4]}/{max_slots[4]}")

    def click6():
        if current_slots[5] > 0:
            current_slots[5] = current_slots[5] - 1
        else:
            current_slots[5] = 0
        sixth_btn.configure(text=f"{current_slots[5]}/{max_slots[5]}")

    def click7():
        if current_slots[6] > 0:
            current_slots[6] = current_slots[6] - 1
        else:
            current_slots[6] = 0
        seventh_btn.configure(text=f"{current_slots[6]}/{max_slots[6]}")

    def click8():
        if current_slots[7] > 0:
            current_slots[7] = current_slots[7] - 1
        else:
            current_slots[7] = 0
        eighth_btn.configure(text=f"{current_slots[7]}/{max_slots[7]}")

    def click9():
        if current_slots[8] > 0:
            current_slots[8] = current_slots[8] - 1
        else:
            current_slots[8] = 0
        ninth_btn.configure(text=f"{current_slots[8]}/{max_slots[8]}")

    def long_rest():
        current_slots = clone(max_slots)
        first_btn.configure(text=f"{current_slots[0]}/{max_slots[0]}")
        second_btn.configure(text=f"{current_slots[1]}/{max_slots[1]}")
        third_btn.configure(text=f"{current_slots[2]}/{max_slots[2]}")
        fourth_btn.configure(text=f"{current_slots[3]}/{max_slots[3]}")
        fifth_btn.configure(text=f"{current_slots[4]}/{max_slots[4]}")
        sixth_btn.configure(text=f"{current_slots[5]}/{max_slots[5]}")
        seventh_btn.configure(text=f"{current_slots[6]}/{max_slots[6]}")
        eighth_btn.configure(text=f"{current_slots[7]}/{max_slots[7]}")
        ninth_btn.configure(text=f"{current_slots[8]}/{max_slots[8]}")

    first_label = tk.Label(spell_window, text="1st")
    first_label.grid(column=0, row=2)

    first_btn = tk.Button(
        spell_window, text=f"{current_slots[0]}/{max_slots[0]}", command=click1
    )
    first_btn.grid(column=1, row=2)

    second_label = tk.Label(spell_window, text="2nd")
    second_label.grid(column=0, row=3)

    second_btn = tk.Button(
        spell_window, text=f"{current_slots[1]}/{max_slots[1]}", command=click2
    )
    second_btn.grid(column=1, row=3)

    third_label = tk.Label(spell_window, text="3rd")
    third_label.grid(column=0, row=4)

    third_btn = tk.Button(
        spell_window, text=f"{current_slots[2]}/{max_slots[2]}", command=click3
    )
    third_btn.grid(column=1, row=4)

    fourth_label = tk.Label(spell_window, text="4th")
    fourth_label.grid(column=0, row=5)

    fourth_btn = tk.Button(
        spell_window, text=f"{current_slots[3]}/{max_slots[3]}", command=click4
    )
    fourth_btn.grid(column=1, row=5)

    fifth_label = tk.Label(spell_window, text="5th")
    fifth_label.grid(column=0, row=6)

    fifth_btn = tk.Button(
        spell_window, text=f"{current_slots[4]}/{max_slots[4]}", command=click5
    )
    fifth_btn.grid(column=1, row=6)

    sixth_label = tk.Label(spell_window, text="6th")
    sixth_label.grid(column=0, row=7)

    sixth_btn = tk.Button(
        spell_window, text=f"{current_slots[5]}/{max_slots[5]}", command=click6
    )
    sixth_btn.grid(column=1, row=7)

    seventh_label = tk.Label(spell_window, text="7th")
    seventh_label.grid(column=0, row=8)

    seventh_btn = tk.Button(
        spell_window, text=f"{current_slots[6]}/{max_slots[6]}", command=click7
    )
    seventh_btn.grid(column=1, row=8)

    eighth_label = tk.Label(spell_window, text="8th")
    eighth_label.grid(column=0, row=9)

    eighth_btn = tk.Button(
        spell_window, text=f"{current_slots[7]}/{max_slots[7]}", command=click8
    )
    eighth_btn.grid(column=1, row=9)

    ninth_label = tk.Label(spell_window, text="9th")
    ninth_label.grid(column=0, row=10)

    ninth_btn = tk.Button(
        spell_window, text=f"{current_slots[8]}/{max_slots[8]}", command=click9
    )
    ninth_btn.grid(column=1, row=10)

    long_rest_btn = tk.Button(
        spell_window, text="Long Rest", command=long_rest
    )
    long_rest_btn.grid(column=0, row=11)


btn = tk.Button(window, text="ENTER", command=clicked)
btn.grid(column=0, row=3)


window.mainloop()
