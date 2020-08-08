# start code

import pandas as pd

import pickle

from tkinter import *

import tkinter as tk

from tkinter import ttk, Frame, Menu

from PIL import ImageTk, Image

import time

import os

#ML

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# with open(BASE_DIR+'\\desktop-app-using-tkinter-for-prediction-master\\Loan_Model.pkl', 'rb') as file:  
#     Pickled_LR_Model = pickle.load(file)

with open(BASE_DIR+'\\desktop-app-using-tkinter-for-prediction-master\\Admission_Model.pkl', 'rb') as file:  
    Admission_Model = pickle.load(file)


#GUI

win = tk.Tk()
win.title("The Predictor")
win.iconbitmap(r'favicon.ico')




#text1=tk.Text(win,height=50,width=30)
#text1.Pack(side=tk.BOTTOM)
#test1.insert(tk.END,"just a text widget")

class Slider:
    def __init__(self,win):
        self.win=win
        #self.bframe.title("The Predictor")
        self.win.geometry("1100x900+0+0")
        self.win.configure(background="#6C757D")
        #########images###########
        self.image1 = ImageTk.PhotoImage(file="14.png")
        self.image2 = ImageTk.PhotoImage(file="15.png")
        self.image3 = ImageTk.PhotoImage(file="16.png")

        #################
        Frame_slider=Frame(win)
        Frame_slider.place(x=0,y=0,width=1100,height=500)
        self.lbl1 = Label(Frame_slider,image=self.image1,bd=0)
        self.lbl1.place(x=0, y=0)
        #self.x = 1100
        self.lbl2 = Label(Frame_slider, image=self.image2,bd=0)
        self.lbl2.place(x=1100, y=0)
        self.x = 1100

        self.lbl3 = Label(Frame_slider, image=self.image3,bd=0)
        self.lbl3.place(x=1100, y=0)
        self.x=1100
        self.slider_func()

    def slider_func(self):
        self.x-=1
        if self.x==0:
            self.x=1100
            time.sleep(1)
            ###Swap######
            self.new_im=self.image1
            self.image1=self.image2
            self.image2=self.image3
            self.image3=self.new_im

            self.lbl1.config(image=self.image1)
            self.lbl2.config(image=self.image3)
            self.lbl3.config(image=self.image2)


        self.lbl3.place(x=self.x,y=0)
        #self.lbl2.after(1,self.slider_func)
        #self.lbl3.place(x=self.x, y=0)
        self.lbl3.after(1, self.slider_func)



obj=Slider(win)

text1=Label(win, text="Difficult times eh?")
text1.pack()
text1.place(x=5,y=510)

text2=Label(win, text="Tired Searching for a job?")
text2.pack()
text2.place(x=5,y=540)

text3=Label(win, text="Admission in a foreign university is your dream?")
text3.pack()
text3.place(x=5,y=570)

text4=Label(win, text="Want a loan to kick start your business?")
text4.pack()
text4.place(x=5,y=600)

text5=Label(win, text="A one stop solution for all your needs.The predictor is a tool that can solve all your queries in a minute.")
text5.pack()
text5.place(x=5,y=630)

text6=Label(win, text="To get your loan amount to kick start your dream business.")
text6.pack()
text6.place(x=5,y=660)

text7=Label(win, text=" We verify your emails and prevent you from falling in the trap of fraudsters.")
text7.pack()
text7.place(x=5,y=690)

text8=Label(win, text="REMEMBER:")
text8.pack(side=RIGHT)
text8.place(x=600,y=510)

text9=Label(win, text="We do not help you get a job or loan.")
text9.pack(side=RIGHT)
text9.place(x=600,y=540)

text10=Label(win, text="We just guide you to save your valuable time and money into useless opportunities ")
text10.pack(side=RIGHT)
text10.place(x=600,y=570)

text10=Label(win, text="and rather focus yourself into the most suitable ones.")
text10.pack(side=RIGHT)
text10.place(x=600,y=590)

