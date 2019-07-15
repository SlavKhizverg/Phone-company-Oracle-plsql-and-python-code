from tkinter import *
import datetime
from tkinter import messagebox
import cx_Oracle

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x600")

    global firstname
    global lastname
    global id
    global email
    global phone
    global numoflines
    global creditcard
    global package
    global broadband

    global firstname_entry
    global lastname_entry
    global id_entry
    global email_entry
    global phone_entry
    global numoflines_entry
    global creditcard_entry
    global package_entry
    global broadband_entry

    firstname = StringVar()
    lastname = StringVar()
    id = StringVar()
    email = StringVar()
    phone = StringVar()
    numoflines = IntVar()
    creditcard = StringVar()
    package = StringVar()
    broadband = IntVar()

    Label(register_screen, text="Please enter details below", font="Times 15").pack()
    Label(register_screen, text="").pack()
    id_lable = Label(register_screen, text="Id",font="Times 10")
    id_lable.pack()
    id_entry = Entry(register_screen, textvariable=id)
    id_entry.pack()
    firstname_label = Label(register_screen, text="First Name",font="Times 10")
    firstname_label.pack()
    firstname_entry = Entry(register_screen, textvariable=firstname)
    firstname_entry.pack()
    lastname_label = Label(register_screen, text="Last Name",font="Times 10")
    lastname_label.pack()
    lastname_entry = Entry(register_screen, textvariable=lastname)
    lastname_entry.pack()
    email_label = Label(register_screen, text="Email",font="Times 10")
    email_label.pack()
    email_entry = Entry(register_screen, textvariable=email)
    email_entry.pack()

    phone_label = Label(register_screen, text="Phone Number",font="Times 10")
    phone_label.pack()
    phone_entry = Entry(register_screen, textvariable=phone)
    phone_entry.pack()



    package_label = Label(register_screen, text="Package",font="Times 10")
    package_label.pack()
    package_label.pack()
 #   package_entry = Entry(register_screen, textvariable=package)
  #  package_entry.pack()

    MODES = [
        ("Gold", "Gold"),
        ("Silver", "Silver"),
        ("Regular", "Regular"),
    ]

    package.set("Regular")

    for text, mode in MODES:
        b = Radiobutton(register_screen, text=text,
                        variable=package, value=mode)
        b.pack(anchor=S)
    broadband_label = Label(register_screen, text="Broadband",font="Times 10")
    broadband_label.pack()

    MODES = [
        ("25", 25),
        ("15", 15),
        ("5", 5),
    ]

    package.set("Regular")

    for text, mode in MODES:
        b = Radiobutton(register_screen, text=text,
                        variable=broadband, value=mode)
        b.pack(anchor=S)
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width="10", height="1", bg="azure", command=register_user).pack()
    Button(register_screen, text="Show", font="Times 10", width="10", height="1", bg="azure",
           command=subscribers).pack(side=BOTTOM, anchor=W)
def register_user():

    id_info = id.get()
    firstname_info = firstname.get()
    lastname_info = lastname.get()
    email_info = email.get()

    phone_info = phone.get()
    credit_info = '7'
    package_info = package.get()
    broadband_info = broadband.get()

    dsn_tns = cx_Oracle.makedsn('localhost', '1521', 'xe')
    conn = cx_Oracle.connect(username1, password1, dsn_tns)
    try:
        c = conn.cursor()

        c.callproc("system.REGISTER_NEW_SUBSCRIBER",
                        [id_info, firstname_info, lastname_info, email_info, 1, phone_info,
                         credit_info, package_info, broadband_info])
        conn.commit()
        Label(register_screen,
              text=firstname_info + " " + lastname_info + " is added to\n our system with\n " + phone_info + " phone number", font="Times 15").pack()
    except:
        Label(register_screen,
              text="INVALID INPUT.\n PLEASE CHECK ONE OF \nTHE FOLLOWING:\nID,EMAIL,PHONE NUMBER", font="Times 8").pack()
        print(sys.exc_info())
    finally:
        conn.close()




def call_someone_screen():
    global call_screen
    call_screen = Toplevel(main_screen)
    call_screen.title("call_screen")
    call_screen.geometry("300x600")
    global out_call
    global in_call
    global out_call_entry
    global in_call_entry
    out_call = StringVar()
    in_call = StringVar()
    Label(call_screen, text="Please enter details below", font="Times 15").pack()
    Label(call_screen, text="").pack()
    Label(call_screen, text="Origin Line", font="Times 10").pack()


    out_call_entry = Entry(call_screen, textvariable=out_call)
    out_call_entry.pack()
    Label(call_screen, text="").pack()
    Label(call_screen, text="Destination Line", font="Times 10").pack()


    in_call_entry = Entry(call_screen, textvariable=in_call)
    in_call_entry.pack()
    Label(call_screen, text="").pack()
    Button(call_screen, text="CALL", width="10", height="1", bg="azure", command=callSomeone).pack()
