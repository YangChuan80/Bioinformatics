#!/usr/bin/env python
# coding: utf-8

# # Modules

# In[1]:


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog


# # Member Functions

# In[2]:


def loadCoronaVirusDNA(filename):
    f = open(filename)
    dna=''
    for line in f:
        if line[0] != '>':
            dna += line.rstrip()
        else:
            header = line[1:]
            #header = line.split()
            #name = header[0][1:]
    return header, dna


# In[3]:


def reverseComplement(sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'N': 'N'}
    csequence=''
    for s in sequence:
        csequence = complement[s] + csequence
    return csequence


# In[4]:


codon = {'ATT': ('Isoleucine', 'Ile', 'I'),
         'ATC': ('Isoleucine', 'Ile', 'I'),
         'ATA': ('Isoleucine', 'Ile', 'I'),
         
         'CTT': ('Leucine', 'Leu', 'L'),
         'CTC': ('Leucine', 'Leu', 'L'),
         'CTA': ('Leucine', 'Leu', 'L'),
         'CTG': ('Leucine', 'Leu', 'L'),
         'TTA': ('Leucine', 'Leu', 'L'),
         'TTG': ('Leucine', 'Leu', 'L'),
         
         'GTT': ('Valine', 'Val', 'V'),
         'GTC': ('Valine', 'Val', 'V'),
         'GTA': ('Valine', 'Val', 'V'),
         'GTG': ('Valine', 'Val', 'V'),
         
         'TTT': ('Phenylalanine', 'Phe', 'F'),
         'TTC': ('Phenylalanine', 'Phe', 'F'),
         
         'ATG': ('Methionine', 'Met', 'M'),
         
         'TGT': ('Cysteine ', 'Cys', 'C'),
         'TGC': ('Cysteine ', 'Cys', 'C'),         
         
         'GCT': ('Alanine', 'Ala', 'A'),
         'GCC': ('Alanine', 'Ala', 'A'),
         'GCA': ('Alanine', 'Ala', 'A'),
         'GCG': ('Alanine', 'Ala', 'A'),
         
         'GGT': ('Glycine ', 'Gly', 'G'),
         'GGC': ('Glycine ', 'Gly', 'G'),
         'GGA': ('Glycine ', 'Gly', 'G'),
         'GGG': ('Glycine ', 'Gly', 'G'),
         
         'CCT': ('Proline', 'Pro', 'P'),
         'CCC': ('Proline', 'Pro', 'P'),
         'CCA': ('Proline', 'Pro', 'P'),
         'CCG': ('Proline', 'Pro', 'P'),
         
         'ACT': ('Threonine', 'Thr', 'T'),
         'ACC': ('Threonine', 'Thr', 'T'),
         'ACA': ('Threonine', 'Thr', 'T'),
         'ACG': ('Threonine', 'Thr', 'T'),
         
         'TCT': ('Serine', 'Ser', 'S'),
         'TCC': ('Serine', 'Ser', 'S'),
         'TCA': ('Serine', 'Ser', 'S'),
         'TCG': ('Serine', 'Ser', 'S'),
         'AGT': ('Serine', 'Ser', 'S'),
         'AGC': ('Serine', 'Ser', 'S'),
         
         'TAT': ('Tyrosine', 'Tyr', 'Y'),
         'TAC': ('Tyrosine', 'Tyr', 'Y'),
         
         'TGG': ('Tryptophan', 'Trp', 'W'),
         
         'CAA': ('Glutamine', 'Gln', 'Q'),
         'CAG': ('Glutamine', 'Gln', 'Q'),
         
         'AAT': ('Asparagine', 'Asn', 'N'),
         'AAC': ('Asparagine', 'Asn', 'N'),
         
         'CAT': ('Histidine ', 'His', 'H'),
         'CAC': ('Histidine ', 'His', 'H'),
         
         'GAA': ('Glutamic acid', 'Glu', 'E'),
         'GAG': ('Glutamic acid', 'Glu', 'E'),
         
         'GAT': ('Aspartic acid', 'Asp', 'D'),
         'GAC': ('Aspartic acid', 'Asp', 'D'),
                  
         'AAA': ('Lysine', 'Lys', 'K'),
         'AAG': ('Lysine', 'Lys', 'K'),
         
         'CGT': ('Arginine', 'Arg', 'R'),
         'CGC': ('Arginine', 'Arg', 'R'),
         'CGA': ('Arginine', 'Arg', 'R'),
         'CGG': ('Arginine', 'Arg', 'R'),
         'AGA': ('Arginine', 'Arg', 'R'),
         'AGG': ('Arginine', 'Arg', 'R'),
         
         'TAA': ('Stop', 'Stop', '___'),
         'TAG': ('Stop', 'Stop', '___'),
         'TGA': ('Stop', 'Stop', '___')
         }


