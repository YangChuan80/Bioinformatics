import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import tkinter.font as tkf
import sqlite3
import datetime

DB_file = 'Samples.sqlite'
conn = sqlite3.connect(DB_file)
cur = conn.cursor()

cur.execute('SELECT * FROM BloodSamples')
samples = cur.fetchall()

headers = [item[0] for item in cur.description]

## Helper functions
#### Table related

def OnDoubleClick(event):
    global idglb
    try:
        item = table.selection()[0]
        value = table.item(item, 'values')
        iden = value[0]    
        extractID(iden)
        idglb = iden
    except:
        pass

def sortby(tree, col, descending):
    """sort tree contents when a column header is clicked on"""
    # grab values to sort
    data = [(tree.set(child, col), child) for child in tree.get_children('')]
    # if the data to be sorted is numeric change to float
    #data =  change_numeric(data)
    # now sort the data in place
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        tree.move(item[1], '', ix)
    # switch the heading so it will sort in the opposite direction
    tree.heading(col, command=lambda col=col: sortby(tree, col, int(not descending)))    

#### Function related

def refreshDB():
    global conn, cur, desc, headers, samples
    conn.close()
    conn = sqlite3.connect(DB_file)
    cur = conn.cursor()

    cur.execute('SELECT * FROM BloodSamples')
    headers = [item[0] for item in cur.description]

    cur.execute('SELECT * FROM BloodSamples')
    samples = cur.fetchall()

def extractID(iden):    
    cur.execute('SELECT * FROM BloodSamples WHERE No = ?', (iden,))    
    row = cur.fetchone() 
    arrange(row)

def arrange(row):
    item = {}
    for i in range(len(row)):
        item[headers[i]] = row[i]
    display_in_text(item)

def display_in_table(samples):
    for sample in samples:
        table.insert("", "end", "", values=sample)
    num = str(len(samples))
    text_num.delete('1.0', tk.END)
    text_num.insert('1.0', num)

def display_in_text(item):
    text_RackNumber.delete('1.0', tk.END)
    text_RackNumber.insert('1.0', item['RackNumber'])  
    
    text_SampleID.delete('1.0', tk.END)
    text_SampleID.insert('1.0', item['SampleID'])  
    
    text_SampleType.delete('1.0', tk.END)
    text_SampleType.insert('1.0', item['SampleType'])
    
    text_SampleStatus.delete('1.0', tk.END)
    text_SampleStatus.insert('1.0', item['SampleStatus'])
    
    text_PatientName.delete('1.0', tk.END)
    text_PatientName.insert('1.0', item['PatientName'])
    
    text_PatientID.delete('1.0', tk.END)
    text_PatientID.insert('1.0', item['PatientID'])
    
    text_ID.delete('1.0', tk.END)
    text_ID.insert('1.0', item['ID'])
    
    text_BirthDate.delete('1.0', tk.END)
    text_BirthDate.insert('1.0', item['BirthDate'])
    
    text_No.delete('1.0', tk.END)
    text_No.insert('1.0', item['No'])
    
    text_Gender.delete('1.0', tk.END)
    text_Gender.insert('1.0', item['Gender'])   
    
    text_PatientName_CN.delete('1.0', tk.END)
    text_PatientName_CN.insert('1.0', item['PatientName_CN'])
        
    text_Proband.delete('1.0', tk.END)
    text_Proband.insert('1.0', item['Proband'])
    
    text_RelationshipOfProband.delete('1.0', tk.END)
    text_RelationshipOfProband.insert('1.0', item['RelationshipOfProband'])
    
    text_Telephone.delete('1.0', tk.END)
    text_Telephone.insert('1.0', item['Telephone'])
    
    text_Comments.delete('1.0', tk.END)
    text_Comments.insert('1.0', item['Comments'])
    
    text_Diagnosis1.delete('1.0', tk.END)
    text_Diagnosis1.insert('1.0', item['Diagnosis1'])
    
    text_Diagnosis2.delete('1.0', tk.END)
    text_Diagnosis2.insert('1.0', item['Diagnosis2'])
    
    text_Diagnosis3.delete('1.0', tk.END)
    text_Diagnosis3.insert('1.0', item['Diagnosis3'])
    
    text_Diagnosis4.delete('1.0', tk.END)
    text_Diagnosis4.insert('1.0', item['Diagnosis4'])
    
    text_Diagnosis5.delete('1.0', tk.END)
    text_Diagnosis5.insert('1.0', item['Diagnosis5'])  

