import os

def shutdown():
    os.system("shutdown now")

def restart():
    os.system("reboot")

def suspend():
    os.system("systemctl suspend")

def lock():
    os.system("gnome-screensaver-command -l")  
    
def execute_action(action):
    actions = {
        "shutdown": shutdown,
        "restart": restart,
        "suspend": suspend,
        "lock": lock
    }
    if action in actions:
        actions[action]()
    else:
        print("Invalid action")