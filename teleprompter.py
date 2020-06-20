# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 06:46:13 2020

@author: asgun
"""
import tkinter as tk
import time


counter = 0

text = """ A mentalidade do caranguejo
Coloque um monte de caranguejos num balde. Eles vão tentar escapar, escalando as paredes. Nisso, um caranguejo se engancha no outro, puxando para baixo o que está acima. No final, ninguém consegue sair do balde.
Daí deriva o termo “mentalidade de caranguejo” para descrever comportamento similar: fofocas e puxadas de tapete para derrubar aquele que se destaca, em especial nas corporações. “Se eu não posso, você também não pode”.
Outra história sobre caranguejo. A segunda missão de Hércules era derrotar a Hidra de Lerna, o terrível monstro de muitas cabeças. Ao cortar uma cabeça, surgiam duas no lugar.
Para ajudar a Hidra, Hera enviou um caranguejo. Este ficou atazanando Hércules na já difícil batalha contra a Hidra. 
Hércules deu um pisão no caranguejo, que se despedaçou todo.
Hera, em homenagem ao caranguejo, criou a constelação de Câncer.
Moral da história: Não seja um caranguejo. Quando aparecer algum, dê um chega-pra-lá nele."""

splitText = text.split("\n")

root = tk.Tk() 
root.title("Teleprompter") 


# Fixing the window size. 
root.minsize(width=2000, height=800) 

label0 = tk.Label(root, text="", fg="black", font="Verdana 40",wraplength=900) 
label0.grid(column=1, row = 1)

start = tk.Button(root, text='Start', width=15, command=lambda:StartCount(label0,splitText, 5000)) 
start.grid(column = 0, row = 0)


def StartCount(label,texto,intervalo): 
    def count(): 
        global counter 
  

        label['text']= splitText[counter] # Or label.config(text=display) 
        counter += 1
        
        # Delays by 1000ms=1 seconds and call count again. 
        
        label.after(intervalo, count)
        
    count()
            
            

root.mainloop() 


for i in range(0,len(splitText)):
    label0['text'] = splitText[i]
    print(i, splitText[i])


