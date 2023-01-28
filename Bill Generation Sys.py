from tkinter import *
import random, math, os
import tempfile
from tkinter import messagebox

# import random
class Bill_Soft:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1280x720+0+0')
        
        self.root.title('Bill Generation')
        bg_colour = 'teal'
        title = Label(self.root, text='Welcome to Food Plaza', bd=7, relief=GROOVE, bg=bg_colour, fg='orange',font=('times new roman', 37, 'bold'), pady=10).pack(fill=X)
        # variables
        # food
        self.dosa = IntVar()
        self.idli = IntVar()
        self.pizza = IntVar()
        self.bhaji = IntVar()
        self.samosa = IntVar()

        # cold drink
        self.thums = IntVar()
        self.sprite = IntVar()
        self.pepsi = IntVar()
        self.maaza = IntVar()
        self.limca = IntVar()

        # total,tax
        self.sub_total = StringVar()
        self.tax = StringVar()
        self.total_amount=StringVar

        # customer
        self.cname = StringVar()
        self.cphn = StringVar()
        self.bill = StringVar()
        r = random.randint(100, 999)
        self.bill.set(str(r))
        

        # cutomer details
        f1 = LabelFrame(self.root, bd=7, relief=GROOVE, text='Customer Details', font=('times new roman', 15, 'bold'),fg='gold', bg=bg_colour)
        f1.place(x=0, y=90, relwidth=1)

        cname_label = Label(f1, text='Cutomer Name', bg=bg_colour, fg='white',font=('times new roman', 19, 'bold')).grid(row=0, column=0, padx=25, pady=13)
        cname_txt = Entry(f1, width=16, textvariable=self.cname, font='arial 15', bd=6, relief=SUNKEN).grid(row=0,column=1,padx=10,pady=13)

        cphn_label = Label(f1, text='Phone No.', bg=bg_colour, fg='white', font=('times new roman', 19, 'bold')).grid(row=0, column=3, padx=25, pady=13)
        cphn_txt = Entry(f1, width=16, textvariable=self.cphn, font='arial 15', bd=6, relief=SUNKEN).grid(row=0,column=4,padx=10,pady=13)

        bill_label = Label(f1, text='Bill No.', bg=bg_colour, fg='white', font=('times new roman', 19, 'bold')).grid(row=0, column=5, padx=25, pady=13)
        bill_txt = Entry(f1, width=14,font='arial 15', bd=6, relief=SUNKEN).grid(row=0,column=6,padx=10,pady=13)

        
        # FOOD FRAME
        f2 = LabelFrame(self.root, bd=7, relief=GROOVE, text='Food Items', font=('times new roman', 15, 'bold'),fg='gold', bg=bg_colour)
        f2.place(x=0, y=184, width=425, height=376)

        dosa_lbl = Label(f2, text='Dosa', font=('times new roman', 20, 'bold'), bg=bg_colour, fg='white').grid(row=0,column=0,padx=16,pady=15)
        dosa_txt = Entry(f2, width=17, textvariable=self.dosa, font='arial 15', bd=5, relief=SUNKEN).grid(row=0,column=1,padx=16,pady=15)

        idli_lbl = Label(f2, text='Idli', font=('times new roman', 20, 'bold'), bg=bg_colour, fg='white').grid(row=1,column=0,padx=16,pady=15)
        idli_txt = Entry(f2, width=17, textvariable=self.idli, font='arial 15', bd=5, relief=SUNKEN).grid(row=1,column=1,padx=16,pady=15)

        pizza_lbl = Label(f2, text='Pizza', font=('times new roman', 20, 'bold'), bg=bg_colour, fg='white').grid(row=2,column=0,padx=16,pady=15)
        pizza_txt = Entry(f2, width=17, textvariable=self.pizza, font='arial 15', bd=5, relief=SUNKEN).grid(row=2,column=1,padx=16,pady=15)

        bhaji_lbl = Label(f2, text='Pav bhaji', font=('times new roman', 20, 'bold'), bg=bg_colour, fg='white').grid(row=3, column=0, padx=16, pady=15)
        bhaji_txt = Entry(f2, width=17, textvariable=self.bhaji, font='arial 15', bd=5, relief=SUNKEN).grid(row=3,column=1,padx=16,pady=15)

        samosa_lbl = Label(f2, text='Samosa', font=('times new roman', 20, 'bold'), bg=bg_colour, fg='white').grid(row=4, column=0, padx=16, pady=15)
        samosa_txt = Entry(f2, width=17, textvariable=self.samosa, font='arial 15', bd=5, relief=SUNKEN).grid(row=4,column=1,padx=16,pady=15)

        # cold drink frame
        f3 = LabelFrame(self.root, bd=7, relief=GROOVE, text='Cold Drinks', font=('times new roman', 15, 'bold'),fg='gold', bg=bg_colour)
        f3.place(x=425, y=184, width=425, height=376)

        thums_lbl = Label(f3, text='Thums Up', font=('times new roman', 20, 'bold'), bg=bg_colour, fg='white').grid(row=0, column=0, padx=16, pady=15)
        thums_txt = Entry(f3, width=17, textvariable=self.thums, font='arial 15', bd=5, relief=SUNKEN).grid(row=0,column=1,padx=16,pady=15)

        sprite_lbl = Label(f3, text='Sprite', font=('times new roman', 20, 'bold'), bg=bg_colour, fg='white').grid(row=1, column=0, padx=16, pady=15)
        sprite_txt = Entry(f3, width=17, textvariable=self.sprite, font='arial 15', bd=5, relief=SUNKEN).grid(row=1,column=1,padx=16,pady=15)

        pepsi_lbl = Label(f3, text='Pepsi', font=('times new roman', 20, 'bold'), bg=bg_colour, fg='white').grid(row=2,column=0,padx=16,pady=15)
        pepsi_txt = Entry(f3, width=17, textvariable=self.pepsi, font='arial 15', bd=5, relief=SUNKEN).grid(row=2,column=1,padx=16,pady=15)

        maaza_lbl = Label(f3, text='Maaza', font=('times new roman', 20, 'bold'), bg=bg_colour, fg='white').grid(row=3,column=0,padx=16,pady=15)
        maaza_txt = Entry(f3, width=17, textvariable=self.maaza, font='arial 15', bd=5, relief=SUNKEN).grid(row=3,column=1,padx=16,pady=15)

        limca_lbl = Label(f3, text='Limca', font=('times new roman', 20, 'bold'), bg=bg_colour, fg='white').grid(row=4,column=0,padx=16,pady=15)
        limca_txt = Entry(f3, width=17, textvariable=self.limca, font='arial 15', bd=5, relief=SUNKEN).grid(row=4,column=1,padx=16,pady=15)

        # bill area
        f4 = Frame(self.root, bd=6,relief=GROOVE)
        f4.place(x=850, y=185,width=430, height=374)
        bill_title = Label(f4, text='Bill Area', font=' arial 15 bold', bd=7,relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(f4, orient=VERTICAL)
        self.txt = Text(f4, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txt.yview)
        self.txt.pack(fill=BOTH, expand=1)

        # buttonframe
        f5 = Frame(self.root, bd=7, relief=GROOVE, bg=bg_colour)
        f5.place(x=0, y=560, relwidth=1, height=150)

        sub_lbl = Label(f5, text='Sub Total', bg=bg_colour, fg='white', font=('times new roman', 20, 'bold')).grid(row=0, column=0, padx=16, pady=15)
        sub_txt = Entry(f5, width=18, textvariable=self.sub_total, font='arial 10 bold', bd=7, relief=SUNKEN).grid(row=0,column=1,padx=6,pady=15)

        tax_lbl = Label(f5, text='Tax', bg=bg_colour, fg='white', font=('times new roman', 20, 'bold')).grid(row=1,column=0,padx=16,pady=13)
        tax_txt = Entry(f5, width=18, textvariable=self.tax, font='arial 10 bold', bd=7, relief=SUNKEN).grid(row=1,column=1,padx=6,pady=13)

        btn_f = Frame(f5, bd=7, relief=GROOVE)
        btn_f.place(x=320, width=947, height=137)


        total_btn = Button(btn_f, text='Total', command=self.total, bg='cadetblue', fg='white', bd=2, pady=11, width=12,font='arial 18 bold').grid(row=0, column=0, padx=21, pady=25)
        Gbill_btn = Button(btn_f, text='Generate Bill', command=self.bill_area, bg='cadetblue', fg='white', bd=2, pady=13, width=12,font='arial 18 bold').grid(row=0, column=1, padx=21, pady=25)
        save_btn = Button(btn_f, text='Save', command=self.save_bill,bg='cadetblue', fg='white', bd=2, pady=11, width=12,font='arial 18 bold').grid(row=0, column=3, padx=21, pady=25)
        clear_btn = Button(btn_f, text='Clear',command=self.clear_data, bg='red', fg='white', bd=2, pady=11, width=12,font='arial 18 bold').grid(row=0, column=4, padx=21, pady=25)
        
        self.welcome()
    def total(self):
        self.d_r=float(self.dosa.get() * 80)
        self.i_r=float(self.idli.get() * 40)
        self.pi_r=float(self.pizza.get() * 120)
        self.pa_r=float(self.bhaji.get() * 60)
        self.s_r=float(self.samosa.get() * 30)
        self.t_r=float(self.thums.get() * 25)
        self.sp_r=float(self.sprite.get() * 25)
        self.pe_r=float(self.pepsi.get() * 25)
        self.m_r=float(self.maaza.get() * 25)
        self.li_r=float(self.limca.get() * 25)
        self.total_sub_total = float(
                    (self.d_r) +
                    (self.i_r) +
                    (self.pi_r) +
                    (self.pa_r) +
                    (self.s_r)+
                    (self.t_r) +
                    (self.sp_r) +
                    (self.pe_r) +
                    (self.m_r) +
                    (self.li_r)
                     )

        self.sub_total.set('Rs.'+str(self.total_sub_total))
        self.t_tax=round((self.total_sub_total*0.1),2)
        self.tax.set('Rs.'+str(self.t_tax))

        #total amount
        self.total_amount=self.total_sub_total+self.t_tax
    def welcome(self):
        self.txt.delete(1.0,END)
        self.txt.insert(END,'\t            \tFood Plaza')
        self.txt.insert(END, '\n-------------------------------------------------')
        self.txt.insert(END,f'\n Bill No.:{self.bill.get()}')
        self.txt.insert(END, f'\n Customer Name :{self.cname.get()}')

        self.txt.insert(END,'\n-------------------------------------------------')
        self.txt.insert(END,f'\n Products\t\t\tQty\t\tRate')
        self.txt.insert(END, '\n-------------------------------------------------')


    def bill_area(self):
        if self.cname.get()=='' or self.cphn.get()=='':
            messagebox.showerror('Error','Please fill Customer Details.')

        elif self.sub_total.get()=='' and self.tax.get()=='':
            messagebox.showerror('Error','Please select the product.')
        else:
            self.welcome()
            #food
            if self.dosa.get()!=0:
                self.txt.insert(END,f'\n Dosa \t\t\t{self.dosa.get()}\t\t{self.d_r}')
            if self.idli.get()!=0:
                self.txt.insert(END,f'\n Idli \t\t\t{self.idli.get()}\t\t{self.i_r}')
            if self.pizza.get()!=0:
                self.txt.insert(END,f'\n Pizza \t\t\t{self.pizza.get()}\t\t{self.pi_r}')
            if self.bhaji.get()!=0:
                self.txt.insert(END,f'\n Pav Bhaji \t\t\t{self.bhaji.get()}\t\t{self.pa_r}')
            if self.samosa.get()!=0:
                self.txt.insert(END,f'\n Samosa \t\t\t{self.samosa.get()}\t\t{self.s_r}')
            #cold drink
            if self.thums.get()!=0:
                self.txt.insert(END,f'\n Thums Up \t\t\t{self.thums.get()}\t\t{self.t_r}')
            if self.sprite.get()!=0:
                self.txt.insert(END,f'\n Sprite \t\t\t{self.sprite.get()}\t\t{self.sp_r}')
            if self.pepsi.get()!=0:
                self.txt.insert(END,f'\n Pepsi \t\t\t{self.pepsi.get()}\t\t{self.pe_r}')
            if self.maaza.get()!=0:
                self.txt.insert(END,f'\n Mazza \t\t\t{self.maaza.get()}\t\t{self.m_r}')
            if self.limca.get()!=0:
                self.txt.insert(END,f'\n Limca \t\t\t{self.limca.get()}\t\t{self.li_r}')

            self.txt.insert(END, '\n-------------------------------------------------')
            self.txt.insert(END, f'\n Sub Total\t\t\t\t     {self.sub_total.get()}')
            self.txt.insert(END, f'\n Tax\t\t\t\t     {self.tax.get()}')
            self.txt.insert(END, '\n=================================================')
            self.txt.insert(END, f'\n Total Amount\t\t\t\t     Rs.{self.total_amount}')

    def save_bill(self):
        ask=messagebox.askyesno('Save Bill','Do you want to save the bill?')
        if ask>0:
            self.bill_data=self.txt.get('1.0',END)
            b_n=open('Bills/'+str(self.bill.get())+'.txt','w')
            b_n.write(self.bill_data)
            op=messagebox.showinfo('Saved',f'Bill No.:{self.bill.get()} saved successfully.')
            b_n.close()
        else:
            return
    
    
    def clear_data(self):
        
            self.txt.delete(1.0,END)
            self.dosa.set(0)
            self.idli.set(0)
            self.pizza.set(0)
            self.bhaji.set(0)
            self.samosa.set(0)

            # cold drink
            self.thums.set(0)
            self.sprite.set(0)
            self.pepsi.set(0)
            self.maaza.set(0)
            self.limca.set(0)

            # total,tax
            self.sub_total.set('')
            self.tax.set('')


            # customer
            self.cname.set('')
            self.cphn.set('')
            self.bill.set('')
            r = random.randint(100, 999)
            self.bill.set(str(r))
            self.welcome()

    

root = Tk()
obj = Bill_Soft(root)
root.mainloop()
