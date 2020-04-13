# -*- coding: cp1252 -*-
from create_game import *
from tkinter import *
#from thread import *

DELAY = 0.5

LINHA = 15
COLUNA = 25
BOMBAS = 50

STARTX = 20
STARTY = 20
ENDX = STARTX + 40*COLUNA
ENDY = STARTY + 40*LINHA
    
def interface(valor):
    global canvas, num_bombs
    if valor == 0:
        root = Tk()
        root.title('Mine-fucking-sweeper')
        root.resizable(FALSE,FALSE)
        frame = Frame(root)
        frame.grid(row =0 , column = 0)
        Label(frame, text = 'Bombas: ').grid(row = 0, column = 0)
        num_bombs = IntVar()
        Label(frame, textvariable = num_bombs).grid(row = 0, column = 1)
        num_bombs.set(BOMBAS)
        canvas = Canvas(root, width=40 + ENDX - STARTX, height=40 + ENDY - STARTY, bg='white')
        canvas.grid(row=1, column=0)
    for i in range(LINHA):
        for j in range(COLUNA):
            ret = canvas.create_rectangle(20 + 40*j, 20 + 40*i,20 + 40*j + 40, 20 + 40*i + 40, fill='grey', activefill='blue', tag=(i,j, situacoes[i][j], 'NO'))
            #canvas.tag_bind(ret,"<Enter>", mostra_vizinhos)
            #canvas.tag_bind(ret, "<Leave>", desmostra_vizinhos)
    canvas.bind("<Button 1>", click1)
    canvas.bind("<Button 2>", click3)
    canvas.bind("<Button 3>", click2)
    mainloop()
    
def click1(event):
    global jogadas
    item = canvas.find_overlapping(event.x,event.y,event.x,event.y)
    tag = canvas.gettags(item)
    coords = canvas.coords(item)

    if canvas.itemcget(item, 'fill') != 'red':
        try:                    
            if tag[0] == 'reiniciar':
                iniciar_jogo(1)
                    
            elif tag[2] == 'X':
                canvas.delete(ALL)
                canvas.create_text((40 + ENDX - STARTX)/2,(40 + ENDY - STARTY)/2, text='Você perdeu!hahaha otário!')
                canvas.create_rectangle((40 + ENDX - STARTX)/2 - 100, (40 + ENDY - STARTY)/2 + 50, (40 + ENDX - STARTX)/2 + 100, (40 + ENDY - STARTY)/2 + 100, fill='grey', tag = 'reiniciar')
                canvas.create_text((40 + ENDX - STARTX)/2, (40 + ENDY - STARTY)/2 + 75, text='Reiniciar', tag = 'reiniciar')             

            if jogadas == 0:
                canvas.delete(ALL)
                canvas.create_text(300,300, text='Parabéns, você ganhou!')
                canvas.create_rectangle(200, 350, 300, 400, fill='grey', tag = 'reiniciar')
                canvas.create_text(250, 375, text='Reiniciar')
        except:
            pass

        escreve_texto(item,coords,tag)
        
    
        
        
def click2(event):
    item = canvas.find_overlapping(event.x,event.y,event.x,event.y)
    tags = canvas.gettags(item)
    posx = tags[0]
    posy = tags[1]
    current_color = canvas.itemcget(item, 'fill')

    if current_color == 'grey':
        if num_bombs.get() != 0:
            canvas.itemconfig(item, fill='red')
            canvas.dtag(item, 'NO')
            canvas.dtag(item, 'current')
            canvas.addtag_withtag('YES', item)
            num_bombs.set(num_bombs.get() - 1)
    elif current_color == 'red':
        canvas.itemconfig(item, fill='grey')
        canvas.dtag(item, 'YES')
        canvas.dtag(item, 'current')
        canvas.addtag_withtag('NO', item)
        num_bombs.set(num_bombs.get() + 1)