def clear():
    for i in table.get_children():
        table.delete(i)

def browse():
    clear()
    refreshDB()
    display_in_table(samples)

def update():
    try:
        No_gotten = text_No.get('1.0', tk.END).rstrip()
        RackNumber_gotten = text_RackNumber.get('1.0', tk.END).rstrip()
        SampleID_gotten = text_SampleID.get('1.0', tk.END).rstrip()
        SampleType_gotten = text_SampleType.get('1.0', tk.END).rstrip()
        SampleStatus_gotten = text_SampleStatus.get('1.0', tk.END).rstrip()
        PatientName_gotten = text_PatientName.get('1.0', tk.END).rstrip()
        PatientName_CN_gotten = text_PatientName_CN.get('1.0', tk.END).rstrip()
        PatientID_gotten = text_PatientID.get('1.0', tk.END).rstrip()
        ID_gotten = text_ID.get('1.0', tk.END).rstrip()
        BirthDate_gotten = text_BirthDate.get('1.0', tk.END).rstrip()        
        Gender_gotten = text_Gender.get('1.0', tk.END).rstrip()        
        Proband_gotten = text_Proband.get('1.0', tk.END).rstrip()
        RelationshipOfProband_gotten = text_RelationshipOfProband.get('1.0', tk.END).rstrip()
        Telephone_gotten = text_Telephone.get('1.0', tk.END).rstrip()
        Comments_gotten = text_Comments.get('1.0', tk.END).rstrip()
        Diagnosis1_gotten = text_Diagnosis1.get('1.0', tk.END).rstrip()
        Diagnosis2_gotten = text_Diagnosis2.get('1.0', tk.END).rstrip()
        Diagnosis3_gotten = text_Diagnosis3.get('1.0', tk.END).rstrip()
        Diagnosis4_gotten = text_Diagnosis4.get('1.0', tk.END).rstrip()
        Diagnosis5_gotten = text_Diagnosis5.get('1.0', tk.END).rstrip()       
        
        Question_mark = '(' + '?, ' * 19 + '?)'
        
        cur.execute('DELETE FROM BloodSamples WHERE No = ?', (No_gotten,))        
        conn.commit()
               
        Update_values = (No_gotten, RackNumber_gotten, SampleID_gotten, SampleType_gotten, 
                         SampleStatus_gotten, PatientName_gotten, PatientName_CN_gotten, 
                         PatientID_gotten, ID_gotten, BirthDate_gotten, Gender_gotten, 
                         Proband_gotten, RelationshipOfProband_gotten, Telephone_gotten, 
                         Comments_gotten, 
                         Diagnosis1_gotten,
                         Diagnosis2_gotten,
                         Diagnosis3_gotten,
                         Diagnosis4_gotten,
                         Diagnosis5_gotten                        
                        )
        Update_Fields = '''(No, RackNumber, SampleID, SampleType, SampleStatus, 
        PatientName, PatientName_CN, PatientID, ID, BirthDate, Gender, Proband, RelationshipOfProband, 
        Telephone, Comments, Diagnosis1, Diagnosis2, Diagnosis3, Diagnosis4, Diagnosis5)
        '''
        
        #cur.execute('INSERT INTO BloodSamples (SampleID, PatientName, SampleType) VALUES (?, ?, ?)', 
        #('201706181718000444', 'PatientName, 'Serum'))
        
        cur.execute('INSERT INTO BloodSamples '+ Update_Fields + ' VALUES ' + Question_mark, 
                    Update_values)
        conn.commit()  
        
        messagebox.showinfo("Updated", "Sample successfully updated!")
        clear()
        refreshDB()
        display_in_table(samples)
        
    except:
        pass