# create menu button

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("The Predictor")

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        HomeMenu = Menu(menubar, tearoff=0)
        #HomeMenu.add_command(label="Show Text", command=showTxt)
        
        PredictMenu = Menu(menubar, tearoff=0)

        PredictMenu.add_command(label="Loan Prediction", command=Predict_new)
        PredictMenu.add_command(label="Addmission Prediction", command=Predict_cut)
        PredictMenu.add_command(label="Spam Email Checker", command=Predict_reset)

        AboutMenu = Menu(menubar, tearoff=0)
        AboutMenu.add_command(label="Exit", command=win.quit)

        menubar.add_cascade(label="Home", menu=HomeMenu)
        menubar.add_cascade(label="Predict", menu=PredictMenu)
        menubar.add_cascade(label="About", menu=AboutMenu)


def our_command():
    my_label = Label(Predict_new_frame, text="you clicked a dropped menu!").pack()


def main():
    # win = Tk()
    app = Example()

def Predict_new():
    hide_all_frames()
    Predict_new_frame.pack(fill="both", expand=1)



def Predict_cut():
    hide_all_frames()
    Predict_cut_frame.pack(fill="both", expand=1)


def Predict_reset():
    hide_all_frames()
    Predict_reset_frame.pack(fill="both", expand=1)


# hide all frame function
def hide_all_frames():
    Predict_new_frame.pack_forget()
    Predict_cut_frame.pack_forget()
    Predict_reset_frame.pack_forget()


if __name__ == '__main__':
    main()


# Create first Loan prediction page

Predict_new_frame = Frame(win, width=600, height=800, bg="#6C757D")
#Predict_new_frame.pack()
# Predict_new_frame = ttk.LabelFrame(win, text='Input Data for Loan Prediction')
# Predict_new_frame.grid(row=0, column=0, padx=100)

Predict_cut_frame = Frame(win, width=600, height=800, bg="#6C757D")
#Predict_cut_frame.pack()
# Predict_cut_frame.grid(row=0, column=0, padx=1)

Predict_reset_frame = Frame(win, width=600, height=800, bg="#6C757D")
#Predict_reset_frame.pack()
#for image




# create labels

name_label = ttk.Label(Predict_new_frame, text='What is your Gender')
name_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

name_label = ttk.Label(Predict_new_frame, text='Whether you are Married')
name_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

name_label = ttk.Label(Predict_new_frame, text='Enter the Dependents value')
name_label.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)

name_label = ttk.Label(Predict_new_frame, text='Enter your Education')
name_label.grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)

name_label = ttk.Label(Predict_new_frame, text='Whether you are Self employed')
name_label.grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)

name_label = ttk.Label(Predict_new_frame, text='Enter the Applicant income')
name_label.grid(row=6, column=0, sticky=tk.W, padx=5, pady=5)

name_label = ttk.Label(Predict_new_frame, text='Enter the Coapplicant income')
name_label.grid(row=7, column=0, sticky=tk.W, padx=5, pady=5)

name_label = ttk.Label(Predict_new_frame, text='Enter the Loan amount')
name_label.grid(row=8, column=0, sticky=tk.W, padx=5, pady=5)

name_label = ttk.Label(Predict_new_frame, text='Enter the Loan amount term')
name_label.grid(row=9, column=0, sticky=tk.W, padx=5, pady=5)

name_label = ttk.Label(Predict_new_frame, text='Enter the Credit History')
name_label.grid(row=10, column=0, sticky=tk.W, padx=5, pady=5)

name_label = ttk.Label(Predict_new_frame, text='Enter the property area')
name_label.grid(row=11, column=0, sticky=tk.W, padx=5, pady=5)

# create entry box


Gender_var = tk.StringVar()
Gender_entrybox = ttk.Entry(Predict_new_frame, width=20, textvariable=Gender_var)
Gender_entrybox.grid(row=1, column=1, padx=5, pady=5)

Married_var = tk.StringVar()
Married_entrybox = ttk.Entry(Predict_new_frame, width=20, textvariable=Married_var)
Married_entrybox.grid(row=2, column=1, padx=5, pady=5)

Dependents_value_var = tk.StringVar()
Dependents_value_entrybox = ttk.Entry(Predict_new_frame, width=20, textvariable=Dependents_value_var)
Dependents_value_entrybox.grid(row=3, column=1, padx=5, pady=5)

Education_var = tk.StringVar()
Education_entrybox = ttk.Entry(Predict_new_frame, width=20, textvariable=Education_var)
Education_entrybox.grid(row=4, column=1, padx=5, pady=5)

