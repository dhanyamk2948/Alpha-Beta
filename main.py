#Stock Performance predictor


import tkinter as tk
from functools import partial

def performance(label_result, n1, n2):
    #Store the inputs from the entry widget in float form
    num1 = float(n1.get())
    num2 = float(n2.get())
    #Logic for evaluating stock's performance
    if (num1>0 and num2>=1):
        if num2==1:
            result="Go ahead, \nstick around for long term:)"
        else:
            result="Too risky, requires active trading:|"
    elif num1>0 and num2<1:
        result="Suitable for long term,minimal risk and \nhigh return- passive trading strategy! :)"
    elif num1<0 and num2<1:
        result="Gain slower than the market, usually \nhelpful to get High dividend yield :|>"
    elif num1<0 and num2>1:
        result="Too risky,suitable for day trading"
    label_result.config(text=" %s" % result)
    return


root = tk.Tk()
root.geometry('400x200+100+200')
#Setting the dimensions of the GUI dialog

root.title('SPP')

number1 = tk.StringVar()
number2 = tk.StringVar()

labelNum1 = tk.Label(root, text="Alpha").grid(row=1, column=0)

labelNum2 = tk.Label(root, text="Beta").grid(row=2, column=0)

labelResult = tk.Label(root,fg='#f00')
labelResult.config(font=("Courier", 20))
labelResult.grid(row=7, column=2)

entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)

entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)

performance = partial(performance, labelResult, number1, number2)

buttonCal = tk.Button(root, text="Analyse", command=performance).grid(row=3, column=0, padx=50, pady=50)

root.mainloop()

