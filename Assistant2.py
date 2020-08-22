import os
from datetime import datetime
def convert(lst):
    return ' '.join(lst)
print("Assistant:Hello I'm your assistant\n")
d=0
while True:
   # launchCommands=["open","launch","execute","access","use","begin","surf"]
    searchCommand=["search","look up","google","find","answer this"]
    exitCommand=["exit","quit","nothing","abort","not now"]
    availableApps=['chrome','mspaint','notepad','calc','explorer','msedge','wmplayer','vlc','cmd']
    questions=['who','whom','whose','what','which','where','whither','whence','when','how','why']
    assistantInput=input("Assistant:What can i do for you?\nYou:")
    assistantInput=assistantInput.lower()
    assistantInput=assistantInput.replace("internet","chrome")
    assistantInput=assistantInput.replace("browser","chrome")
    assistantInput=assistantInput.replace("text","notepad")
    assistantInput=assistantInput.replace("microsoft edge","msedge")
    assistantInput=assistantInput.replace("windows media player","wmplayer")
    assistantInput=assistantInput.replace("audio","wmplayer")
    assistantInput=assistantInput.replace("video","wmplayer")
    assistantInput=assistantInput.replace("my files","explorer")
    assistantInput=assistantInput.replace("microsoft paint","mspaint")
    assistantInput=assistantInput.replace("windows paint","mspaint")
    assistantInput=assistantInput.replace("windows microsoft paint","mspaint")


    l=list(assistantInput.split(sep=" "))
    d=0
    t=0
    flag=0
    for i in l:
        t=t+1
        if i in exitCommand:
            flag=1
            t=-99
            break
        elif i in "date" or i in "time":
            flag=1
            now = datetime.now()
            # dd/mm/YY H:M:S
            dt= now.strftime("%d/%m/%Y \n\t   %H:%M:%S")
            print("Aissitant:"+dt)
            break
        elif i in availableApps and i not in "chrome":
            flag=1
            y1="start "
            y=''
            y=y.join(i)
            os.system(y1+y)
            break
        elif i in searchCommand:
            flag=1
            h=convert(l[t:])
            u="start chrome \"? "
            e=u+h+"\""
            os.system(e)
            break
        elif i in l and "chrome" in i:
            src=input("Assistant:May i open a website or perform a search?(yes/no)")
            if src=="no":
                flag=1
                y1="start "
                y=''
                y=y.join(i)
                os.system(y1+y)
                break
            else:
                query=input("Assistant:Enter search query or website you wish to open\nYou:")
                if query[-3:]=="com" or query[-3:]=="org":
                    flag=1
                    os.system("start chrome "+query)
                    break
                else:
                    flag=1
                    s="start chrome \"? "
                    s1=""
                    s1=s1.join(query)
                    finalS=s+s1+"\""
                    os.system(finalS)
                    break    
        elif i in questions:
            flag=1
            g=convert(l[t:])
            g="start chrome \"? "
            finalg=g+assistantInput+"\""
            os.system(finalg)
            break
        if "jupyter notebook" in assistantInput:
            flag=1
            print("Assistant: Connecting...")
            os.system("jupyter notebook")
            break                      
    if flag==0:
        s="start chrome \"? "
        finalS=s+assistantInput+"\""
        os.system(finalS)
        
    if t==-99:
        break



