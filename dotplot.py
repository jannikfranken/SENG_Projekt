#Dotplot
from tkinter import *
from tkinter import messagebox
seq1 = ""
seq2 = ""

def enter_sequences():
    input = Tk()
    input.title("Enter sequences")

    def submit_sequences():
        global seq1
        global seq2
        seq1 = seq1_entry.get()
        seq2 = seq2_entry.get()
        input.destroy()


    seq1_label = Label(input, text = "Sequence 1 :", bg="#FFFFFF", fg="#53868b", font="none 12").grid(row=0, column=0, sticky=W)
    seq1_entry = Entry(input, width=20, bg="#53868b")
    seq1_entry.grid(row=0, column=1, sticky=W)
    seq2_label = Label(input, text = "Sequence 2 :", bg="#FFFFFF", fg="#53868b", font="none 12").grid(row=1, column=0, sticky=W)
    seq2_entry = Entry(input, width=20, bg="#53868b")
    seq2_entry.grid(row=1, column=1, sticky=W)
    submit_button = Button(text="SUBMIT", width=10, command=submit_sequences, bg="green").grid(row=3, column=1, sticky=W)

    input.mainloop()
    return [seq1, seq2]

#___________________main__________________
sequence_list = enter_sequences()
seq1 = sequence_list[0].upper()
seq2 = sequence_list[1].upper()

matrix = [["" for i in range(len(seq1))] for j in range(len(seq2))]      #initialize matrix filled with empty spaces
S = [seq1, seq2]
for i in range(0, len(S[0]), 1):
    for j in range(0, len(S[1]), 1):
        if(S[0][i] == S[1][j]):
            matrix[j][i] = "\\"
        else:
            matrix[j][i] = "."

print("DOTPLOT ALGORITHM")
print("SEQUENCE 1: ", seq1)
print("SEQUENCE 2: ", seq2)
print("")
#output matrix and sequenes above and left of it
print("  ", end="")
for i in seq1:
    print("%2s" % i, end="")
print("")
for i in range(len(matrix)):
    print("%2s" % seq2[i], end="")
    for j in range(len(matrix[i])):
        print("%2s" % matrix[i][j], end="")
    print("")


messagebox.showinfo(title="End", message="Success!")
