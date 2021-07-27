from tkinter import *
import pygame
import random
import time
array=[None]*14
img=[None]*14
txt=[None]*14
recbtn=None
default=None

class Introduction:
    root=Tk()
    root.title('Memory Game')
    root.geometry('1365x700')
    head = PhotoImage(file=r'mg.png')
    c=Canvas(root,width=1365,height=700)
    hand = PhotoImage(file=r'plbtn.png')
    c.create_image(0,0,image=head, anchor=NW)
    c.place(x=0,y=10)
    btn1 = Button(root,image=hand ,command = root.destroy) 
    btn1.pack(pady = 10)
    root.mainloop()
    
class Program:
    click=1
    match=0
    u_timer=0
    v_timer=0

    def main(self):
        global array,img,txt,default
        def checkwin():
          if(Program.match==6):
            Program.v_timer=time.time()
            now=Program.v_timer-Program.u_timer
            
            from tkinter import messagebox
            import sys
            messagebox.showinfo("GAME OVER","ALL MATCHES FOUND PERFECTLY\nTIME TAKEN:  %.2f seconds"%now)
            root.destroy()
            sys.exit()

        def checkmatch(b):
            if(b['text']==recbtn['text'] and b!=recbtn):
                b.destroy()
                recbtn.destroy()
                play1()
                Program.match+=1
                checkwin()
            else:
                b['image']=default
                recbtn['image']=default
                
            

        def but1(b):
            global img,recbtn
            b['image']=img[0]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but2(b):
            global img,recbtn
            b['image']=img[1]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but3(b):
            global img,recbtn
            b['image']=img[2]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but4(b):
            global img,recbtn
            b['image']=img[3]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but5(b):
            global img,recbtn
            b['image']=img[4]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but6(b):
            global img,recbtn
            b['image']=img[5]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but7(b):
            global img,recbtn
            b['image']=img[6]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but8(b):
            global img,recbtn
            b['image']=img[7]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but9(b):
            global img,recbtn
            b['image']=img[8]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but10(b):
            global img,recbtn
            b['image']=img[9]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but11(b):
            global img,recbtn
            b['image']=img[10]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but12(b):
            global img,recbtn
            b['image']=img[11]
            if(Program.click==1):  
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

     
                       
        Program.u_timer=time.time()                            
        root=Tk()
        root.geometry('1365x700')
        root.title('PLAY GAME')

        loc1=r'doraemon.png'
        loc2=r'nobita.png'
        loc3=r'manny.png'
        loc4=r'buzz.png'
        loc5=r'buck.png'
        loc6=r'hima.png'
        loc=r'imga.png'
        
        pygame.mixer.init()
        def play(a):
            pygame.mixer.music.load("click.mp3")
            pygame.mixer.music.play(loops=0)
        def play1():
            pygame.mixer.music.load("wow.mp3")
            pygame.mixer.music.play(loops=0)

        default=PhotoImage(file=loc)
          #fp1=PhotoImage(file=r'imga.png')
        #fp2=PhotoImage(file=r'imga.png')
        #fp3=PhotoImage(file=r'ol.png')
        #fp4=PhotoImage(file=r'ol.png')
        array=[loc1,loc2,loc3,loc4,loc5,loc6,loc1,loc2,loc3,loc4,loc5,loc6]
        for i in range(0,12):
            x=random.choice(array)#random image
            img[i]=PhotoImage(file=x)#stores images in img list
            txt[i+1]=str(x)#grid images same order will be present
            array.remove(x)#empties array
        
        im=PhotoImage(file=r'go1.png')
        c=Canvas(root,width=1365,height=700)
        c.create_image(0,0,image=im,anchor=NW)
        c.place(x=10,y=0)
        

        #row1
        b11=Button(root,image=default,text=txt[1],bg='white',height=200,width=300,command=lambda:play(but1(b11)))
      
        b11.place(x=81,y=21)
        b12=Button(root,image=default,text=txt[2],bg='white',height=200,width=300,command=lambda:play(but2(b12)))
        b12.place(x=385,y=20)
        b13=Button(root,image=default,text=txt[3],bg='white',height=200,width=300,command=lambda:play(but3(b13)))
        b13.place(x=688,y=20)
        b14=Button(root,image=default,text=txt[4],bg='white',height=200,width=300,command=lambda:play(but4(b14)))
        b14.place(x=990,y=20)
        

        #row2
        b21=Button(root,image=default,text=txt[5],bg='white',height=200,width=300,command=lambda:play(but5(b21)))
        b21.place(x=81 ,y=224)
        b22=Button(root,image=default,text=txt[6],bg='white',height=200,width=300,command=lambda:play(but6(b22)))
        b22.place(x=385,y=224)
        b23=Button(root,image=default,text=txt[7],bg='white',height=200,width=300,command=lambda:play(but7(b23)))
        b23.place(x=688,y=224)
        b24=Button(root,image=default,text=txt[8],bg='white',height=200,width=300,command=lambda:play(but8(b24)))
        b24.place(x=990,y=224)
        

        #row3
        b31=Button(root,image=default,text=txt[9],bg='white',height=200,width=300,command=lambda:play(but9(b31)))
        b31.place(x=81,y=426)
        b32=Button(root,image=default,text=txt[10],bg='white',height=200,width=300,command=lambda:play(but10(b32)))
        b32.place(x=385,y=426)
        b33=Button(root,image=default,text=txt[11],bg='white',height=200,width=300,command=lambda:play(but11(b33)))
        b33.place(x=688,y=426)
        b34=Button(root,image=default,text=txt[12],bg='white',height=200,width=300,command=lambda:play(but12(b34)))
        b34.place(x=990,y=426)
        



        root.mainloop()

obj1=Program()
obj1.main()