def new_record():
    root_new_bundle = tk.Tk()    
    
    w = 1100 # width for the Tk root
    h = 580 # height for the Tk root

    # get screen width and height
    ws = root_new_bundle.winfo_screenwidth() # width of the screen
    hs = root_new_bundle.winfo_screenheight() # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # set the dimensions of the screen 
    # and where it is placed
    root_new_bundle.geometry('%dx%d+%d+%d' % (w, h, x, y))   
    root_new_bundle.title('New Record')
    
    time_text = str(datetime.datetime.now())
    id = ''
    for t in time_text:
        if t!=' 'and t!= '-' and t != ':' and t != '.':
            id += t
    
    def save():
        #try:
            RackNumber_gotten = text_RackNumber.get('1.0', tk.END).rstrip()
            SampleID_gotten = text_SampleID.get('1.0', tk.END).rstrip()
            SampleType_gotten = text_SampleType.get('1.0', tk.END).rstrip()
            SampleStatus_gotten = text_SampleStatus.get('1.0', tk.END).rstrip()
            PatientName_gotten = text_PatientName.get('1.0', tk.END).rstrip()
            PatientName_CN_gotten = text_PatientName_CN.get('1.0', tk.END).rstrip()
            PatientID_gotten = text_PatientID.get('1.0', tk.END).rstrip()
            ID_gotten = text_ID.get('1.0', tk.END).rstrip()
            BirthDate_gotten = text_BirthDate.get('1.0', tk.END).rstrip()        
            Gender_gotten = text_Gender.get('1.0', tk.END).rstrip()        
            Proband_gotten = text_Proband.get('1.0', tk.END).rstrip()
            RelationshipOfProband_gotten = text_RelationshipOfProband.get('1.0', tk.END).rstrip()
            Telephone_gotten = text_Telephone.get('1.0', tk.END).rstrip()
            Comments_gotten = text_Comments.get('1.0', tk.END).rstrip()
            Diagnosis1_gotten = text_Diagnosis1.get('1.0', tk.END).rstrip()
            Diagnosis2_gotten = text_Diagnosis2.get('1.0', tk.END).rstrip()
            Diagnosis3_gotten = text_Diagnosis3.get('1.0', tk.END).rstrip()
            Diagnosis4_gotten = text_Diagnosis4.get('1.0', tk.END).rstrip()
            Diagnosis5_gotten = text_Diagnosis5.get('1.0', tk.END).rstrip()       

            Question_mark = '(' + '?, ' * 18 + '?)'
            
            Update_values = (RackNumber_gotten, SampleID_gotten, SampleType_gotten, 
                             SampleStatus_gotten, PatientName_gotten, PatientName_CN_gotten, 
                             PatientID_gotten, ID_gotten, BirthDate_gotten, Gender_gotten, 
                             Proband_gotten, RelationshipOfProband_gotten, Telephone_gotten, 
                             Comments_gotten, 
                             Diagnosis1_gotten,
                             Diagnosis2_gotten,
                             Diagnosis3_gotten,
                             Diagnosis4_gotten,
                             Diagnosis5_gotten                        
                            )
            Update_Fields = '''(RackNumber, SampleID, SampleType, SampleStatus, 
            PatientName, PatientName_CN, PatientID, ID, BirthDate, Gender, Proband, RelationshipOfProband, 
            Telephone, Comments, Diagnosis1, Diagnosis2, Diagnosis3, Diagnosis4, Diagnosis5)
            '''

            #cur.execute('INSERT INTO BloodSamples (SampleID, PatientName, SampleType) VALUES (?, ?, ?)', 
            #('201706181718000444', 'PatientName, 'Serum'))

            cur.execute('INSERT INTO BloodSamples '+ Update_Fields + ' VALUES ' + Question_mark, 
                        Update_values)
            conn.commit()  

            messagebox.showinfo("Updated", "Sample successfully added!")
            clear()
            refreshDB()
            display_in_table(samples)
            root_new_bundle.destroy()

        #except:
            #pass
    
    # ///////////// Routine Edits////////////////

    y_origin = 100
    gain = 55
    i = 0

    text_PatientName_CN = tk.Text(root_new_bundle, width=20, height=1, font=('tahoma', 9), wrap='none')
    text_PatientName_CN.place(x=20, y=y_origin+i*gain)
    label_PatientName_CN = tk.Label(root_new_bundle, text='Patient\'s Chinese Name:', font=('tahoma', 8))
    label_PatientName_CN.place(x=20,y=y_origin+i*gain-25)

    text_PatientName = tk.Text(root_new_bundle, width=20, height=1, font=('tahoma', 8), wrap='none')
    text_PatientName.place(x=220, y=y_origin+i*gain)
    label_PatientName = tk.Label(root_new_bundle, text='Patient\' Name:', font=('tahoma', 8))
    label_PatientName.place(x=220,y=y_origin+i*gain-25)

    text_Gender = tk.Text(root_new_bundle, width=20, height=1, font=('tahoma', 8), wrap='none')
    text_Gender.place(x=420, y=y_origin+i*gain)
    label_Gender = tk.Label(root_new_bundle, text='Gender:', font=('tahoma', 8))
    label_Gender.place(x=420,y=y_origin+i*gain-25)

    text_Proband = tk.Text(root_new_bundle, width=20, height=1, font=('tahoma', 8), wrap='none')
    text_Proband.place(x=620, y=y_origin+i*gain)
    label_Proband = tk.Label(root_new_bundle, text='Proband:', font=('tahoma', 8))
    label_Proband.place(x=620,y=y_origin+i*gain-25)

    text_RelationshipOfProband = tk.Text(root_new_bundle, width=40, height=1, font=('tahoma', 8), wrap='none')
    text_RelationshipOfProband.place(x=820, y=y_origin+i*gain)
    label_RelationshipOfProband = tk.Label(root_new_bundle, text='Relationship of Proband:', font=('tahoma', 8))
    label_RelationshipOfProband.place(x=820,y=y_origin+i*gain-25)

    i = 1

    text_PatientID = tk.Text(root_new_bundle, width=20, height=1, font=('tahoma', 8), wrap='none')
    text_PatientID.place(x=20, y=y_origin+i*gain)
    label_PatientID = tk.Label(root_new_bundle, text='Patient ID:', font=('tahoma', 8))
    label_PatientID.place(x=20,y=y_origin+i*gain-25)

    text_ID = tk.Text(root_new_bundle, width=25, height=1, font=('tahoma', 8), wrap='none')
    text_ID.place(x=220, y=y_origin+i*gain)
    label_ID = tk.Label(root_new_bundle, text='ID:', font=('tahoma', 8))
    label_ID.place(x=220,y=y_origin+i*gain-25)


    text_BirthDate = tk.Text(root_new_bundle, width=20, height=1, font=('tahoma', 8), wrap='none')
    text_BirthDate.place(x=420, y=y_origin+i*gain)
    label_BirthDate = tk.Label(root_new_bundle, text='Birth Date:', font=('tahoma', 8))
    label_BirthDate.place(x=420,y=y_origin+i*gain-25)

    i = 2

    text_RackNumber = tk.Text(root_new_bundle, width=20, height=1, font=('tahoma', 8), wrap='none')
    text_RackNumber.place(x=20, y=y_origin+i*gain)
    label_RackNumber = tk.Label(root_new_bundle, text='Rack Number:', font=('tahoma', 8))
    label_RackNumber.place(x=20,y=y_origin+i*gain-25)

    text_SampleID = tk.Text(root_new_bundle, width=26, height=1, font=('tahoma', 8), wrap='none')
    text_SampleID.place(x=220, y=y_origin+i*gain)
    label_SampleID = tk.Label(root_new_bundle, text='Sample ID:', font=('tahoma', 8))
    label_SampleID.place(x=220,y=y_origin+i*gain-25)
    
    text_SampleID.delete('1.0', tk.END)
    text_SampleID.insert('1.0', id)  

    text_SampleType = tk.Text(root_new_bundle, width=20, height=1, font=('tahoma', 8), wrap='none')
    text_SampleType.place(x=420, y=y_origin+i*gain)
    label_SampleType = tk.Label(root_new_bundle, text='Sample Type:', font=('tahoma', 8))
    label_SampleType.place(x=420,y=y_origin+i*gain-25)

    text_SampleStatus = tk.Text(root_new_bundle, width=20, height=1, font=('tahoma', 8), wrap='none')
    text_SampleStatus.place(x=620, y=y_origin+i*gain)
    label_SampleStatus = tk.Label(root_new_bundle, text='Sample Status:', font=('tahoma', 8))
    label_SampleStatus.place(x=620,y=y_origin+i*gain-25)

    i = 3

    text_Diagnosis1 = tk.Text(root_new_bundle, width=40, height=1, font=('tahoma', 8), wrap='none')
    text_Diagnosis1.place(x=20, y=y_origin+i*gain)
    label_Diagnosis1 = tk.Label(root_new_bundle, text='Diagnosis 1:', font=('tahoma', 8))
    label_Diagnosis1.place(x=20,y=y_origin+i*gain-25)
    
    
    text_Diagnosis2 = tk.Text(root_new_bundle, width=40, height=1, font=('tahoma', 8), wrap='none')
    text_Diagnosis2.place(x=320, y=y_origin+i*gain)
    label_Diagnosis2 = tk.Label(root_new_bundle, text='Diagnosis 2:', font=('tahoma', 8))
    label_Diagnosis2.place(x=320,y=y_origin+i*gain-25)
    
    text_Diagnosis3 = tk.Text(root_new_bundle, width=40, height=1, font=('tahoma', 8), wrap='none')
    text_Diagnosis3.place(x=620, y=y_origin+i*gain)
    label_Diagnosis3 = tk.Label(root_new_bundle, text='Diagnosis 3:', font=('tahoma', 8))
    label_Diagnosis3.place(x=620,y=y_origin+i*gain-25)
    
    i = 4

    text_Diagnosis4 = tk.Text(root_new_bundle, width=40, height=1, font=('tahoma', 8), wrap='none')
    text_Diagnosis4.place(x=20, y=y_origin+i*gain)
    label_Diagnosis4 = tk.Label(root_new_bundle, text='Diagnosis 4:', font=('tahoma', 8))
    label_Diagnosis4.place(x=20,y=y_origin+i*gain-25)

    text_Diagnosis5 = tk.Text(root_new_bundle, width=40, height=1, font=('tahoma', 8), wrap='none')
    text_Diagnosis5.place(x=320, y=y_origin+i*gain)
    label_Diagnosis5 = tk.Label(root_new_bundle, text='Diagnosis 5:', font=('tahoma', 8))
    label_Diagnosis5.place(x=320,y=y_origin+i*gain-25)

    i = 5

    text_Telephone = tk.Text(root_new_bundle, width=40, height=1, font=('tahoma', 8), wrap='none')
    text_Telephone.place(x=20, y=y_origin+i*gain)
    label_Telephone = tk.Label(root_new_bundle, text='Telephone:', font=('tahoma', 8))
    label_Telephone.place(x=20,y=y_origin+i*gain-25)
    
    i = 6

    text_Comments = tk.Text(root_new_bundle, width=140, height=1, font=('tahoma', 8), wrap='none')
    text_Comments.place(x=20, y=y_origin+i*gain)
    label_Comments = tk.Label(root_new_bundle, text='Comments:', font=('tahoma', 8))
    label_Comments.place(x=20,y=y_origin+i*gain-25)
    
    # //// Button /////////////
    
    i = 7
    
    button_add=ttk.Button(root_new_bundle, text='Save', width=15, command=save)
    button_add.place(x=300, y=y_origin+i*gain)

    button_cancel=ttk.Button(root_new_bundle, text='Cancel', width=15, command=root_new_bundle.destroy)
    button_cancel.place(x=650, y=y_origin+i*gain)   
    
    
    root.mainloop()

