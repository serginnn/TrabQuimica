from molmass import Formula
import tkinter as tk
from tkinter import messagebox

def descobrir_massa_molar(entrada_massa_molar):
    try:
        elemento = entrada_massa_molar.get()
        result = Formula(elemento)  
        massa_molar = result.mass
        messagebox.showinfo("Massa Molar", f"{massa_molar:.2f} g/mol")
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível calcular a massa molar: {e}")

def quantidade_de_atomos(entrada_quantidade_elemento,entrada_quantidade_massa):
    try:
        elemento = entrada_quantidade_elemento.get()
        massa = float(entrada_quantidade_massa.get())
        result = Formula(elemento)
        massa_molar = result.mass
        x = massa / massa_molar
        atomos = x * 6.022e23  # Constante de Avogadro
        messagebox.showinfo("Quantidade de Átomos", f"Foram utilizados aproximadamente {atomos:.2e} átomos de {elemento}")
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido")
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível calcular a quantidade de átomos: {e}")

def numero_de_mols(entrada_numero_elemento, entrada_numero_massa):
    try:
        elemento = entrada_numero_elemento.get()
        massa = float(entrada_numero_massa.get())
        result = Formula(elemento)
        massa_molar = result.mass
        mols = massa / massa_molar
        messagebox.showinfo("Número de Mols", f"O número de mols é {mols:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido")
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível calcular o número de mols: {e}")

def molaridade(entrada_elemento,entrada_volume,entrada_quantidade):
    try:
        elemento = entrada_elemento.get()
        volume = float(entrada_volume.get())
        quantidade = float(entrada_quantidade.get())
        result = Formula(elemento)
        massa_molar = result.mass
        x = quantidade/massa_molar
        final =  x/volume
        messagebox.showinfo("Molaridade", f"{final:.2f} mol/L")
    except ValueError:
        messagebox.showerror("Erro, Digite um avlor válido")
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possivel calcular a molaridade: {e}")

def concentracao_comum(entrada_volume, entrada_massa):
    try:
        volume=float(entrada_volume.get())
        massa=float(entrada_massa.get())
        concentracao= massa/volume
        messagebox.showinfo("Concentração", f"{concentracao:.2f} g/L")
    except ValueError:
        messagebox.showerror("Erro, Digite um valor válido")
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possivel calcular a concentração: {e}")

def trasformar(entrada_trasformada):
    try:      
        entrada = float(entrada_trasformada.get())
        result = entrada/1000
        messagebox.showinfo("Em Litros: ", f"{result:.2f} L")
        
    except ValueError:
        messagebox.showerror("Erro, Digite um valor válido")
    except Exception:
        messagebox.showerror("Erro, não foi possivel trasformar para litros")


# Conteúdo da Aba 1
def opcao_1():
    janela2=tk.Toplevel(janela)
    janela2.title("Descobrir Massa Molar")
    janela2.geometry("640x480")
    frame = tk.Frame(janela, bg='blue')
    frame.pack(expand=True, fill='both')

    label_entrada_massa_molar = tk.Label(janela2, text="Digite a fórmula molecular:")
    label_entrada_massa_molar.pack(padx=10, pady=5)
    entrada_massa_molar = tk.Entry(janela2)
    entrada_massa_molar.pack(padx=10, pady=5)
    botao_massa_molar_aba1 = tk.Button(janela2, text="Calcular Massa Molar", command=lambda: descobrir_massa_molar(entrada_massa_molar))
    botao_massa_molar_aba1.pack(padx=20, pady=5)

# Conteúdo da Aba 2
def opcao_2():
    janela2=tk.Toplevel(janela)
    janela2.title("Quantidade de Átomos")
    janela2.geometry("640x480")
    frame = tk.Frame(janela, bg='blue')
    frame.pack(expand=True, fill='both')

    label_entrada_quantidade_elemento = tk.Label(janela2, text="Elemento Químico:")
    label_entrada_quantidade_elemento.pack(padx=10, pady=5)
    entrada_quantidade_elemento = tk.Entry(janela2)
    entrada_quantidade_elemento.pack(padx=10, pady=5)
    label_entrada_quantidade_massa = tk.Label(janela2, text="Quantidade em gramas:")
    label_entrada_quantidade_massa.pack(padx=10, pady=5)
    entrada_quantidade_massa = tk.Entry(janela2)
    entrada_quantidade_massa.pack(padx=10, pady=5)
    botao_quantidade_atomos_aba2 = tk.Button(janela2, text="Calcular Quantidade de Átomos", command=lambda: quantidade_de_atomos(entrada_quantidade_elemento, entrada_quantidade_massa))
    botao_quantidade_atomos_aba2.pack(padx=10, pady=5)

# Conteúdo da Aba 3
def opcao_3():
    janela2=tk.Toplevel(janela)
    janela2.title("Numero de Mols")
    janela2.geometry("640x480")
    frame = tk.Frame(janela, bg='blue')
    frame.pack(expand=True, fill='both')

    label_entrada_numero_elemento = tk.Label(janela2, text="Elemento Químico:")
    label_entrada_numero_elemento.pack(padx=10, pady=5)
    entrada_numero_elemento = tk.Entry(janela2)
    entrada_numero_elemento.pack(padx=10, pady=5)
    label_entrada_numero_massa = tk.Label(janela2, text="Quantidade em gramas:")
    label_entrada_numero_massa.pack(padx=10, pady=5)
    entrada_numero_massa = tk.Entry(janela2)
    entrada_numero_massa.pack(padx=10, pady=5)
    botao_numero_mols_aba3 = tk.Button(janela2, text="Calcular Número de Mols", command=lambda: numero_de_mols(entrada_numero_elemento, entrada_numero_massa))
    botao_numero_mols_aba3.pack(padx=10, pady=5)

