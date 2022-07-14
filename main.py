# working to translate Western piano notes to Uttar Hindustani Sargam notes
"""
Naming Sargam notes:
Swara: S r R g G M M# P d D n N (madhya saptak)
Saptak: ,S ,r ,R ,g etc (mandra saptak
         S' r' R' g' etc (taar saptak)
extras: ~ is for meend, - is for lamba swar (or idk the right word #fixthis),
        I start with biji (dusri) kali as sa - first of 2 black keys as sa
"""
"""
Naming Piano Wester notes:
Notes: C, c, D, d, E, F, f, G, g, A, a, B (Octave #2)
Octaves: Numbered 1, 2, 3. I will use - and + for Mandra = -C, Madhya = C, Taar = C+. 
        Unnumbered notes are octave2.
extras: black keys in lowecase (sharps). White keys are in uppercase (regular)
"""

# global list of notes and swara I will need (in order)
hindustani_notes = [,S ,r ,R ,g ,G ,M ,M# ,P ,d ,D ,n ,N S r R g G M M# P d D n N S' r' R' g' G' M' M'# P' d' D' n' N'] 
western_notes =    [-c -D -d -E -F -f -G -g -A -a -B -C  c D d E F f G g A a B C  c+ D+ d+ E+ F+ f+ G+ g+ A+ a+ B+ C+]

oct_saptak = {",":"-", "'":"+"}
notes_swara = {"c":"S", } #todo

