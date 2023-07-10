import win32com.client as wincl

speaker = wincl.Dispatch("SAPI.SpVoice")
voices = speaker.GetVoices()
speaker.Voice = voices.item(0)

class cal_reps:

    change = None

    #read function in file
    def read_file(self):
        with open("Reps_value", "r")as f:
            val = f.read()
            print("Remaining reps: ", val)
            speaker.speak(f"you have{val} remaining reps to finish")
            return val

    #write function in file
    def write_file(self, newVal):
        with open("Reps_value", "w")as f:
            f.write(newVal)

    #calculate
    def add50(self, val):
        change = int(val)+50
        self.write_file(str(change))
    def add100(self, val):
        change = int(val)+100
        self.write_file(str(change))
    def subtract(self, val, subt):
        if subt >= val:
            self.write_file("0")
            print("you did it king, I am proud")
            speaker.speak("you did it king, I am proud")
        else:
            change = int(val)-subt
            self.write_file(str(change))
            print("Nice work, King!!")
            speaker.speak("Nice work, King")

#outside class
aryan = cal_reps()
while(True):
    #output reps
    Reps = int(aryan.read_file())


    #user input
    uin = input("use add or sub function(pf, f, -, q): ")
    if uin == "q":
        print("Stay focused king")
        speaker.speak("Stay focused king")
        break
    elif uin!="pf" and uin!="f" and uin!="-" and uin!="q":
        print("Please enter a valid value")
        speaker.speak("Please Enter a valid number")
        continue
    #cases
    match uin:
        case "f":
            aryan.add50(Reps)
        case"pf":
            aryan.add100(Reps)
        case"-":
            sub = int(input("sub reps: "))
            aryan.subtract(Reps, sub)