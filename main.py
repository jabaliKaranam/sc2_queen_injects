import sys
import time
import pyautogui
import configparser
import pytesseract
from PIL import Image, ImageOps
import psutil
import tkinter
from tkinter import messagebox
from playsound import playsound



hatchCount = 1
config = configparser.ConfigParser()
config.read("app.config")
tesseract_location = config["data"]["tesseract_location"]
image_name = config["data"]["image_name"]
hatchery_hotkey = config["data"]["hatchery_hotkey"]
queen_hotkey = config["data"]["queen_hotkey"]
queen_injcet_hotkey = config["data"]["queen_injcet_hotkey"]
cycle_base_hotkey = config["data"]["cycle_base_hotkey"]
inject_interval = config["data"]["inject_interval"]
x_start = config["data"]["x_start"]
x_offset = config["data"]["x_offset"]
continous_run = config["data"].getboolean("auto_run_continuous")

pytesseract.pytesseract.tesseract_cmd = tesseract_location


def getHatchCount(imgLoc):
    thresh = 50
    img3 = getBWImg(imgLoc, thresh)
    # img3.show()
    hatchCount = pytesseract.image_to_string(img3,
                                             config=('-l eng --oem 3 --psm 10 -c tessedit_char_whitelist=0123456789'))
    if hatchCount != '' and int(hatchCount) >= 2:
        return int(hatchCount)
    threshes = [60, 70, 80, 90, 100, 110]
    hc = []
    for th in threshes:
        img3 = getBWImg(imgLoc, th)
        hatchCount = pytesseract.image_to_string(img3,
                                                 config=(
                                                     '-l eng --oem 3 --psm 10 -c tessedit_char_whitelist=0123456789'))
        # print(hatchCount, th)
        if hatchCount != '':
            hc.append(int(hatchCount))
    return max(hc)


def getBWImg(imgLoc, thresh):
    img = Image.open(imgLoc)
    fn = lambda x: 255 if x > thresh else 0
    # img2 = ImageOps.grayscale(img)
    img3 = img.convert('L').point(fn, mode='1')
    return img3


def main():
    imgLoc = image_name
    # pyautogui.screenshot(imgLoc, region=(1035, 830, 30, 20))
    # print("sc1")
    # pyautogui.screenshot(imgLoc + ".png", region=(556, 830, 30, 20))

    hatch_img_postion = int(x_start) + (int(x_offset) * (int(hatchery_hotkey) - 1))
    # pyautogui.moveTo(hatch_img_postion, 830)
    pyautogui.screenshot(imgLoc, region=(hatch_img_postion, 830, 30, 20))
    # pyautogui.moveTo(591, 830)
    # pyautogui.screenshot(imgLoc, region=(1005, 830, 60, 20))
    # pyautogui.screenshot(imgLoc, region=(1068, 822, 64, 34))
    hatchCount = getHatchCount(imgLoc)
    print("Hatch Count : ", hatchCount)
    inject(hatchCount)

def inject(hatchCount):
    print("Initiate inject")
    if(hatchCount >= 15):
        print("Error in process. Detected " + str(hatchCount) +" bases")
        sys.exit()
    try:
        # Center mouse on screen
        screenWidth, screenHeight = pyautogui.size()
        pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
        pyautogui.move(0, -50)
        # Move screen to a hatchery
        pyautogui.press(hatchery_hotkey)
        pyautogui.press(hatchery_hotkey)
        # Select Queen group
        pyautogui.press(queen_hotkey)
        for i in range(int(hatchCount)):
            # Inject
            pyautogui.hotkey(cycle_base_hotkey, queen_injcet_hotkey)
            pyautogui.click()
            time.sleep(float(inject_interval))
    except Exception as e:
        print(e)
    print("inject done")


if __name__ == "__main__":
    if "SC2_x64.exe" or "SC2_x32.exe" in (p.name().lower() for p in psutil.process_iter()):
        if(continous_run):
            while(True):
                playsound("beep-07a.wav")
                print("Found Starcraft 2. Initiating inject sequence continously")
                main()
                time.sleep(30)
        else:
            print("Found Starcraft 2. Initiating inject sequence")
            main()
    else:
        tkinter.Tk().geometry("100x100")
        messagebox.showerror(title="Error", message="Game not found!")