def delete():
    No_gotten = text_No.get('1.0', tk.END).rstrip()
    
    if No_gotten == '':
        messagebox.showinfo("Empty", "There's no sample to delete. Please make sure.")
        
    else:           
        result = messagebox.askquestion('Delete', 'Are you sure to delete this sample?', icon='warning')

        if result == 'yes':
            cur.execute('DELETE FROM BloodSamples WHERE No = ?', (No_gotten,))        
            conn.commit()            
            messagebox.showinfo("Deleted", "Sample has been deleted!")
            
            clear()
            refreshDB()
            display_in_table(samples)

def patientNameSearch():
    gotten = text_PatientName_Search.get('1.0', tk.END).rstrip()
    
    cur.execute('SELECT * FROM BloodSamples WHERE PatientName = ?', (gotten,))
    items = cur.fetchall()
    
    clear()
    display_in_table(items)    

## Main Flow

root = tk.Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
#root.attributes('-fullscreen', True)
root.title('CharlestonPark')
root.iconbitmap('CharlestonParkIcon.ico')

### Multicolumn Listbox

# Multicolumn Listbox/////////////////////////////////////////////////////////////////////////////
table = ttk.Treeview(height="20", columns=headers, selectmode="extended")
table.pack(padx=10, pady=20, ipadx=1200, ipady=200)

