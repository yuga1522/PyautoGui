import pyautogui
import pyperclip
import time
import os
import schedule

# ============ CONFIGURATION ============
contacts = ["Bonda Tea", "Thai kelavi"]   # 👈 Add all contact names here
message = "Good Morning 🌞"
search_bar = (126, 146)          # 👈 Replace with your WhatsApp search bar coordinates
# ======================================

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.2


def send_message(contact, msg):
    """Send a message to a WhatsApp contact"""
    # Step 1: Click search bar
    pyautogui.click(search_bar)
    time.sleep(1)

    # Step 2: Type contact name
    pyperclip.copy(contact)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1.5)

    # Step 3: Open chat
    pyautogui.press('Tab')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(1.5)

    # Step 4: Type and send message
    pyperclip.copy(msg)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(1)

    print(f"✅ Sent '{msg}' to {contact}")


def send_good_morning():
    """Send Good Morning to all contacts"""
    print("☀️ Sending Good Morning messages...")
    os.system("start whatsapp:")  # open WhatsApp Desktop
    time.sleep(5)  # wait for app to load

    for name in contacts:
        send_message(name, message)

    print("🎉 All messages sent successfully!")


# ============ DAILY SCHEDULE ============
# Schedule the task every day at 6:00 AM
schedule.every().day.at("6:15").do(send_good_morning)

print("⏰ WhatsApp Good Morning scheduler running...")

# Keep script running forever
while True:
    schedule.run_pending()
    time.sleep(30)
