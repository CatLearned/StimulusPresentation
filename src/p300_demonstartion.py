# import threading
from psychopy import core, visual, event
#import time

"""Класс не реализован, должен производить демонстрацию стимулов асинхронно"""

"""
class ThreadTest(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.ori=0
        self.running = 1
        print ('initialised')

    def run(self):
        #win = visual.Window((700, 700), allowGUI=False)
        print('created window')
        #stim = visual.PatchStim(win)
        print('created stim')
        while self.running:
            #stim.ori = self.ori
            #stim.draw()
            #win.flip()
            print('.')
            #core.wait(0.01)

        print('Stopping auxil thread')

    def setOri(self, ori):
        self.ori=ori

    def stopTest(self):
        self.running = 0
"""

#tt = ThreadTest()
#tt.start()
#for frameN in range(180):
#    tt.setOri(frameN)
#    time.sleep(0.01)
#time.sleep(30)
#tt.stopTest()
#def main():
#    print('Stopping main thread')


#if __name__ == '__main__':
#    print("Hello")
#    main()
