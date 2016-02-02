### Module Import

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import tkinter.font as tkf
import sqlite3
import numpy as np
import pandas as pd

### DB Connection

conn = sqlite3.connect('AnalysisDB.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Combined')
desc = cur.description
headers = [item[0] for item in desc]

cur.execute('SELECT * FROM Combined')
genes = cur.fetchall()

### Helper Functions

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

def extractID(iden):
    cur.execute('SELECT * FROM Combined WHERE GeneID = ?', (iden,))    
    row = cur.fetchone()    
    arrange(row)

def arrange(row):
    item = {}
    for i in range(len(row)):
        item[headers[i]] = row[i]
    display_in_text(item)

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

def clear():
    for i in table.get_children():
        table.delete(i)

def refreshDB():
    global conn, cur, desc, headers, genes
    conn.close()
    conn = sqlite3.connect('AnalysisDB.sqlite')
    cur = conn.cursor()

    cur.execute('SELECT * FROM Combined')
    desc = cur.description
    headers = [item[0] for item in desc]

    cur.execute('SELECT * FROM Combined')
    genes = cur.fetchall()

def show():
    gotten = text_SearchID.get('1.0', tk.END)
    gotten = gotten.rstrip()
    
    cur.execute('SELECT * FROM Combined WHERE PatientID = ?', (gotten,))
    items = cur.fetchall()
    
    clear()
    display_in_table(items)    

def delete_case():
    try:
        gotten = text_SearchID.get('1.0', tk.END)
        gotten = gotten.rstrip()
        cur.execute('DELETE FROM Combined WHERE PatientID = ?', (gotten,))
        conn.commit()
        messagebox.showinfo("Deleted", "Case successfully deleted!")
        clear()
        refreshDB()
        display_in_table(genes)
    except:
        pass

def delete_gene():
    try:
        gotten = idglb
        cur.execute('DELETE FROM Combined WHERE GeneID = ?', (gotten,))
        conn.commit()
        messagebox.showinfo("Deleted", "Gene successfully deleted!")
        clear()
        refreshDB()
        display_in_table(genes)
    except:
        pass

def browse():
    clear()
    refreshDB()
    display_in_table(genes)

def display_in_table(genes):
    for gene in genes:
        table.insert("", "end", "", values=gene)
    num = str(len(genes))
    text_num.delete('1.0', tk.END)
    text_num.insert('1.0', num)

