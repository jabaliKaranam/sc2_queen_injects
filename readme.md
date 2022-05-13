##Code Script to auto inject hatcheries in Starcraft 2

# WARNING: THIS MAY BE ILLEGAL TO USE ON THE LADDER. USE AT YOUR OWN PERIL. I TAKE NO RESPONSIBILITY FOR ANYTHING THIS CODE DOES.

## Installation
### Download & Run as a windows application
#### Recomended for most users
Install Tesseract. Follow instructions found here https://github.com/UB-Mannheim/tesseract/wiki

If you are looking for the executable(exe) file, download the dist folder.

Copy the folder to any location.

### Updating app.config

Copy the install location of Tesseract into app.config

Update the rest of app.config as per your preferences.
app.config has descriptions for each value to help.
Under normal circumstances, you should not need to update most values.

x_start & x_offset may need to be updated based on your specific screen size and resolution

#### Measuring x_start & x_offset

Use the sc2AutoInject_MousePositionHelper tool. Download from here () and run it.

It will show a small window with the X & Y Coordinates of your mouse.

Launch Starcraft 2 in Fullscreen Windowed mode

Start a throwaway game (against an AI).

Create control group 1 and 2

Position your mouse pointer between the Control Group 1 Icon and the Control Group 1 Unit Count

Note down the numbers shown in sc2AutoInject_MousePositionHelper

Do the same for Control Group 2.

The X Coordinate (first number) you got from Control Group 1 will be the x_start value

![get_x_coords](https://user-images.githubusercontent.com/84337220/168389483-874f2d9e-aacf-41d8-b3e6-3e817c57c77b.png)
![get_x_coords2](https://user-images.githubusercontent.com/84337220/168389489-0c7119ab-a92d-4610-8f63-cad22e505d0b.png)


The difference between the X Coordinates of Group 1 & 2 will be the x_offset value

_If you are using the source code, install the packages in requirements.txt

If you are using the exe file, you dont need to install the packages_

WARNING: Enabling the auto run continuous option can and probably will result in the program running forever.
If you move your mouse to the corner of the screen, the 
In the case you do enable it, alt tabbing out of the game and waiting for 30 seconds or closing the game should work.
A double beep sound is played just before the inject cycle starts to notify you.


## Usage

### For the exe file
Recommendation is to use a hotkey bind to the exe file.

Start the game in windowed fullscreen mode

Hit the hotkey and watch the magic

_Note: You need to have at least 2 hatcheries and 1 queen bound to the hotkeys specific in app.config_

### For the source code
Recommendation is to use a hotkey to bind the running of the script to a keyboard/mouse hotkey

Use run_injects.bat as the "application" to bind to the hotkey.

Start the game in windowed fullscreen mode

Hit the hotkey and watch the magic

_Note: You need to have at least 2 hatcheries and 1 queen bound to the hotkeys specific in app.config_

The batch file produces a log which might be useful in fixing any issues.

During the injection sequence, if you move your mouse to the corner of the screen, the application will stop. This is a safety feature.
