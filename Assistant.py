import os
from datetime import datetime
print("Assistant:Hello I'm your assistant\n")
d=0
while True:
    launchCommands=["open","launch","execute","access","use","begin"]
    searchCommand=["search","look up","google","find","answer this"]
    exitCommand=["exit","quit","nothing","abort","not now"]
    assistantInput=input("Assistant:What can i do for you?\nYou:")
    assistantInput=assistantInput.lower()
    assistantInput=assistantInput.replace("web browser","chrome")
    assistantInput=assistantInput.replace("internet","chrome")
    assistantInput=assistantInput.replace("browser","chrome")
    assistantInput=assistantInput.replace("text editor","notepad")
    assistantInput=assistantInput.replace("text document","notepad")
    flag=0
    for p in exitCommand:
        if p in assistantInput:
            flag=flag+1
    if flag==0:
        l=list(assistantInput.split(sep=" "))
        if "time" in assistantInput or "date" in assistantInput:
            now = datetime.now()
            # dd/mm/YY H:M:S
            dt= now.strftime("%d/%m/%Y \n\t   %H:%M:%S")
            print("Aissitant:"+dt)
        else:
            t=0
            for i in l:
                t=t+1
                if l[t-1]=="don't":
                    break
                else:
                    if i in launchCommands:
                        
                        launch="start "
                        launch1=""
                        launch=launch+launch1.join(l[t])
                        if launch!="start chrome":
                            d=os.system(launch)
                            break
                        else:
                            srch=input("Assistant:May I Search something for you or open a website?\nYou:")
                            if srch=="no":
                               d= os.system("chrome")
                            else:
                                query=input("Assistant:Enter search query or website you wish to open\nYou:")
                                if query[-3:]=="com":
                                    d=os.system("start chrome "+query)
                                else:
                                    s="start chrome \"? "
                                    s1=""
                                    s1=s1.join(query)
                                    finalS=s+s1+"\""
                                    print(finalS)
                                    t=os.system(finalS)
            t=0
            for j in l:
                if l[t-1]=="don't":
                    break
                else:  
                    t=t+1
                    if j in searchCommand:
                        search="start chrome \"? "
                        search1=""
                        search1=search1.join(l[t])
                        finalSearch=search+search1+"\""
                        d=os.system(finalSearch)
                        print(t)
        if d!=0:
            print("Assistant: Sorry I don't support this Operation")
    else:
        break
