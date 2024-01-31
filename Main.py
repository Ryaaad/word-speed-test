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
    stdscr.addstr(1,1,text)
    key=''
    userText=''
    index=0
    color=curses.color_pair(1)
    start_time = time.time()
    while True : 
     key=stdscr.getkey()    
     if key=='KEY_BACKSPACE':
        if index>0 :
         index-=1
        userText=userText[0:-1]
     if index>=len(text):
       break
     if key !='KEY_DOWN' and key !='KEY_UP' and key !='KEY_RIGHT' and key !='KEY_LEFT' and key!='KEY_BACKSPACE' and key!='\n' :

        userText=userText+key
        index+=1
        for i in userText :
          if i==text[index-1]:
              stdscr.addstr(1,index,key,curses.color_pair(1))
          else :
             if i==' ' :
              stdscr.addstr(1,index,key,curses.color_pair(3))
             else : 
              stdscr.addstr(1,index,key,curses.color_pair(2))
    end_time = time.time()
    Writngtime=end_time-start_time
    Errs=0
    for i in range(len(text)):
      if userText[i]!=text[i]:
        Errs+=1
    accurency = (len(text)-Errs)*100 / len(text)
    stdscr.addstr(5,1,f"Done with {int(accurency)}% with {Errs} Erreurs and time of {int(Writngtime)} second")
    key=stdscr.getch()    
wrapper(main) 