def click3(event):
    a_deletar = []
    temp_list = []
    check_var = True
    content = canvas.find_overlapping(event.x,event.y,event.x,event.y)
    tags = canvas.gettags(content)

    if len(tags) != 0 and tags[2] == 'aberto':
        posx = int(tags[0])
        posy = int(tags[1])
        items = canvas.find_all()
        for item in items:
            try:
                tags = canvas.gettags(item)
                coords = canvas.coords(item)
                if tags[2] != 'aberto':
                    if int(tags[0]) == (posx-1) and int(tags[1]) == (posy-1):
                        if tags[2] != 'X':
                            temp_list.append(item)
                            temp_list.append(coords)
                            temp_list.append(tags)
                            a_deletar.append(temp_list)
                            temp_list = []
                        elif tags[3] == 'NO':
                            check_var = False
                    elif int(tags[0]) == (posx-1) and int(tags[1]) == posy:
                        if tags[2] != 'X':
                            temp_list.append(item)
                            temp_list.append(coords)
                            temp_list.append(tags)
                            a_deletar.append(temp_list)
                            temp_list = []
                        elif tags[3] == 'NO':
                            check_var = False
                    elif int(tags[0]) == (posx-1) and int(tags[1]) == (posy+1):
                        if tags[2] != 'X':
                            temp_list.append(item)
                            temp_list.append(coords)
                            temp_list.append(tags)
                            a_deletar.append(temp_list)
                            temp_list = []
                        elif tags[3] == 'NO':
                            check_var = False
                    elif int(tags[0]) == posx and int(tags[1]) == (posy-1):
                        if tags[2] != 'X':
                            temp_list.append(item)
                            temp_list.append(coords)
                            temp_list.append(tags)
                            a_deletar.append(temp_list)
                            temp_list = []
                        elif tags[3] == 'NO':
                            check_var = False
                    elif int(tags[0]) == posx and int(tags[1]) == (posy+1):
                        if tags[2] != 'X':
                            temp_list.append(item)
                            temp_list.append(coords)
                            temp_list.append(tags)
                            a_deletar.append(temp_list)
                            temp_list = []
                        elif tags[3] == 'NO':
                            check_var = False
                    elif int(tags[0]) == (posx+1) and int(tags[1]) == (posy-1):
                        if tags[2] != 'X':
                            temp_list.append(item)
                            temp_list.append(coords)
                            temp_list.append(tags)
                            a_deletar.append(temp_list)
                            temp_list = []
                        elif tags[3] == 'NO':
                            check_var = False
                    elif int(tags[0]) == (posx+1) and int(tags[1]) == posy:
                        if tags[2] != 'X':
                            temp_list.append(item)
                            temp_list.append(coords)
                            temp_list.append(tags)
                            a_deletar.append(temp_list)
                            temp_list = []
                        elif tags[3] == 'NO':
                            check_var = False
                    elif int(tags[0]) == (posx+1) and int(tags[1]) == (posy+1):
                        if tags[2] != 'X':
                            temp_list.append(item)
                            temp_list.append(coords)
                            temp_list.append(tags)
                            a_deletar.append(temp_list)
                            temp_list = []
                        elif tags[3] == 'NO':
                            check_var = False
            except:
                pass

    if check_var == True:
        for item in a_deletar:
            escreve_texto(item[0], item[1], item[2])

