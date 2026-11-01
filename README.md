# Python Calculator

A simple desktop calculator built with **Python** and **Tkinter**, featuring a modern dark theme, basic arithmetic operations, keyboard support, and an intuitive graphical user interface.

## Features

- **Basic arithmetic:** Addition, subtraction, multiplication, and division.
- **Decimal numbers:** Perform calculations with floating-point numbers.
- **Percentage calculations:** Convert numbers into percentages.
- **Sign toggle:** Switch between positive and negative numbers.
- **Clear button:** Reset the calculator.
- **Backspace:** Remove the last digit from the display.
- **Keyboard support:** Enter numbers and perform calculations using your keyboard.
- **Error handling:** Handle invalid operations, including division by zero.
- **Modern dark theme:** A clean interface with dark colors and blue accents.
- **Calculation repetition:** Press `=` again to repeat the last operation.

## Preview

The calculator features a dark interface with a large display and a grid of buttons for numbers and mathematical operations.

## Technologies

- **Python 3** — Main programming language
- **Tkinter** — Graphical user interface
- **Math module** — Mathematical utilities and validation

## Requirements

- Python 3.10 or newer recommended
- Tkinter installed and available in your Python environment
- Windows, macOS, or Linux

Tkinter is included with many standard Python installations. On some Linux distributions, you may need to install it separately.

## Installation

### 1. Clone the repository

```bash
git clone [<YOUR_REPOSITORY_URL>](https://github.com/itsjxnah/python-calcualtor.git)
```

### 2. Navigate to the project directory

```bash
cd python-calculator
```

Make sure `calculator.py` is located in this directory.

### 3. Run the application

On Windows:

```bash
python calculator.py
```

Alternatively, you can use:

```bash
py calculator.py
```

On macOS or Linux:

```bash
python3 calculator.py
```

The calculator window should open automatically.

## Keyboard Shortcuts

| Key | Action |
|---|---|
| `0–9` | Enter a digit |
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `Enter` | Calculate the result |
| `Backspace` | Delete the last digit |
| `Delete` | Delete the last digit |
| `Escape` | Clear the calculator |
| `.` or `,` | Enter a decimal separator |

Keyboard behavior may depend on the operating system and keyboard layout.

## Project Structure

```text
python-calculator/
├── calculator.py
└── README.md
```

- `calculator.py` — Contains the application, user interface, calculation logic, and keyboard controls.
- `README.md` — Provides project documentation and setup instructions.

## What I Learned

This project is designed to practice and demonstrate fundamental Python programming concepts, including:

- Creating graphical interfaces with Tkinter
- Working with variables and functions
- Using conditional statements and loops
- Handling button clicks and keyboard events
- Managing application state
- Formatting numerical results
- Handling exceptions and invalid operations
- Organizing code into reusable functions

## Limitations

- This is a basic calculator, not a scientific calculator.
- The percentage button converts the current number by dividing it by 100. It does not implement every convention used by physical calculators.
- Floating-point calculations can introduce small precision differences.
- The calculator does not currently save calculation history.
- Complex expressions with parentheses and operator precedence are not supported.

## Future Improvements

Possible improvements include:

- Adding a calculation history
- Implementing a scientific calculator mode
- Supporting parentheses and complex expressions
- Adding customizable themes
- Improving input validation
- Refactoring the application using object-oriented programming
- Adding automated unit tests

## License

This project is available for personal learning and experimentation. If you plan to publish or distribute it, consider adding a license file that clearly defines the permitted use.

## Author

Created by itsjxnah as a Python learning project to explore Tkinter and desktop application development.