def display_in_text(item):
    text_PatientID.delete('1.0', tk.END)
    text_PatientID.insert('1.0', item['PatientID'])    
    
    text_CHROM.delete('1.0', tk.END)
    text_CHROM.insert('1.0', item['CHROM'])
        
    text_POS.delete('1.0', tk.END)
    text_POS.insert('1.0', item['POS'])
    
    text_REF.delete('1.0', tk.END)
    text_REF.insert('1.0', item['REF'])
    
    text_ALT.delete('1.0', tk.END)
    text_ALT.insert('1.0', item['ALT'])    
    
    text_Reads.delete('1.0', tk.END)
    text_Reads.insert('1.0', item['Reads'])
    
    text_reason_for_inclusion_postParsing.delete('1.0', tk.END)
    text_reason_for_inclusion_postParsing.insert('1.0', item['reason_for_inclusion_postParsing'])
    
    text_filt_freq.delete('1.0', tk.END)
    text_filt_freq.insert('1.0', item['filt_freq'])
    
    text_filt_alt_count.delete('1.0', tk.END)
    text_filt_alt_count.insert('1.0', item['filt_alt_count'])
    
    text_filt_total_count.delete('1.0', tk.END)
    text_filt_total_count.insert('1.0', item['filt_total_count'])
    
    text_filt_db_name.delete('1.0', tk.END)
    text_filt_db_name.insert('1.0', item['filt_db_name'])
    
    text_Func__refGene.delete('1.0', tk.END)
    text_Func__refGene.insert('1.0', item['Func__refGene'])
    
    text_Gene__refGene.delete('1.0', tk.END)
    text_Gene__refGene.insert('1.0', item['Gene__refGene'])
    
    text_GeneDetail__refGene.delete('1.0', tk.END)
    text_GeneDetail__refGene.insert('1.0', item['GeneDetail__refGene'])
    
    text_ExonicFunc__refGene.delete('1.0', tk.END)
    text_ExonicFunc__refGene.insert('1.0', item['ExonicFunc__refGene'])
    
    text_AAChange__refGene.delete('1.0', tk.END)
    text_AAChange__refGene.insert('1.0', item['AAChange__refGene'])
    
    text_Func__knownGene.delete('1.0', tk.END)
    text_Func__knownGene.insert('1.0', item['Func__knownGene'])
    
    text_Gene__knownGene.delete('1.0', tk.END)
    text_Gene__knownGene.insert('1.0', item['Gene__knownGene'])
    
    text_GeneDetail__knownGene.delete('1.0', tk.END)
    text_GeneDetail__knownGene.insert('1.0', item['GeneDetail__knownGene'])
    
    text_ExonicFunc__knownGene.delete('1.0', tk.END)
    text_ExonicFunc__knownGene.insert('1.0', item['ExonicFunc__refGene'])
    
    text_AAChange__knownGene.delete('1.0', tk.END)
    text_AAChange__knownGene.insert('1.0', item['AAChange__knownGene'])
    
    text_geneDisease_annotation.delete('1.0', tk.END)
    text_geneDisease_annotation.insert('1.0', item['geneDisease_annotation'])
    
    text_HGMD_mutations_nearby.delete('1.0', tk.END)
    text_HGMD_mutations_nearby.insert('1.0', item['HGMD_mutations_nearby'])   
    
    text_retinaSpecific_exon.delete('1.0', tk.END)
    text_retinaSpecific_exon.insert('1.0', item['retinaSpecific_exon'])
    
    text_variant_exceptions_list.delete('1.0', tk.END)
    text_variant_exceptions_list.insert('1.0', item['variant_exceptions_list'])
    
    text_ada_score.delete('1.0', tk.END)
    text_ada_score.insert('1.0', item['ada_score'])
    
    text_rf_score.delete('1.0', tk.END)
    text_rf_score.insert('1.0', item['rf_score'])
    
    text_rs_dbSNP141.delete('1.0', tk.END)
    text_rs_dbSNP141.insert('1.0', item['rs_dbSNP141'])
    
    text_Interpro_domain.delete('1.0', tk.END)
    text_Interpro_domain.insert('1.0', item['Interpro_domain'])
    
    text_SIFT_pred.delete('1.0', tk.END)
    text_SIFT_pred.insert('1.0', item['SIFT_pred'])
    
    text_Polyphen2_HDIV_pred.delete('1.0', tk.END)
    text_Polyphen2_HDIV_pred.insert('1.0', item['Polyphen2_HDIV_pred'])
    
    text_Polyphen2_HVAR_pred.delete('1.0', tk.END)
    text_Polyphen2_HVAR_pred.insert('1.0', item['Polyphen2_HVAR_pred'])
    
    text_LRT_pred.delete('1.0', tk.END)
    text_LRT_pred.insert('1.0', item['LRT_pred'])
    
    text_MutationTaster_pred.delete('1.0', tk.END)
    text_MutationTaster_pred.insert('1.0', item['MutationTaster_pred'])
    
    text_MutationAssessor_pred.delete('1.0', tk.END)
    text_MutationAssessor_pred.insert('1.0', item['MutationAssessor_pred'])
    
    text_FATHMM_pred.delete('1.0', tk.END)
    text_FATHMM_pred.insert('1.0', item['FATHMM_pred'])
    
    text_MetaSVM_pred.delete('1.0', tk.END)
    text_MetaSVM_pred.insert('1.0', item['MetaSVM_pred'])
    
    text_MetaLR_pred.delete('1.0', tk.END)
    text_MetaLR_pred.insert('1.0', item['MetaLR_pred'])
    
    text_VEST3_rankscore.delete('1.0', tk.END)
    text_VEST3_rankscore.insert('1.0', item['VEST3_rankscore'])
    
    text_PROVEAN_pred.delete('1.0', tk.END)
    text_PROVEAN_pred.insert('1.0', item['PROVEAN_pred'])
    
    text_CADD_raw_rankscore.delete('1.0', tk.END)
    text_CADD_raw_rankscore.insert('1.0', item['CADD_raw_rankscore'])
    
    text_GERP_RS_rankscore.delete('1.0', tk.END)
    text_GERP_RS_rankscore.insert('1.0', item['GERP_RS_rankscore'])
    
    text_phyloP100way_vertebrate_rankscore.delete('1.0', tk.END)
    text_phyloP100way_vertebrate_rankscore.insert('1.0', item['phyloP100way_vertebrate_rankscore'])
    
    text_phastCons100way_vertebrate_rankscore.delete('1.0', tk.END)
    text_phastCons100way_vertebrate_rankscore.insert('1.0', item['phastCons100way_vertebrate_rankscore'])
    
    text_SiPhy_29way_logOdds_rankscore.delete('1.0', tk.END)
    text_SiPhy_29way_logOdds_rankscore.insert('1.0', item['SiPhy_29way_logOdds_rankscore'])
    
    text_clinvar_clnsig.delete('1.0', tk.END)
    text_clinvar_clnsig.insert('1.0', item['clinvar_clnsig'])
    
    text_clinvar_trait.delete('1.0', tk.END)
    text_clinvar_trait.insert('1.0', item['clinvar_trait'])
    
    text_SearchID.delete('1.0', tk.END)
    text_SearchID.insert('1.0', item['PatientID'])

def load():
    fname = filedialog.askopenfilename(filetypes=(('CSV files', '*.csv'),
                                                  ('Excel files', '*.xlsx'),
                                                  ('All files', '*.*')))
    if fname !='':
        loadDB(fname)

