import glob;
import sys;
import os;
import threading
import time


if  (len(sys.argv)<2) :
    print "provide directory path in fisrt argument\n";
    sys.exit();

if ( not os.path.isdir(sys.argv[1])  ) :
    print "Not a valid directory\n";
    sys.exit();

sFiles = glob.glob(sys.argv[1] + "/*.docx");
print(sFiles);

def readAndSent( sFileName ) :
    print "Reading files :-"+ sFileName;
    print "Sending files :-"+ sFileName;

class myThreadForReading (threading.Thread):
   def __init__(self, sFile):
      threading.Thread.__init__(self);
      self.sFile = sFile;
   def run(self):
      readAndSent(self.sFile)

tCounter =0;
for index in range(len(sFiles)):
    tCounter = myThreadForReading(sFiles[index])
    tCounter.start();