def callSomeone():

    x = -1
    outcall = out_call.get()
    incall = in_call.get()
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', 'xe')
    conn = cx_Oracle.connect(username1, password1, dsn_tns)


    try:
        c = conn.cursor()
        c.callproc("system.ADD_CALL",
                   [outcall, incall])

        c.execute("SELECT STATUS FROM phone_numbers WHERE phone_number = '%s' " % outcall)
        for row in c:
            x = int(row[0])
        conn.commit()

        Label(call_screen , text="").pack()
        Label(call_screen , text="").pack()
        Label(call_screen , text="").pack()
        if (x == 1):
            Label(call_screen, text=outcall + " calls to " + incall, font="Times 15", ).pack()

        else:
            Label(call_screen, text=outcall + " is not activated ", font="Times 15").pack()
    # except:
    #     Label(call_screen,
    #           text="INVALID INPUT.\n PLEASE CHECK ONE OF \nTHE FOLLOWING:\nOrigin Line,Destination Line",
    #           font="Times 8").pack()

    finally:
        conn.close()


def sms_someone_screen():
    global sms_screen
    sms_screen = Toplevel(main_screen)
    sms_screen.title("sms_screen")
    sms_screen.geometry("300x600")
    global out_sms
    global in_sms
    global text
    global out_sms_entry
    global in_sms_entry
    out_sms = StringVar()
    in_sms = StringVar()
    text = StringVar()

    Label(sms_screen, text="Please enter details below", font="Times 15").pack()
    Label(sms_screen, text="").pack()
    Label(sms_screen, text="Origin Line", font="Times 10").pack()


    out_sms_entry = Entry(sms_screen, textvariable=out_sms)
    out_sms_entry.pack()
    Label(sms_screen, text="").pack()
    Label(sms_screen, text="Destiantion Line", font="Times 10").pack()
    in_sms_entry = Entry(sms_screen, textvariable=in_sms)
    in_sms_entry.pack()
    Label(sms_screen, text="").pack()
    Label(sms_screen, text="Text?", font="Times 10").pack()

    text_entry = Entry(sms_screen, textvariable=text)
    text_entry.pack()
    Label(sms_screen, text="").pack()
    Button(sms_screen, text="SMS", width="10", height="1", bg="azure", command=smsSomeone).pack()

def smsSomeone():

    outsms = out_sms.get()
    insms = in_sms.get()
    mytext = text.get()
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', 'xe')
    conn = cx_Oracle.connect(username1, password1, dsn_tns)
    try:
        c = conn.cursor()
        c.callproc("system.ADD_SMS",
                [outsms, insms,mytext])

        c.execute("SELECT STATUS FROM phone_numbers WHERE phone_number = '%s' " % outsms)
        for row in c:
            x = int(row[0])
        conn.commit()

        Label(sms_screen, text="").pack()
        Label(sms_screen, text="").pack()
        Label(sms_screen, text="").pack()
        if (x == 1):
            Label(sms_screen, text=outsms +" sent "+mytext+"\n to " + insms+" ", font="Times 15",).pack()

        else:
            Label(sms_screen, text=outsms + " is not activated ", font="Times 15").pack()

    except:
        Label(sms_screen,
              text="INVALID INPUT.\n PLEASE CHECK ONE OF \nTHE FOLLOWING:\nOrigin Line,Destination Line",
              font="Times 8").pack()

    finally:
        conn.close()



def phone_isactive_show():
    global disactivate_screen
    disactivate_screen = Toplevel(main_screen)
    disactivate_screen.title("disactivate_screen")
    disactivate_screen.geometry("300x600")

    global number
    global number_lable
    global number_entry
    global v
    number = StringVar()
    Label(disactivate_screen, text="Please enter details below", font="Times 15").pack()
    Label(disactivate_screen, text="").pack()
    Label(disactivate_screen, text="Please enter phone namber", font="Times 10").pack()



    number_entry = Entry(disactivate_screen, textvariable=number)
    number_entry.pack()

    MODES = [
        ("active", 1),
        ("diactive", 0),
    ]
    v = IntVar()
    v.set("active")

    for text, mode in MODES:
        b = Radiobutton(disactivate_screen, text=text,
                        variable=v, value=mode)
        b.pack(anchor=S)
    Button(disactivate_screen, text="PRESS", width="10", height="1", bg="azure", command=update_isActive).pack()