def loadDB(fname):
    df = pd.read_csv(fname)

    columns_raw = list(df.columns)
    columns = [column.split('=')[0] for column in columns_raw]

    patientid = columns[4]
    columns[4] = 'Reads'
    columns[:0] = ['GeneID', 'PatientID']

    column_types = [column+' TEXT,' for column in columns]
    column_types[0] = column_types[0][:-5]+'INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,'

    column_types[3] = column_types[3][:-5]+'INTEGER,'
    column_types[8] = column_types[8][:-5]+'NUMBER,'
    column_types[9] = column_types[9][:-5]+'NUMBER,'
    column_types[10] = column_types[10][:-5]+'NUMBER,'
    column_types[26] = column_types[26][:-5]+'NUMBER,'
    column_types[27] = column_types[27][:-5]+'NUMBER,'
    column_types[39] = column_types[39][:-5]+'NUMBER,'
    column_types[41] = column_types[41][:-5]+'NUMBER,'
    column_types[42] = column_types[42][:-5]+'NUMBER,'
    column_types[43] = column_types[43][:-5]+'NUMBER,'
    column_types[44] = column_types[44][:-5]+'NUMBER,'
    column_types[45] = column_types[45][:-5]+'NUMBER,'

    body = ' '.join(column_types)

    body_cleaned = ''
    i = 0
    for l in body:
        if l == '-':
            i = 1
            continue
        elif l == '.':
            body_cleaned +='__'
        elif l == '#':
            body_cleaned +=''
        elif l == '+':
            body_cleaned +=''
        elif i == 1:
            body_cleaned += l.upper()
            i = 0
        else:
            body_cleaned += l        

    body_cleaned = body_cleaned[:-1]
    create_command = 'CREATE TABLE IF NOT EXISTS Combined' + '(' + body_cleaned + ')'

    columns_withoutid = columns[1:]
    columns_joined = ', '.join(columns_withoutid)
    columns_joined

    headers_cleaned = ''
    i = 0
    for l in columns_joined:
        if l == '-':
            i = 1
            continue
        elif l == '.':
            headers_cleaned +='__'
        elif l == '#':
            headers_cleaned +=''
        elif l == '+':
            headers_cleaned +=''
        elif i == 1:
            headers_cleaned += l.upper()
            i = 0
        else:
            headers_cleaned += l

    #Create Table if not exist
    cur.execute(create_command)

    for i in range(len(df.index)):
        value = list(df.ix[i])
        value[:0] = [patientid]
        value[2] = int(value[2])
        value = tuple(value)
        insert_command = 'INSERT INTO Combined' + '(' + headers_cleaned + ') VALUES(' + '?, '*(len(columns)-2) +'?' +')'
        cur.execute(insert_command, value)

    type(value[1])

    conn.commit()
    messagebox.showinfo("Loaded", "Database Loaded!")
    clear()
    refreshDB()
    display_in_table(genes)

