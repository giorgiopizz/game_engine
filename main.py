#main.py
import json
from time import sleep
with open("game.dat","r") as file:
    game=json.load(file)
path=game
print("Resume game?")
link=[]
if input()=='y':
    #reload choices
    with open('choices.dat','r') as file:
        line=file.readline()
        while(line):
            link.append(int(line))
            line=file.readline()
    if len(link)>0:
        for i in link:
            path=path['options'][i]
    
game_over=0

while(not game_over):
    print('\n'+path['title'])
    sleep(2)
    if path['title']=='Win':
        print("\nCongratulations!\nYou have won the game!\n"+\
            "Please come back to visit us!\n")
        break
        game_over=1
    print(path["text"]+'\n')
    sleep(2)
    
    for i in range(len(path["options"])):
        #display the options
        print(str(i+1)+') '+path['options'][i]["title"])

    if len(path["options"])==0:
        #go back
        print("Game over, go back, press b")
        

    #ask to player what to do
    choice=input()
    if choice=='b':
        #go back
        subpath=game
        del link[len(link)-1]
        for i in link:
            subpath=subpath['options'][i]
        path=subpath
    elif choice=='q':
        #save and quit
        with open("choices.dat","w") as file:
            for i in link:
                file.write(str(i)+'\n')
        print("Bye bye")
        break 
    else:
        choice=int(choice)-1
        try:
            path=path["options"][choice]
            link.append(choice)
        except IndexError:
            print("Select only between the possible options")
