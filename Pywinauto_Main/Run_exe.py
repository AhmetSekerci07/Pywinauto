import pywinauto.application


program_path ="C:\Program Files (x86)\Asekerci\Asekerci.exe"
process_name = "Asekerci"  # Replace with the name of the process you want to monitor (PID name)


app = pywinauto.Application(backend="uia").start(
        cmd_line=program_path)
# Better  to use some wait time
app.window(title_re=".*Canfield Capture").wait('visible', timeout=30)



#If you need another def and can't connect automatically use this

from pywinauto import application

yourExeName = "Asekerci"
pid = application.process_from_module(module=yourExeName)
app = pywinauto.Application(backend='uia').connect(process=pid)


