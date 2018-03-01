import numpy as np
from scipy.signal import zpk2ss, ss2zpk, tf2zpk, zpk2tf
from numpy import linspace, logspace
from numpy import asarray, tan, array, pi, arange, cos, log10, unwrap, angle
from matplotlib.pyplot import axvline, axhline
from scipy.signal import freqz
import matplotlib.pyplot as plt
from PyQt4.uic import loadUiType

import matplotlib.backends.backend_qt4agg
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from PyQt4.QtGui import *
import wave
from scipy.fftpack import rfft, irfft, fftfreq ,fft ,ifft
import pyglet
import scipy.io.wavfile as wav
import serial  # import Serial Library
import numpy as np
import matplotlib.pyplot as plt  # import matplotlib library
from drawnow import *
Ui_MainWindow, QMainWindow = loadUiType('digital_filter.ui')


class Main(QMainWindow, Ui_MainWindow):

    """
    Demonstrates a basic example of the "scaffolding" you need to efficiently
    blit drawable/draggable/deleteable artists on top of a background.
    """

    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)

        pixmap = QPixmap('x.jpg')
        self.label.setPixmap(pixmap)

        #self.fig, self.ax = plt.subplots()
        self.fig = plt.figure()
        plt.axis('scaled')
        plt.axis([-1, 1, -1, 1])
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.circle = plt.Circle((0, 0), 1, fill=False)
        self.ax.add_patch(self.circle)
        axvline(0, color='0.3')
        axhline(0, color='0.3')
        self.ax.plot()

        self.canvas = matplotlib.backends.backend_qt4agg.FigureCanvasQTAgg(self.fig)
        self.verticalLayout.addWidget(self.canvas)
        self.canvas.draw()
        self.ax.set_title('Left click to add/drag a point\nRight-click to delete',fontsize=9)
        self.toolbar = NavigationToolbar(self.canvas, self, coordinates=True)
        self.addToolBar(self.toolbar)

        self.figure2 = Figure()# Frequency Response
        self.drawing2 = self.figure2.add_subplot(211)
        self.drawing3 = self.figure2.add_subplot(212)
        self.figure2.suptitle('Frequency Response')
        self.drawing2.plot()
        self.drawing3.plot()
        self.drawing2.set_xlabel('Normalized frequency',fontsize = 9)
        self.drawing2.set_ylabel('Amplitude[dB]', fontsize=9)
        self.drawing2.yaxis.set_label_position("right")
        self.drawing3.set_xlabel('Normalized Frequency', fontsize=9)
        self.drawing3.set_ylabel('Phase (radians)', fontsize=9)
        self.drawing3.yaxis.set_label_position("right")
        self.figure2.subplots_adjust(hspace=0.4, bottom=0.11, left=0.15)
        self.canvas2 = matplotlib.backends.backend_qt4agg.FigureCanvasQTAgg(self.figure2)
        self.verticalLayout_2.addWidget(self.canvas2)
        self.canvas2.draw()
        self.toolbar = NavigationToolbar(self.canvas2, self, coordinates=True)
        self.addToolBar(self.toolbar)

        self.figure3 = Figure() #Before
        self.drawing4 = self.figure3.add_subplot(311)
        self.drawing5 = self.figure3.add_subplot(312)
        self.drawing55 = self.figure3.add_subplot(313)
        self.figure3.suptitle('Wave Before Manipulation')
        self.drawing4.plot()
        self.drawing5.plot()
        self.drawing55.plot()
        self.drawing4.set_xlabel('Time', fontsize=9)
        self.drawing4.set_ylabel('Amplitude', fontsize=9)
        self.drawing4.yaxis.set_label_position("right")
        self.drawing5.set_xlabel('Frequency', fontsize=9)
        self.drawing5.set_ylabel('Amplitude', fontsize=9)
        self.drawing5.yaxis.set_label_position("right")
        self.drawing55.set_xlabel('Frequency', fontsize=9)
        self.drawing55.set_ylabel('Phase', fontsize=9)
        self.drawing55.yaxis.set_label_position("right")
        self.figure3.subplots_adjust(hspace=0.9, bottom=0.18, left=0.15)
        self.canvas3 = matplotlib.backends.backend_qt4agg.FigureCanvasQTAgg(self.figure3)
        self.verticalLayout_3.addWidget(self.canvas3)
        self.canvas3.draw()
        self.toolbar = NavigationToolbar(self.canvas3, self, coordinates=True)
        self.addToolBar(self.toolbar)

        self.figure4 = Figure()#After
        self.drawing6 = self.figure4.add_subplot(311)
        self.drawing7 = self.figure4.add_subplot(312)
        self.drawing77 = self.figure4.add_subplot(313)
        self.figure4.suptitle('Wave After Manipulation')
        self.drawing6.plot()
        self.drawing7.plot()
        self.drawing77.plot()
        self.drawing6.set_xlabel('Time', fontsize=9)
        self.drawing6.set_ylabel('Amplitude', fontsize=9)
        self.drawing6.yaxis.set_label_position("right")
        self.drawing7.set_xlabel('Frequency', fontsize=9)
        self.drawing7.set_ylabel('Amplitude', fontsize=9)
        self.drawing7.yaxis.set_label_position("right")
        self.drawing77.set_xlabel('Frequency', fontsize=9)
        self.drawing77.set_ylabel('Phase', fontsize=9)
        self.drawing77.yaxis.set_label_position("right")
        self.figure4.subplots_adjust(hspace=0.9, bottom=0.18, left=0.15)
        self.canvas4 = matplotlib.backends.backend_qt4agg.FigureCanvasQTAgg(self.figure4)
        self.verticalLayout_3.addWidget(self.canvas4)
        self.canvas4.draw()
        self.toolbar = NavigationToolbar(self.canvas4, self, coordinates=True)
        self.addToolBar(self.toolbar)

        self.figure5 = Figure()  # Online section
        self.drawing8 = self.figure5.add_subplot(311)
        self.drawing9 = self.figure5.add_subplot(312)
        self.drawing10 = self.figure5.add_subplot(313)
        self.figure5.suptitle('Wave Online Manipulation')
        self.drawing8.plot()
        self.drawing9.plot()
        self.drawing10.plot()
        self.drawing8.set_xlabel('Time', fontsize=9)
        self.drawing8.set_ylabel('Amplitude', fontsize=9)
        self.drawing8.yaxis.set_label_position("right")
        self.drawing9.set_xlabel('Frequency', fontsize=9)
        self.drawing9.set_ylabel('Amplitude', fontsize=9)
        self.drawing9.yaxis.set_label_position("right")
        self.drawing10.set_xlabel('Frequency', fontsize=9)
        self.drawing10.set_ylabel('Phase', fontsize=9)
        self.drawing10.yaxis.set_label_position("right")
        self.figure5.subplots_adjust(hspace=0.6, bottom=0.12, left=0.15)
        self.canvas5 = matplotlib.backends.backend_qt4agg.FigureCanvasQTAgg(self.figure5)
        self.verticalLayout_4.addWidget(self.canvas5)
        self.canvas5.draw()
        self.toolbar = NavigationToolbar(self.canvas5, self, coordinates=True)
        self.addToolBar(self.toolbar)

        # self.fig, self.ax = self.setup_axes()
        self.xy = [] #for the circle
        self.xy2 = []
        self.zero = [] #for trans func
        self.poles = []
        self.tolerance = 10
        #self._num_clicks = 0
        self.points = self.ax.scatter([], [], s=30, color='blue',
                                      picker=self.tolerance, animated=True) #for zeros
        self.points2 = self.ax.scatter([], [], s=30, color='red',
                                      picker=self.tolerance, animated=True) #for poles


        connect = self.fig.canvas.mpl_connect
        connect('button_press_event', self.on_click)
        self.draw_cid = connect('draw_event', self.grab_background)

        self.pushButton.clicked.connect(self.browse_txt)
        self.pushButton_2.clicked.connect(self.file_save_txt)
        self.pushButton_3.clicked.connect(self.reset)
        self.pushButton_4.clicked.connect(self.browse_wav)
        self.pushButton_4.setStyleSheet("background-color: red")
        self.pushButton_5.clicked.connect(self.drawOn4)
        self.pushButton_5.setStyleSheet("background-color: red")
        self.pushButton_6.clicked.connect(self.online)
        self.pushButton_6.setStyleSheet("background-color: red")
        self.flag1 = 0

        #self.radioButton.toggled.connect(self.setup)

    def reset(self):
        if self.radioButton.isChecked() == True:
            index = len(self.xy) -2
            while 0 <= index :

                self.delete_point(index)
                index -= 2
        if self.radioButton_2.isChecked() == True:
            index = len(self.xy2) - 2
            while 0 <= index:
                self.delete_point(index)
                index -= 2




    def on_click(self, event):
        """Decide whether to add, delete, or drag a point."""
        # If we're using a tool on the toolbar, don't add/draw a point...
        # if self.fig.canvas.toolbar._active is not None:
        # return
        if self.radioButton.isChecked() == True:

            contains, info = self.points.contains(event)

            if contains:
                i = info['ind'][0]
                if event.button == 1:
                    self.start_drag(i)
                elif event.button == 3:

                    self.delete_point(i)
            else:

                self.x=event.xdata
                self.y=event.ydata
                self.add_point()

        if self.radioButton_2.isChecked() == True:
            contains2, info2 = self.points2.contains(event)

            if contains2:
                i = info2['ind'][0]
                if event.button == 1:
                    self.start_drag(i)
                elif event.button == 3:
                    self.delete_point(i)
            else:
                self.x2 = event.xdata
                self.y2 = event.ydata
                self.add_point()


    def update(self):
        """Update the artist for any changes to self.xy."""
        if self.radioButton.isChecked() == True:

            self.points.set_offsets(self.xy)
            self.blit()
        if self.radioButton.isChecked() == False:
            self.points2.set_offsets(self.xy2)
            self.blit()

    def add_point(self):
        if self.radioButton.isChecked() == True:
            #limitation of circle
            if ((self.x) ** 2 + (self.y) ** 2) ** 0.5 < 1 and self.y > 0:
                z = self.x + self.y * 1j

                self.xy.append([self.x, self.y])
                self.xy.append([self.x, -self.y])


                self.zero.append(z)
                print (self.zero)
                self.update()
                self.drawOn2()
        if self.radioButton_2.isChecked() == True:
            if ((self.x2) ** 2 + (self.y2) ** 2) ** 0.5 < 1 and self.y2 > 0:
                z = self.x2 + self.y2 * 1j

                self.xy2.append([self.x2, self.y2])
                self.xy2.append([self.x2, -self.y2])
                self.poles.append(z)
                print (self.poles)
                self.update()
                self.drawOn2()



    def delete_point(self, i):
        if self.radioButton.isChecked() == True:
            self.xy.pop(i)
            self.xy.pop()
            self.zero.pop()
            print (self.zero)

            self.update()
            self.drawOn2()
        if self.radioButton.isChecked() == False:
            self.xy2.pop(i)
            self.xy2.pop()
            self.poles.pop()
            print (self.poles)
            self.update()
            self.drawOn2()

    def start_drag(self, i):
        """Bind mouse motion to updating a particular point."""
        if self.radioButton.isChecked() == True:

            self.drag_i = i
            connect = self.fig.canvas.mpl_connect
            cid1 = connect('motion_notify_event', self.drag_update)
            cid2 = connect('button_release_event', self.end_drag)

            self.drag_cids = [cid1, cid2 ]

        if self.radioButton.isChecked() == False:
            self.drag_i2 = i
            connect = self.fig.canvas.mpl_connect
            cid1 = connect('motion_notify_event', self.drag_update)
            cid2 = connect('button_release_event', self.end_drag)

            self.drag_cids2 = [cid1, cid2]


    def drag_update(self, event):
        """Update a point that's being moved interactively."""
        if self.radioButton.isChecked() == True:
            if ((event.xdata) ** 2 + (event.ydata) ** 2) ** 0.5 < 1 and event.ydata > 0:

                self.xy[self.drag_i] = [event.xdata, event.ydata]
                self.xy[self.drag_i+1] = [event.xdata, -event.ydata]
                z = event.xdata + event.ydata * 1j
                self.zero[self.drag_i /2] = z

                self.update()
                self.drawOn2()
        if self.radioButton.isChecked() == False:
            if ((event.xdata) ** 2 + (event.ydata) ** 2) ** 0.5 < 1 and event.ydata > 0:

                self.xy2[self.drag_i2] = [event.xdata, event.ydata]
                self.xy2[self.drag_i2 + 1] = [event.xdata, -event.ydata]

                z = event.xdata + event.ydata * 1j
                self.poles[self.drag_i2/2] = z

                self.update()
                self.drawOn2()



    def end_drag(self, event):
        """End the binding of mouse motion to a particular point."""
        if self.radioButton.isChecked() == True:

            for cid in self.drag_cids:
                self.fig.canvas.mpl_disconnect(cid)
        if self.radioButton.isChecked() == False:
            for cid in self.drag_cids2:
                self.fig.canvas.mpl_disconnect(cid)


    def safe_draw(self):
        if self.radioButton.isChecked() == True:

            #"""Temporarily disconnect the draw_event callback to avoid recursion"""
            canvas = self.fig.canvas
            #canvas.mpl_disconnect(self.draw_cid)
            #canvas.draw()
            self.draw_cid = canvas.mpl_connect('draw_event', self.grab_background)
        if self.radioButton.isChecked() == False:
            #canvas = self.fig.canvas
            #canvas.mpl_disconnect(self.draw_cid)
            #canvas.draw()
            self.draw_cid = canvas.mpl_connect('draw_event', self.grab_background)


    def grab_background(self, event=None):
        """
        When the figure is resized, hide the points, draw everything,
        and update the background.
        """
        if self.radioButton.isChecked() == True:

            self.points.set_visible(False)
            self.safe_draw()

            # With most backends (e.g. TkAgg), we could grab (and refresh, in
            # self.blit) self.ax.bbox instead of self.fig.bbox, but Qt4Agg, and
            # some others, requires us to update the _full_ canvas, instead.
            self.background = self.fig.canvas.copy_from_bbox(self.fig.bbox)


            self.points.set_visible(True)
            self.blit()
        if self.radioButton_2.isChecked() == True    :
            self.points2.set_visible(False)
            self.safe_draw()

            self.background2 = self.fig.canvas.copy_from_bbox(self.fig.bbox)

            self.points2.set_visible(True)
            self.blit()


    def blit(self):
        """
        Efficiently update the figure, without needing to redraw the
        "background" artists.
        """
        self.fig.canvas.restore_region(self.background)
        self.ax.draw_artist(self.points)
        self.ax.draw_artist(self.points2)
        self.fig.canvas.blit(self.fig.bbox)


    def drawOn2(self): # Frequency response
        if self.flag1== 0 : #before browse
            self.num, self.den = zpk2tf(self.zero, self.poles, 1)
            #print (self.num.size)
            #print (self.den.size)
            w, self.h = freqz(self.num, self.den)

        if self.flag1 == 1 : #after browse
            self.num, self.den = zpk2tf(self.zero, self.poles, 1)

            w, self.h = freqz(self.num, self.den, worN=self.yfourier.size)


        self.drawing2.clear()

        #test =np.angle(self.h)

        h_dB = 20 * log10(np.abs(self.h))
        self.drawing2.plot(w / max(w), h_dB)
        self.drawing2.set_xlabel('Normalized frequency', fontsize=9)
        self.drawing2.set_ylabel('Amplitude[dB]', fontsize=9)

        h_Phase = np.unwrap(np.arctan2(np.imag(self.h), np.real(self.h)))




        self.drawing3.clear()
        self.drawing3.plot(w / max(w),h_Phase)
        #self.drawing4.set_title('Phase')
        self.drawing3.set_xlabel('Normalized Frequency', fontsize=9)
        self.drawing3.set_ylabel('Phase (radians)', fontsize=9)
        #plt.gcf().subplots_adjust(bottom=0.15)
        #self.drawing2.plot(w / pi, 20 * log10(abs(h)))
        #self.drawing2.set_xscale('log')
        # self.drawing2.set_xlim([0, 10000])
        # self.drawing2.set_ylim([0, 100000])
        self.canvas2.draw()



    def drawOn3(self): #Before --- time , fourier magnitude , fourier phase
        self.drawing4.clear()

        self.drawing4.plot(self.time,self.signal)
        self.drawing4.set_xlabel('Time', fontsize=9)
        self.drawing4.set_ylabel('Amplitude', fontsize=9)
        self.drawing4.set_xlim([0, 0.01])
        self.drawing5.clear()
        self.drawing5.plot(self.xfourier, self.yfourier_mag)
        self.drawing5.set_xlabel('Frequency', fontsize=9)
        self.drawing5.set_ylabel('Amplitude', fontsize=9)
        self.drawing55.clear()
        self.drawing55.plot(self.xfourier, self.yfourier_phase)
        self.drawing55.set_xlabel('Frequency', fontsize=9)
        self.drawing55.set_ylabel('Phase', fontsize=9)

        self.drawing55.set_xlim([0,55])
        #self.drawing.set_ylim([0, 10000])
        self.canvas3.draw()
    def drawOn4(self): #  offline after
        #xfourier2 = fftfreq(self.signal.size, d=self.time[1] - self.time[0])
        spectrum = fft(self.signal)


        self.zico = spectrum

        for i in self.h:
            self.zico[i]=spectrum[i] * self.h[i]
        mag = np.abs(self.zico)
        pha = np.angle(self.zico)


        #h_Phase = np.unwrap(np.arctan2(np.imag(self.h), np.real(self.h)))
        #for i in h_Phase:
            #self.zico_phase[i]=yfourier_phase[i] * h_Phase[i]

        self.cut_signal = ifft(self.zico)



        #self.drawing6.hold(False)
        self.drawing6.clear()
        self.drawing6.plot(self.time,self.cut_signal)
        self.drawing6.set_xlabel('Time', fontsize=9)
        self.drawing6.set_ylabel('Amplitude', fontsize=9)
        self.drawing6.set_xlim([0, 0.01])
        self.drawing7.clear()
        self.drawing7.plot(self.xfourier, mag)
        self.drawing7.set_xlabel('Frequency', fontsize=9)
        self.drawing7.set_ylabel('Amplitude', fontsize=9)
        self.drawing77.clear()
        self.drawing77.plot(self.xfourier, pha)
        self.drawing77.set_xlabel('Frequency', fontsize=9)
        self.drawing77.set_ylabel('Phase', fontsize=9)
        self.drawing77.set_xlim([0,55])
        #self.drawing.set_ylim([0, 10000])
        self.canvas4.draw()
        scaled = np.int16(self.cut_signal / np.max(np.abs(self.cut_signal)) * 32767)

        wav.write('test2.wav', 44100, scaled)

        music = pyglet.resource.media('test2.wav')
        music.play()

        pyglet.app.run()

    def drawOn5(self): #online section
        self.drawing8.clear()

        self.drawing8.plot(self.time,self.f)
        self.drawing8.set_xlabel('Time', fontsize=9)
        self.drawing8.set_ylabel('Amplitude', fontsize=9)
        self.drawing8.set_xlim([0, 0.01])
        self.drawing9.clear()
        self.drawing9.plot(self.xfourier, self.f_mag)
        self.drawing9.set_xlabel('Frequency', fontsize=9)
        self.drawing9.set_ylabel('Amplitude', fontsize=9)
        self.drawing10.clear()
        self.drawing10.plot(self.xfourier, self.f_phase)
        self.drawing10.set_xlabel('Frequency', fontsize=9)
        self.drawing10.set_ylabel('Phase', fontsize=9)
        #self.drawing10.set_xlim([0,55])
        #self.drawing.set_ylim([0, 10000])
        self.canvas5.draw()

    def online(self):
        y1 = []
        y2 = []
        y = []

        for i in range(0, self.signal.size):
            e = 0
            for n in range(0, self.num.size):
                if i -n < 0 :
                    t = 0
                    e += t
                else :
                    t = self.num[n] * self.signal[i - n]
                    e += t

            y1.append(e)

            e2 = 0
            for d in range(1, self.den.size):
                if i - n < 0:
                    t2 = 0
                    e2 -= t2
                else :
                    t2 = self.den[d] * y[i - d]
                    e2 -= t2

            y2.append(e2)

            t3 = y1[i] + y2[i]
            y.append(t3)

        self.f = np.array(y)


        self.On = fft(self.f)

        self.f_mag = np.abs(self.On)

        self.f_phase = np.angle(self.On)

        self.drawOn5()
        scaled = np.int16(self.f / np.max(np.abs(self.f)) * 32767)

        wav.write('test.wav', 44100, scaled)

        music = pyglet.resource.media('test.wav')
        music.play()

        pyglet.app.run()



    def browse_txt(self):

        filepath = QtGui.QFileDialog.getOpenFileName(self, 'Single File', "C:\Users\Hanna Nabil\Desktop",'*.txt')



        with open(filepath, "r") as f:
            content = f.readlines()
        content = [x.strip() for x in content]

        if self.radioButton.isChecked() == True:
            index = 0
            while index < len(content):
                self.x = float(content[index])
                self.y = float(content[index + 1])
                self.add_point()
                index += 2
        if self.radioButton_2.isChecked() == True:
            index = 0
            while index < len(content):
                self.x2 = float(content[index])
                self.y2 = float(content[index + 1])
                self.add_point()
                index += 2
    def browse_wav(self):
        self.flag1=1

        filepath = QtGui.QFileDialog.getOpenFileName(self, 'Single File', "C:\Users\Hanna Nabil\Desktop",'*.wav')
        f= str(filepath)
        if f != "":
            spf = wave.open(f, 'r')
        import contextlib

        with contextlib.closing(wave.open(f, 'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
            print "Duration is " , duration

        # Extract Raw Audio from Wav File
        self.signal = spf.readframes(-1)
        self.signal = np.fromstring(self.signal, 'Int16')
        self.fs = spf.getframerate()
        print "Sampling Rate is " ,self.fs

        # If Stereo
        if spf.getnchannels() == 2:
            print 'Just mono files'
            sys.exit(0)
        print (self.signal.size)
        #self.time = np.linspace(0, len(self.signal) / fs, num=len(self.signal))
        self.time = np.linspace(0, duration, self.fs * duration)

        self.xfourier = fftfreq(self.signal.size, d=self.time[1] - self.time[0])

        self.yfourier= fft(self.signal)
        self.yfourier_mag = np.abs(self.yfourier)

        self.yfourier_phase = np.angle(self.yfourier)

        #self.test = np.unwrap(np.arctan2(np.imag(spectrum), np.real(spectrum)))

        self.zico = self.yfourier

        self.cut_signal = ifft(self.zico)



        self.drawOn3()







    def file_save_txt(self):


        name = QtGui.QFileDialog.getSaveFileName(self, 'Save Point', "C:\Users\Hanna Nabil\Desktop", '*.txt')



        file = open(name, "w")

        file.write(str(self.x) + "\n")
        file.write(str(self.y))
        file.close()



if __name__ == '__main__':
    import sys
    from PyQt4 import QtGui
    import numpy as np

    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
