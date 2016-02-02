'''
This is the translate action of Codon and protein
'''
translation={'GCA': ['Alanine', 'Ala', 'A'], 
             'GCC': ['Alanine', 'Ala', 'A'],
             'GCG': ['Alanine', 'Ala', 'A'], 
             'GCT': ['Alanine', 'Ala', 'A'], 
             'AGA': ['Arginine', 'Arg', 'R'], 
             'AGG': ['Arginine', 'Arg', 'R'], 
             'CGA': ['Arginine', 'Arg', 'R'], 
             'CGC': ['Arginine', 'Arg', 'R'], 
             'CGG': ['Arginine', 'Arg', 'R'],
             'CGT': ['Arginine', 'Arg', 'R'], 
             'AAC': ['Asparagine', 'Asn', 'N'], 
             'AAT': ['Asparagine', 'Asn', 'N'], 
             'GAC': ['Aspartic Acid', 'Asp', 'D'], 
             'GAT': ['Aspartic Acid', 'Asp', 'D'], 
             'TGC': ['Cysteine', 'Cys', 'C'], 
             'TGT': ['Cysteine', 'Cys', 'C'], 
             'GAA': ['Glutamic Acid', 'Glu', 'E'], 
             'GAG': ['Glutamic Acid', 'Glu', 'E'], 
             'CAA': ['Glutamine', 'Gln', 'Q'], 
             'CAG': ['Glutamine', 'Gln', 'Q'], 
             'GGA': ['Glycine', 'Gly', 'G'], 
             'GGC': ['Glycine', 'Gly', 'G'], 
             'GGG': ['Glycine', 'Gly', 'G'], 
             'GGT': ['Glycine', 'Gly', 'G'], 
             'CAC': ['Histidine', 'His', 'H'], 
             'CAT': ['Histidine', 'His', 'H'], 
             'ATA': ['Isoleucine', 'Ile', 'I'], 
             'ATC': ['Isoleucine', 'Ile', 'I'], 
             'ATT': ['Isoleucine', 'Ile', 'I'], 
             'CTA': ['Leucine', 'Leu', 'L'], 
             'CTC': ['Leucine', 'Leu', 'L'], 
             'CTG': ['Leucine', 'Leu', 'L'], 
             'CTT': ['Leucine', 'Leu', 'L'], 
             'TTA': ['Leucine', 'Leu', 'L'], 
             'TTG': ['Leucine', 'Leu', 'L'], 
             'AAA': ['Lysine', 'Lys', 'K'], 
             'AAG': ['Lysine', 'Lys', 'K'], 
             'ATG': ['Methionine', 'Met', 'M'], 
             'TTC': ['Phenylalanine', 'Phe', 'F'], 
             'TTT': ['Phenylalanine', 'Phe', 'F'], 
             'CCA': ['Proline', 'Pro', 'P'], 
             'CCC': ['Proline', 'Pro', 'P'], 
             'CCG': ['Proline', 'Pro', 'P'], 
             'CCT': ['Proline', 'Pro', 'P'], 
             'AGC': ['Serine', 'Ser', 'S'], 
             'AGT': ['Serine', 'Ser', 'S'], 
             'TCA': ['Serine', 'Ser', 'S'], 
             'TCC': ['Serine', 'Ser', 'S'], 
             'TCG': ['Serine', 'Ser', 'S'], 
             'TCT': ['Serine', 'Ser', 'S'], 
             'TAA': ['-Stop', '-Stop', '-Stop'], 
             'TAG': ['-Stop', '-Stop', '-Stop'], 
             'TGA': ['-Stop', '-Stop', '-Stop'], 
             'ACA': ['Threonine', 'Thr', 'T'], 
             'ACC': ['Threonine', 'Thr', 'T'], 
             'ACG': ['Threonine', 'Thr', 'T'], 
             'ACT': ['Threonine', 'Thr', 'T'], 
             'TGG': ['Tryptophan', 'Trp', 'W'], 
             'TAC': ['tyrosine', 'Tyr', 'Y'], 
             'TAT': ['Tyrosine', 'Tyr', 'Y'], 
             'GTA': ['Valine', 'Val', 'V'], 
             'GTC': ['Valine', 'Val', 'V'], 
             'GTG': ['Valine', 'Val', 'V'], 
             'GTT': ['Valine', 'Val', 'V']
            }  

def translate(dna_sequence):
    dna_sequence=dna_sequence.upper()    
    protein_abb=''
    for i in range(0, len(dna_sequence)-3, 3):        
        protein_abb+=(translation[dna_sequence[i:i+3]][2])
    return protein_abb

def translate3(dna_sequence):
    dna_sequence=dna_sequence.upper()
    protein=''
    for i in range(0, len(dna_sequence)-3, 3):
        protein+=(translation[dna_sequence[i:i+3]][1]+'-')
    return protein
