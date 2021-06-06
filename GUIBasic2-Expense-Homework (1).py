# GUIBasic2-Expense.py
from tkinter import *
from tkinter import ttk, messagebox
import csv
from datetime import datetime
# ttk is theme of Tk

GUI = Tk()
GUI.title('ໂປຣເເກຣມບັນທຶກຄ່າໃຊ້ຈ່າຍ by Uncle Media')
GUI.geometry('500x700+500+50')

# B1 = Button(GUI,text='Hello')
# B1.pack(ipadx=50,ipady=20) #.pack() ติดปุ่มเข้ากับ GUI หลัก

#########################MENU#########################

menubar = Menu(GUI)
GUI.config(menu=menubar)

#file menu
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='import CSV')
filemenu.add_command(label='Export to Googlesheet')
#help menu
def About():
    messagebox.showinfo('About','ສະບາຍດີທຸກທ່ານ\nຫາກສົນໃຈຊ່ວຍເຫລືອພວກເຮົາສາມາດຕິດຕໍ່ພວກເຮົາໄດ້ທີ່\nເເຟນເພຈ:@Unclemedia0')
helpmenu = Menu(menubar,tearoff=0) 
menubar.add_cascade(label='Help',menu=helpmenu)
#Donate
donatmenu = Menu(menubar,tearoff=0) 
menubar.add_cascade(label='Donate',menu=donatmenu)
helpmenu.add_command(label='About',command=About)

##################################################

Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
Tab.pack(fill=BOTH,expand=1)

icon_1 = PhotoImage(file='t1_money.png')
icon_2 = PhotoImage(file='t2_story.png')
icon_3 = PhotoImage(file='t3_save.png')


Tab.add(T1, text=f'{"ເພີມລາຍການ":^{30}}',image=icon_1,compound='top')
Tab.add(T2, text=f'{"ຄ່າໃຊ້ຈ່າຍທັ້ງໝົດ":^{30}}',image=icon_2,compound='top')




F1 = Frame(T1)
F1.pack()

days = {'Mon':'ຈັນ',
        'Tue':'ອັງຄານ',
        'Wed':'ພຸດ',
        'Thu':'ພະຫັດ',
        'Fri':'ສຸກ',
        'Sat':'ເສົາ',
        'Sun':'ທິດ'}

def Save(event=None):
    expense = v_expense.get()
    price = v_price.get()
    quantity = v_quantity.get()

    if expense =='':
        print('No! Data')
        messagebox.showwarning('ERROR','ກະລຸນາກອຂໍ້ມູນສີນຄ້າ')
        return
    elif price == '':
        messagebox.showwarning('ERROR','ກະລຸນາກອກລາຄາສີນຄ້າ')
        return
    elif quantity == '':
        messagebox.showwarning('ERROR','ກະລຸນາກອກຈຳນວນສີນຄ້າ')
        return
    total = float(price) * float(quantity)

    try:
        total = float(price) * float(quantity)
        # .get() คือดึงค่ามาจาก v_expense = StringVar()
        print('ລາຍການ: {} ລາຄາ: {}'.format(expense,price))
        print('ຈຳນວນ: {} ລວມທັ້ງໝົດ: {} ກີບ'.format(quantity,total))
        text = 'ລາຍການ: {} ລາຄາ: {}\n'.format(expense,price)
        text = text + 'ຈຳນວນ: {} ລວມທັ້ງໝົດ: {} ກີບ'.format(quantity,total)
        v_result.set(text)
        # clear ข้อมูลเก่า
        v_expense.set('')
        v_price.set('')
        v_quantity.set('')

        # บันทึกข้อมูลลง csv อย่าลืม import csv ด้วย
        today = datetime.now().strftime('%a') # days['Mon'] = 'จันทร์'
        print(today)
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        dt = days[today] + '-' + dt
        with open('savenote.csv','a',encoding='utf-8',newline='') as f:
            # with คือสั่งเปิดไฟล์แล้วปิดอัตโนมัติ
            # 'a' การบันทึกเรื่อยๆ เพิ่มข้อมูลต่อจากข้อมูลเก่า
            # newline='' ทำให้ข้อมูลไม่มีบรรทัดว่าง
            fw = csv.writer(f) #สร้างฟังชั่นสำหรับเขียนข้อมูล
            data = [dt,expense,price,quantity,total]
            fw.writerow(data)

        # ทำให้เคอเซอร์กลับไปตำแหน่งช่องกรอก E1
        E1.focus()
        update_table()
    except Exception as e:

        print('ERROR',e)
        messagebox.showwarning('ERROR','ກະລຸນາກອກຂໍ້ມູນໃໝ່')
        v_expense.set('')
        v_price.set('')
        v_quantity.set('')