def update_isActive():

    number_info = number.get()
    activate_not = v.get()

    dsn_tns = cx_Oracle.makedsn('localhost', '1521', 'xe')
    conn = cx_Oracle.connect(username1, password1, dsn_tns)
    try:
        c = conn.cursor()
        c.callproc("system.NOT_ACTIVE_PHONE",
               [number_info,activate_not])
        conn.commit()

        if activate_not == 0:
            Label(disactivate_screen, text=number_info + " Disactivated", font="Times 15", ).pack()

        else:
            Label(disactivate_screen, text=number_info + " Activated", font="Times 15", ).pack()
    except:
        Label(disactivate_screen,
              text="INVALID INPUT.\n PLEASE CHECK IF\n THE ID IS VALID", font="Times 8", ).pack()

    finally:
        conn.close()



def delete_subscriber_screen():
    global delete_subscriber_screen
    delete_subscriber_screen = Toplevel(main_screen)
    delete_subscriber_screen.title("disactivate_screen")
    delete_subscriber_screen.geometry("300x600")

    global sub_id

    sub_id = StringVar()
    Label(delete_subscriber_screen, text="Please enter details below", font="Times 15").pack()
    Label(delete_subscriber_screen, text="").pack()
    Label(delete_subscriber_screen, text="Please enter subscriber id", font="Times 10").pack()


    sub_id_entry = Entry(delete_subscriber_screen, textvariable=sub_id)
    sub_id_entry.pack()
    Label(delete_subscriber_screen, text="").pack()

    Button(delete_subscriber_screen, text="PRESS", width="10", height="1", bg="azure", command=delete_subscriber).pack()
def delete_subscriber():

    s_id = sub_id.get()
    n=0
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', 'xe')
    conn = cx_Oracle.connect(username1, password1, dsn_tns)
    c = conn.cursor()
    c.execute("select SUBSCRIBER_ID from subscribers")
    for row in c:
        t = ''.join(row)
        if t == s_id:
            n = 1
    c.callproc("system.DELETE_SUBSCRIBER",
               [s_id])

    conn.commit()
    conn.close()
    Label(delete_subscriber_screen,text="",).pack()
    Label(delete_subscriber_screen, text="", ).pack()
    if n == 1:
        Label(delete_subscriber_screen, text=s_id + " removed from phone one hundred", font="Times 15", ).pack()
    else:
        Label(delete_subscriber_screen, text=s_id + " is not a subscriber in \n phone one hundred", font="Times 15", ).pack()

def add_line_screen():
    global line_screen
    line_screen = Toplevel(main_screen)
    line_screen.title("NEW LINE SCREEN")
    line_screen.geometry("300x600")
    global subscriber_id
    global new_phone_number
    global new_package
    global new_brodband
    global imei
    subscriber_id = StringVar()
    new_phone_number = StringVar()
    new_package = StringVar()
    new_brodband = IntVar()
    imei = StringVar()
    Label(line_screen, text="Please enter details below", font="Times 15").pack()
    Label(line_screen, text="").pack()
    Label(line_screen, text="Enter Subscriber ID",font="Times 10").pack()

    subscriber_id_entry = Entry(line_screen, textvariable=subscriber_id)
    subscriber_id_entry.pack()
    Label(line_screen, text="").pack()
    Label(line_screen, text="Enter New Phone Number",font="Times 10").pack()
    new_phone_number_entry = Entry(line_screen, textvariable=new_phone_number)
    new_phone_number_entry.pack()
    Label(line_screen, text="").pack()

    Label(line_screen, text="Enter Package",font="Times 10").pack()

    MODES = [
        ("Gold", "Gold"),
        ("Silver", "Silver"),
        ("Regular", "Regular"),
    ]

    new_package.set("Regular")

    for text, mode in MODES:
        b = Radiobutton(line_screen, text=text,
                        variable=new_package, value=mode)
        b.pack(anchor=S)
    Label(line_screen, text="").pack()
    Label(line_screen, text="Enter brodband",font="Times 10").pack()


    MODES = [
        ("25", 25),
        ("15", 15),
        ("5", 5),
    ]

    new_brodband.set("25")

    for text, mode in MODES:
        b = Radiobutton(line_screen, text=text,
                        variable=new_brodband, value=mode)
        b.pack(anchor=S)
    Label(line_screen, text="").pack()


    Label(line_screen, text="Enter IMEI",font="Times 10").pack()

    imei_entry = Entry(line_screen, textvariable=imei)
    imei_entry.pack()
    Label(line_screen, text="").pack()
    Button(line_screen, text="ADD LINE", width="10", height="1", bg="azure", command=add_line).pack()
    Button(line_screen, text="Show", font="Times 10", width="10", height="1", bg="azure",
           command=phone_numbers_show).pack(side=BOTTOM, anchor=W)
