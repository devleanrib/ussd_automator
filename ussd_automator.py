import tkinter as tk
from tkinter import messagebox
import subprocess
import time

def enviar_ussd(codigo):
    try:
        
        print("Tentando enviar código:", codigo)

        
        process_text = subprocess.Popen(f"adb shell input text '{codigo}'", shell=True)
        process_text.wait()  

        print("Comando texto enviado:", codigo)

        
        time.sleep(1)

        
        process_enter = subprocess.Popen("adb shell input keyevent 66", shell=True)
        process_enter.wait() 

        print("Tecla Enter enviada")

        
        messagebox.showinfo("Sucesso", f"Código {codigo} enviado!")
    except Exception as e:
        
        print("Erro ao enviar código:", e)
        messagebox.showerror("Erro", f"Falha ao enviar código USSD: {str(e)}")

def exibir_imei():
    enviar_ussd("*#06#")


janela = tk.Tk()
janela.title("Automação USSD Samsung")


botao_imei = tk.Button(janela, text="Exibir IMEI", command=exibir_imei)
botao_imei.pack(pady=10)


botao_codigo = tk.Button(janela, text="Enviar *#1234#", command=lambda: enviar_ussd("*#1234#"))
botao_codigo.pack(pady=10)


janela.mainloop()