i = 1
header_width = [20, 20, 100, 40, 20, 30, 10, 40, 70, 55, 140, 50, 35, 90, 90, 90, 90, 90, 60, 50]
for header in headers:
    table.heading('#'+str(i), text=header.title(), anchor=tk.W, command=lambda c=header: sortby(table, c, 0))
    table.column('#'+str(i), stretch=tk.NO, minwidth=0, width=tkf.Font().measure(header.title())+header_width[i-1])
    i+=1    
table.column('#0', stretch=tk.NO, minwidth=0, width=0)

table.bind("<Double-1>", OnDoubleClick)
#///////////////////////////////////////////////////////////////////////////////////////////

# Scrollbar////////////////////////////////////////////////////////////////////////////////////////
vsb = ttk.Scrollbar(table, orient = "vertical",  command = table.yview)
hsb = ttk.Scrollbar(table, orient = "horizontal", command = table.xview)
## Link scrollbars activation to top-level object
table.configure(yscrollcommand = vsb.set, xscrollcommand = hsb.set)
## Link scrollbar also to every columns
map(lambda col: col.configure(yscrollcommand = vsb.set, xscrollcommand = hsb.set), table)
vsb.pack(side = tk.RIGHT, fill = tk.Y)
hsb.pack(side = tk.BOTTOM, fill = tk.X) 

