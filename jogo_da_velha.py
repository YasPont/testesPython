import tkinter as tk 
from tkinter import messagebox 

class JogoDaVelha:
    def __init__(self):
        self.janela = tk.Tk() 
        self.janela.title("Jogo da Velha") 
        self.turno = "X" 
        self.tabuleiro = [""] * 9 
        self.botoes = [] 
        self.criar_interface()
        
    def criar_interface(self):
        for i in range(9): 
            btn = tk.Button(self.janela, text="", font=("Arial", 20, "bold"), 
                            width=5, height=2,
                            command=lambda i=i: self.clique(i))
            btn.grid(row=i//3, column=i%3, sticky="nsew") 
            self.botoes.append(btn)
            
    def clique(self, indice):
        
        if self.tabuleiro[indice] == "" and self.turno: 
            self.tabuleiro[indice] = self.turno
            self.botoes[indice].config(text=self.turno) 
            
            if self.verificar_vitoria():
                messagebox.showinfo("Fim de Jogo", f"O jogador {self.turno} venceu!")
                self.reiniciar()
            elif "" not in self.tabuleiro:
                messagebox.showinfo("Fim de Jogo", "Empate!")
                self.reiniciar()
            else:
               
                self.turno = "O" if self.turno == "X" else "X"

    def verificar_vitoria(self):
        vitorias = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), # Horizontais
            (0, 3, 6), (1, 4, 7), (2, 5, 8), # Verticais
            (0, 4, 8), (2, 4, 6)             # Diagonais
        ]
        for a, b, c in vitorias:      
            if self.tabuleiro[a] == self.tabuleiro[b] == self.tabuleiro[c] != "":
                return True
        return False

    def reiniciar(self): 
        self.turno = "X"
        self.tabuleiro = [""] * 9
        for btn in self.botoes:
            btn.config(text="")

    def rodar(self):
        self.janela.mainloop() 

if __name__ == "__main__":
    jogo = JogoDaVelha()
    jogo.rodar()