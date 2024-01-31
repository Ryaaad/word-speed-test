import curses
from curses import wrapper
import time

def main(stdscr):
    curses.init_pair(4,curses.COLOR_BLACK,curses.COLOR_GREEN)
    curses.init_pair(1,curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK,curses.COLOR_RED)
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()
    text='Are You Quick Enough to Finish this and without Erreur'
    key=''
    userText=''
    index=0
    stdscr.addstr(1,1,text)
    start_time = time.time()
    while True : 
     key=stdscr.getkey()    
     if index>=len(text):
       break
     if key=='KEY_BACKSPACE':
        if index>0 :
         index-=1
        userText=userText[0:-1]
        stdscr.refresh()
     if key !='KEY_DOWN' and key !='KEY_UP' and key !='KEY_RIGHT' and key !='KEY_LEFT' and key!='KEY_BACKSPACE' and key!='\n' :
        userText=userText+key
        index+=1
     stdscr.addstr(1,1,text)
     for i in range(0,len(userText)) :
          if userText[i]==text[i]:
              stdscr.addstr(1,i+1,userText[i],curses.color_pair(1))
          else :
             if userText[i]==' ' :
              stdscr.addstr(1,i+1,userText[i],curses.color_pair(3))
             else : 
              stdscr.addstr(1,i+1,userText[i],curses.color_pair(2))
    end_time = time.time()
    Writngtime=end_time-start_time
    Errs=0
    for i in range(len(text)):
      if userText[i]!=text[i]:
        Errs+=1
    Accuracy = (len(text)-Errs)*100 / len(text)
    height , width=stdscr.getmaxyx()
    stdscr.clear()
    color=curses.color_pair(1)
    if Accuracy<50:
      color=curses.color_pair(2)
    Results="Results"
    pos= width/2 - len(Results)/2  
    stdscr.addstr(1,int(pos),Results)
    stdscr.addstr(2,1,f"Accuracy: "); stdscr.addstr(2,12,f"{int(Accuracy)}%",color)
    stdscr.addstr(3,1,f"Number of Errs: "); stdscr.addstr(3,17,f"{Errs}",color)
    stdscr.addstr(4,1,f"Time : {int(Writngtime)} second")
    key=stdscr.getch()    
wrapper(main) 

