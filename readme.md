Code Script to auto inject hatcheries
#WARNING: THIS MAY BE ILLEGAL TO USE ON THE LADDER. USE AT YOUR OWN PERIL. I TAKE NO RESPONSIBILITY FOR ANYTHING THIS CODE DOES.
##Installation

Install Tesseract. Follow instructions found here https://github.com/UB-Mannheim/tesseract/wiki

Copy the install location into app.config

Provide a location for the code to store an image for processing.
The script only stores 1 image and will keep overwriting it.

Update the rest of app.config as per your preferences.

x_start & x_offset may need to updated based on your specific screen size and resolution

Install the packages in requirements.txt

WARNING: Enabling the auto run continuous option can and probably will result in the program running forever.
If you move your mouse to the corner of the screen, the 
In the case you do enable it, alt tabbing out of the game and waiting for 30 seconds or closing the game should work.
A double beep sound is played just before the inject cycle starts to notify you.


##Usage
Recommendation is to use a hotkey to bind the running of the script to a keyboard/mouse hotkey

Use run_injects.bat as the "application" to bind to the hotkey.

The batch file produces a log which might be useful in fixing any issues.

