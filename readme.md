Code Script to auto inject hatcheries

# WARNING: THIS MAY BE ILLEGAL TO USE ON THE LADDER. USE AT YOUR OWN PERIL. I TAKE NO RESPONSIBILITY FOR ANYTHING THIS CODE DOES.

## Installation

Install Tesseract. Follow instructions found here https://github.com/UB-Mannheim/tesseract/wiki

If you are looking for the executable(exe) file, download the dist folder.

Copy the folder to any location.

### Updating app.config

Copy the install location of Tesseract into app.config

Update the rest of app.config as per your preferences.
app.config has descriptions for each value to help.
Under normal circumstances, you should not need to update most values.

x_start & x_offset may need to be updated based on your specific screen size and resolution

If you are using the source code, install the packages in requirements.txt
If you are using the exe file, you dont need to install the packages

WARNING: Enabling the auto run continuous option can and probably will result in the program running forever.
If you move your mouse to the corner of the screen, the 
In the case you do enable it, alt tabbing out of the game and waiting for 30 seconds or closing the game should work.
A double beep sound is played just before the inject cycle starts to notify you.


## Usage

### For the exe file
Recommendation is to use a hotkey bind to the exe file.

Start the game.

Hit the hotkey

### For the source code
Recommendation is to use a hotkey to bind the running of the script to a keyboard/mouse hotkey

Use run_injects.bat as the "application" to bind to the hotkey.

The batch file produces a log which might be useful in fixing any issues.

During the injection sequence, if you move your mouse to the corner of the screen, the application will stop. This is a safety feature.
