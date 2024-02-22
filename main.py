import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=500, height=500)


def bmi_calculator():
    value1, value2 = get_value()
    if value1 == "" or value2 == "":
        result = "Enter both weight and height."
    else:
        bmi = value1 / (value2 / 100) ** 2
        if bmi < 18.5:
            result = "Underweight"
        elif 18.5 <= bmi < 25:
            result = "Normal"
        elif 25 <= bmi < 30:
            result = "Overweight"
        else:
            result = "Obese"
    return bmi, result


def get_value():
    value1 = float(kg_entry.get())
    value2 = float(height_entry.get())
    return value1, value2


def button_click():
    value1, value2 = get_value()
    bmi, result = bmi_calculator()
    final_label.config(text="Your BMI is {:.2f}. You are {}.".format(bmi, result))


kg_button = tkinter.Label(window, text="Enter Your Weight (kg): ", width=20, height=10)
kg_button.grid(row=0, column=0)

kg_entry = tkinter.Entry(window)
kg_entry.grid(row=0, column=1)

height_button = tkinter.Label(window, text="Enter Your Height (cm): ", width=20, height=10)
height_button.grid(row=1, column=0)

height_entry = tkinter.Entry(window)
height_entry.grid(row=1, column=1)

# command = button_clik yaptigimizda button altinda labeli yazdiriyor
my_button = tkinter.Button(window, text="Calculate", command=button_click)
my_button.grid(row=2, column=1)

final_label = tkinter.Label(window, text="", width=30, height=10, )
final_label.grid(row=3, column=1)

window.mainloop()