### Other Controls

# ///////Text Edit/////////////////////////

# ///////////// Routine Edits////////////////

y_origin = 600
gain = 55
i = 0

text_PatientName_CN = tk.Text(root, width=20, height=1, font=('tahoma', 9), wrap='none')
text_PatientName_CN.place(x=20, y=y_origin+i*gain)
label_PatientName_CN = tk.Label(root, text='Patient\'s Chinese Name:', font=('tahoma', 8))
label_PatientName_CN.place(x=20,y=y_origin+i*gain-25)

text_PatientName = tk.Text(root, width=20, height=1, font=('tahoma', 8), wrap='none')
text_PatientName.place(x=220, y=y_origin+i*gain)
label_PatientName = tk.Label(root, text='Patient\' Name:', font=('tahoma', 8))
label_PatientName.place(x=220,y=y_origin+i*gain-25)

text_Gender = tk.Text(root, width=20, height=1, font=('tahoma', 8), wrap='none')
text_Gender.place(x=420, y=y_origin+i*gain)
label_Gender = tk.Label(root, text='Gender:', font=('tahoma', 8))
label_Gender.place(x=420,y=y_origin+i*gain-25)

text_Proband = tk.Text(root, width=20, height=1, font=('tahoma', 8), wrap='none')
text_Proband.place(x=620, y=y_origin+i*gain)
label_Proband = tk.Label(root, text='Proband:', font=('tahoma', 8))
label_Proband.place(x=620,y=y_origin+i*gain-25)