# In[5]:


def translate(dna):
    aminoacid = ''
    amino = ''
    a = ''
    i = 0
    dna_len = len(dna)
    DNA = dna.upper()
    
    while(1):
        if i+3 <= dna_len:
            c = DNA[i:i+3]
            residue = codon[c][0]
            res = codon[c][1]
            r = codon[c][2]
            
            if i == 0:
                aminoacid = residue
                amino = res
                a = a + r
                
            else:
                aminoacid = aminoacid + '-' + residue
                amino = amino + '-' + res
                a = a + r

            i = i + 3
        else:
            break
    return aminoacid, amino, a


# # Control Functions

# In[6]:


def browseFileButton():
   
    filename = filedialog.askopenfilename(filetypes=(('FASTA files', '*.fa'), ('All files', '*.*')))
    name, dna = loadCoronaVirusDNA(filename)
    
    text_header.delete('1.0', tk.END)
    text_header.insert('1.0', name)
    
    text_raw.delete('1.0', tk.END)
    text_raw.insert('1.0', dna)

    text_rawLen.delete('1.0', tk.END)
    text_rawLen.insert('1.0', len(dna))  


# In[7]:


def buttonTrim():
    dna_raw = text_raw.get('1.0', tk.END).rstrip().upper()
    
    dna_temp_list1 = dna_raw.split(' ')
    dna_withoutBlank = ''.join(dna_temp_list1)
    
    dna_temp_list2 = dna_withoutBlank.split('\n')
    dna_withoutReturn = ''.join(dna_temp_list2)    
  
    text_dna.delete('1.0', tk.END)
    text_dna.insert('1.0', dna_withoutReturn)  
    
    text_dnaLen.delete('1.0', tk.END)
    text_dnaLen.insert('1.0', len(dna_withoutReturn))  


# In[8]:


def buttonDnaSlice():
    dnaSliceNo = text_dna_sliceRange.get('1.0', tk.END).rstrip()
    dna_withoutSlice = text_dna.get('1.0', tk.END).rstrip()
    
    start = 0
    end = 3
    
    if dnaSliceNo.find('..') != -1:
        duration = dnaSliceNo.split('..')
        start = int(duration[0])
        end = int(duration[1])
                
    elif dnaSliceNo.find(':') != -1:
        duration = dnaSliceNo.split(':')
        start = int(duration[0])
        end = int(duration[1])        
        
    elif dnaSliceNo.find(', ') != -1:
        duration = dnaSliceNo.split(', ')
        start = int(duration[0])
        end = int(duration[1])        
        
    elif dnaSliceNo.find(' ') != -1:
        duration = dnaSliceNo.split(' ')       
        start = int(duration[0])
        end = int(duration[1])       
        
    elif dnaSliceNo.find(',') != -1:
        duration = dnaSliceNo.split(',')
        start = int(duration[0])
        end = int(duration[1])
        
    else:
        messagebox.showwarning("No Effective Slice Number", 
                               "Sorry, there's no effective slice number! Please check.")
    
    # Another if //////////////////////////////////////
         
    if start >= end:
        messagebox.showwarning("Invalid Slice Number", 
                               "Sorry, invalid slice number! Please check.")
        
    elif end-start > len(dna_withoutSlice):
        messagebox.showwarning("Invalid Slice Number", 
                               "Sorry, the slice number you input is longer than the sequence! Please check.")
        
    else:
        dna_slice = dna_withoutSlice[(start-1):(end-1)]
        text_dna.delete('1.0', tk.END)
        text_dna.insert('1.0', dna_slice)
        
        text_dnaLen.delete('1.0', tk.END)
        text_dnaLen.insert('1.0', len(dna_slice))  


