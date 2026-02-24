import os
import tkinter as tk
from tkinter import filedialog, messagebox


# Função para gerar um nome único
def gerar_nome_unico(pasta, nome_base, contador, extensao):
    while True:
        if extensao:
            novo_nome = f"{nome_base}_{contador}.{extensao}"
        else:
            novo_nome = f"{nome_base}_{contador}"

        caminho_novo = os.path.join(pasta, novo_nome)

        if not os.path.exists(caminho_novo):
            return caminho_novo, novo_nome

        contador += 1


# Função para renomear arquivos
def renomear_arquivos():
    pasta = entry_pasta.get().strip()
    nome_base = entry_nome.get().strip()

    if not os.path.exists(pasta):
        messagebox.showerror("Erro", "Pasta inválida.")
        return

    if not nome_base:
        messagebox.showerror("Erro", "Digite um nome base.")
        return

    contador = 1
    arquivos_renomeados = 0

    for arquivo in sorted(os.listdir(pasta)):
        caminho_antigo = os.path.join(pasta, arquivo)

        if os.path.isfile(caminho_antigo):
            nome, extensao = os.path.splitext(arquivo)
            extensao = extensao.lstrip(".")

            caminho_novo, novo_nome = gerar_nome_unico(
                pasta, nome_base, contador, extensao
            )

            os.rename(caminho_antigo, caminho_novo)

            contador += 1
            arquivos_renomeados += 1

    messagebox.showinfo(
        "Sucesso",
        f"{arquivos_renomeados} arquivos renomeados com sucesso!",
    )


# Função para selecionar pasta
def selecionar_pasta():
    pasta = filedialog.askdirectory()
    if pasta:
        entry_pasta.delete(0, tk.END)
        entry_pasta.insert(0, pasta)


# Configuração da interface gráfica
janela = tk.Tk()
janela.title("Renomeador de Arquivos")
janela.geometry("400x220")
janela.resizable(False, False)

# Elementos da interface

tk.Label(janela, text="Pasta:").pack(pady=(10, 0))

frame_pasta = tk.Frame(janela)
frame_pasta.pack()

entry_pasta = tk.Entry(frame_pasta, width=35)
entry_pasta.pack(side=tk.LEFT, padx=5)

btn_pasta = tk.Button(frame_pasta, text="Selecionar", command=selecionar_pasta)
btn_pasta.pack(side=tk.LEFT)

tk.Label(janela, text="Nome base:").pack(pady=(10, 0))

entry_nome = tk.Entry(janela, width=30)
entry_nome.pack()

tk.Button(
    janela,
    text="Renomear Arquivos",
    command=renomear_arquivos,
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=5,
).pack(pady=20)

janela.mainloop()