text_RelationshipOfProband = tk.Text(root, width=40, height=1, font=('tahoma', 8), wrap='none')
text_RelationshipOfProband.place(x=820, y=y_origin+i*gain)
label_RelationshipOfProband = tk.Label(root, text='Relationship of Proband:', font=('tahoma', 8))
label_RelationshipOfProband.place(x=820,y=y_origin+i*gain-25)

i = 1

text_PatientID = tk.Text(root, width=20, height=1, font=('tahoma', 8), wrap='none')
text_PatientID.place(x=20, y=y_origin+i*gain)
label_PatientID = tk.Label(root, text='Patient ID:', font=('tahoma', 8))
label_PatientID.place(x=20,y=y_origin+i*gain-25)

text_ID = tk.Text(root, width=25, height=1, font=('tahoma', 8), wrap='none')
text_ID.place(x=220, y=y_origin+i*gain)
label_ID = tk.Label(root, text='ID:', font=('tahoma', 8))
label_ID.place(x=220,y=y_origin+i*gain-25)


text_BirthDate = tk.Text(root, width=20, height=1, font=('tahoma', 8), wrap='none')
text_BirthDate.place(x=420, y=y_origin+i*gain)
label_BirthDate = tk.Label(root, text='Birth Date:', font=('tahoma', 8))
label_BirthDate.place(x=420,y=y_origin+i*gain-25)

text_No = tk.Text(root, width=10, height=1, font=('tahoma', 8), wrap='none')
text_No.place(x=620, y=y_origin+i*gain)

i = 2

text_RackNumber = tk.Text(root, width=20, height=1, font=('tahoma', 8), wrap='none')
text_RackNumber.place(x=20, y=y_origin+i*gain)
label_RackNumber = tk.Label(root, text='Rack Number:', font=('tahoma', 8))
label_RackNumber.place(x=20,y=y_origin+i*gain-25)

text_SampleID = tk.Text(root, width=26, height=1, font=('tahoma', 8), wrap='none')
text_SampleID.place(x=220, y=y_origin+i*gain)
label_SampleID = tk.Label(root, text='Sample ID:', font=('tahoma', 8))
label_SampleID.place(x=220,y=y_origin+i*gain-25)

text_SampleType = tk.Text(root, width=20, height=1, font=('tahoma', 8), wrap='none')
text_SampleType.place(x=420, y=y_origin+i*gain)
label_SampleType = tk.Label(root, text='Sample Type:', font=('tahoma', 8))
label_SampleType.place(x=420,y=y_origin+i*gain-25)

text_SampleStatus = tk.Text(root, width=20, height=1, font=('tahoma', 8), wrap='none')
text_SampleStatus.place(x=620, y=y_origin+i*gain)
label_SampleStatus = tk.Label(root, text='Sample Status:', font=('tahoma', 8))
label_SampleStatus.place(x=620,y=y_origin+i*gain-25)


i = 3

