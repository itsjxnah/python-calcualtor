# A Simple Calculator made by itsjxnah aka. Jonah
# https://github.com/itsjxnah/
# https://github.com/itsjxnah/python-calcualtor

import tkinter as tk
import math

# ========================
# |     Settings        |
# ========================
root = tk.Tk()
root.title("Calc")
root.geometry("350x300")
root.configure(bg="#361264")

# ========================
# |     State            |
# ========================

first_number = None
operator = None
waiting_for_second_number = False

last_operator = None
last_operand = None
just_calculated = False
error_state = False

# ========================
# |     Display          |
# ========================

display_var = tk.StringVar(value="0")
display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Arial", 28),
    justify="right",
    state="readonly",
    readonlybackground="#181825",
    fg="#cdd6f4",
    bd=0,
    relief="flat"
)

display.pack(fill="x", padx=16, pady=(20,16), ipady=18)

# ========================
# |     Helper           |
# ========================

def update_display(value):
    display_var.set(str(value))

def format_result(value):
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError("The result isn't finite.")
        if value.is_integer():
            return str(int(value))

        return f"{value:.10g}"
    return str(value)

def reset_calculation_state():
    global first_number, operator
    global waiting_for_second_number
    global last_operator, last_operand
    global just_calculated, error_state

    first_number = None
    operator = None
    waiting_for_second_number = False

    last_operator = None
    last_operand = None
    just_calculated = False
    error_state = False

# ========================
# |     Number input     |
# ========================

def enter_digit(digit):
    global waiting_for_second_number
    global just_calculated, error_state

    if error_state:
        reset_calculation_state()
        update_display(digit)
        return
    current_value = display_var.get()

    if waiting_for_second_number or just_calculated:
        update_display(digit)
        waiting_for_second_number = False
        just_calculated = False
        return

    if current_value == "0":
        update_display(digit)
    else:
        update_display(current_value + digit)

def enter_decimal():
    global waiting_for_second_number
    global just_calculated, error_state

    if error_state:
        reset_calculation_state()
        update_display("0.")
        return
    current_value = display_var.get()

    if waiting_for_second_number or just_calculated:
        update_display("0.")
        waiting_for_second_number = False
        just_calculated = False
    elif "." not in current_value:
        update_display(current_value + ".")

# ========================
# |   Arithmetic         |
# ========================

def calculate(first, second, selected_operator):
    if selected_operator == "+":
        result = first + second

    elif selected_operator == "-":
        result = first - second

    elif selected_operator == "*":
        result = first * second

    elif selected_operator == "/":
        if second == 0:
            raise ZeroDivisionError(
                "Cannot divide by zero."
            )
        result = first / second

    else:
        raise ValueError("Unknown operator.")

    if isinstance(result, float) and not math.isfinite(result):
        raise ValueError("The result is too large.")
    return result

def choose_operator(selected_operator):
    global first_number, operator
    global waiting_for_second_number
    global just_calculated, error_state
    global last_operator, last_operand

    if error_state:
        return

    current_number = float(display_var.get())

    if operator is not None and not waiting_for_second_number:
        try:
            current_number = calculate(
                first_number,
                current_number,
                operator
            )
            update_display(format_result(current_number))

        except (ZeroDivisionError, ValueError, OverflowError):
            show_error()
            return

    first_number = current_number
    operator = selected_operator
    waiting_for_second_number = True
    just_calculated = False

    last_operator = None
    last_operand = None

def calculate_result():
    global first_number, operator
    global waiting_for_second_number
    global last_operator, last_operand
    global just_calculated, error_state

    if error_state:
        return

    if operator is None:
        if last_operator is None:
            return
        try:
            current_number = float(display_var.get())
            result = calculate(
                current_number,
                last_operand,
                last_operator
            )

            update_display(format_result(result))
            just_calculated = True

        except (ZeroDivisionError, ValueError, OverflowError):
            show_error()

        return
    if waiting_for_second_number:
        return

    second_number = float(display_var.get())

    try:
        result = calculate(
            first_number,
            second_number,
            operator
        )

        last_operator = operator
        last_operand = second_number

        update_display(format_result(result))

        first_number = result
        operator = None
        waiting_for_second_number = False
        just_calculated = True

    except (ZeroDivisionError, ValueError, OverflowError):
        show_error()