def add_line():

    sub_id = subscriber_id.get()
    new_number = new_phone_number.get()
    new_pack = new_package.get()
    new_brod = new_brodband.get()
    new_imei = imei.get()
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', 'xe')
    conn = cx_Oracle.connect(username1, password1, dsn_tns)
    try:
        c = conn.cursor()
        c.callproc("ADD_NEW_LINE",
                [sub_id, new_number, new_pack,new_brod,new_imei])
        conn.commit()
        Label(line_screen, text="").pack()
        Label(line_screen, text="New line add to " + sub_id + "  \n and his new line is  " + new_number,
              font="Times 15", ).pack()
    except:
        Label(line_screen,
              text="INVALID INPUT.\n PLEASE CHECK ONE OF \nTHE FOLLOWING:\nID,EMAIL,PHONE NUMBER",
              font="Times 8").pack()
    finally:
        conn.close()

def generate_calls():
    global generate_calls_screen
    generate_calls_screen = Toplevel(main_screen)
    generate_calls_screen.title("generate_calls")
    generate_calls_screen.geometry("200x200")
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', 'xe')
    conn = cx_Oracle.connect(username1, password1, dsn_tns)
    c = conn.cursor()
    c.callproc('system.generate_calls',[5])
    conn.commit()
    conn.close()
    Label(generate_calls_screen, text="").pack()
    Label(generate_calls_screen, text="").pack()
    Label(generate_calls_screen, text="").pack()
    Label(generate_calls_screen, text="CALLS is generated  ", font="Times 15", ).pack()

    Button(generate_calls_screen, text="OK", font="Times 10", width="10", height="1", bg="azure",
           command=destroy_generate_calls_screen).pack(side=BOTTOM, anchor=S)
def destroy_generate_calls_screen():
    generate_calls_screen.destroy()

def generate_sms():
    global generate_sms_screen
    generate_sms_screen = Toplevel(main_screen)
    generate_sms_screen.title("generate_sms")
    generate_sms_screen.geometry("200x200")
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', 'xe')
    conn = cx_Oracle.connect(username1, password1, dsn_tns)
    c = conn.cursor()
    c.callproc('system.generate_sms',[5])
    conn.commit()
    conn.close()

    Label(generate_sms_screen, text="").pack()
    Label(generate_sms_screen, text="").pack()
    Label(generate_sms_screen, text="").pack()
    Label(generate_sms_screen, text="SMS is generated  ", font="Times 15", ).pack()

    Button(generate_sms_screen, text="OK", font="Times 10", width="10", height="1", bg="azure",
           command=destroy_generate_sms_screen).pack(side=BOTTOM, anchor=S)
def destroy_generate_sms_screen():
    generate_sms_screen.destroy()

def upgrade_broadband():
    global upgrade_broadband_screen
    upgrade_broadband_screen = Toplevel(main_screen)
    upgrade_broadband_screen.title("upgrade_broadband")
    upgrade_broadband_screen.geometry("200x200")
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', 'xe')
    conn = cx_Oracle.connect(username1, password1, dsn_tns)
    c = conn.cursor()
    c.callproc('system.UPGRADE_BROADBAND')
    conn.commit()
    conn.close()
    Label(upgrade_broadband_screen, text="").pack()
    Label(upgrade_broadband_screen, text="").pack()
    Label(upgrade_broadband_screen, text="").pack()
    Label(upgrade_broadband_screen, text="Brodband is upgraded\n for all the users  ",font="Times 15",).pack()

    Button(upgrade_broadband_screen, text="OK",font="Times 10", width="10", height="1", bg="azure", command=destroy_upgrade_broadband_screen).pack(side=BOTTOM, anchor=S)
def destroy_upgrade_broadband_screen():
    upgrade_broadband_screen.destroy()

def create_invoice_screen():
    global invoice_screen
    invoice_screen = Toplevel(main_screen)
    invoice_screen.title("create invoice screen")
    invoice_screen.geometry("300x600")

    global phone_number
    global id_number
    phone_number = StringVar()
    id_number = StringVar()
    Label(invoice_screen, text="Please enter details below", font="Times 15").pack()
    Label(invoice_screen, text="").pack()
    Label(invoice_screen, text="enter id", font="Times 10").pack()


    phone_number_entry = Entry(invoice_screen, textvariable=id_number)
    phone_number_entry.pack()
    Label(invoice_screen, text="").pack()
    Label(invoice_screen, text="enter phone number", font="Times 10").pack()

    phone_number_entry = Entry(invoice_screen, textvariable=phone_number)
    phone_number_entry.pack()
    Label(invoice_screen, text="").pack()
    Button(invoice_screen, text="create invoice", width="10", height="1", bg="azure", command=create_invoice).pack()