# In[9]:


def buttonAaSlice():
    aaSliceNo = text_aa_sliceRange.get('1.0', tk.END).rstrip()
    aa_withoutSlice = text_aa.get('1.0', tk.END).rstrip()
    
    start = 0
    end = 10
    
    if aaSliceNo.find('..') != -1:
        duration = aaSliceNo.split('..')
        start = int(duration[0])
        end = int(duration[1])
                
    elif aaSliceNo.find(':') != -1:
        duration = aaSliceNo.split(':')
        start = int(duration[0])
        end = int(duration[1])        
        
    elif aaSliceNo.find(', ') != -1:
        duration = aaSliceNo.split(', ')
        start = int(duration[0])
        end = int(duration[1])        
        
    elif aaSliceNo.find(' ') != -1:
        duration = aaSliceNo.split(' ')       
        start = int(duration[0])
        end = int(duration[1])       
        
    elif aaSliceNo.find(',') != -1:
        duration = aaSliceNo.split(',')
        start = int(duration[0])
        end = int(duration[1])
        
    else:
        messagebox.showwarning("No Effective Slice Number", 
                               "Sorry, there's no effective slice number! Please check.")
        
    # /////// Another if /////////////////////////
         
    if start >= end:
        messagebox.showwarning("Invalid Slice Number", 
                               "Sorry, invalid slice number! Please check.")
        
    elif end-start > len(aa_withoutSlice):
        messagebox.showwarning("Invalid Slice Number", 
                               "Sorry, the slice number you input is longer than the sequence! Please check.")
        
    else:
        aa_slice = aa_withoutSlice[(start-1):(end-1)]
        text_aa_slice.delete('1.0', tk.END)
        text_aa_slice.insert('1.0', aa_slice) 
        
        text_aa_sliceLen.delete('1.0', tk.END)
        text_aa_sliceLen.insert('1.0', len(aa_slice))


# In[10]:


def buttonTranslate():    
    dna = text_dna.get('1.0', tk.END).rstrip()
    
    aa_tuple = translate(dna)
    
    text_aminoAcid.delete('1.0', tk.END)
    text_aminoAcid.insert('1.0', aa_tuple[1])
    
    text_aa.delete('1.0', tk.END)
    text_aa.insert('1.0', aa_tuple[2])    
    
    text_aaLen.delete('1.0', tk.END)
    text_aaLen.insert('1.0', len(aa_tuple[2]))


# In[11]:


def about():
    about_root=tk.Tk()
    
    w = 367 # width for the Tk root
    h = 230 # height for the Tk root

    # get screen width and height
    ws = about_root.winfo_screenwidth() # width of the screen
    hs = about_root.winfo_screenheight() # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # set the dimensions of the screen 
    # and where it is placed
    about_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    about_root.title('About Buffalo Sequences')  

    label_author=tk.Label(about_root,text='Buffalo Sequences Version 1.0', font=('tahoma', 9))
    label_author.place(x=90,y=30)

    label_author=tk.Label(about_root,text='Copyright (C) 2020', font=('tahoma', 9))
    label_author.place(x=125,y=60)
    
    label_author=tk.Label(about_root,text='Author: Chuan Yang', font=('tahoma', 9))
    label_author.place(x=125,y=90)
    
    label_author=tk.Label(about_root,text='Shengjing Hospital of China Medical University', font=('tahoma', 9))
    label_author.place(x=50,y=120)
   

    button_refresh=ttk.Button(about_root, width=15, text='OK', command=about_root.destroy)
    button_refresh.place(x=135, y=170)

    about_root.mainloop()


# # Main

# In[12]:


# Main Frame////////////////////////////////////////////////////////////////////////////////////////
root = tk.Tk()