Self_employed_var = tk.StringVar()
Self_employed_entrybox = ttk.Entry(Predict_new_frame, width=20, textvariable=Self_employed_var)
Self_employed_entrybox.grid(row=5, column=1, padx=5, pady=5)

Applicant_income_var = tk.StringVar()
Applicant_income_entrybox = ttk.Entry(Predict_new_frame, width=20, textvariable=Applicant_income_var)
Applicant_income_entrybox.grid(row=6, column=1, padx=5, pady=5)

Coapplicant_income_var = tk.StringVar()
Coapplicant_income_entrybox = ttk.Entry(Predict_new_frame, width=20, textvariable=Coapplicant_income_var)
Coapplicant_income_entrybox.grid(row=7, column=1, padx=5, pady=5)

Loan_amount_var = tk.StringVar()
Loan_amount_entrybox = ttk.Entry(Predict_new_frame, width=20, textvariable=Loan_amount_var)
Loan_amount_entrybox.grid(row=8, column=1, padx=5, pady=5)

Loan_amount_term_var = tk.StringVar()
Loan_amount_term_entrybox = ttk.Entry(Predict_new_frame, width=20, textvariable=Loan_amount_term_var)
Loan_amount_term_entrybox.grid(row=9, column=1, padx=5, pady=5)

Credit_History_var = tk.StringVar()
Credit_History_entrybox = ttk.Entry(Predict_new_frame, width=20, textvariable=Credit_History_var)
Credit_History_entrybox.grid(row=10, column=1, padx=3, pady=3)

property_area_var = tk.StringVar()
property_area_entrybox = ttk.Entry(Predict_new_frame, width=20, textvariable=property_area_var)
property_area_entrybox.grid(row=11, column=1, padx=3, pady=3)

# create combobox


Gender_var = tk.StringVar()
Gender_combobox = ttk.Combobox(Predict_new_frame, width=17, textvariable=Gender_var, state='readonly')
Gender_combobox['values'] = ('Male', 'Female')
# Gender_combobox.current(0)
Gender_combobox.grid(row=1, column=1)

Married_var = tk.StringVar()
Married_combobox = ttk.Combobox(Predict_new_frame, width=17, textvariable=Married_var, state='readonly')
Married_combobox['values'] = ('Yes', 'No')
# Married_combobox.current(0)
Married_combobox.grid(row=2, column=1)

Dependents_value_var = tk.StringVar()
Dependents_value_combobox = ttk.Combobox(Predict_new_frame, width=17, textvariable=Dependents_value_var,
                                         state='readonly')
Dependents_value_combobox['values'] = ('0', '1', '2', '3', '4', '5')
# Education_combobox.current(0)
Dependents_value_combobox.grid(row=3, column=1)

Education_var = tk.StringVar()
Education_combobox = ttk.Combobox(Predict_new_frame, width=17, textvariable=Education_var, state='readonly')
Education_combobox['values'] = ('Graduate', 'Not Graduate')
# Education_combobox.current(0)
Education_combobox.grid(row=4, column=1)

Self_employed_var = tk.StringVar()
Self_employed_combobox = ttk.Combobox(Predict_new_frame, width=17, textvariable=Self_employed_var, state='readonly')
Self_employed_combobox['values'] = ('Yes', 'No')
# Self_employed_combobox.current(0)
Self_employed_combobox.grid(row=5, column=1)

property_area_var = tk.StringVar()
property_area_combobox = ttk.Combobox(Predict_new_frame, width=17, textvariable=property_area_var, state='readonly')
property_area_combobox['values'] = ('Urban', 'SemiUrban', 'Rural')
# property_area_combobox.current(0)
property_area_combobox.grid(row=11, column=1)

Credit_History_var = tk.StringVar()
Credit_History_combobox = ttk.Combobox(Predict_new_frame, width=17, textvariable=Credit_History_var, state='readonly')
Credit_History_combobox['values'] = ('Good', 'bad')
# Self_employed_combobox.current(0)
Credit_History_combobox.grid(row=10, column=1)

# create a buttton Label

label_frame = ttk.LabelFrame(Predict_new_frame, text='submit')
label_frame.grid(row=16, column=0, padx=100)

name_label = ttk.Label(Predict_new_frame)
name_label.grid(row=16, column=0, sticky=tk.W, padx=160, pady=10)


