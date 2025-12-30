# Imports
from tkinter.filedialog import *
from libraries.guizero import *
from tkinter import filedialog
#from libraries import keyboard
import os
print("finished importing libraries")
THEME_FILES = {
    "Blue Paint": "blue_paint.theme",
    "Bluelight": "blueLight.theme",
    "Default Dark": "default_dark.theme",
    "Default Light": "defaultDark.theme",
    "Defaultdark": "defaultDark.theme",
    "Hotdog Stand": "hotdog_stand.theme",
    "Midnight": "midnight.theme",
}
themeType = 0
themesMemContent = ["Default Light"]
memInt = 0
themesDirContent = os.listdir("assets/themes")
for i in range(len(themesDirContent)):
    memItem = str(themesDirContent[memInt]).replace("_", " ").replace("#", "").replace(".theme", "").title()
    themesMemContent.append(memItem)
    memInt = memInt + 1
themesMemContent.sort()
print("content of themes dir" + str(os.listdir("assets/themes")))
print("content of loaded themes" + str(themesMemContent))
print("Opened adv config")
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
    print("Open file")
def saveAs():
    files = [('loger script Text Document', '*.lst'),
             ('Text Document', '*.txt'),
             ('All Files', '*.*')]
    file = filedialog.asksaveasfilename(filetypes=files,defaultextension=".lst", initialdir='projects', title="Save - loger file editor")
    if file:  # user selected file
        with open(file, 'w') as f:
            f.write(inputBox.value)
            fd = open(file, "r")
            d = fd.read()
            fd.close()
            m = d.split("\n")
            s = "\n".join(m[:-1])
            fd = open(file, "w+")
            for i in range(len(s)):
                fd.write(s[i])
            fd.close()
    else:  # user cancel the file browser window
        app.info("loger File editor", "Action Canceled")
    print("Save file")
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
    print("New file")
def close():
    closeT = app.yesno("loger File editor", "Are you sure you want to quit? All unsaved progress will be lost.")
    if closeT:
        app.disable()
        app.destroy()
def fontColor():
    inputBox.text_color = app.select_color(color='Black')
    print("Font color window opened")
def comingSoon():
    app.info("loger File editor", "This feature is still a work in progress.")
    print("It's not done yet 😤")  # It's not done yet 😤
def lfeCredits():
    creditsWind = Window(app, title="Credits - loger file editor", width=300, height=200)
    memBox = TitleBox(creditsWind, "")
    Text(memBox, text="-+{loger file editor}-+\n"
                           "Development - logerdex97\n"
                           "Github - logerdex97\n"
                           "keyboard - boppreh and it's contributors\n"
                           "guizero - lawsie and it's contributors\n"
                           "illum font - logerdex97\n"
                           "All themes - logerdex97\n"
                           "--=Special thanks=--\n"
                           "Python - The python team")
    print("Python credits:")
    credits()
    print(":)")
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
        print("Updated all font values")
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
        print("Reset all font values")
    def theme():
        global themeType
        if themeSel.value == "Default Light":
            inputBox.text_color = None
            app.bg = None
            app.text_color = None
            themeType = 0
            print("switched theme to: Default Light")
        else:
            # open the theme file selected
            filename = THEME_FILES.get(themeSel.value)
            if not filename:
                print("Unknown theme:", themeSel.value)
                return

            file = open("assets/themes/" + filename)

            # read the content of the file opened
            content = file.readlines()
            app.bg = content[1]
            app.text_color = content[2]
            themeType = int(content[3])
            inputBox.bg = content[4]
            inputBox.text_color = content[0]
            print("switched theme to: " + themeSel.value)
    def resetTheme():
        themeSel.value = "Default Light"
        theme()
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
    font = Combo(formatLabel, command=formatSel, options=["Courier New", "Cascadia Code", "ilium", "Symbol",
                                                          "Times New Roman", "Webdings", "Wingdings", "Yu Gothic"])
    PushButton(formatLabel, text="Reset", command=resetFont)
    themeLabel = TitleBox(configAd, text="Theme options", grid=[2,1])  # Theme Options
    Text(themeLabel, text="--Theme--")
    themeSel = Combo(themeLabel, command=theme, options=themesMemContent)
    themeSel.value = "Default Light"
    PushButton(themeLabel, text="Reset", command=resetTheme)
    theme()
def textWrap():
    if inputBox.wrap:
        inputBox.wrap = False
    else:
        inputBox.wrap = True
    print("Toggled text wrap")
def curserPOS():
    curserPOSV.value = "loger File Editor | " + inputBox.cursor_position
# Main Gui code
app = App(title="loger File editor", layout="center", width=800, height=600)
root = app.tk

root.bind("<Control-n>", lambda e: newFile())
root.bind("<Control-o>", lambda e: openFile())
root.bind("<Control-s>", lambda e: saveAs())
root.bind("<Control-q>", lambda e: close())

inputBox = TextBox(app, width="fill", height="fill", multiline=True, command=curserPOS)
inputBox.tk.bind("<Control-s>", lambda e: saveAs())
inputBox.text_size = 11
curserPOSV = Text(app, text="")
menubar = MenuBar(app,
                  toplevel=["File", "Edit", "View", "Tools"],
                  options=[
                      [["New", newFile], ["Open", openFile], ["Save as", saveAs], ["Exit", close]],  #File
                      [["Toggle text wrap", textWrap]],  #Edit
                      [["Credits", lfeCredits]],  #View
                      [["Settings (Beta)", adConfig]]  #Tools
                    ])
# Hotkeys
#keyboard.add_hotkey('ctrl + n', newFile)
#keyboard.add_hotkey('ctrl + o', openFile)
#keyboard.add_hotkey('ctrl + s', saveAs)
app.when_closed = close
app.icon = "assets/ico.png"
curserPOS()
app.when_clicked = curserPOS
app.display()