#w = 1250 # width for the Tk root
#h = 720 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
#x = (ws/2) - (w/2)
#y = (hs/4) - (h/4)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (ws, hs, 0, 0))
#root.attributes('-fullscreen', True)
root.title('Buffalo Sequences')
#root.iconbitmap('Heart.ico')

# //////// Frame /////////////////////////////

#label_expression=tk.Label(root,width=174, height=44, font=('tahoma', 9), relief='raised', borderwidth=2)
#label_expression.place(x=20,y=15)


#/////////////Text///////////////////////////////////////////////////////////////////
y_position = 35
text_header=tk.Text(root, width=126,height=1, font=('tahoma', 9), bd=1)
text_header.place(x=160, y=y_position)

y_position = 70
text_raw=tk.Text(root, width=160,height=6, font=('tahoma', 9), bd=1)
text_raw.place(x=30, y=y_position)
label_dna=tk.Label(root, text='DNA', font=('tahoma', 9))
label_dna.place(x=30,y=y_position-30)

text_rawLen=tk.Text(root, width=12,height=1, font=('tahoma', 9), bd=1)
text_rawLen.place(x=1170, y=y_position)

y_position = 180
text_dna=tk.Text(root, width=160,height=6, font=('tahoma', 9), bd=1)
text_dna.place(x=30, y=y_position)

text_dnaLen=tk.Text(root, width=12,height=1, font=('tahoma', 9), bd=1)
text_dnaLen.place(x=1170, y=y_position)

y_position = 290

text_dna_sliceRange=tk.Text(root, width=25,height=1, font=('tahoma', 9), bd=1)
text_dna_sliceRange.place(x=30, y=y_position+5)

#//////////////////
y_position = 365

text_aminoAcid=tk.Text(root, width=160,height=5, font=('tahoma', 9), bd=1)
text_aminoAcid.place(x=30, y=y_position)
label_aminoAcid=tk.Label(root, text='Amino Acid', font=('tahoma', 9))
label_aminoAcid.place(x=30,y=y_position-30)

text_aa=tk.Text(root, width=160,height=4, font=('tahoma', 9), bd=1)
text_aa.place(x=30, y=y_position+90)

text_aaLen=tk.Text(root, width=12,height=1, font=('tahoma', 9), bd=1)
text_aaLen.place(x=1170, y=y_position+90)

text_aa_slice=tk.Text(root, width=160,height=5, font=('tahoma', 9), bd=1)
text_aa_slice.place(x=30, y=y_position+170)

text_aa_sliceLen=tk.Text(root, width=12,height=1, font=('tahoma', 9), bd=1)
text_aa_sliceLen.place(x=1170, y=y_position+170)

text_aa_sliceRange=tk.Text(root, width=25,height=1, font=('tahoma', 9), bd=1)
text_aa_sliceRange.place(x=30, y=y_position+270)

# Initial Slice No /////////////////////////

text_dna_sliceRange.delete('1.0', tk.END)
text_dna_sliceRange.insert('1.0', '1..10')    

text_aa_sliceRange.delete('1.0', tk.END)
text_aa_sliceRange.insert('1.0', '1..10')    

#/////////////Button///////////////////////////////////////////////////////////////

button_translate=ttk.Button(root, text='Translate', width=30, command=buttonTranslate)
button_translate.place(x=500, y=290)

button_trim=ttk.Button(root, text='Trim', width=13, command=buttonTrim)
button_trim.place(x=1170, y=120)

button_dna_slice=ttk.Button(root, text='Slice', width=13, command=buttonDnaSlice)
button_dna_slice.place(x=240, y=290)

button_aa_slice=ttk.Button(root, text='Slice', width=13, command=buttonAaSlice)
button_aa_slice.place(x=240, y=635)

button_browse=ttk.Button(root, text='Browse...', width=20, command=browseFileButton)
button_browse.place(x=1120, y=32)

button_close=ttk.Button(root, text='Exit', width=20, command=root.destroy)
button_close.place(x=1120, y=635)

button_about=ttk.Button(root, text='About...', width=20, command=about)
button_about.place(x=930, y=635)

root.mainloop()