def create_invoice():

    phone = phone_number.get()
    id_in = id_number.get()
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', 'xe')
    conn = cx_Oracle.connect(username1, password1, dsn_tns)
    try:
        c = conn.cursor()
        c.callproc("system.NEW_INVOICE", [id_in,phone])
        conn.commit()
        Label(invoice_screen, text="").pack()
        Label(invoice_screen, text="New invoice created for " + id_in, font="Times 10", ).pack()
    except:
        Label(invoice_screen,
              text="INVALID INPUT.\n PLEASE CHECK ONE OF \nTHE FOLLOWING:\nID,PHONE NUMBER", font="Times 8",).pack()

    finally:
        conn.close()

def payment_screen():

    global my_payment_screen

    my_payment_screen = Toplevel(main_screen)
    my_payment_screen.title("payment_screen")
    my_payment_screen.geometry("300x600")

    global payment_id

    payment_id = StringVar()
    Label(my_payment_screen, text="Please enter details below", font="Times 15").pack()
    Label(my_payment_screen, text="").pack()
    Label(my_payment_screen, text="Enter id to know the charge", font="Times 10").pack()


    payment_id_entry = Entry(my_payment_screen, textvariable=payment_id)
    payment_id_entry.pack()
    Label(my_payment_screen, text="").pack()
    Button(my_payment_screen, text="Enter", width="10", height="1", bg="azure", command=payment).pack()
def payment():

    paymentid = payment_id.get()

    dsn_tns = cx_Oracle.makedsn('localhost', '1521', 'xe')
    conn = cx_Oracle.connect(username1, password1, dsn_tns)
    try:
        c = conn.cursor()
        test = c.callfunc("system.Total_Charges_Subscriber",int,[paymentid])
        conn.commit()
        Label(my_payment_screen, text="\n" +" Total charge for\n all phones of subscriber\n id "+paymentid +"  is " + str(test),
              font="Times 15", ).pack()
    except:
        Label(my_payment_screen,
              text="INVALID INPUT.\n PLEASE CHECK IF\n THE ID IS VALID", font="Times 8", ).pack()

    finally:
        conn.close()

def subscribers_and_phones():
    global subscribers_and_phones_screen
    subscribers_and_phones_screen = Toplevel(main_screen)
    subscribers_and_phones_screen.title("subscribers_and_phones_screen")
    subscribers_and_phones_screen.geometry("725x400")

    dsn_tns = cx_Oracle.makedsn('localhost', '1521', 'xe')
    conn = cx_Oracle.connect(username1, password1, dsn_tns)
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM system.SUBSCRIBERSANDPHONES")

        r = 0
        Label(subscribers_and_phones_screen, text='SUBSCRIBER ID', bg="seagreen", relief=RIDGE, width=25).grid(row=r,
                                                                                                               column=0)
        Label(subscribers_and_phones_screen, text='FIRST NAME', bg="seagreen", relief=RIDGE, width=25).grid(row=r,
                                                                                                            column=1)
        Label(subscribers_and_phones_screen, text='LAST NAME', bg="seagreen", relief=RIDGE, width=25).grid(row=r,
                                                                                                           column=2)
        Label(subscribers_and_phones_screen, text='PHONE NUMBER', bg="seagreen", relief=RIDGE, width=25).grid(row=r,
                                                                                                              column=3)
        r = r + 1
        for row in c:

            k = 0
            for p in range(4):
                Label(subscribers_and_phones_screen, text=row[p], bg="DarkOliveGreen1", relief=RIDGE, width=25).grid(
                    row=r, column=k)

                k = k + 1
            r = r + 1
        conn.commit()
    except:
        Label(subscribers_and_phones_screen,
              text="You don't have enough privileges ", font="Times 8", ).pack()

    finally:
        conn.close()
