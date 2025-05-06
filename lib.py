import qrcode
import time
import os
import pyfiglet
import json
import ai
from tabulate import tabulate

data = {
    "Books": [
        {"id": 1, "Name": "To Kill a Mockingbird", "Author": "Harper Lee", "Price": 899, "Available": True},
        {"id": 2, "Name": "1984", "Author": "George Orwell", "Price": 750, "Available": True},
        {"id": 3, "Name": "The Great Gatsby", "Author": "F. Scott Fitzgerald", "Price": 650, "Available": True},
        {"id": 4, "Name": "Pride and Prejudice", "Author": "Jane Austen", "Price": 500, "Available": True},
        {"id": 5, "Name": "The Catcher in the Rye", "Author": "J.D. Salinger", "Price": 799, "Available": True},
        {"id": 6, "Name": "The Hobbit", "Author": "J.R.R. Tolkien", "Price": 950, "Available": True},
        {"id": 7, "Name": "Fahrenheit 451", "Author": "Ray Bradbury", "Price": 600, "Available": True},
        {"id": 8, "Name": "Moby-Dick", "Author": "Herman Melville", "Price": 850, "Available": True},
        {"id": 9, "Name": "The Lord of the Rings", "Author": "J.R.R. Tolkien", "Price": 1200, "Available": True},
        {"id": 10, "Name": "War and Peace", "Author": "Leo Tolstoy", "Price": 1100, "Available": True},
        {"id": 11, "Name": "Crime and Punishment", "Author": "Fyodor Dostoevsky", "Price": 900, "Available": True},
        {"id": 12, "Name": "Brave New World", "Author": "Aldous Huxley", "Price": 780, "Available": True},
        {"id": 13, "Name": "The Alchemist", "Author": "Paulo Coelho", "Price": 700, "Available": True},
        {"id": 14, "Name": "The Catch-22", "Author": "Joseph Heller", "Price": 890, "Available": True},
        {"id": 15, "Name": "One Hundred Years of Solitude", "Author": "Gabriel García Márquez", "Price": 980, "Available": True},
    ]
}



def tabData():
    dt = data["Books"]
    print(tabulate(dt, headers="keys", tablefmt = "psql"))

def AvailableBooks():

    dt = []
    for i in range(len(data["Books"])):
        if data["Books"][i]["Available"] == True:
            dt.append(data["Books"][i])

    return dt



def InvertAvailableBook(id):

    found = True
    for item in data["Books"]:
        if item["id"] == id:
            item["Available"] = not item["Available"]

            found = False
            break


def menu():
        print(pyfiglet.figlet_format("-- Library --"))
        print("1) View Available Books")
        print("2) Buy")
        print("3) Return Book")
        print("4) View Book summery")
        print("5) View Book summery by QR code")
        print("6) Clear Screen")
        print("7) Exit")


def main():

    first = False

    while True:
        if first == True:
            os.system('clear')
        else:
            first = False
        menu()
        choice = int(input("Enter choice : "))

        if choice == 1:
            print()
            print("---------------------------------")
            tabData()
            print("---------------------------------")

            sh = input("Tap enter to contiue...")
            if sh == '':
                continue


        elif choice == 2:
            Buyid = int(input("Book Id : "))

            for i in range(len(data["Books"])):
                if (Buyid == data["Books"][i]["id"]) and (data["Books"][i]["Available"] == True ):
        
                    confirm = input("Confirm (y/n) : ")

                    if confirm == "y":
                            
                        print("Please wait....")
                        # time.sleep(3)

                        InvertAvailableBook(Buyid)

                        os.system("clear")
                        print("---------------------------------")
                        print(f"You just borrowed a book")
                        print("---------------------------------")
                        break
                    else:
                        print("invalid input..")
                        break
            else:
                print("---------------------------------")
                print("Book is not available.")
                print("---------------------------------")

        elif choice == 3:
            
            Buyid = int(input("Book Id : "))

            for i in range(len(data["Books"])):
                if (Buyid == data["Books"][i]["id"]) and (data["Books"][i]["Available"] == False ):
        
                    confirm = input("Confirm (y/n) : ")

                    if confirm == "y":
                            
                        print("Please wait....")
                        # time.sleep(3)

                        InvertAvailableBook(Buyid)

                        os.system("clear")
                        print("---------------------------------")
                            
                        print(f"You just returned a book")
                        break
                    else:
                        print("invalid input..")
                        break
            else:
                print("---------------------------------")
                print("Book is already present.")
                print("---------------------------------")
                
        
        elif choice == 4:

            Bookid = int(input("Enter book id : "))
            
            for book in data["Books"]:
                if Bookid == book["id"]:
                    bookName = book["Name"]
                    resp = ai.chatGemini(f"Summery of book {bookName} in 100 words.")
                    break
            print("------------------------------------------------------------------------")
            print(str(resp))
            print("------------------------------------------------------------------------")
            sh = input("Tap enter to contiue...")
            if sh == '':
                continue


        elif choice == 5:

            Bookid = int(input("Enter book id : "))
            
            for book in data["Books"]:
                if Bookid == book["id"]:
                    bookName = book["Name"]
                    resp = ai.chatGemini(f"Summery of book {bookName} in 100 words.")
                    resp = str(resp)
                    qr = qrcode.make(resp)
                    qr.show()
                    break
        elif choice == 6:
            os.system("clear")

        else:
            os.system("clear")
            break


main()