def apaga_vizinhos(i,j):
    i = int(i)
    j = int(j)
    items = canvas.find_all()

    for item in items:
        try:
            tags = canvas.gettags(item)
            coords = canvas.coords(item)
            if tags[2] != 'aberto':
                if int(tags[0]) == (i-1) and int(tags[1]) == (j-1):
                    escreve_texto(item, coords, tags)
                elif int(tags[0]) == (i-1) and int(tags[1]) == j:
                    escreve_texto(item, coords, tags)
                elif int(tags[0]) == (i-1) and int(tags[1]) == (j+1):
                    escreve_texto(item, coords, tags)
                elif int(tags[0]) == i and int(tags[1]) == (j-1):
                    escreve_texto(item, coords, tags)
                elif int(tags[0]) == i and int(tags[1]) == (j+1):
                    escreve_texto(item, coords, tags)
                elif int(tags[0]) == (i+1) and int(tags[1]) == (j-1):
                    escreve_texto(item, coords, tags)
                elif int(tags[0]) == (i+1) and int(tags[1]) == j:
                    escreve_texto(item, coords, tags)
                elif int(tags[0]) == (i+1) and int(tags[1]) == (j+1):
                    escreve_texto(item, coords, tags)
        except:
            pass

def mostra_vizinhos(event):
    global quadrado
    quadrado = canvas.find_overlapping(event.x,event.y,event.x,event.y)
    tag = canvas.gettags(quadrado)

    try:
        pisca_vizinhos(int(tag[0]) - 1, int(tag[1]) - 1)
    except: pass

    try:
        pisca_vizinhos(int(tag[0]) - 1, int(tag[1]))
    except: pass

    try:
        pisca_vizinhos(int(tag[0]) - 1, int(tag[1]) + 1)
    except: pass

    try:
        pisca_vizinhos(int(tag[0]), int(tag[1]) - 1)
    except: pass

    try:
        pisca_vizinhos(int(tag[0]), int(tag[1]) + 1)
    except: pass
    
    try:
        pisca_vizinhos(int(tag[0]) + 1, int(tag[1]) - 1)
    except: pass

    try:
        pisca_vizinhos(int(tag[0]) + 1, int(tag[1]))
    except: pass

    try:
        pisca_vizinhos(int(tag[0]) + 1, int(tag[1]) + 1)
    except: pass


def desmostra_vizinhos(event):
    tag = canvas.gettags(quadrado)

    try:
        despisca_vizinhos(int(tag[0]) - 1, int(tag[1]) - 1)
    except: pass

    try:
        despisca_vizinhos(int(tag[0]) - 1, int(tag[1]))
    except: pass

    try:
        despisca_vizinhos(int(tag[0]) - 1, int(tag[1]) + 1)
    except: pass

    try:
        despisca_vizinhos(int(tag[0]), int(tag[1]) - 1)
    except: pass

    try:
        despisca_vizinhos(int(tag[0]), int(tag[1]) + 1)
    except: pass

    try:
        despisca_vizinhos(int(tag[0]) + 1, int(tag[1]) - 1)
    except: pass

    try:
        despisca_vizinhos(int(tag[0]) + 1, int(tag[1]))
    except: pass

    try:
        despisca_vizinhos(int(tag[0]) + 1, int(tag[1]) + 1)
    except: pass
    

def pisca_vizinhos(i,j):
    
    items = canvas.find_all()

    for item in items:
        try:
            tags = canvas.gettags(item)
            if int(tags[0]) == i and int(tags[1]) == j:
                canvas.itemconfig(item, outline='green')
        except:
            pass

def despisca_vizinhos(i,j):
    items = canvas.find_all()

    for item in items:
        try:
            tags = canvas.gettags(item)
            if int(tags[0]) == i and int(tags[1]) == j:
                canvas.itemconfig(item, outline = 'black')
        except:
            pass
                
    
    

