try:
    import PySimpleGUI as sg;import threading,time,pip
except:
    import pip
    pip.main(["install","pysimplegui"])
    import PySimpleGUI as sg;import threading,time
sg.theme("Black")
global threadstop
threadstop=[0]
loadinglayout=[
    [sg.Image(filename="DRACO-X.png")],
    [sg.Text("-Loading-",text_color="Red",font="Bold,50")],
    [sg.ProgressBar(10,orientation="h",key="Prog",bar_color=("Green","White"),size=(12,10))],

]



load=sg.Window("DRACO-X Loading...",loadinglayout, icon="DRACO-X.ico",finalize=True)

def guithread():
    pip.main(["install","psutil"]);
    load["Prog"].update(2)
    pip.main(["install","pythonnet"])
    load["Prog"].update(4)
    time.sleep(1)
    load["Prog"].update(10)
    threadstop[0]=1
x=threading.Thread(target=guithread);x.start()
while True:
    e,v=load.read(timeout=500)
    if threadstop[0]==1:
        load.close()
        break
    elif e==sg.WIN_CLOSED:
        load.close()
        quit()


time.sleep(1)
import clr,psutil


clr.AddReference("WeAreDevs_API")
from WeAreDevs_API import ExploitAPI
api=ExploitAPI()
def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

class ExploitCommand:
    def Inject():
        if api.isAPIAttached():
            return
        if checkIfProcessRunning("roblox"):
            sg.Popup("Please wait while DRACO-X injects!",icon="DRACO-X.ico")


            api.LaunchExploit()
            temp=0
            while True:
                time.sleep(3)
                temp+=1

                if api.isAPIAttached():
                    sg.Popup("DRACO-X has finished injecting!",icon="DRACO-X.ico")
                    break
                else:
                    try:
                        api.LaunchExploit()
                    except:
                        pass



        else:
            pass


    def Execute(inb):
        if api.isAPIAttached():
            api.SendLuaScript(inb)
        else:
            pass






inlayout=[
    [sg.Text("Key:"),sg.Input(key="in"),sg.Button("Inject")],
    []
]
MainWindow=sg.Window("DRACO-X",inlayout,icon="DRACO-X.ico",finalize=True)
while True:

    e,v=MainWindow.read()

    if e==sg.WIN_CLOSED:
        quit()
    elif e=="Inject":
        try:
            if checkIfProcessRunning("roblox"):
                if int(v["in"])==553245:

                    ExploitCommand.Inject()
                    MainWindow.close()
                    break
                else:
                    sg.Popup("Invalid key!",icon="DRACO-X.ico")
            else:
                sg.Popup("Roblox is not running!",icon="DRACO-X.ico")

        except Exception as err:
            sg.Popup("Must not be empy and must not have letters or special characters!",icon="DRACO-X.ico")
newlayout=[
    [sg.Text("Commands: ",font="Bold, 10",text_color="Red"),sg.Button("Execute",key="ex")],
    [sg.Multiline(key="in",size=(35,10) )],
    [sg.Text("Fps cap:"),sg.Spin(["100","30","60"],key="sp",enable_events=True)]


]
newwin=sg.Window("DRACO-X",newlayout,icon="DRACO-X.ico",finalize=True)

while True:
    e,v=newwin.read()
    if e=="ex":
        ExploitCommand.Execute(v["in"])
    if e=="sp":
        ExploitCommand.Execute(f"set_fps_cap("+v["sp"]+")")
    if e==sg.WIN_CLOSED:
        newwin.close()
        quit()