def cheat_sheet():
    cheat_sheet_win = tk.Tk()
    cheat_sheet_win.geometry('1250x690+50+10')    
    
    cheat_sheet_win.title('Cheat Sheet')
    text_cstext = tk.Text(cheat_sheet_win, width=170, height=43, font=('tahoma', 9))
    text_cstext.place(x=20, y=20)
    
    txt = '''#CHROM
    
POS

REF

ALT

SRF_1658
reason_for_inclusion_post-parsing = The category this variant falls in as to why we are interested in it.

filt_freq = The highest observed ethnicity-specific population frequency of the variant if found in control databases.

filt_alt_count = Number of alternative alleles in control group.

filt_total_count = Total number of alleles in control group.

filt_db_name = Name of control database where the highest frequency is observed.

Func.refGene = Func.refGene annotation provided by ANNOVAR

Gene.refGene = Gene.refGene annotation provided by ANNOVAR

GeneDetail.refGene = GeneDetail.refGene annotation provided by ANNOVAR

ExonicFunc.refGene = ExonicFunc.refGene annotation provided by ANNOVAR

AAChange.refGene = AAChange.refGene annotation provided by ANNOVAR

Func.knownGene = Func.knownGene annotation provided by ANNOVAR

Gene.knownGene = Gene.knownGene annotation provided by ANNOVAR

GeneDetail.knownGene = GeneDetail.knownGene annotation provided by ANNOVAR

ExonicFunc.knownGene = ExonicFunc.knownGene annotation provided by ANNOVAR

AAChange.knownGene = AAChange.knownGene annotation provided by ANNOVAR

gene-disease_annotation = Diseases and inheritance patterns associated with mutations in the corresponding gene, likely recessive if not specified

HGMD_mutations_nearby = Mutations present in HGMD v.11-15-2014 within 15bp of the variant will be listed separated by '&'.  If an HGMD mutation matching the variant is found it will be printed first prefixed by 'MATCH-'. Format of the annotation  =  chr:pos:ref>alt:gene:isoform:cDNA change:Protein change(if SNV):HGMD's confidence of causality:disease:pubmed ID references&[next mutation]

retina-specific_exon = The boundaries of the proposed retina-specific exon in which the variant lies as identified using human RNA-seq by the Eric Pierce group.

variant_exceptions_list = The reason for the variant's inclusion in the variant_exceptions_list.

ada_score = ensemble prediction score based on ada-boost. Ranges 0 to 1. The larger the score the higher probability the scSNV will affect splicing. The suggested cutoff for a binary prediction (affecting splicing vs. not affecting splicing) is 0.6.

rf_score = ensemble prediction score based on random forests. Ranges 0 to 1. The larger the score the higher probability the scSNV will affect splicing. The suggested cutoff for a binary prediction (affecting splicing vs. not affecting splicing) is 0.6.

rs_dbSNP141 = rs number from dbSNP 141

Interpro_domain = domain or conserved site on which the variant locates. Domain annotations come from Interpro database. The number in the brackets following a specific domain is the count of times Interpro assigns the variant position to that domain, typically coming from different predicting databases. Multiple entries separated by "&".

SIFT_pred = If SIFTori is smaller than 0.05 (rankscore>0.55) the corresponding NS is predicted as "D(amaging)"; otherwise it is predicted as "T(olerated)". Multiple predictions separated by "&"

Polyphen2_HDIV_pred = Polyphen2 prediction based on HumDiv, "D" ("probably damaging", HDIV score in [0.957,1] or rankscore in [0.52996,0.89917]), "P" ("possibly damaging", HDIV score in [0.453,0.956] or rankscore in [0.34412,0.52842]) and "B" ("benign", HDIV score in [0,0.452] or rankscore in [0.02656,0.34399]). Score cutoff for binary classification is 0.5 for HDIV score or 0.35411 for rankscore, i.e. the prediction is "neutral" if the HDIV score is smaller than 0.5 (rankscore is smaller than 0.35411), and "deleterious" if the HDIV score is larger than 0.5 (rankscore is larger than 0.35411). Multiple entries are separated by "&".

Polyphen2_HVAR_pred = Polyphen2 prediction based on HumVar, "D" ("probably damaging", HVAR score in [0.909,1] or rankscore in [0.62955,0.9711]), "P" ("possibly damaging", HVAR in [0.447,0.908] or rankscore in [0.44359,0.62885]) and "B" ("benign", HVAR score in [0,0.446] or rankscore in [0.01281,0.44315]). Score cutoff for binary classification is 0.5 for HVAR score or 0.45998 for rankscore, i.e. the prediction is "neutral" if the HVAR score is smaller than 0.5 (rankscore is smaller than 0.45998), and "deleterious" if the HVAR score is larger than 0.5 (rankscore is larger than 0.45998). Multiple entries are separated by "&".

LRT_pred = LRT prediction, D(eleterious), N(eutral) or U(nknown), which is not solely determined by the score. 

MutationTaster_pred = MutationTaster prediction, "A" ("disease_causing_automatic"), "D" ("disease_causing"), "N" ("polymorphism") or "P" ("polymorphism_automatic"). The score cutoff between "D" and "N" is 0.5 for MTori and 0.328 for the rankscore.

MutationAssessor_pred = MutationAssessor's functional impact of a variant predicted functional, i.e. high ("H") or medium ("M"), or predicted non-functional, i.e. low ("L") or neutral ("N"). The MAori score cutoffs between "H" and "M", "M" and "L", and "L" and "N", are 3.5, 1.9 and 0.8, respectively. The rankscore cutoffs between "H" and "M", "M" and "L", and "L" and "N", are 0.9416, 0.61387 and 0.26162, respectively.

FATHMM_pred = If a FATHMMori score is < = -1.5 (or rankscore < = 0.81415) the corresponding NS is predicted as "D(AMAGING)"; otherwise it is predicted as "T(OLERATED)". Multiple predictions separated by "&"

MetaSVM_pred = Prediction of our SVM based ensemble prediction score,"T(olerated)" or "D(amaging)". The score cutoff between "D" and "T" is 0. The rankscore cutoff between "D" and "T" is 0.83357.

MetaLR_pred = Prediction of our MetaLR based ensemble prediction score,"T(olerated)" or "D(amaging)". The score cutoff between "D" and "T" is 0.5. The rankscore cutoff between "D" and "T" is 0.82268.

VEST3_rankscore = (0-1, <.5 likely benign, .5-.7 uncertain, >.7 likely damaging)VEST3 scores were ranked among all VEST3 scores in dbNSFP. The rankscore is the ratio of the rank of the score over the total number of VEST3 scores in dbNSFP. The scores range from 0 to 1. Please note VEST score is free for non-commercial use. For more details please refer to http://wiki.chasmsoftware.org/index.php/SoftwareLicense. Commercial users should contact the Johns Hopkins Technology Transfer office.

PROVEAN_pred = If PROVEANori < =  -2.5 (rankscore> = 0.59) the corresponding NS is predicted as "D(amaging)"; otherwise it is predicted as "N(eutral)". Multiple predictions separated by "&"

CADD_raw_rankscore = (0-1, cutoff = ~0.738 which corresponds to a score of '15' from original scoring system, so score> = .75 is damaging)CADD raw scores were ranked among all CADD raw scores in dbNSFP. The rankscore is the ratio of the rank of the score over the total number of CADD raw scores in dbNSFP. Please note the following copyright statement for CADD: "CADD scores (http://cadd.gs.washington.edu/) are Copyright 2013 University of Washington and Hudson-Alpha Institute for Biotechnology (all rights reserved) but are freely available for all academic, non-commercial applications. For commercial licensing information contact Jennifer McCullar (mccullaj@uw.edu)."

GERP++_RS_rankscore = (cutoff arbitrary)GERP++ RS scores were ranked among all GERP++ RS scores in dbNSFP. The rankscore is the ratio of the rank of the score over the total number of GERP++ RS scores in dbNSFP.

phyloP100way_vertebrate_rankscore = (cutoff arbitrary)phyloP100way_vertebrate scores were ranked among all phyloP100way_vertebrate scores in dbNSFP. The rankscore is the ratio of the rank of the score over the total number of phyloP100way_vertebrate scores in dbNSFP.

phastCons100way_vertebrate_rankscore = (cutoff arbitrary)phastCons100way_vertebrate scores were ranked among all phastCons100way_vertebrate scores in dbNSFP. The rankscore is the ratio of the rank of the score over the total number of phastCons100way_vertebrate scores in dbNSFP.

SiPhy_29way_logOdds_rankscore = (cutoff arbitrary)SiPhy_29way_logOdds scores were ranked among all SiPhy_29way_logOdds scores in dbNSFP. The rankscore is the ratio of the rank of the score over the total number of SiPhy_29way_logOdds scores in dbNSFP.

clinvar_clnsig = clinical significance as to the clinvar data set 2 - Benign, 3 - Likely benign, 4 - Likely pathogenic, 5 - Pathogenic, 6 - drug response, 7 - histocompatibility. A negative score means the the score is for the ref allele

clinvar_trait = the trait/disease the clinvar_clnsig referring to
'''
    text_cstext.delete('1.0', tk.END)
    text_cstext.insert('1.0', txt)
    
    button_close=ttk.Button(cheat_sheet_win, text='Close', width=15, command=cheat_sheet_win.destroy)
    button_close.place(x=560, y=650)
    
    cheat_sheet_win.mainloop()    