def escreve_texto(item, coords,tag):
    global jogadas
    
    canvas.delete(item)
    jogadas -= 1
    try:
        if tag[2] == '0':
            canvas.create_rectangle(20 + 40*int(tag[1]), 20 + 40*int(tag[0]),20 + 40*int(tag[1]) + 40, 20 + 40*int(tag[0]) + 40)
            apaga_vizinhos(tag[0],tag[1])
        elif tag[2] == '1':
            canvas.create_rectangle(20 + 40*int(tag[1]), 20 + 40*int(tag[0]),20 + 40*int(tag[1]) + 40, 20 + 40*int(tag[0]) + 40, fill = 'white', tag = (tag[0], tag[1], 'aberto'))
            canvas.create_text(coords[0]+20, coords[1]+20, text=tag[2], tag = (tag[0], tag[1], 'aberto'))
        elif tag[2] == '2':
            canvas.create_rectangle(20 + 40*int(tag[1]), 20 + 40*int(tag[0]),20 + 40*int(tag[1]) + 40, 20 + 40*int(tag[0]) + 40, fill = 'white', tag = (tag[0], tag[1], 'aberto'))
            canvas.create_text(coords[0]+20, coords[1]+20, text=tag[2], fill = 'grey', tag = (tag[0], tag[1], 'aberto'))
        elif tag[2] == '3':
            canvas.create_rectangle(20 + 40*int(tag[1]), 20 + 40*int(tag[0]),20 + 40*int(tag[1]) + 40, 20 + 40*int(tag[0]) + 40, fill = 'white', tag = (tag[0], tag[1], 'aberto'))
            canvas.create_text(coords[0]+20, coords[1]+20, text=tag[2], fill = 'red', tag = (tag[0], tag[1], 'aberto'))
        elif tag[2] == '4':
            canvas.create_rectangle(20 + 40*int(tag[1]), 20 + 40*int(tag[0]),20 + 40*int(tag[1]) + 40, 20 + 40*int(tag[0]) + 40, fill = 'white', tag = (tag[0], tag[1], 'aberto'))
            canvas.create_text(coords[0]+20, coords[1]+20, text=tag[2], fill = 'blue', tag = (tag[0], tag[1], 'aberto'))
        elif tag[2] == '5':
            canvas.create_rectangle(20 + 40*int(tag[1]), 20 + 40*int(tag[0]),20 + 40*int(tag[1]) + 40, 20 + 40*int(tag[0]) + 40, fill = 'white', tag = (tag[0], tag[1], 'aberto'))
            canvas.create_text(coords[0]+20, coords[1]+20, text=tag[2], fill = 'pink', tag = (tag[0], tag[1], 'aberto'))
        elif tag[2] == '6':
            canvas.create_rectangle(20 + 40*int(tag[1]), 20 + 40*int(tag[0]),20 + 40*int(tag[1]) + 40, 20 + 40*int(tag[0]) + 40, fill = 'white', tag = (tag[0], tag[1], 'aberto'))
            canvas.create_text(coords[0]+20, coords[1]+20, text=tag[2], fill = 'green', tag = (tag[0], tag[1], 'aberto'))
        elif tag[2] == '7':
            canvas.create_rectangle(20 + 40*int(tag[1]), 20 + 40*int(tag[0]),20 + 40*int(tag[1]) + 40, 20 + 40*int(tag[0]) + 40, fill = 'white', tag = (tag[0], tag[1], 'aberto'))
            canvas.create_text(coords[0]+20, coords[1]+20, text=tag[2], fill = 'cyan', tag = (tag[0], tag[1], 'aberto'))
        elif tag[2] == '8':
            canvas.create_rectangle(20 + 40*int(tag[1]), 20 + 40*int(tag[0]),20 + 40*int(tag[1]) + 40, 20 + 40*int(tag[0]) + 40, fill = 'white', tag = (tag[0], tag[1], 'aberto'))
            canvas.create_text(coords[0]+20, coords[1]+20, text=tag[2], fill = 'yellow', tag = (tag[0], tag[1], 'aberto'))
    except: pass
    
    

def iniciar_jogo(valor):
    global inicio, situacoes, jogadas, bombas
    try:
        canvas.delete(ALL)
    except: pass
    lista = []
    inicio = Tuplas(LINHA,COLUNA,BOMBAS)
    situacoes = inicio.get_tupla()
    jogadas = 100
    interface(valor)

iniciar_jogo(0)

