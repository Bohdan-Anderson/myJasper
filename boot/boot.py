#!/usr/bin/env python

import os, json
import urllib2

import vocabcompiler

def say(phrase, OPTIONS = " -vdefault+m3 -p 40 -s 160 --stdout > say.wav"):

    os.system("espeak " + json.dumps(phrase) + OPTIONS)
    os.system("aplay -D hw:1,0 say.wav")


def configure():
    try:

        urllib2.urlopen("http://www.google.com").getcode()

        print "CONNECTED TO INTERNET"
        print "COMPILING DICTIONARY"
        vocabcompiler.compile()

        print "STARTING CLIENT PROGRAM"

        try:
            os.system("/home/pi/jasper/client/start.sh")
        except:
            os.system("/home/pi/jasper/backup/start.sh")
        finally:
            return

    except:
        say("it failed, try again")

if __name__ == "__main__":
    say("Hello.... custom boot")
    configure()
