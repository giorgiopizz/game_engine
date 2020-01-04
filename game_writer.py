#write.py
import json
import sys
structure={}
def node(title):
    return {'title':title,'text':'','options':[]}

print("Edit file or create a new one?(0/1)")
c=input()
print("Enter file name:")
name=input()
if c=='1':
    #create
    print("Enter a title")
    title=input()
    structure=node(title)
else:
    try:
        with open(name,"r") as file:
            structure=json.load(file)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(0)
        
#let's keep asking for text and options
path=structure
link=[]

while True:
    print('Do you want to edit the title of this node?')
    print(path['title'])
    if input()=='y':
        title=input()
        path['title']=title
    print('Do you want to edit the text of this node?')
    print(path['text'])
    if input()=='y':
        t=""
        text=input()
        while(text!='#'):
            t+=(text+'\n')
            text=input()
        path['text']=t[:len(t)-1]
    print('Do you want to add options of this node?')
    print(path['options'])
    if input()=='y':
        if len(path['options'])!=0:
            print("Are you sure you want to delete these options?")
            print(path['options'])
            if input()=='y':
                print("How many options?")
                try:
                    num_options=int(input())
                except ValueError:
                    print("Please input an int")
                    pass
                options=[]
                for i in range(num_options):
                    print("Insert title for option %i"%i)
                    title=input()
                    options.append(node(title))
                path['options']=options
        else:
            print("How many options?")
            try:
                num_options=int(input())
            except ValueError:
                print("Please input an int")
                pass
            options=[]
            for i in range(num_options):
                print("Insert title for option %i"%i)
                title=input()
                options.append(node(title))
            path['options']=options
    print(path['options'])
    print('Which option do you want to edit?(if none press b for going back, q to quit or t for this)')
    i=input()
    if i=='b':
        #go back
        subpath=structure
        del link[len(link)-1]
        for i in link:
            print(i)
            subpath=subpath['options'][i]
        path=subpath
    elif i=='q':
        #quit
        break
    elif i=='t':
        #edit this
        pass
    else:
        i=int(i)
        try:
            path=path['options'][i]
            link.append(i)
            print(link)
        except IndexError:
            print("Please input a number between limits")
        except ValueError:
            print("Please input an int")
        
print(structure)
with open(name,"w") as file:
    json.dump(structure, file)
