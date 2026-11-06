import pyautogui
import pyperclip
import webbrowser
import time
import os
from datetime import datetime

pyautogui.FAILSAFE = True
pyautogui.PAUSE =  1

SAVE_FOLDER = os.path.join(
    os.path.expanduser("~"),
    "Desktop",
    "Daily_Reports"
)

os.makedirs(SAVE_FOLDER, exist_ok=True)

current_time=datetime.now()
date_time = current_time.strftime("%Y-%m-%d  %H:%M:%S")
current_date = current_time.strftime("%Y-%m-%d")

excel_filename = f"daily_report_{current_date}.xlsx"
screenshot_filename = f"daily_report_screenshot_{current_date}.png"

excel_path = os.path.join(SAVE_FOLDER,excel_filename)
screenshot_path= os.path.join(SAVE_FOLDER,screenshot_filename)


#step 1: opening Chrome:

print("Opening Chrome...")
time.sleep(2)
pyautogui.hotkey('win','r',interval=0.1)
time.sleep(1)
pyautogui.write('chrome',interval=0.15)
time.sleep(1)
pyautogui.press('enter')
time.sleep(3)
print("Selecting Chrome Profile 1...")

pyautogui.click(x=635, y=595)

time.sleep(2)
pyautogui.hotkey('ctrl','t',interval=0.1)
time.sleep(1)
pyautogui.write("https://wttr.in/Coimbatore?format=3")
time.sleep(1)
pyautogui.press('enter')
time.sleep(5)

# webbrowser.open(
#     "https://www.accuweather.com/en/in/coimbatore/206673/weather-forecast/206673?type=locality"
# )



# step 2: COPY WEATHER INFORMATION:
print("Fetching weather information...")

pyautogui.hotkey("ctrl", "a" , interval=0.10)
time.sleep(1)

pyautogui.hotkey("ctrl", "c", interval=0.1)
time.sleep(2)

weather_data = pyperclip.paste().strip()

if not weather_data:
    weather_data = "Weather information unavailable"

print("Weather Data:", weather_data)

#step3:prepare comment
# STEP 3: PREPARE COMMENT

if "🌧️" in weather_data or "rain" in weather_data.lower():
    comment = "Carry an umbrella today."

elif "☀️" in weather_data or "sun" in weather_data.lower():
    comment = "Good for outdoor activities."

elif "☁️" in weather_data or "cloud" in weather_data.lower():
    comment = "Suitable for a relaxed day."

else:
    comment = "Daily weather status recorded."

print("Weather Comment:", comment)

#step4 open workbook excel
print("Opening Microsoft Excel...")

pyautogui.hotkey("win", "r")
time.sleep(2)

pyautogui.write("excel", interval=0.1)
pyautogui.press("enter")

time.sleep(10)
# Open a new blank workbook
pyautogui.hotkey("ctrl", "n")
print("Creating new Excel workbook...")

pyautogui.click(x=350, y=185)

time.sleep(5)

print("Blank workbook opened successfully!")

#step6 :Enter Report Data:
# Create headings
headers = "Date & Time\tFetched Information\tComment"

# Create data row
data = f"{date_time}\t{weather_data}\t{comment}"

# Paste headings into Excel
pyperclip.copy(headers)
pyautogui.hotkey("ctrl", "v")

time.sleep(2)

# Move to the next row
pyautogui.press("down")
pyautogui.press("home")

# Paste report data
pyperclip.copy(data)
pyautogui.hotkey("ctrl", "v")

time.sleep(3)

#Step 7: format excel sheet:
# Select the first row and make headings bold
pyautogui.hotkey("ctrl", "home")
pyautogui.hotkey("shift", "end")
pyautogui.hotkey("ctrl", "b")

# Adjust column widths
pyautogui.hotkey("ctrl", "a")
pyautogui.hotkey("alt", "h")
pyautogui.press("o")
pyautogui.press("i")

time.sleep(3) 


# STEP 8: SAVE EXCEL FILE

print("Saving Excel report...")

# Open Save As dialog
pyautogui.press('f12')

time.sleep(4)

# Enter file path in the File name box
pyperclip.copy(excel_path)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'v')

time.sleep(2)

# Save the file
pyautogui.press('enter')

time.sleep(5)

print("Excel file saved successfully!")

#step 9: take screen shot
print("Taking screenshot...")
time.sleep(3)
# Capture the completed Excel screen
screenshot = pyautogui.screenshot()
screenshot.save(screenshot_path)

#Completed 
print("\n================================")
print("DAILY REPORT COMPLETED!")
print("================================")

print("Weather:", weather_data)
print("Date & Time:", date_time)
print("Comment:", comment)

print("\nExcel File:", excel_path)
print("Screenshot:", screenshot_path)

print("\nAll tasks completed successfully!")