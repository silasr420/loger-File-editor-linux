# Imports
from tkinter.filedialog import *
from guizero import *
from tkinter import filedialog
import keyboard
themeType = 0
# Opens .TXT, .SAV (only loger studios compiled savs and .LST)
def openFile():
    global inputBox
    Tk().withdraw()   # we don't want a full GUI, so keep the root window from appearing
    fileContent = askopenfilename(defaultextension='lst', initialdir='projects', title="Open - loger file editor")  # show an "Open" dialog box and return the path to the selected file
    # Open the file in read mode
    if fileContent != '':
        with open(fileContent, 'r') as f:
            # Read the entire content of the file
            content = f.read()
        inputBox.value = content
        # Close the file
    else:
        app.info("loger File editor", "Action Canceled")
# Saves .LST
def saveAs():
    files = [('loger script Text Document', '*.lst'),
             ('Text Document', '*.txt'),
             ('All Files', '*.*')]
    file = filedialog.asksaveasfilename(filetypes=files,defaultextension=".lst", initialdir='projects', title="Save - loger file editor")
    if file:  # user selected file
        with open(file, 'w') as f:
            f.write(inputBox.value)
    else:  # user cancel the file browser window
        app.info("loger File editor", "Action Canceled")
    fd = open(file, "r")
    d = fd.read()
    fd.close()
    m = d.split("\n")
    s = "\n".join(m[:-1])
    fd = open(file, "w+")
    for i in range(len(s)):
        fd.write(s[i])
    fd.close()
def saveAsTxt():
    global inputBox
    files = [('Text Document', '*.txt'),
             ('loger script Text Document', '*.lst'),
             ('All Files', '*.*')
             ]
    file = filedialog.asksaveasfilename(
        filetypes=files, defaultextension=".txt", initialdir='projects', title="Save As - loger file editor")
    if file:  # user selected file
        with open(file, 'w') as f:
            f.write(inputBox.value)
    else:  # user cancel the file browser window
        app.info("loger File editor", "Action Canceled")
    fd = open(file, "r")
    d = fd.read()
    fd.close()
    m = d.split("\n")
    s = "\n".join(m[:-1])
    fd = open(file, "w+")
    for i in range(len(s)):
        fd.write(s[i])
    fd.close()
def newFile():
    files = [('All Files', '*.*'),
             ('loger script Text Document', '*.lst'),
             ('Text Document', '*.txt')]
    file = filedialog.asksaveasfilename(filetypes=files,defaultextension=".lst", initialdir='projects', title="New file - loger file editor")
    if file:  # user selected file
        fob = open(file,'x')
        fob.close()
    else:  # user cancel the file browser window
        app.info("loger File editor", "Action Canceled")
def close():
    closeT = app.yesno("loger File editor", "Are you sure you want to quit? All unsaved progress will be lost.")
    if closeT:
        app.disable()
        app.destroy()
def fontColor():
    inputBox.text_color = app.select_color(color='Black')
# It's not done yet 😤
def comingSoon():
    app.info("loger File editor", "This feature is still a work in progress.")
# ----------------------------------------------------------
def adConfig():
    configAd = Window(app, title="Settings - loger File editor", width=400, height=300, layout="grid")
    # Config gui for advanced menu
    def formatSel():
        inputBox.text_bold = bold.value
        inputBox.text_italic = italix.value
        inputBox.text_underline = underline.value
        inputBox.text_size = sizeSel.value
        inputBox.font = font.value
    def resetFont():
        bold.value = 0
        italix.value = 0
        underline.value = 0
        sizeSel.value = 11
        if themeType == 0:
            inputBox.text_color = None
        elif themeType == 1:
            inputBox.text_color = "White"
        font.value = "Courier New"
        formatSel()
    def theme():
        global themeType
        if theme.value == "Default Light":
            inputBox.text_color = None
            app.bg = None
            app.text_color = None
            themeType = 0
        elif theme.value == "Midnight":
            # open the sample file used
            file = open('themes/midnight.theme')
            # read the content of the file opened
            content = file.readlines()
            inputBox.text_color = content[0]
            app.bg = content[1]
            app.text_color = content[2]
            themeType = int(content[3])
            inputBox.bg = content[4]
        elif theme.value == "Default Dark":
            # open the sample file used
            file = open('themes/defaultDark.theme')
            # read the content of the file opened
            content = file.readlines()
            inputBox.text_color = content[0]
            app.bg = content[1]
            app.text_color = content[2]
            themeType = int(content[3])
            inputBox.bg = content[4]
        elif theme.value == "Cool light":
            # open the sample file used
            file = open('themes/blueLight.theme')
            # read the content of the file opened
            content = file.readlines()
            inputBox.text_color = content[0]
            app.bg = content[1]
            app.text_color = content[2]
            themeType = int(content[3])
            inputBox.bg = content[4]
    # Settings Wind:
    formatLabel = TitleBox(configAd, text='Font options', grid=[1,1])  # Font options
    bold = CheckBox(formatLabel, text='Bold', command=formatSel)
    italix = CheckBox(formatLabel, text='Italix', command=formatSel)
    underline = CheckBox(formatLabel, text="Underline", command=formatSel)
    PushButton(formatLabel, text='Font color', command=fontColor)  # Font Color
    Text(formatLabel, text="--Font size--")
    sizeSel = Slider(formatLabel, start=9, end=16, command=formatSel)
    sizeSel.value = 11
    Text(formatLabel, text="--Font--")
    font = Combo(formatLabel, command=formatSel, options=["Courier New", "Cascadia Code", "Symbol", "Times New Roman", "Webdings", "Wingdings", "Yu Gothic"])
    PushButton(formatLabel, text="Reset", command=resetFont)
    themeLabel = TitleBox(configAd, text="Theme options", grid=[2,1])  # Theme Options
    Text(themeLabel, text="--Theme--")
    theme = Combo(themeLabel, command=theme, options=["Default Light", "Default Dark",
    "Midnight", "Cool light"])

def textWrap():
    if inputBox.wrap:
        inputBox.wrap = False
    else:
        inputBox.wrap = True
# Main Gui code
app = App(title="loger File editor", layout="center", width=800, height=600)
inputBox = TextBox(app, width="fill", height="fill", multiline=True)
inputBox.text_size = 11
Text(app, text="loger File Editor")
menubar = MenuBar(app,
                  toplevel=["File", "Edit", "Tools"],
                  options=[
                      [["New", newFile], ["Open", openFile], ["Save as", saveAs], ["Save as TXT", saveAsTxt], ["Exit", close]],  #File
                      [ ["Toggle text wrap", textWrap] ],  #Edit
                      [["Settings (Beta)", adConfig]]  #Tools
                    ])
# Hotkeys
keyboard.add_hotkey('ctrl + alt + t', adConfig)
keyboard.add_hotkey('ctrl + n', newFile)
keyboard.add_hotkey('ctrl + o', openFile)
keyboard.add_hotkey('ctrl + s', saveAs)
keyboard.add_hotkey('ctrl + shift + s', saveAsTxt)
app.when_closed = close
app.icon = "assets/ico.png"
app.display()
