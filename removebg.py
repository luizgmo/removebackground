import os
import tkinter as tk
from tkinter import filedialog
from rembg import remove
from PIL import Image
import io

def remove_background(input_path, output_path):
    with open(input_path, 'rb') as input_file:
        input_data = input_file.read()
    
    output_data = remove(input_data)
    
    with open(output_path, 'wb') as output_file:
        output_file.write(output_data)
    
    img = Image.open(io.BytesIO(output_data))
    img.show()

def choose_input_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    entry_input_image.delete(0, tk.END)
    entry_input_image.insert(0, file_path)

def choose_output_path():
    folder_path = filedialog.askdirectory()  
    if folder_path:
        input_file_path = entry_input_image.get()
        if input_file_path:
            input_filename = os.path.basename(input_file_path)
            output_filename = os.path.splitext(input_filename)[0] + "_removebg.png"
            file_path = os.path.join(folder_path, output_filename)
            
            entry_output_path.delete(0, tk.END)
            entry_output_path.insert(0, file_path)

def process_image():
    input_path = entry_input_image.get()
    output_path = entry_output_path.get()
    
    if input_path and output_path:
        remove_background(input_path, output_path)
        label_status.config(text="Processamento concluído!", fg="green")
    else:
        label_status.config(text="Por favor, selecione os caminhos da imagem.", fg="red")

root = tk.Tk()
root.title("Remover Fundo de Imagem")
root.geometry("500x400")
root.config(bg="#f0f0f0")

label_input_image = tk.Label(root, text="Escolha a Imagem:", font=("Arial", 12), bg="#f0f0f0")
label_input_image.pack(pady=5)

entry_input_image = tk.Entry(root, width=40, font=("Arial", 12))
entry_input_image.pack(pady=5)

button_choose_input = tk.Button(root, text="Escolher Imagem", font=("Arial", 12), bg="#4CAF50", fg="white", relief="raised", command=choose_input_image)
button_choose_input.pack(pady=5)

label_output_path = tk.Label(root, text="Escolha o local para salvar a imagem:", font=("Arial", 12), bg="#f0f0f0")
label_output_path.pack(pady=5)

entry_output_path = tk.Entry(root, width=40, font=("Arial", 12))
entry_output_path.pack(pady=5)

button_choose_output = tk.Button(root, text="Escolher Pasta", font=("Arial", 12), bg="#4CAF50", fg="white", relief="raised", command=choose_output_path)
button_choose_output.pack(pady=5)

button_process = tk.Button(root, text="Remover Fundo", font=("Arial", 12), bg="#FF9800", fg="white", relief="raised", command=process_image)
button_process.pack(pady=20)

label_status = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
label_status.pack(pady=5)

root.mainloop()
