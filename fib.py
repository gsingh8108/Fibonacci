from tkinter import *
root = Tk()

root.title('Fibonacci')
root.geometry('600x400')


entry_no = Entry(root)
label_series = Label(root, text="Fibonacci Series")
label_sum = Label(root, text="Fibonacci Sum")

def Fibonacci():
   
    input_no =  int(entry_no.get())
    first_no = 0
    second_no = 1
    sum=0
    sum2 = 0
    counter = 1
    
    while(counter <= input_no):
        
        label_series["text"] += str(sum) + " "
        label_sum["text"] = "Fibonacci Sum = " + str(sum2)
        counter = counter + 1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
        sum2 = sum2 + sum
    

entry_no.pack()
button = Button(root, text="Start Series", command=Fibonacci, fg="black", bg="red")
label_series.pack()
button.pack()
label_sum.pack()

root.mainloop()