### Main Flow

# Main Frame////////////////////////////////////////////////////////////////////////////////////////
root = tk.Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
#root.attributes('-fullscreen', True)
root.title('Analysis Parser')
root.iconbitmap('dna.ico')

# Multicolumn Listbox/////////////////////////////////////////////////////////////////////////////
table = ttk.Treeview(height="20", columns=headers, selectmode="extended")
table.pack(padx=10, pady=20, ipadx=1200, ipady=115)

i = 1
for header in headers:
    table.heading('#'+str(i), text=header.title(), anchor=tk.W, command=lambda c=header: sortby(table, c, 0))
    table.column('#'+str(i), stretch=tk.NO, minwidth=0, width=tkf.Font().measure(header.title())+30) 
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

#//////////////////////////////////////////////////////////////////////////////////

text_SearchID = tk.Text(root, width=15, height=1, font=('tahoma', 8), wrap='none', bd=2)
text_SearchID.place(x=20, y=320)
text_SearchID.delete('1.0', tk.END)
text_SearchID.insert('1.0', '')

text_num = tk.Text(root, width=8, height=1, font=('tahoma', 8), wrap='none')
text_num.place(x=1280, y=320)

#//////////////////////////////////////////////////////////////////////////////////////
y_origin = 370
gain = 47
i = 0

text_PatientID = tk.Text(root, width=12, height=1, font=('tahoma', 8), wrap='none')
text_PatientID.place(x=20, y=y_origin+i*gain)
label_PatientID=tk.Label(root, text='PatientID:', font=('tahoma', 8))
label_PatientID.place(x=20,y=y_origin+i*gain-25)


text_CHROM = tk.Text(root, width=10, height=1, font=('tahoma', 8), wrap='none')
text_CHROM.place(x=120, y=y_origin+i*gain)
label_CHROM=tk.Label(root, text='CHROM:', font=('tahoma', 8))
label_CHROM.place(x=120,y=y_origin+i*gain-25)

text_POS = tk.Text(root, width=15, height=1, font=('tahoma', 8), wrap='none')
text_POS.place(x=210, y=y_origin+i*gain)
label_POS=tk.Label(root, text='POS:', font=('tahoma', 8))
label_POS.place(x=210,y=y_origin+i*gain-25)

text_REF = tk.Text(root, width=6, height=1, font=('tahoma', 8), wrap='none')
text_REF.place(x=340, y=y_origin+i*gain)
label_REF=tk.Label(root, text='REF:', font=('tahoma', 8))
label_REF.place(x=340,y=y_origin+i*gain-25)

text_ALT = tk.Text(root, width=6, height=1, font=('tahoma', 8), wrap='none')
text_ALT.place(x=400, y=y_origin+i*gain)
label_ALT=tk.Label(root, text='ALT:', font=('tahoma', 8))
label_ALT.place(x=400,y=y_origin+i*gain-25)

text_Reads = tk.Text(root, width=20, height=1, font=('tahoma', 8), wrap='none')
text_Reads.place(x=460, y=y_origin+i*gain)
label_Reads=tk.Label(root, text='Reads:', font=('tahoma', 8))
label_Reads.place(x=460,y=y_origin+i*gain-25)

text_reason_for_inclusion_postParsing = tk.Text(root, width=30, height=1, font=('tahoma', 8), wrap='none')
text_reason_for_inclusion_postParsing.place(x=620, y=y_origin)
label_reason_for_inclusion_postParsing=tk.Label(root, text='reason_for_inclusion_postParsing:', font=('tahoma', 8))
label_reason_for_inclusion_postParsing.place(x=620,y=y_origin+i*gain-25)

text_filt_freq = tk.Text(root, width=18, height=1, font=('tahoma', 8), wrap='none')
text_filt_freq.place(x=850, y=y_origin+i*gain)
label_filt_freq=tk.Label(root, text='filt_freq:', font=('tahoma', 8))
label_filt_freq.place(x=850,y=y_origin+i*gain-25)

