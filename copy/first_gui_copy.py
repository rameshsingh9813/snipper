from tkinter import *
import pyperclip



ws = Tk()

t_n = "Autosnipper"  # title name
s_a = '300x420'  # canvas size of application
bg_c = '#F1F1F5'  # background color of application
fg_c_f = '#C8C7C7'  # foreground color of footer_w
fg_c_l = '#373737'  # foreground color of label
fg_c_e = '#9D9B9B'  # foreground color of entry
i_l = 'C:/Users/hp/Desktop/code_practise/day_17 screenshot taker  modification/modification of screenshot ' \
      'taker/image_file/icon_7.png'  # icon link

ws.title(t_n)
ws.geometry(s_a)
ws['bg'] = bg_c
p1 = PhotoImage(file=i_l)
ws.iconphoto(False, p1)  # setting of icon
pasted = pyperclip.paste()







def printvalue():
    paths = file_path.get()
    print(paths)
    return paths


Label(ws,
      text="Path *",
      fg=fg_c_l,
      # bg=fg_c_l,
      font=('Times', 15),
      height=2,
      width=25,
      # relief="solid",
      bd=1,
      anchor="sw",
      justify=LEFT).pack()

file_path = Entry(ws,
                  width=33,
                  fg=fg_c_l,
                  font='Arial 11'
                  )

file_path.insert(0, pasted)
file_path.pack(ipadx=5, ipady=5)
print(file_path.get())

Label(ws,
      text="Size",
      fg=fg_c_l,
      # bg=fg_c_l,
      font=('Times', 15),
      height=2,
      width=25,
      # relief="solid",
      bd=1,
      anchor="sw",
      justify=LEFT).pack()

im_size = Entry(ws,
                  width=33,
                  fg=fg_c_e,
                  font='Arial 11'
                  )
im_size.insert(0, '345, 85, 855, 535')
im_size.pack(ipadx=5, ipady=5)
print(im_size.get())

Button(ws,
       text="Start",
       width=20,
       command=ws.destroy).pack(pady=10, padx=10, ipady=5)

Label(ws,
      text="@C2023 Developed by ramesh kr. mahato \n         rameshsingh9813@gmail.com",
      fg=fg_c_f,
      bg=bg_c,
      # font=('Times', 15),
      height=13,
      width=40,
      # relief="solid",
      bd=1,
      anchor="s",
      justify=LEFT).pack()
ws.mainloop()
