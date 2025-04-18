def shutdown():
    import os
    os.system("shutdown now")

def restart():
    import os
    os.system("reboot")

def suspend():
    import os
    os.system("systemctl suspend")

def lock():
    import os
    os.system("gnome-screensaver-command -l")  # Adjust this command based on your desktop environment

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