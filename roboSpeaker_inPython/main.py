import win32com.client as wincl

if __name__ == '__main__':   #main program start form here
            speaker = wincl.Dispatch("SAPI.SpVoice")  # .Dispatch is a method in wincl, .SpVoice is a com object that represent the speach synthesis engine
            '''---------------------------------------------------------------------------------'''
            voices = speaker.GetVoices()
            speaker.Voice = voices.Item(1)  #changes the voice to a female speaker
            speaker.speak("welcome to RoboSpeaker version1.1 Created by Mr.Aryan Chandra")
            speaker.speak("My name is robica, type anything you want me to speak")
            '''------------------------------------------------------------------------------------'''
            while(True):    #infinite loop
                  x = input("Enter what you want me to speak: ")

                  if x =="q":   #type q to break the loop
                          speaker.speak("it was nice speaking for you, bye bye")
                          break
                  speaker.speak(x)    #.speak is a function that synthesis speech, speaker is the object