# ทำให้สามารถกด enter ได้
GUI.bind('<Return>',Save) #ต้องเพิ่มใน def Save(event=None) ด้วย

FONT1 = ('Phetsarath OT',20) # None เปลี่ยนเป็น 'Angsana New'

main_icon = PhotoImage(file='t5.png')
Main_icon = Label(F1,image=main_icon)
Main_icon.pack()
#------text1--- -----
L = Label(F1,text='ລາຍການຄ່າໃຊ້ຈ່າຍ',font=FONT1).pack()
v_expense = StringVar()
# StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E1 = Entry(F1,textvariable=v_expense,font=FONT1)
E1.pack()
#-------------------

#------text2--------
L = Label(F1,text='ລາຄາ (ບາທ)',font=FONT1).pack()
v_price = StringVar()
# StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E2 = Entry(F1,textvariable=v_price,font=FONT1)
E2.pack()
#-------------------

#------text3--------
L = Label(F1,text='ຈຳນວນ (ຊີ້ນ)',font=FONT1).pack()
v_quantity = StringVar()
# StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E3 = Entry(F1,textvariable=v_quantity,font=FONT1)
E3.pack()
#-------------------

B2 = Button(F1,text='Save',image=icon_3,compound='top',command=Save)
B2.pack(ipadx=30,ipady=10,padx=10,pady=20)

v_result = StringVar()
v_result.set('------ສະເເດງຜົນລັບ----')
result = Label(F1,textvariable=v_result,font=FONT1,fg='green')
result.pack(pady=20)

############# Tab2 ####################

def read_csv():
    with open('savenote.csv',newline='',encoding='utf-8') as f:
        fr = csv.reader(f)
        data = list(fr)
    return data
        #print(data)
        #print('-------')
        #print(data[0][0])
        #for a,b,c,d,e in data:
        #    print(b)
#rs = read_csv()
#print(rs[3])

# table #
L = Label(T2,text='ຕາລາງສະເເດງຜົນລັບທັງໝົດ',font=FONT1).pack()
header = ['ວັນ - ເວລາ','ລາຍການ','ຄ່າໃຊ້ຈ່າຍ','ຈຳນວນ','ລວມ']
resulttable = ttk.Treeview(T2,column=header,show='headings',height=20)
resulttable.pack()

#for i in range(len(header)):
#    resulttable.heading(header[i],text=header[i])
for h in header:
    resulttable.heading(h,text=h)
headerwidth = [200,150,100,80,80]
for h,w in zip(header,headerwidth):
    resulttable.column(h,width=w)

 

'''
resulttable.heading(header[0],text=header[0])
resulttable.heading(header[1],text=header[1])
resulttable.heading(header[2],text=header[2])
resulttable.heading(header[3],text=header[3])
resulttable.heading(header[4],text=header[4])
'''
#resulttable.insert('',0,value=['จันทร์','น้ำดืม',100000,5,150])
#resulttable.insert('','end',value=['อังคาร','น้ำดืม',100000,5,150])



def update_table():
    resulttable.delete(*resulttable.get_children())
    data = read_csv()
    for d in data:
        resulttable.insert('',0,value=d)
    #print(data)
update_table()
print('GET CHILD:',resulttable.get_children())



GUI.bind('<Tab>',lambda x: E2.focus())
GUI.mainloop()