text_filt_alt_count = tk.Text(root, width=10, height=1, font=('tahoma', 8), wrap='none')
text_filt_alt_count.place(x=1020, y=y_origin+i*gain)
label_filt_alt_count=tk.Label(root, text='filt_alt_count:', font=('tahoma', 8))
label_filt_alt_count.place(x=1020,y=y_origin+i*gain-25)

text_filt_total_count = tk.Text(root, width=10, height=1, font=('tahoma', 8), wrap='none')
text_filt_total_count.place(x=1140, y=y_origin+i*gain)
label_filt_total_count=tk.Label(root,text='filt_total_count:', font=('tahoma', 8))
label_filt_total_count.place(x=1140,y=y_origin+i*gain-25)

text_filt_db_name = tk.Text(root, width=10, height=1, font=('tahoma', 8), wrap='none')
text_filt_db_name.place(x=1250, y=y_origin+i*gain)
label_filt_db_name=tk.Label(root, text='filt_db_name:', font=('tahoma', 8))
label_filt_db_name.place(x=1250,y=y_origin+i*gain-25)

#/////////////////////////////////////////////////////////////////////////////////
i += 1
label_refGene=tk.Label(root,text='refGene:', font=('tahoma', 6))
label_refGene.place(x=10,y=y_origin+i*gain)

text_Func__refGene = tk.Text(root, width=15, height=1, font=('tahoma', 8), wrap='none')
text_Func__refGene.place(x=60, y=y_origin+i*gain)
label_Func__refGene=tk.Label(root, text='Func:', font=('tahoma', 8))
label_Func__refGene.place(x=60,y=y_origin+i*gain-25)

text_Gene__refGene = tk.Text(root, width=10, height=1, font=('tahoma', 8), wrap='none')
text_Gene__refGene.place(x=180, y=y_origin+i*gain)
label_Gene__refGene=tk.Label(root,text='Gene:', font=('tahoma', 8))
label_Gene__refGene.place(x=180,y=y_origin+i*gain-25)

text_GeneDetail__refGene = tk.Text(root, width=50, height=3, font=('tahoma', 8))
text_GeneDetail__refGene.place(x=265, y=y_origin+i*gain)
label_GeneDetail__refGene=tk.Label(root, text='GeneDetaile:', font=('tahoma', 8))
label_GeneDetail__refGene.place(x=265,y=y_origin+i*gain-25)

text_ExonicFunc__refGene = tk.Text(root, width=20, height=1, font=('tahoma', 8), wrap='none')
text_ExonicFunc__refGene.place(x=600, y=y_origin+i*gain)
label_ExonicFunc__refGene=tk.Label(root, text='ExonicFunc:', font=('tahoma', 8))
label_ExonicFunc__refGene.place(x=600,y=y_origin+i*gain-25)

text_AAChange__refGene = tk.Text(root, width=98, height=3, font=('tahoma', 8))
text_AAChange__refGene.place(x=755, y=y_origin+i*gain)
label_AAChange__refGene=tk.Label(root, text='AAChange:', font=('tahoma', 8))
label_AAChange__refGene.place(x=755,y=y_origin+i*gain-25)

half = 60
label_knownGene=tk.Label(root,text='KnownGene:', font=('tahoma', 6))
label_knownGene.place(x=10,y=y_origin+i*gain+half)

text_Func__knownGene = tk.Text(root, width=15, height=1, font=('tahoma', 8), wrap='none')
text_Func__knownGene.place(x=60, y=y_origin+i*gain+half)

text_Gene__knownGene = tk.Text(root, width=10, height=1, font=('tahoma', 8), wrap='none')
text_Gene__knownGene.place(x=180, y=y_origin+i*gain+half)

text_GeneDetail__knownGene = tk.Text(root, width=50, height=3, font=('tahoma', 8))
text_GeneDetail__knownGene.place(x=265, y=y_origin+i*gain+half)

text_ExonicFunc__knownGene = tk.Text(root, width=20, height=1, font=('tahoma', 8), wrap='none')
text_ExonicFunc__knownGene.place(x=600, y=y_origin+i*gain+half)

text_AAChange__knownGene = tk.Text(root, width=98, height=3, font=('tahoma', 8))
text_AAChange__knownGene.place(x=755, y=y_origin+i*gain+half)

y_origin = 550
gain = 65
i = 0

text_geneDisease_annotation = tk.Text(root, width=73, height=4, font=('tahoma', 8))
text_geneDisease_annotation.place(x=20, y=y_origin+i*gain)
label_geneDisease_annotation=tk.Label(root,text='geneDisease_annotation:', font=('tahoma', 8))
label_geneDisease_annotation.place(x=20,y=y_origin+i*gain-25)

text_HGMD_mutations_nearby = tk.Text(root, width=72, height=4, font=('tahoma', 8))
text_HGMD_mutations_nearby.place(x=500, y=y_origin+i*gain)
label_HGMD_mutations_nearby=tk.Label(root,text='HGMD_mutations_nearby:', font=('tahoma', 8))
label_HGMD_mutations_nearby.place(x=500,y=y_origin+i*gain-25)

text_retinaSpecific_exon = tk.Text(root, width=10, height=1, font=('tahoma', 8), wrap='none')
text_retinaSpecific_exon.place(x=970, y=y_origin+i*gain)
label_retinaSpecific_exon=tk.Label(root,text='retinaSpecific_exon:', font=('tahoma', 7))
label_retinaSpecific_exon.place(x=970,y=y_origin+i*gain-25)