def phone_numbers_show():
    global phone_numbers_screen
    phone_numbers_screen = Toplevel(main_screen)
    phone_numbers_screen.title("subscribers_and_phones_screen")
    phone_numbers_screen.geometry("1500x600")

    dsn_tns = cx_Oracle.makedsn('localhost', '1521', 'xe')
    conn = cx_Oracle.connect(username1, password1, dsn_tns)
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM system.phone_numbers")

        r = 0
        Label(phone_numbers_screen, text='PHONE_NUMBER', bg="seagreen", relief=RIDGE, width=25).grid(row=r,
                                                                                                               column=0)
        Label(phone_numbers_screen, text='SUBSCRIBER_ID', bg="seagreen", relief=RIDGE, width=25).grid(row=r,
                                                                                                            column=1)
        Label(phone_numbers_screen, text='STATUS', bg="seagreen", relief=RIDGE, width=25).grid(row=r,
                                                                                                           column=2)
        Label(phone_numbers_screen, text='PACKAGE', bg="seagreen", relief=RIDGE, width=25).grid(row=r,
                                                                                                              column=3)
        Label(phone_numbers_screen, text='DATE_ACTIVE', bg="seagreen", relief=RIDGE, width=25).grid(row=r,
                                                                                                column=4)
        Label(phone_numbers_screen, text='CALLS', bg="seagreen", relief=RIDGE, width=25).grid(row=r,
                                                                                                column=5)
        Label(phone_numbers_screen, text='SMS', bg="seagreen", relief=RIDGE, width=25).grid(row=r,
                                                                                                column=6)
        Label(phone_numbers_screen, text='BROADBAND', bg="seagreen", relief=RIDGE, width=25).grid(row=r,
                                                                                                column=7)

        r = r + 1
        for row in c:

            k = 0
            for p in range(8):
                Label(phone_numbers_screen, text=row[p], bg="DarkOliveGreen1", relief=RIDGE, width=25).grid(
                    row=r, column=k)

                k = k + 1
            r = r + 1
        conn.commit()
    except:
        Label(phone_numbers_screen,
              text="You don't have enough privileges ", font="Times 8", ).pack()

    finally:
        conn.close()
def subscribers():
    global subscribers_screen
    subscribers_screen = Toplevel(main_screen)
    subscribers_screen.title("subscribers_screen")
    subscribers_screen.geometry("1500x400")

    dsn_tns = cx_Oracle.makedsn('localhost', '1521', 'xe')
    conn = cx_Oracle.connect(username1, password1, dsn_tns)
    c = conn.cursor()

    c.execute("SELECT * FROM system.SUBSCRIBERS")

    r=0
    Label(subscribers_screen,text='SUBSCRIBER ID', bg="gold", relief=RIDGE, width=30).grid(row=r, column=0)
    Label(subscribers_screen,text='FIRST NAME', bg="gold", relief=RIDGE, width=30).grid(row=r, column=1)
    Label(subscribers_screen,text='LAST NAME', bg="gold", relief=RIDGE, width=30).grid(row=r, column=2)
    Label(subscribers_screen,text='Email', bg="gold", relief=RIDGE, width=30).grid(row=r, column=3)
    Label(subscribers_screen,text=' NUMBER OF LINES', bg="gold", relief=RIDGE, width=30).grid(row=r, column=4)
    Label(subscribers_screen,text='Date', bg="gold", relief=RIDGE, width=30).grid(row=r, column=5)
    Label(subscribers_screen,text='PHONE NUMBER', bg="gold", relief=RIDGE, width=30).grid(row=r, column=6)

    r = r +1
    for row in c:

        k = 0
        for p in range(7):
            Label(subscribers_screen,text=row[p], bg="yellow2", relief=RIDGE, width=30).grid(row=r, column=k)

            k = k + 1
        r = r + 1
    conn.commit()
    conn.close()

def list_of_invoices_DESC():
    global list_of_invoices_DESC_screen
    list_of_invoices_DESC_screen = Toplevel(main_screen)
    list_of_invoices_DESC_screen.title("DESC list of invoices")
    list_of_invoices_DESC_screen.geometry("910x400")



    dsn_tns = cx_Oracle.makedsn('localhost', '1521', 'xe')
    conn = cx_Oracle.connect(username1, password1, dsn_tns)
    try:
        c = conn.cursor()

        c.execute('SELECT SUBSCRIBER_ID,LINE_NUMBER,FIRST_NAME,LAST_NAME,CHARGE FROM system.INVOICES ORDER BY CHARGE DESC')
        r = 0
        Label(list_of_invoices_DESC_screen, text='SUBSCRIBER ID', bg="deepskyblue", relief=RIDGE, width=25).grid(row=r,
                                                                                                                 column=0)
        Label(list_of_invoices_DESC_screen, text='PHONE NUMBER', bg="deepskyblue", relief=RIDGE, width=25).grid(row=r,
                                                                                                                column=1)
        Label(list_of_invoices_DESC_screen, text='FIRST NAME', bg="deepskyblue", relief=RIDGE, width=25).grid(row=r,
                                                                                                              column=2)
        Label(list_of_invoices_DESC_screen, text='LAST NAME', bg="deepskyblue", relief=RIDGE, width=25).grid(row=r,
                                                                                                             column=3)
        Label(list_of_invoices_DESC_screen, text='CHARGE', bg="deepskyblue", relief=RIDGE, width=25).grid(row=r,
                                                                                                          column=4)
        r = r + 1
        for row in c:

            k = 0
            for p in range(5):
                Label(list_of_invoices_DESC_screen, text=row[p], bg="darkturquoise", relief=RIDGE, width=25).grid(row=r,
                                                                                                                  column=k)

                k = k + 1
            r = r + 1
        conn.commit()
    except:
        Label(list_of_invoices_DESC_screen,
              text="You don't have enough privileges ", font="Times 8", ).pack()

    finally:
        conn.close()

