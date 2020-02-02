import shutil, sys, os, datetime 

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)
            
def list():
    for i, name in enumerate(os.listdir("saves/")):
        print(str(i+1) + ") " + name)

def save(save_path):
    date = datetime.datetime.now().strftime("%d.%m.%Y %H-%M-%S")
    os.mkdir("saves/"+date)
    copytree(save_path, "saves/"+date)
    print("Success!")
    
def load(save_path):
    list_saves = os.listdir("saves/")
    try:
        arg = int(sys.argv[2])
    except:
        arg = len(list_saves)
    if arg > len(list_saves):
        arg = len(list_saves)
    shutil.rmtree(save_path)
    os.mkdir(save_path)
    copytree( "saves/"+list_saves[arg-1], save_path )
    print("Success!")

save_path = os.getenv("LocalAppData") + r"Low\Nolla_Games_Noita\save00"
arg = sys.argv[1]
if arg == "list":
    list()
elif arg == "save":
    save(save_path)
elif arg == "load":
    load(save_path)
else:
    sys.exit("Error param")