# ========================
# |     Editing          |
# ========================

def clear_display():
    reset_calculation_state()
    update_display("0")

def delete_last_digit():
    global waiting_for_second_number
    global just_calculated, error_state

    if error_state or just_calculated:
        clear_display()
        return

    if waiting_for_second_number:
        return

    current_value = display_var.get()
    if len(current_value) <= 1:
        update_display("0")
    elif len(current_value) == 2 and current_value.startswith("-"):
        update_display("0")
    else:
        update_display(current_value[:-1])

def toggle_sign():
    global just_calculated, error_state

    if error_state:
        clear_display()
        return
    current_number = float(display_var.get())

    if current_number == 0:
        return

    if display_var.get().startswith("-"):
        update_display(display_var.get()[1:])
    else:
        update_display("-" + display_var.get())

    just_calculated = False

def calculate_percentage():
    global just_calculated, error_state

    if error_state:
        return

    current_number = float(display_var.get())
    update_display(format_result(current_number / 100))
    just_calculated = False

def show_error():
    global first_number, operator
    global waiting_for_second_number
    global last_operator, last_operand
    global just_calculated, error_state

    update_display("Error")

    first_number = None
    operator = None
    waiting_for_second_number = False
    last_operator = None
    last_operand = None
    just_calculated = False
    error_state = True

# ========================
# | Button               |
# ========================

def handle_button(value):
    actions = {
        "C": clear_display,
        "DEL": delete_last_digit,
        "+": toggle_sign,
        "%": calculate_percentage,
        ".": enter_decimal,
        "=": calculate_result,
        "+": lambda: choose_operator("+"),
        "-": lambda: choose_operator("-"),
        "x": lambda: choose_operator("*"),
        "/": lambda: choose_operator("/")
    }

    if value in actions:
        actions[value]()
    elif value.isdigit():
        enter_digit(value)

# ========================
# |     Button layout    |
# ========================

button_frame = tk.Frame(root, bg="#1e1e2e")
button_frame.pack(fill="both", expand=True, padx=12, pady=(0, 12))

button_rows = [
    ["C", "DEL", "%", "/"],
    ["7", "8", "9", "x"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["+", "0", ".", "="]
]

def get_button_color(value):
    if value == "=":
        return "#89b4fa"
    if value in ["+", "-", "x", "/"]:
        return "#45475a"
    if value in ["C", "DEL", "%", "+"]:
        return "#313244"

    return "#585870"

for row_index, row_values in enumerate(button_rows):
    button_frame.grid_rowconfigure(
        row_index,
        weight=1,
        uniform="row"
    )

    for column_index, value in enumerate(row_values):
        button_frame.grid_columnconfigure(
            column_index,
            weight=1,
            uniform="column"
        )

        text_color = "#11111b" if value == "=" else "#cdd6f4"

        button = tk.Button(
            button_frame,
            text=value,
            font=("Arial", 17, "bold"),
            bg=get_button_color(value),
            fg=text_color,
            activebackground="#74c7ec",
            activeforeground="#11111b",
            bd=0,
            relief="flat",
            cursor="hand2",
            command=lambda item=value: handle_button(item)
        )

        button.grid(
            row=row_index,
            column=column_index,
            sticky="nsew",
            padx=4,
            pady=4
        )

# ========================
# |     Keyboard         |
# ========================

def handle_keypress(event):
    key = event.keysym

    if key.isdigit():
        handle_button(key)
    elif key in ["plus", "KP_Add"]:
        handle_button("+")
    elif key in ["minus", "KP_Subtract"]:
        handle_button("-")
    elif key in ["asterisk", "KP_Multiply"]:
        handle_button("*")
    elif key in ["slash", "KP_Divide"]:
        handle_button("/")
    elif key in ["Return", "KP_Enter", "equal"]:
        handle_button("=")
    elif key in ["BackSpace", "Delete"]:
        handle_button("DEL")
    elif key in ["Escape"]:
        handle_button("C")
    elif key in ["period", "comma", "KP_Decimal"]:
        handle_button(".")

root.bind("<Key>", handle_keypress)

root.mainloop()