text_variant_exceptions_list = tk.Text(root, width=10, height=1, font=('tahoma', 8), wrap='none')
text_variant_exceptions_list.place(x=1070, y=y_origin+i*gain)
label_variant_exceptions_list=tk.Label(root,text='variant_exceptions_list:', font=('tahoma', 7))
label_variant_exceptions_list.place(x=1070,y=y_origin+i*gain-25)

text_ada_score = tk.Text(root, width=12, height=1, font=('tahoma', 8), wrap='none')
text_ada_score.place(x=1190, y=y_origin+i*gain)
label_ada_score=tk.Label(root,text='ada_score:', font=('tahoma', 8))
label_ada_score.place(x=1190,y=y_origin+i*gain-25)

text_rf_score = tk.Text(root, width=7, height=1, font=('tahoma', 8), wrap='none')
text_rf_score.place(x=1300, y=y_origin+i*gain)
label_rf_score=tk.Label(root,text='rf_score:', font=('tahoma', 8))
label_rf_score.place(x=1300,y=y_origin+i*gain-25)

y_origin = 635
gain = 65
i = 0

text_rs_dbSNP141 = tk.Text(root, width=16, height=1, font=('tahoma', 8), wrap='none')
text_rs_dbSNP141.place(x=20, y=y_origin+i*gain)
label_rs_dbSNP141=tk.Label(root,text='rs_dbSNP141:', font=('tahoma', 8))
label_rs_dbSNP141.place(x=20,y=y_origin+i*gain-25)

text_Interpro_domain = tk.Text(root, width=70, height=2, font=('tahoma', 8))
text_Interpro_domain.place(x=150, y=y_origin+i*gain)
label_Interpro_domain=tk.Label(root,text='Interpro_domain:', font=('tahoma', 8))
label_Interpro_domain.place(x=150,y=y_origin+i*gain-25)

text_SIFT_pred = tk.Text(root, width=13, height=2, font=('tahoma', 8))
text_SIFT_pred.place(x=600, y=y_origin+i*gain)
label_SIFT_pred=tk.Label(root,text='SIFT_pred:', font=('tahoma', 8))
label_SIFT_pred.place(x=600,y=y_origin+i*gain-25)

text_Polyphen2_HDIV_pred = tk.Text(root, width=15, height=2, font=('tahoma', 8))
text_Polyphen2_HDIV_pred.place(x=700, y=y_origin+i*gain)
label_Polyphen2_HDIV_pred=tk.Label(root,text='Polyphen2_HDIV_pred:', font=('tahoma', 7))
label_Polyphen2_HDIV_pred.place(x=700,y=y_origin+i*gain-25)

text_Polyphen2_HVAR_pred = tk.Text(root, width=15, height=2, font=('tahoma', 8))
text_Polyphen2_HVAR_pred.place(x=820, y=y_origin+i*gain)
label_Polyphen2_HVAR_pre=tk.Label(root,text='Polyphen2_HVAR_pre:', font=('tahoma', 7))
label_Polyphen2_HVAR_pre.place(x=820,y=y_origin+i*gain-25)

text_LRT_pred = tk.Text(root, width=8, height=2, font=('tahoma', 8), wrap='none')
text_LRT_pred.place(x=940, y=y_origin+i*gain)
label_LRT_pred=tk.Label(root,text='LRT_pred:', font=('tahoma', 7))
label_LRT_pred.place(x=940,y=y_origin+i*gain-25)

text_MutationTaster_pred = tk.Text(root, width=8, height=2, font=('tahoma', 8), wrap='none')
text_MutationTaster_pred.place(x=1010, y=y_origin+i*gain)
label_MutationTaster_pred=tk.Label(root,text='MutationTaster_pred:', font=('tahoma', 7))
label_MutationTaster_pred.place(x=1010,y=y_origin+i*gain-25)

text_MutationAssessor_pred = tk.Text(root, width=8, height=2, font=('tahoma', 8), wrap='none')
text_MutationAssessor_pred.place(x=1080, y=y_origin+i*gain)
label_MutationAssessor_pred=tk.Label(root,text='MutationAssessor_pred:', font=('tahoma', 7))
label_MutationAssessor_pred.place(x=1080,y=y_origin+i*gain-25)

text_FATHMM_pred = tk.Text(root, width=8, height=2, font=('tahoma', 8))
text_FATHMM_pred.place(x=1150, y=y_origin+i*gain)
label_FATHMM_pred=tk.Label(root,text='FATHMM_pred:', font=('tahoma', 7))
label_FATHMM_pred.place(x=1150,y=y_origin+i*gain-25)

text_MetaSVM_pred = tk.Text(root, width=8, height=2, font=('tahoma', 8), wrap='none')
text_MetaSVM_pred.place(x=1220, y=y_origin+i*gain)
label_MetaSVM_pred=tk.Label(root,text='MetaSVM_pred:', font=('tahoma', 7))
label_MetaSVM_pred.place(x=1220,y=y_origin+i*gain-25)

