import pyautogui
import time
import os
import pyperclip

# ==============================
# CONFIGURATION
# ==============================
group_name = "Bangaru family"
message = "One week completed - Task completed for PyautoGui"

# 🧭 Replace this with your search bar coordinates
search_bar = (126, 146)  # Example: update with your actual values

# ==============================
# START
# ==============================
pyautogui.FAILSAFE = True  # move mouse to top-left to stop

# Step 1: Open WhatsApp Desktop
os.system("start whatsapp:")  # For Windows
print("Opening WhatsApp...")
time.sleep(3)  # Give WhatsApp time to load fully

# Step 2: Click on the search bar
pyautogui.click(search_bar)
time.sleep(1)

# Step 3: Type the group name using clipboard (faster and avoids missed letters)
pyperclip.copy(group_name)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)

# Step 4: Try to move to the first result and open it
pyautogui.press("tab")    # Move focus to search results
time.sleep(0.5)
pyautogui.press("enter")  # Open chat
time.sleep(2)

# Step 5: Type and send message
pyperclip.copy(message)
pyautogui.hotkey("ctrl", "v")
time.sleep(0.5)
pyautogui.press("enter")

print("✅ Message sent successfully!")