def Predict():
    # print("Loan is approved")
    print('Testing Start')
    
    
    # LOAN
    """gender=Gender_var.get()
    married=Married_var.get()
    dependents=Dependents_value_var.get()
    Education=Education_var.get()
    SelfEmployed=Self_employed_var.get()
    ApplicantIncome=int(Applicant_income_var.get())
    coApplicantIncome=int(Coapplicant_income_var.get())
    LoanAmount=int(Loan_amount_var.get())
    LoanAmountTerm=int(Loan_amount_term_var.get())
    if Credit_History_var.get()=='Good':
        CreditHistory=1
    else:
        CreditHistory=0
    PropertyArea=property_area_var.get()

    data = [[gender,married,dependents,Education,SelfEmployed,ApplicantIncome,coApplicantIncome,LoanAmount,LoanAmountTerm,CreditHistory,PropertyArea]]

    newdf = pd.DataFrame(data, columns = ['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area'])

    newdf = pd.get_dummies(newdf)

    XtrainCols=['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
        'Loan_Amount_Term', 'Credit_History', 'Gender_Female', 'Gender_Male',
        'Married_No', 'Married_Yes', 'Dependents_0', 'Dependents_1',
        'Dependents_2', 'Dependents_3+', 'Education_Graduate',
        'Education_Not Graduate', 'Self_Employed_No', 'Self_Employed_Yes',
        'Property_Area_Rural', 'Property_Area_Semiurban',
        'Property_Area_Urban']

    missing_cols = set( XtrainCols ) - set( newdf.columns )
    for c in missing_cols:
        newdf[c] = 0

    newdf = newdf[XtrainCols]
    yp=Pickled_LR_Model.predict(newdf)

    if yp[0]=='Y':
        print('Your Loan can be Approved')
    else:
        print("Sorry! Your Loan can't be Approved")"""

    #Admission

    # print(GRE_Score_var.get())
    # print(TOEFL_Score_var.get())
    # print(University_Rating_var.get())
    # print(Statement_of_Purpose_Rating_var.get())
    # print(Letter_of_Recommendation_Strength_var.get())
    # print(CGPA_var.get())
    # print(Research_var.get())

    gre=GRE_Score_var.get()
    toefl=TOEFL_Score_var.get()
    uni_rating=University_Rating_var.get()
    sop=Statement_of_Purpose_Rating_var.get()
    lor=Letter_of_Recommendation_Strength_var.get()
    cgpa=CGPA_var.get()
    if Research_var.get()=='Yes':
        research=1
    else:
        research=0

    newx=[[int(gre),int(toefl),int(uni_rating),float(sop),float(lor),float(cgpa),int(research)]]

    newy=Admission_Model.predict(newx)
    
    if newy[0] < 0:
        newy[0]=0

    print('Your Chance of Admission is',int(100*newy[0]),'%')

b1 = tk.Button(Predict_new_frame, text="Predict", command=Predict)
b1.grid(row=16, column=0)


# create second admission page
# create labels
name_label = ttk.Label(Predict_cut_frame, text='Enter the GRE Score')
name_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

name_label = ttk.Label(Predict_cut_frame, text='Enter the TOEFL Score')
name_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

name_label = ttk.Label(Predict_cut_frame, text='Enter the University Rating')
name_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

name_label = ttk.Label(Predict_cut_frame, text='Enter the Statement_of_Purpose_Rating')
name_label.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)

name_label = ttk.Label(Predict_cut_frame, text='Enter the Letter_of_Recommendation_Strength')
name_label.grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)

name_label = ttk.Label(Predict_cut_frame, text='Enter the CGPA')
name_label.grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)

name_label = ttk.Label(Predict_cut_frame, text='Have you done Research')
name_label.grid(row=6, column=0, sticky=tk.W, padx=5, pady=5)

# create entry box


GRE_Score_var = tk.StringVar()
GRE_Score_entrybox = ttk.Entry(Predict_cut_frame, width=20, textvariable=GRE_Score_var)
GRE_Score_entrybox.grid(row=0, column=1, padx=5, pady=5)
GRE_Score_entrybox.focus()

TOEFL_Score_var = tk.StringVar()
TOEFL_Score_entrybox = ttk.Entry(Predict_cut_frame, width=20, textvariable=TOEFL_Score_var)
TOEFL_Score_entrybox.grid(row=1, column=1, padx=5, pady=5)

