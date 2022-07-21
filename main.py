# working to translate Western piano notes to Uttar Hindustani Sargam notes
"""
Naming Sargam notes:
Swara: S r R g G M M# P d D n N (madhya saptak)
Saptak: ,S ,r ,R ,g etc (mandra saptak
         S' r' R' g' etc (taar saptak)
extras: ~ is for meend, - is for lamba swar (or idk the right word #fixthis),
        I start with biji (dusri) kali as sa - second of 3 black keys as sa
"""
"""
Naming Piano Wester notes:
Notes: g, A, a, B, C, c, D, d, E, F, f, G (Octave #2)
Octaves: Numbered 1, 2, 3. I will use - and + for Mandra = -C, Madhya = C, Taar = C+. 
        Unnumbered notes are octave2.
extras: black keys in lowecase (sharps). White keys are in uppercase (regular)
"""

# global list of notes and swara I will need (in order)
"""
hindustani_notes = [",S", ",r", ",R", ",g", ",G", ",M", ",M#", ",P", ",d", ",D", ",n", ",N", "S", "r", "R", "g", "G", "M","M#", "P", "d", "D", "n", "N", "S'", "r'", "R'", "g'", "G'", "M'", "M'#", "P'", "d'", "D'", "n'", "N'"] 
western_notes =    ["-c", "-D", "-d", "-E", "-F", "-f", "-G", "-g", "-A", "-a", "-B", "-C", "c", "D", "d", "E", "F", "f", "G", "g", "A", "a", "B", "C", "c+", "D+", "d+", "E+", "F+", "f+", "G+", "g+", "A+", "a+", "B+", "C+"]
"""
oct_saptak = {",":"-", "'":"+"}
notes_swara = {"g":"S", "A":"r", "a":"R", "B":"g", "C":"G", "c":"M", "D":"M#", "d":"P", "E":"d", "F":"D", "f":"n", "G":"N" } #todo

def music_translate(in_w):
    # in_w is a string of notes
    notes_list_w = in_w.split()
    notes_list_in=[]
    for note_w in notes_list_w:
        if len(note_w)==1:
            note_in = str(notes_swara[note_w])
            notes_list_in.append(note_in)
        else:
            if note_w[0]=="-":
                note_in=","
            else:
                note_in[0]="'"
            note_in+=str(notes_swara[(note_w[1])])
            notes_list_in.append(note_in)
    return notes_list_in
    
test="G B F D A"
print(music_translate(test))
