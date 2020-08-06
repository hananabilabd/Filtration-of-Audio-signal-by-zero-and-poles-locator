# Filtration-of-Audio-signal-by-zero-and-poles-locator

The purpose of this desktop application using Python and PyQt is Filtration of audio signals by zero and poles graphical manipulation and plotting the Fourier magnitude and phase in both 2 cases before and after filtration.

## It is also useful to show the difference between online and offline filtration:
   * In online( real-time) mode we use digital filters.
   * In offline mode we use Fourier transform to manipulate magnitude.
## Application usage:
  * First you select the filter you want by drawing zero and poles into the unit circle.
  * Then you browse the .wav file we want to apply the filter on.
  * **Offline mode(Fourier transform):**
  
      * You can apply offline mode on the selected .wav file.
      * Three Graphs for offline filtration before manipulation will appear after browsing for the .wav file:
        * One for time domain (amplitude vs time).
        * One for magnitude in Fourier transform(frequency vs amplitude).
        * One for phase in Fourier transform(frequency vs phase).
  * Application will apply the offline filter by converting the .wav signal to Fourier then apply the frequency response on it
  * You can hear the sound after applying filter.
  * **Online Mode (Digital filters)**:
  
      * You also can apply online mode on the selected .wav file (apply digital filters without convert the signal to Fourier).
      * Three Graphs for Online Filtration:
        * One for time domain (amplitude vs time ),
        * One for Magnitude in Fourier transform (frequency vs amplitude).
        * One for phase in Fourier transform (frequency vs phase).





[youtube video](https://www.youtube.com/watch?v=L0CDQk00URU)