University_Rating_var = tk.StringVar()
University_Rating_entrybox = ttk.Entry(Predict_cut_frame, width=20, textvariable=University_Rating_var)
University_Rating_entrybox.grid(row=2, column=1, padx=5, pady=5)

Statement_of_Purpose_Rating_var = tk.StringVar()
Statement_of_Purpose_Rating_entrybox = ttk.Entry(Predict_cut_frame, width=20,
                                                 textvariable=Statement_of_Purpose_Rating_var)
Statement_of_Purpose_Rating_entrybox.grid(row=3, column=1, padx=5, pady=5)

Letter_of_Recommendation_Strength_var = tk.StringVar()
Letter_of_Recommendation_Strength_entrybox = ttk.Entry(Predict_cut_frame, width=20,
                                                       textvariable=Letter_of_Recommendation_Strength_var)
Letter_of_Recommendation_Strength_entrybox.grid(row=4, column=1, padx=5, pady=5)

CGPA_var = tk.StringVar()
CGPA_employed_entrybox = ttk.Entry(Predict_cut_frame, width=20, textvariable=CGPA_var)
CGPA_employed_entrybox.grid(row=5, column=1, padx=5, pady=5)

Research_var = tk.StringVar()
Research_entrybox = ttk.Entry(Predict_cut_frame, width=20, textvariable=Research_var)
Research_entrybox.grid(row=6, column=1, padx=5, pady=5)

# create combobox

University_Rating_var = tk.StringVar()
University_Rating_combobox = ttk.Combobox(Predict_cut_frame, width=17, textvariable=University_Rating_var,
                                          state='readonly')
University_Rating_combobox['values'] = ('1', '2', '3', '4', '5')
# University_Rating_combobox.current(0)
University_Rating_combobox.grid(row=2, column=1)

Research_var = tk.StringVar()
Research_combobox = ttk.Combobox(Predict_cut_frame, width=17, textvariable=Research_var, state='readonly')
Research_combobox['values'] = ('Yes', 'No')
# University_Rating_combobox.current(0)
Research_combobox.grid(row=6, column=1)

# create a button label
label_frame = ttk.LabelFrame(Predict_cut_frame, text='submit')
label_frame.grid(row=8, column=0, padx=100)

name_label = ttk.Label(Predict_cut_frame)
name_label.grid(row=8, column=0, sticky=tk.W, padx=160, pady=10)


# user_info = {'Enter the GRE Score':tk.StringVar(),
# 'Enter the TOEFL Score':tk.StringVar(),
# 'Enter the University Rating':tk.StringVar(),
# 'Enter the SOP':tk.StringVar(),
# 'Enter the LOR':tk.StringVar(),
# 'Enter the CGPA':tk.StringVar(),
# 'Have you done Research':tk.StringVar()
# }
# counter=0
# for i in user_info:
#   cur_entrybox = 'entry' + i # entryname # entryage
#  cur_entrybox = ttk.Entry(Predict_cut_frame, width=16, textvariable=user_info[i])
# cur_entrybox.grid(column=0, row=counter)
# counter += 1


b1 = tk.Button(Predict_cut_frame, text="Predict", command=Predict)
b1.grid(row=8, column=0)


# create third page


# create a button label
# label_frame = ttk.LabelFrame(Predict_reset_frame, text='Predict')
# label_frame.grid(row=4, column=0, padx=100)

# name_label = ttk.Label(Predict_reset_frame)
# name_label.grid(row=4, column=0, sticky=tk.W, padx=160, pady=10)

def myclick():
    hello = "Hello" + Text_Here.get()  # change
    myLabel = Label(Predict_reset_frame, text=hello)


# myLabel.pack()

# create combobox
Text_Here_var = tk.StringVar()
Text_Here_entrybox = ttk.Entry(Predict_reset_frame, width=20, textvariable=Text_Here_var, font=('gotham', 24))
Text_Here_entrybox.grid(row=3, column=0, padx=5, pady=5)
Text_Here_entrybox.focus()

# create labels
name_label = ttk.Label(Predict_reset_frame, text='Enter Your Text Here')
name_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

myButton = Button(Predict_reset_frame, text="Predict", command=myclick)
myButton.grid(row=4, column=0)
# myButton.pack()




win.mainloop()
