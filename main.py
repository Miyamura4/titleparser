from tkinter import *
from bs4 import BeautifulSoup
from urllib.request import urlopen
from tkinter import ttk
from colorama import init, Fore

file = open('pars.txt', 'a')


print(Fore.WHITE,'Welcome to the gulag parser! ')
print(Fore.BLUE,'If you wanna pars any html ')
print(Fore.RED,'press the "start pars" button to start parsing.')

root = Tk()


def click_button():
    root.title('Type a url in console')
    download_label["text"] = "Parsed"
    url = [
        input("Type a url: ")

    ]
    for x in url:
        html_code = str(urlopen(x).read(), 'UTF-8')
        soup = BeautifulSoup(html_code, 'html.parser')

        s = soup.find('title').text
        file.write(s + '\n')
        p = soup.find_all('p')
        print(s)
        for i in p:
            print(i.text)
            file.write(i.text + '\n')
            file.close()
            break
        return root.title('Account parser'),


entry = ttk.Entry()
entry.pack(anchor=NE, padx=6, pady=6)
root.iconbitmap('D:\\Program Files\\Cyberpunk 2077.ico')
root.geometry('250x250')
root.title('Account parser')


bg = PhotoImage(file='D:\\Program Files\\bosinn.gif')
my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)


button = Button(root, text="start pars", font=50, command=click_button)
button.pack(fill=X, padx=1, pady=10)


download_label = Label(root, text="Status:\n-", font=50)
download_label.pack(pady=(50, 0))
download_label.pack(anchor=NW)


root.mainloop()