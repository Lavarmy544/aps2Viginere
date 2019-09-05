from tkinter import *
from tkinter import scrolledtext
from random import randint

class Application:
    def __init__(self, master=None):
        texto = "#ff6200"
        fundo = "#0b212e"
        selecionado = "#ffffff"#"#11405c"
        fonte = ("Arial", "20", "bold")
        main = Frame(master)
        main["padx"] = 50
        main["pady"] = 10
        main["bg"] = fundo
        main.grid()

        label1 = Label(main, font = fonte, text = "Chave:",relief=FLAT,
                bg = fundo, fg = texto)
        label1.grid(row = 0, columnspan = 2)
        self.chave = Entry(main, font = fonte, width = 31, bg=fundo,
                insertbackground = texto,selectbackground = selecionado, borderwidth = 4, fg=texto)
        self.chave.focus_set()
        self.chave.grid(row = 1, columnspan = 2)

        label2 = Label(main, font = fonte, text = "Mensagem:",
                bg = fundo, fg = texto)
        label2.grid(row = 2, columnspan = 2)
        self.mensagem = scrolledtext.ScrolledText(main, font = fonte,
                insertbackground = texto, borderwidth = 4,width=30,
                height=5, bg=fundo, fg=texto)
        self.mensagem.grid(row = 3, columnspan = 2)

        button = Button(main, font = fonte, text = "Criptografar",
                width = 13, bg = fundo, bd = "3", fg = texto,command = self.criptografar
                ,borderwidth = 4,).grid(row = 4, column = 0, stick = W)

        button1 = Button(main, font = fonte, text = "Descriptografar",
                width = 13, bg = fundo, fg = texto, command = self.descriptografar
                ,borderwidth = 4,).grid(row = 4, column = 1, stick = E)

        copiar = Button(main, font = fonte, text = "Copiar",
                width = 13, bg = fundo, fg = texto, command = self.copiar
                ,borderwidth = 4,).grid(row = 5, column = 0, stick = W)

        button2 = Button(main, font = fonte, text = "Chave aleatória",
                width = 13, bg = fundo, fg = texto, command = self.random
                ,borderwidth = 4,).grid(row = 5, column = 1, stick = E)

        self.resultado = scrolledtext.ScrolledText(main, font = fonte,
                borderwidth = 4,width=30,height=5, bg=fundo, fg=texto)
        self.resultado.config(state=DISABLED)
        self.resultado.grid(row = 6, columnspan = 2)


    def random(self):
        self.variaveis()
        quantidade = randint(5,20)
        i = 0
        novo = ""
        while i < quantidade:
            novo += alfabeto[randint(0,25)]
            i+=1
        self.chave.delete(0, END)
        self.chave.insert(0, novo)

    def copiar(self):
        if self.resultado.get(1.0)!= "":
            self.variaveis()
            r = Tk()
            r.withdraw()
            r.clipboard_clear()
            r.clipboard_append(self.resultado.get(1.0, END)[0:sizeCodigo-1])
            r.update()

    def variaveis(self):
        global chave, mensagem, codigo, sizeCodigo, charChave, charCodigo, final, alfabeto, i, cifrado, sizeChave
        chave = str(self.chave.get())
        chave = chave.lower()
        mensagem = str(self.mensagem.get(1.0, END))
        mensagem = mensagem.lower()
        chave = chave.replace(" ", "")
        sizeCodigo = len(mensagem)
        alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                    "t", "u", "v", "w", "x", "y", "z"]
        charChave = []
        charCodigo = []
        final = []

    def inicio(self):
        self.variaveis()
        global sizeChave
        sizeChave = len(chave)
        i = 0
        q = 0
        if sizeChave != 0:
            tirar = 0
            while i < sizeChave:
                trava = True
                for l in alfabeto:
                    q += 1
                    if chave[i].isalpha():
                        if chave[i] == l:
                            charChave.append(q)
                            trava = False
                if trava:
                    tirar += 1
                i += 1
                q = 0
            i = 0
            sizeChave -= tirar
            while i != sizeCodigo:
                charCodigo.append(mensagem[i].lower())
                p = 1
                for l in alfabeto:
                    if charCodigo[i] == l:
                        if charCodigo[i] == " ":
                            charCodigo[i] = " "
                        else:
                            charCodigo[i] = p
                    p += 1
                i += 1
        else:
            self.resultado.config(state=NORMAL)
            self.resultado.delete(1.0, END)
            self.resultado.insert(INSERT, "Digite uma chave")
            self.resultado.config(state=DISABLED)

    def fim(self):
        cifrado = ""
        a = 0
        for l in final:
            cifrado += str(final[a])
            a += 1
        cifrado = cifrado[0:sizeCodigo-1]
        self.resultado.config(state=NORMAL)
        self.resultado.delete(1.0, END)
        self.resultado.insert(INSERT, cifrado)
        self.resultado.config(state=DISABLED)

    def criptografar(self):
        self.inicio()
        if sizeChave != 0:
            i = 0
            k = 0
            c = 0
            while sizeCodigo > i:
                if k > sizeChave - 1:
                    k = 0
                if charCodigo[c] != " ":
                    if type(charChave[k]) == int and type(charCodigo[c]) == int:
                        temp = int(charChave[k]) + int(charCodigo[c]) - 2
                        if temp >= 26:
                            temp -= 26
                        final.append(alfabeto[temp])
                        k += 1
                    else:
                        final.append(charCodigo[c])
                else:
                    final.append(" ")
                i += 1
                c += 1
            self.fim()

    def descriptografar(self):
        self.inicio()
        if sizeChave != 0:
            i = 0
            k = 0
            c = 0
            while i < sizeCodigo:
                if k > sizeChave - 1:
                    k = 0
                if charCodigo[c] != " ":
                    if type(charChave[k]) == int and type(charCodigo[c]) == int:
                        if charChave[k] >= charCodigo[c]:
                            charCodigo[c] += 26
                        temp = -charChave[k] + charCodigo[c]
                        if temp >= 26:
                            temp -= 26
                        final.append(alfabeto[temp])
                        k += 1
                    else:
                        final.append(charCodigo[c])
                else:
                    final.append(" ")
                i += 1
                c += 1
            self.fim()
root = Tk()
root.title("Viginere")
Application(root)
root.mainloop()