def Revenues_input():
    global Revenues_input_screen
    Revenues_input_screen = Toplevel(main_screen)
    Revenues_input_screen.title("call_screen")
    Revenues_input_screen.geometry("300x600")
    global fromCharge
    global uptoCharge

    global fromCharge_entry
    global uptoCharge_entry

    fromCharge = StringVar()
    uptoCharge = StringVar()


    Label(Revenues_input_screen, text="Please enter details below", font="Times 15").pack()
    Label(Revenues_input_screen, text="").pack()
    Label(Revenues_input_screen, text="from charge", font="Times 10").pack()

    fromCharge_entry = Entry(Revenues_input_screen, textvariable=fromCharge)
    fromCharge_entry.pack()
    Label(Revenues_input_screen, text="").pack()
    Label(Revenues_input_screen, text="upto charge", font="Times 10").pack()

    uptoCharge_entry = Entry(Revenues_input_screen, textvariable=uptoCharge)
    uptoCharge_entry.pack()
    Label(Revenues_input_screen, text="").pack()

    Button(Revenues_input_screen, text="SHOW", width="10", height="1", bg="azure", command=Revenues).pack()
def Revenues():
    Revenues_input_screen.destroy()
    f=fromCharge.get()
    t=uptoCharge.get()
    global Revenues_screen
    Revenues_screen = Toplevel(main_screen)
    Revenues_screen.title("Revenues screen")
    Revenues_screen.geometry("910x400")

    dsn_tns = cx_Oracle.makedsn('localhost', '1521', 'xe')
    conn = cx_Oracle.connect(username1, password1, dsn_tns)
    try:
        c = conn.cursor()

        str = 'SELECT SUBSCRIBER_ID,LINE_NUMBER,FIRST_NAME,LAST_NAME,CHARGE FROM system.INVOICES where CHARGE  BETWEEN ' + f + ' AND ' + t + ' ORDER BY CHARGE '
        c = conn.cursor()
        c.execute(str)
        r = 0
        Label(Revenues_screen, text='SUBSCRIBER ID', bg="red4", relief=RIDGE, width=25).grid(row=r,
                                                                                                             column=0)
        Label(Revenues_screen, text='PHONE NUMBER', bg="red4", relief=RIDGE, width=25).grid(row=r,
                                                                                                            column=1)
        Label(Revenues_screen, text='FIRST NAME', bg="red4", relief=RIDGE, width=25).grid(row=r,
                                                                                                          column=2)
        Label(Revenues_screen, text='LAST NAME', bg="red4", relief=RIDGE, width=25).grid(row=r,
                                                                                                         column=3)
        Label(Revenues_screen, text='CHARGE', bg="red4", relief=RIDGE, width=25).grid(row=r, column=4)
        r = r + 1
        for row in c:

            k = 0
            for p in range(5):
                Label(Revenues_screen, text=row[p], bg="red2", relief=RIDGE, width=25).grid(row=r,
                                                                                                          column=k)

                k = k + 1
            r = r + 1
        conn.commit()


    finally:
        conn.close()

