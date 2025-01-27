text = "Yoooooooo\nThis is some text\nHave a good one!\n"

with open('test.txt','w') as file:
    file.write(text)
    
text1 = "Have a nice day! see ya " 
with open('test.txt','a') as file:
    file.write(text1)