text_MetaLR_pred = tk.Text(root, width=8, height=2, font=('tahoma', 8), wrap='none')
text_MetaLR_pred.place(x=1290, y=y_origin+i*gain)
label_MetaLR_pred=tk.Label(root,text='MetaLR_pred:', font=('tahoma', 7))
label_MetaLR_pred.place(x=1290,y=y_origin+i*gain-25)

i += 1
text_VEST3_rankscore = tk.Text(root, width=15, height=1, font=('tahoma', 8), wrap='none')
text_VEST3_rankscore.place(x=20, y=y_origin+i*gain)
label_VEST3_rankscore=tk.Label(root,text='VEST3_rankscore:', font=('tahoma', 8))
label_VEST3_rankscore.place(x=20,y=y_origin+i*gain-25)

text_PROVEAN_pred = tk.Text(root, width=20, height=2, font=('tahoma', 8))
text_PROVEAN_pred.place(x=140, y=y_origin+i*gain)
label_PROVEAN_pred=tk.Label(root,text='PROVEAN_pred:', font=('tahoma', 8))
label_PROVEAN_pred.place(x=140,y=y_origin+i*gain-25)

text_CADD_raw_rankscore = tk.Text(root, width=15, height=1, font=('tahoma', 8))
text_CADD_raw_rankscore.place(x=300, y=y_origin+i*gain)
label_CADD_raw_rankscore=tk.Label(root,text='CADD_raw_rankscore:', font=('tahoma', 7))
label_CADD_raw_rankscore.place(x=300,y=y_origin+i*gain-25)

text_GERP_RS_rankscore = tk.Text(root, width=15, height=1, font=('tahoma', 8), wrap='none')
text_GERP_RS_rankscore.place(x=420, y=y_origin+i*gain)
label_GERP_RS_rankscore=tk.Label(root,text='GERP_RS_rankscore:', font=('tahoma', 7))
label_GERP_RS_rankscore.place(x=420,y=y_origin+i*gain-25)

text_phyloP100way_vertebrate_rankscore = tk.Text(root, width=15, height=1, font=('tahoma', 8), wrap='none')
text_phyloP100way_vertebrate_rankscore.place(x=540, y=y_origin+i*gain)
label_phyloP100way_vertebrate_rankscore=tk.Label(root,text='phyloP100way_vertebrate_rankscore:', font=('tahoma', 7))
label_phyloP100way_vertebrate_rankscore.place(x=540,y=y_origin+i*gain-25)

text_phastCons100way_vertebrate_rankscore = tk.Text(root, width=15, height=1, font=('tahoma', 8), wrap='none')
text_phastCons100way_vertebrate_rankscore.place(x=710, y=y_origin+i*gain)
label_phastCons100way_vertebrate_rankscore=tk.Label(root,text='phastCons100way_vertebrate_rankscore:', font=('tahoma', 7))
label_phastCons100way_vertebrate_rankscore.place(x=710,y=y_origin+i*gain-25)

text_SiPhy_29way_logOdds_rankscore = tk.Text(root, width=15, height=1, font=('tahoma', 8), wrap='none')
text_SiPhy_29way_logOdds_rankscore.place(x=880, y=y_origin+i*gain)
label_SiPhy_29way_logOdds_rankscore=tk.Label(root,text='SiPhy_29way_logOdds_rankscore:', font=('tahoma', 7))
label_SiPhy_29way_logOdds_rankscore.place(x=880,y=y_origin+i*gain-25)

text_clinvar_clnsig = tk.Text(root, width=20, height=1, font=('tahoma', 8), wrap='none')
text_clinvar_clnsig.place(x=1060, y=y_origin+i*gain)
label_clinvar_clnsig=tk.Label(root,text='Clinvar_Clnsig:', font=('tahoma', 8))
label_clinvar_clnsig.place(x=1060,y=y_origin+i*gain-25)

text_clinvar_trait = tk.Text(root, width=20, height=2, font=('tahoma', 8), wrap='none')
text_clinvar_trait.place(x=1220, y=y_origin+i*gain)
label_clinvar_trait=tk.Label(root,text='Clinvar_Trait:', font=('tahoma', 8))
label_clinvar_trait.place(x=1220,y=y_origin+i*gain-25)

#//////////////////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////////////////
button_y = 315
button_show=ttk.Button(root, text='Show', width=15, command=show)
button_show.place(x=140, y=button_y)

button_delete_gene=ttk.Button(root, text='Delete Gene', width=18, command=delete_gene)
button_delete_gene.place(x=285, y=button_y)

button_delete_case=ttk.Button(root, text='Delete Case', width=18, command=delete_case)
button_delete_case.place(x=450, y=button_y)

button_load=ttk.Button(root, text='Load...', width=15, command=load)
button_load.place(x=640, y=button_y)

button_refreshDB=ttk.Button(root, text='Refresh DB', width=15, command=refreshDB)
button_refreshDB.place(x=800, y=button_y)

button_clear=ttk.Button(root, text='Clear', width=15, command=clear)
button_clear.place(x=950, y=button_y)

button_browse=ttk.Button(root, text='Browse', width=15, command=browse)
button_browse.place(x=1120, y=button_y)

button_cheat_sheet=ttk.Button(root, text='Cheat Sheet', width=20, command=cheat_sheet)
button_cheat_sheet.place(x=1120, y=580)

root.mainloop()

conn.close()