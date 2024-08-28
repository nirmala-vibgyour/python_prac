# lauch other or external programs on computer with Popen()
import subprocess, webbrowser

website = webbrowser.open(r'https://www.google.com')
# webbrowser.open_new(...), webbrowser.open_new_tab(...); c = wbbrowser.get(...search engine...) c.open(...)

calcProc = subprocess.Popen(r'C:\Windows\System32\calc.exe')

# Popen module has two methods poll() and wait().
print(calcProc.poll() == None)

print(calcProc.wait())

print(calcProc.poll())

notePad = subprocess.Popen([r'C:\Windows\notepad.exe', r'C:\hello.txt'])


# python -m webbrowser -t "https://www.google.com" 
# opens browser using terminal

file = subprocess.Popen(['C:\\python312\\python.exe', 'duration.py'])

# txt_file = subprocess.Popen(['start', 'hello.txt'], shell=True)