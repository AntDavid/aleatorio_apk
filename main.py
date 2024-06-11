
import tkinter as tk
import random



# Função para criar as duplas
def formar_duplas():
    nomes = entry.get().split(", ")  # Obtém os nomes inseridos e os separa por vírgula e espaço
    duplas_listbox.delete(0, tk.END)  # Limpa a lista de duplas

    # Embaralha a ordem dos nomes
    random.shuffle(nomes)

    # Garante que o número de nomes seja par para criar as duplas
    if len(nomes) % 2 != 0:
        nomes.append("solo")

    # Cria as duplas
    for i in range(0, len(nomes), 2):
        dupla = f"{nomes[i]} e {nomes[i + 1]}"
        duplas_listbox.insert(tk.END, dupla)

# Configurações da interface
root = tk.Tk()
root.title("Formar Duplas")

label = tk.Label(root, text="Digite os nomes separados por vírgula e espaço:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Formar Duplas", command=formar_duplas)
button.pack()

duplas_listbox = tk.Listbox(root)
duplas_listbox.pack()
label = tk.Label(root, text="©AD-Enterprise, 2023")
label.pack()

root.mainloop()