#conteudo aba 4
def opcao_4():
    janela2=tk.Toplevel(janela)
    janela2.title("Molaridade")
    janela2.geometry("640x480")
    frame = tk.Frame(janela, bg='blue')
    frame.pack(expand=True, fill='both')

    label_entrada_volume = tk.Label(janela2, text="Volume em L: " )
    label_entrada_volume.pack(padx=10, pady=5)
    entrada_volume= tk.Entry(janela2)
    entrada_volume.pack(padx=10, pady=5)
    label_entrada_elemento = tk.Label(janela2, text="Elemento Químico: ")
    label_entrada_elemento.pack(padx=10, pady=5)
    entrada_elemento = tk.Entry(janela2)
    entrada_elemento.pack(padx=10, pady=5)
    label_entrada_quantidade = tk.Label(janela2, text = "Quantidade em gramas: ")
    label_entrada_quantidade.pack(padx=10, pady=5)
    entrada_quantidade = tk.Entry(janela2)
    entrada_quantidade.pack(padx=10, pady=5)
    botao_molaridade_aba4 = tk.Button(janela2, text="Molaridade", command=lambda: molaridade(entrada_elemento, entrada_volume, entrada_quantidade))
    botao_molaridade_aba4.pack(padx=10, pady=5)

#conteudo aba 5
def opcao_5():
    janela2=tk.Toplevel(janela)
    janela2.title("Concentração")
    janela2.geometry("640x480")
    frame = tk.Frame(janela, bg='blue')
    frame.pack(expand=True, fill='both')

    label_entrada_volume= tk.Label(janela2, text="Volume em L: " )
    label_entrada_volume.pack(padx=10, pady=5)
    entrada_volume = tk.Entry(janela2)
    entrada_volume.pack(padx=10, pady=5)
    label_entrada_massa = tk.Label(janela2, text="Massa: ")
    label_entrada_massa.pack(padx=10, pady=5)
    entrada_massa = tk.Entry(janela2)
    entrada_massa.pack(padx=10, pady=5)
    botao_concentracao_aba5 = tk.Button(janela2, text="Concentração", command=lambda: concentracao_comum(entrada_volume,entrada_massa))
    botao_concentracao_aba5.pack(padx=10, pady=5)

#conteudo aba 6
def opcao_6():
    janela2=tk.Toplevel(janela)
    janela2.title("Transformar ml Para L")
    janela2.geometry("640x480")
    frame = tk.Frame(janela, bg='blue')
    frame.pack(expand=True, fill='both')

    label_entrada_trasformada = tk.Label(janela2, text="Trasformar para Litros: ")
    label_entrada_trasformada.pack(padx=10, pady=5)
    entrada_trasformada= tk.Entry(janela2)
    entrada_trasformada.pack(padx=10, pady=5)
    botao_trasformar_aba6 = tk.Button(janela2, text="Trasformar", command=lambda: trasformar(entrada_trasformada))
    botao_trasformar_aba6.pack(padx=10, pady=5)

def sair():
    janela.quit()


janela = tk.Tk()
janela.title("Menu Inicial")
janela.geometry("1280x720")

frame = tk.Frame(janela, bg='blue')
frame.pack(expand=True, fill='both')

#garantir expansao
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(2, weight=1)
frame.grid_rowconfigure(3, weight=1)
frame.grid_rowconfigure(4, weight=1)
frame.grid_rowconfigure(5, weight=1)
#garante todos na coluna 3, com expansão correta
frame.grid_columnconfigure(3, weight=1)  

btn_option1 = tk.Button(frame, text="Massa Molar", font=('Arial', 20), command=opcao_1, bg='purple')
btn_option1.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")

btn_option2 = tk.Button(frame, text="Quantidade de Átomos", font=('Arial', 20), command=opcao_2, bg='purple')
btn_option2.grid(row=1, column=3, padx=10, pady=10, sticky="nsew")

btn_option3 = tk.Button(frame, text="Número de mols", font=('Arial', 20), command=opcao_3, bg='purple')
btn_option3.grid(row=2, column=3, padx=10, pady=10, sticky="nsew")

btn_option4 = tk.Button(frame, text="Molaridade", font=('Arial', 20), command=opcao_4, bg='purple')
btn_option4.grid(row=3, column=3, padx=10, pady=10, sticky="nsew")

btn_option5 = tk.Button(frame, text="Concentração", font=('Arial', 20), command=opcao_5, bg='purple')
btn_option5.grid(row=4, column=3, padx=10, pady=10, sticky="nsew")

btn_option6 = tk.Button(frame, text="Trasformar Para Litros ", font=('Arial', 20), command=opcao_6, bg='purple')
btn_option6.grid(row=5, column=3, padx=10, pady=10, sticky="nsew")

botao_sair = tk.Button(janela, text="Sair", command=sair, bg='black', fg='white')
botao_sair.pack(padx=20, pady=20)

# Início do loop principal da interface gráfica
janela.mainloop()


