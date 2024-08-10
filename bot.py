import pyautogui
import time
import pyperclip
import google.generativeai as genai
import key

# Directly configure the API key for this project

# Configure the API key for the Generative AI model
genai.configure(api_key=key.api_key)

# Initialize the model with the API key specifically for this instance
model = genai.GenerativeModel('gemini-1.5-flash')

def is_last_message_from_sender(chat_log, sender_name = "Suryaansh(MITb)"):
    # Step 1: Split the copied text into individual messages
    messages = chat_log.strip().split('/2024] ') [-1]
    if sender_name in messages:
        return True
    else:
        return False

    

# Step 1: Click on an icon at (581, 1161)
pyautogui.click(581, 1161)
# Wait for a moment to ensure the action completes
time.sleep(1)

# while True: # if we need it to continously text

    # Step 2: Click and hold at the start point (836, 221)
pyautogui.moveTo(836, 221)
pyautogui.mouseDown()

# Step 3: Drag to the end point (1791, 991)
pyautogui.moveTo(1791, 991, duration=2)  # Adjust the duration as needed
pyautogui.mouseUp()

# Step 4: Copy the selected text to the clipboard
pyautogui.hotkey('ctrl', 'c')

# Wait for the clipboard to update
time.sleep(1)

# Step 5: Unselect the text by clicking elsewhere
pyautogui.click(836, 221)  # Click at an arbitrary location to unselect text

# Step 6: Store the copied text in a variable
chat_history = pyperclip.paste()

# Print the copied text to verify
print("Copied text:", chat_history)

    # if is_last_message_from_sender(chat_history):

system_role = "you are a person named Siddhant who speaks hindi as well as english but prefer to text in English . You are a 3rd year Computer science student. Analize chat history and reply like Siddhant would (text message only)"
user_role = chat_history
response = model.generate_content(f"{system_role}. {user_role} ")
a =response.text # actual response
pyperclip.copy(a)

# Step 7: Click on the text box to focus it
pyautogui.click(1212, 1084)  # Adjust these coordinates to your text box location
time.sleep(1)

# Step 8: Paste the text
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

# Step 9: Press Enter to send the text
pyautogui.press('enter')


