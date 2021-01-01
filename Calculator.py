import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        root.title("Calculator")
        width=273
        height=375
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        def btn1_command():
            txtAnswer.insert("end", "1")

        def btn2_command():
            txtAnswer.insert("end", "2")

        def btn3_command():
            txtAnswer.insert("end", "3")     

        def btn4_command():            
            txtAnswer.insert("end", "4")

        def btn5_command():
            txtAnswer.insert("end", "5")     

        def btn6_command():
            txtAnswer.insert("end", "6")

        def btn7_command():
            txtAnswer.insert("end", "7")

        def btn8_command():
            txtAnswer.insert("end", "8")

        def btn9_command():
            txtAnswer.insert("end", "9")

        def btn0_command():
            txtAnswer.insert("end", "0")

        def btn00_command():
            txtAnswer.insert("end", "00")

        def btndecimal_command():
            txtAnswer.insert("end", ".")

        def btnadd_command():
            txtAnswer.insert("end", "+")

        def btnmin_command():
            txtAnswer.insert("end", "-")

        def btnmul_command():
            txtAnswer.insert("end", "*")

        def btnmod_command():
            txtAnswer.insert("end", "%")

        def btndivide_command():
            txtAnswer.insert("end", "/")

        def btnCancel_command():
            txtAnswer.delete(0, "end")

        def equalTxt_command():
            result = txtAnswer.get()
            if result == "":
                txtAnswer.insert("end","error")
            elif result[0] == "0":
                txtAnswer.delete(0,"end")
                txtAnswer.insert("end","error")
            else:
                result = eval(result)
                # txtAnswer.insert("end"," = ")
                txtAnswer.delete(0,"end")
                txtAnswer.insert("end", result)


        txtAnswer = tk.Entry(root)        
        txtAnswer["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=23)
        txtAnswer["font"] = ft
        txtAnswer["fg"] = "#333333"
        txtAnswer["justify"] = "center"
        txtAnswer["relief"] = "sunken"
        txtAnswer.place(x=20,y=10,width=169,height=51)

        btnCancel = tk.Button(root)
        btnCancel["bg"] = "#ff0505"
        ft = tkFont.Font(family='Times',size=18)
        btnCancel["font"] = ft
        btnCancel["fg"] = "#000000"
        btnCancel["justify"] = "center"
        btnCancel["text"] = "C"
        btnCancel["relief"] = "groove"
        btnCancel.place(x=200,y=10,width=50,height=48)
        btnCancel["command"] = btnCancel_command

        btn7 = tk.Button(root)
        btn7["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        btn7["font"] = ft
        btn7["fg"] = "#000000"
        btn7["justify"] = "center"
        btn7["text"] = "7"
        btn7["relief"] = "groove"
        btn7.place(x=20,y=70,width=50,height=48)
        btn7["command"] = btn7_command

        btn4 = tk.Button(root)
        btn4["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        btn4["font"] = ft
        btn4["fg"] = "#000000"
        btn4["justify"] = "center"
        btn4["text"] = "4"
        btn4["relief"] = "groove"
        btn4.place(x=20,y=130,width=49,height=49)
        btn4["command"] = btn4_command

        btn1 = tk.Button(root)
        btn1["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        btn1["font"] = ft
        btn1["fg"] = "#000000"
        btn1["justify"] = "center"
        btn1["text"] = "1"
        btn1["relief"] = "groove"
        btn1.place(x=20,y=190,width=49,height=48)
        btn1["command"] = btn1_command

        btn0 = tk.Button(root)
        btn0["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        btn0["font"] = ft
        btn0["fg"] = "#000000"
        btn0["justify"] = "center"
        btn0["text"] = "0"
        btn0["relief"] = "groove"
        btn0.place(x=20,y=250,width=49,height=48)
        btn0["command"] = btn0_command

        equalTxt = tk.Button(root)
        equalTxt["bg"] = "#14ff0f"
        ft = tkFont.Font(family='Times',size=23)
        equalTxt["font"] = ft
        equalTxt["fg"] = "#000000"
        equalTxt["justify"] = "center"
        equalTxt["text"] = "="
        equalTxt["relief"] = "groove"
        equalTxt.place(x=20,y=310,width=171,height=44)
        equalTxt["command"] = equalTxt_command

        btn8 = tk.Button(root)
        btn8["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        btn8["font"] = ft
        btn8["fg"] = "#000000"
        btn8["justify"] = "center"
        btn8["text"] = "8"
        btn8["relief"] = "groove"
        btn8.place(x=80,y=70,width=50,height=49)
        btn8["command"] = btn8_command

        btn5 = tk.Button(root)
        btn5["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        btn5["font"] = ft
        btn5["fg"] = "#000000"
        btn5["justify"] = "center"
        btn5["text"] = "5"
        btn5["relief"] = "groove"
        btn5.place(x=80,y=130,width=51,height=49)
        btn5["command"] = btn5_command

        btn2 = tk.Button(root)
        btn2["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        btn2["font"] = ft
        btn2["fg"] = "#000000"
        btn2["justify"] = "center"
        btn2["text"] = "2"
        btn2["relief"] = "groove"
        btn2.place(x=80,y=190,width=49,height=48)
        btn2["command"] = btn2_command

        btn00 = tk.Button(root)
        btn00["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        btn00["font"] = ft
        btn00["fg"] = "#000000"
        btn00["justify"] = "center"
        btn00["text"] = "00"
        btn00["relief"] = "groove"
        btn00.place(x=80,y=250,width=49,height=48)
        btn00["command"] = btn00_command

        btn6 = tk.Button(root)
        btn6["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        btn6["font"] = ft
        btn6["fg"] = "#000000"
        btn6["justify"] = "center"
        btn6["text"] = "6"
        btn6["relief"] = "groove"
        btn6.place(x=140,y=130,width=49,height=49)
        btn6["command"] = btn6_command

        btn3 = tk.Button(root)
        btn3["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        btn3["font"] = ft
        btn3["fg"] = "#000000"
        btn3["justify"] = "center"
        btn3["text"] = "3"
        btn3["relief"] = "groove"
        btn3.place(x=140,y=190,width=49,height=48)
        btn3["command"] = btn3_command

        btndecimal = tk.Button(root)
        btndecimal["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        btndecimal["font"] = ft
        btndecimal["fg"] = "#000000"
        btndecimal["justify"] = "center"
        btndecimal["text"] = "."
        btndecimal["relief"] = "groove"
        btndecimal.place(x=140,y=250,width=49,height=48)
        btndecimal["command"] = btndecimal_command

        btnadd = tk.Button(root)
        btnadd["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=23)
        btnadd["font"] = ft
        btnadd["fg"] = "#000000"
        btnadd["justify"] = "center"
        btnadd["text"] = "+"
        btnadd["relief"] = "groove"
        btnadd.place(x=200,y=70,width=51,height=48)
        btnadd["command"] = btnadd_command

        btnmin = tk.Button(root)
        btnmin["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=23)
        btnmin["font"] = ft
        btnmin["fg"] = "#000000"
        btnmin["justify"] = "center"
        btnmin["text"] = "-"
        btnmin["relief"] = "groove"
        btnmin.place(x=200,y=130,width=50,height=51)
        btnmin["command"] = btnmin_command

        btnmul = tk.Button(root)
        btnmul["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=23)
        btnmul["font"] = ft
        btnmul["fg"] = "#000000"
        btnmul["justify"] = "center"
        btnmul["text"] = "*"
        btnmul["relief"] = "groove"
        btnmul.place(x=200,y=190,width=49,height=48)
        btnmul["command"] = btnmul_command

        btnmod = tk.Button(root)
        btnmod["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=23)
        btnmod["font"] = ft
        btnmod["fg"] = "#000000"
        btnmod["justify"] = "center"
        btnmod["text"] = "%"
        btnmod["relief"] = "groove"
        btnmod.place(x=200,y=310,width=48,height=44)
        btnmod["command"] = btnmod_command

        btndivide = tk.Button(root)
        btndivide["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=23)
        btndivide["font"] = ft
        btndivide["fg"] = "#000000"
        btndivide["justify"] = "center"
        btndivide["text"] = "/"
        btndivide["relief"] = "groove"
        btndivide.place(x=200,y=250,width=48,height=48)
        btndivide["command"] = btndivide_command

        btn9 = tk.Button(root)
        btn9["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        btn9["font"] = ft
        btn9["fg"] = "#000000"
        btn9["justify"] = "center"
        btn9["text"] = "9"
        btn9["relief"] = "groove"
        btn9.place(x=140,y=70,width=49,height=48)
        btn9["command"] = btn9_command



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()