import tkinter as tk
import requests

def fetchDummy3():
    res = requests.get('localhost:5000/api/dummydata')
    if res.status_code == 200:
        data = res.json()


def fetchDummy2():
    try:
        res = requests.get('http://127.0.0.1:5000/api/dummydata2')
        if res.status_code == 200:
            data = res.json()  # Convert the JSON response to a Python list of dictionaries
            # Format the data into a single string with each item on a new line
            display_data = "\n".join([f"Title: {item['title']}, ID: {item['id']}, Link: {item['link']}" for item in data])
            # Update the label's text to display the formatted data
            label.config(text=display_data)
        else:
            label.config(text="Failed to fetch dataa")
    except requests.exceptions.RequestException as e:
        label.config(text=f"Error: {e}")

def fetch_data():
    response = requests.get('http://127.0.0.1:5000/api/scan')
    if response.status_code == 200:
        data = response.json()
        label.config(text=f"Message: {data['message']}, Value: {data['value']}")
    else:
        label.config(text="Failed to fetch data")


def fetch_homePage():
    responce = requests.get('localhost:5000/')
    if responce.status_code == 200:
        data = responce
        print(data)

    # Create the Tkinter application


root = tk.Tk()
root.title("Tkinter and Flask Communication")

# Create a label to display the data
label = tk.Label(root, text="Click the button to fetch data from Flask")
label.pack(pady=20)

# Create a button to fetch data
button = tk.Button(root, text="Fetch Data", command=fetchDummy2)
button.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()
