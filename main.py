
# CREATED BY: AKABharat
# CREATED DATE TIME: 2025-10-29 10:00:15

# importing modules
import tkinter as tk;
from tkinter import Label;
from tkinter import Button;

# font variables
DISPLAY_FONT = ("Verdana", 40)
BTN_FONT = ("Verdana", 20)

# creating main application window with configs
root = tk.Tk();
root.title("Calculator");
root.configure(background="#161616");
root.geometry("349x492")
root.resizable(False, False); # or root.resizable(0,0)

# display for output and number showing
display_label = Label(root, text="");
display_label.config(font= DISPLAY_FONT, bg="#161616", fg="#FFFFFF");
display_label.grid(row=0, column=0, columnspan=4, pady=(50,50), padx=(5,5))

# holds all button in a list for handling state config
number_buttons = []; 

# variables for holding operands and operator
first_num = second_num = operator = None;

# function for handling user's number entered
def digit_handle(val):
  current_val = display_label['text'];
  new_val = current_val + str(val);
  display_label.config(text=new_val);
  btn_enter.config(state='normal');

# function for clearning screen and data holding variables
def clear_handle():
  global first_num, second_num,operator;
  display_label.config(text='');
  first_num = second_num = operator = None;
  btn_enter.config(state='normal');
  for button in number_buttons:
    button.config(state = 'normal');

# function for handling operator entered
def operator_handle(oper):
  global first_num, operator;
  operator = oper;
  if (display_label['text']) != '':
    first_num = int(display_label['text']);
  display_label.config(text='');
  btn_enter.config(state='normal');
  for button in number_buttons:
    button.config(state = 'normal');

# function for handling result calculation
def result_handle():
  global first_num, second_num, operator;
  result='';
  if (display_label['text']) != '':
    second_num = int(display_label['text']);
  if(first_num != None and second_num != None):
    match(operator):
      case '+': 
        result = first_num + second_num;
      case '-':
        result = first_num - second_num;
      case '/':
        if(second_num == 0):
          result = 'Error';
        else:
          result = first_num / second_num;
      case 'x':
        result = first_num * second_num;
      case _:
        result = '';
    display_label.config(text = result);
    btn_enter.config(state='disabled');
    for button in number_buttons:
      button.config(state = 'disabled');

# ROW 1 ---------------------------------------------------------------
btn_9  = Button(root, text='9', width=3, height=1, padx=11, pady=10, font=BTN_FONT, bg='#2D3037', fg='white', command= lambda:digit_handle(9))
btn_9.grid(row=1, column=0, padx=3, pady=3)

btn_8  = Button(root, text='8', width=3, height=1,padx=11, pady=10, font=BTN_FONT, bg='#2D3037', fg='white', command= lambda:digit_handle(8))
btn_8.grid(row=1, column=1, padx=3, pady=3)

btn_7  = Button(root, text='7', width=3, height=1, padx=11, pady=10, font=BTN_FONT, bg='#2D3037', fg='white', command= lambda:digit_handle(7))
btn_7.grid(row=1, column=2, padx=3, pady=3)

btn_add  = Button(root, text='+', width=3, height=1, padx=11, pady=10, font=BTN_FONT, bg='#4A4A4F', fg='white', command= lambda: operator_handle('+'))
btn_add.grid(row=1, column=3, padx=3, pady=3)
# ROW 2 ---------------------------------------------------------------
btn_6  = Button(root, text='6', width=3, height=1, padx=11, pady=10, font=BTN_FONT, bg='#2D3037', fg='white', command= lambda:digit_handle(6))
btn_6.grid(row=2, column=0, padx=3, pady=3)

btn_5  = Button(root, text='5', width=3, height=1, padx=11, pady=10, font=BTN_FONT, bg='#2D3037', fg='white', command= lambda:digit_handle(5))
btn_5.grid(row=2, column=1, padx=3, pady=3)

btn_4  = Button(root, text='4', width=3, height=1, padx=11, pady=10, font=BTN_FONT, bg='#2D3037', fg='white', command= lambda:digit_handle(4))
btn_4.grid(row=2, column=2, padx=3, pady=3)

btn_multi  = Button(root, text='x', width=3, height=1, padx=11, pady=10, font=BTN_FONT, bg='#4A4A4F', fg='white', command= lambda: operator_handle('x'))
btn_multi.grid(row=2, column=3, padx=3, pady=3)
# ROW 3 ---------------------------------------------------------------
btn_3  = Button(root, text='3', width=3, height=1, padx=11, pady=10, font=BTN_FONT, bg='#2D3037', fg='white', command= lambda:digit_handle(3))
btn_3.grid(row=3, column=0, padx=3, pady=3)

btn_2  = Button(root, text='2', width=3, height=1, padx=11, pady=10, font=BTN_FONT, bg='#2D3037', fg='white', command= lambda:digit_handle(2))
btn_2.grid(row=3, column=1, padx=3, pady=3)

btn_1  = Button(root, text='1', width=3, height=1, padx=11, pady=10, font=BTN_FONT, bg='#2D3037', fg='white', command= lambda:digit_handle(1))
btn_1.grid(row=3, column=2, padx=3, pady=3)

btn_sub  = Button(root, text='-', width=3, height=1, padx=11, pady=10, font=BTN_FONT, bg="#4A4A4F", fg='white', command= lambda: operator_handle('-'))
btn_sub.grid(row=3, column=3, padx=3, pady=3)
# ROW 4 ---------------------------------------------------------------
btn_0  = Button(root, text='0', width=3, height=1, padx=11, pady=10, font=BTN_FONT, bg='#2D3037', fg='white', command= lambda:digit_handle(0))
btn_0.grid(row=4, column=0, padx=3, pady=3)

btn_clear  = Button(root, text='Clear', width=3, height=1, padx=11, pady=10, font=BTN_FONT, bg='#008442', fg='white', command= lambda: clear_handle())
btn_clear.grid(row=4, column=1, padx=3, pady=3)

btn_enter  = Button(root, text='Enter', width=3, height=1, padx=11, pady=10, font=BTN_FONT, bg="#830027", fg='white', command= result_handle)
btn_enter.grid(row=4, column=2, padx=3, pady=3)

btn_div  = Button(root, text='/', width=3, height=1, padx=11, pady=10, font=BTN_FONT, bg="#4A4A4F", fg='white', command= lambda: operator_handle('/'))
btn_div.grid(row=4, column=3, padx=3, pady=3)

# storing all buttons in list
number_buttons.extend([btn_9, btn_8, btn_7, btn_6, btn_5, btn_4, btn_3, btn_2, btn_1, btn_0]);

# start the tkinter event loop and keep the window open and resposive
root.mainloop();