def list_of_invoices_ASC():
    global list_of_invoices_DESC_screen
    list_of_invoices_DESC_screen = Toplevel(main_screen)
    list_of_invoices_DESC_screen.title("ASC list of invoices")
    list_of_invoices_DESC_screen.geometry("910x400")

    dsn_tns = cx_Oracle.makedsn('localhost', '1521', 'xe')
    conn = cx_Oracle.connect(username1, password1, dsn_tns)

    try:
        c = conn.cursor()

        c.execute('SELECT SUBSCRIBER_ID,LINE_NUMBER,FIRST_NAME,LAST_NAME,CHARGE FROM system.INVOICES ORDER BY CHARGE ASC')
        r = 0
        Label(list_of_invoices_DESC_screen, text='SUBSCRIBER ID', bg="mediumvioletred", relief=RIDGE, width=25).grid(
            row=r,
            column=0)
        Label(list_of_invoices_DESC_screen, text='PHONE NUMBER', bg="mediumvioletred", relief=RIDGE, width=25).grid(
            row=r,
            column=1)
        Label(list_of_invoices_DESC_screen, text='FIRST NAME', bg="mediumvioletred", relief=RIDGE, width=25).grid(row=r,
                                                                                                                  column=2)
        Label(list_of_invoices_DESC_screen, text='LAST NAME', bg="mediumvioletred", relief=RIDGE, width=25).grid(row=r,
                                                                                                                 column=3)
        Label(list_of_invoices_DESC_screen, text='CHARGE', bg="mediumvioletred", relief=RIDGE, width=25).grid(row=r,
                                                                                                              column=4)
        r = r + 1
        for row in c:

            k = 0
            for p in range(5):
                Label(list_of_invoices_DESC_screen, text=row[p], bg="palevioletred", relief=RIDGE, width=25).grid(row=r,
                                                                                                                  column=k)

                k = k + 1
            r = r + 1
        conn.commit()
    except:
        Label(list_of_invoices_DESC_screen,
              text="You don't have enough privileges ", font="Times 8", ).pack()

    finally:
        conn.close()

def main_account_screen():
    global main_screen
    main_screen = Tk()
    global top
    top=Toplevel()
    top.title("Login ")
    top.geometry("300x200")
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    global username_login_entry
    global password_login_entry
    Label(top, text="Username ",font="Times 10").pack()
    username_login_entry = Entry(top, textvariable=username_verify)
    username_login_entry.pack()
    Label(top, text="").pack()
    Label(top, text="Password",font="Times 10").pack()
    password_login_entry = Entry(top, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(top, text="").pack()
    button1 = Button(top, text="Login", command=lambda: command1()).pack()  # Login button
    Label(top, text="").pack()
    button2 = Button(top, text="Cancel", command=lambda: command2()).pack()  # Cancel button
    main_screen.geometry("300x650")
    main_screen.title("Cellular OneHundred ")
    Label(text="Choose the option", bg="DeepSkyBlue2", width="300", height="2", font="Verdana 10 bold").pack()
    Button(text="Register Subscriber", height="2", width="30", command=register).pack()
    Button(text="Add new line", height="2", width="30", command=add_line_screen).pack()
    Button(text="Upgrade broadband", height="2", width="30", command=upgrade_broadband).pack()
    Button(text="Create invoice", height="2", width="30", command=create_invoice_screen).pack()
    Button(text="Remove account", height="2", width="30", command=delete_subscriber_screen).pack()
    Button(text="Total Charge", height="2", width="30", command=payment_screen).pack()
    Button(text="Activate or Deactivate phone ", height="2", width="30", command=phone_isactive_show).pack()
    Button(text="Generate SMS", height="2", width="30", command=generate_sms).pack()
    Button(text="Generate Calls", height="2", width="30", command=generate_calls).pack()
    Button(text="Send 1 SMS", height="2", width="30", command=sms_someone_screen).pack()
    Button(text="Make 1 Call", height="2", width="30", command=call_someone_screen).pack()
    Button(text="DESC list of invoices", height="2", width="30", command=list_of_invoices_DESC).pack()
    Button(text="ASC list of invoices", height="2", width="30", command=list_of_invoices_ASC).pack()
    Button(text="show subscribers and phones", height="2", width="30", command=subscribers_and_phones).pack()
    Button(text="Revenues", height="2", width="30", command=Revenues_input).pack()

    main_screen.withdraw()
    main_screen.mainloop()

def command1():

    global username1
    global password1
    username1 = username_verify.get()
    password1 = password_verify.get()
    try:
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', 'xe')
        conn = cx_Oracle.connect(username1, password1, dsn_tns)
        c = conn.cursor()
        main_screen.deiconify()  # Unhides the root window
        top.destroy()  # Removes the toplevel window

    except:
        Label(top,
                text="INVALID INPUT.\n PLEASE CHECK ONE OF \nTHE FOLLOWING:\nUSERNAME OR PASSWORD",
                font="Times 8").pack()
        print(sys.exc_info())


def command2():
    top.destroy()  # Removes the toplevel window
    main_screen.destroy()  # Removes the hidden root window
    sys.exit()  # Ends the script

main_account_screen()
