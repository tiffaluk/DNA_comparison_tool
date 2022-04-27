#%%
import Sequence

seq_txt = "atgctcccaaacgatgaatggctccgtgataaccagccgtaaacttctctggaagcttca \
cattggagattggcaatcacggtctcattatttctctcacatgcgaaagttcatgtctac \
taacagttcttctaactcaagacaaacgatgtattacagactgacaggaggatgagctac \
agcttgactcgaaaatagctagccacccaccgacatatctgatacgccgcgtatcaaacg \
tctcgtgaggcggcacgcactgaatgtattgggtggagttattacatctagtatggggtg \
ggcctagtccttaagcactacatcagttaggcggctttacgggggaaccccgatcctccc \
ttgtaggaactcagcatctcggcgcagggtggtcaggtatcttcctgtacgggcaggact \
ttgtattcgtaccaacgaccgtttgtattactgtctattggcctgagggcccgcactcgc \
ctcttgctgcgttgggggatgcaacggtggccggccgactataatcagccgcggaatccg \
attcgagagagataaaatggtggcgcttaccgcttccttaggccctgttggcgatggagg \
gacagtacaagatgtaccggataattggccatgtactacacggcaacgtatatatgtaaa \
gccagtgggatagcacgcccgtcctattcaactaccgaaattaaaatagatgctcgtcct \
aaaaatgggaatgacacggggaatgccgaacatcattgcgtccaggtcgcggcgtcgcaa \
ccgagactctgctgtttgaaacgagtaagcgcgctattatacgtgccaattttcgctttt \
ggtatccgcttttgaggcccgcctggatacgctaacctggcctggaggtagggtataaac \
tccggagaatgtgggtgtcgatcattaggaatctccaatcttgtaacaatgaccccccag \
acgtcgatatactttgacagcgcttcgagtattagtaacc"

seq_txt = seq_txt.replace(" ", "")
seq = Sequence.Sequence(seq_txt, 1)

seq.get_gc_content()
print(seq.gc_content)
# %%