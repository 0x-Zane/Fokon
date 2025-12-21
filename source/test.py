import json

with open('assets/text_sources/periodic.json', 'r') as periodic:
    periodic_data = json.load(periodic)





arg = input("Entrez l'argument").strip().title()

if arg.isdigit():
    arg = int(arg)
    input(f"arg is {arg} ")
    try:
        print(periodic_data["elements"][arg-1])
    except:
        print(f"{arg} n'est pas dans le tableau periodique")

        

elif len(arg) == 2:
    try:
        pass
    except:
        print(f"{arg} n'est pas dans le tableau periodique")
    #donc c'est un symbole

else:
    #donc c'est le nom de l'élément
    try:
        pass
    except:
        print(f"{arg} n'est pas dans le tableau periodique")
        
        