text_Diagnosis1 = tk.Text(root, width=40, height=1, font=('tahoma', 8), wrap='none')
text_Diagnosis1.place(x=20, y=y_origin+i*gain)
label_Diagnosis1 = tk.Label(root, text='Diagnosis 1:', font=('tahoma', 8))
label_Diagnosis1.place(x=20,y=y_origin+i*gain-25)

text_Diagnosis2 = tk.Text(root, width=40, height=1, font=('tahoma', 8), wrap='none')
text_Diagnosis2.place(x=320, y=y_origin+i*gain)
label_Diagnosis2 = tk.Label(root, text='Diagnosis 2:', font=('tahoma', 8))
label_Diagnosis2.place(x=320,y=y_origin+i*gain-25)

text_Diagnosis3 = tk.Text(root, width=40, height=1, font=('tahoma', 8), wrap='none')
text_Diagnosis3.place(x=620, y=y_origin+i*gain)
label_Diagnosis3 = tk.Label(root, text='Diagnosis 3:', font=('tahoma', 8))
label_Diagnosis3.place(x=620,y=y_origin+i*gain-25)

text_Diagnosis4 = tk.Text(root, width=40, height=1, font=('tahoma', 8), wrap='none')
text_Diagnosis4.place(x=920, y=y_origin+i*gain)
label_Diagnosis4 = tk.Label(root, text='Diagnosis 4:', font=('tahoma', 8))
label_Diagnosis4.place(x=920,y=y_origin+i*gain-25)

text_Diagnosis5 = tk.Text(root, width=40, height=1, font=('tahoma', 8), wrap='none')
text_Diagnosis5.place(x=1220, y=y_origin+i*gain)
label_Diagnosis5 = tk.Label(root, text='Diagnosis 5:', font=('tahoma', 8))
label_Diagnosis5.place(x=1220,y=y_origin+i*gain-25)

i = 4

text_Telephone = tk.Text(root, width=40, height=1, font=('tahoma', 8), wrap='none')
text_Telephone.place(x=20, y=y_origin+i*gain)
label_Telephone = tk.Label(root, text='Telephone:', font=('tahoma', 8))
label_Telephone.place(x=20,y=y_origin+i*gain-25)

text_Comments = tk.Text(root, width=140, height=1, font=('tahoma', 8), wrap='none')
text_Comments.place(x=320, y=y_origin+i*gain)
label_Comments = tk.Label(root, text='Comments:', font=('tahoma', 8))
label_Comments.place(x=320,y=y_origin+i*gain-25)

# /////Buttons//////////////////////

button_browse=ttk.Button(root, text='Browse', width=15, command=browse)
button_browse.place(x=1450, y=500)

# ////////////// Record Num/////////////////
text_num = tk.Text(root, width=8, height=1, font=('tahoma', 8), wrap='none')
text_num.place(x=1290, y=500)

# ////////////// Function Button //////////

button_update=ttk.Button(root, text='Update', width=15, command=update)
button_update.place(x=1230, y=820)

button_exit=ttk.Button(root, text='Exit', width=15, command=root.destroy)
button_exit.place(x=1450, y=820)

button_new_record=ttk.Button(root, text='New...', width=15, command=new_record)
button_new_record.place(x=30, y=500)

button_delete=ttk.Button(root, text='Delete', width=15, command=delete)
button_delete.place(x=220, y=500)

# ///// Search Edit Box//////////

text_PatientName_Search = tk.Text(root, width=20, height=1, font=('tahoma', 9), wrap='none')
text_PatientName_Search.place(x=420, y=510)
label_PatientName_Search = tk.Label(root, text='Patient\'s Name:', font=('tahoma', 8))
label_PatientName_Search.place(x=420,y=485)

button_PatientName_Search=ttk.Button(root, text='Search', width=15, command=patientNameSearch)
button_PatientName_Search.place(x=600, y=500)

root.mainloop()

conn.close()

#t = datetime.datetime.now()
#ts = str(datetime.datetime.now())

#datetime.datetime.strptime(ts, '%Y%m%d%I%M%S%f')