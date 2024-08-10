# testing gemini on texts
import key
# pip install -q -U google-generativeai
import google.generativeai as genai

# Directly configure the API key for this project

# Configure the API key for the Generative AI model
genai.configure(api_key=key.api_key)

# Initialize the model with the API key specifically for this instance
model = genai.GenerativeModel('gemini-1.5-flash')

history = '''
Copied text: [10:45 pm, 7/8/2024] Sakshyam Patro: Bro insane
[10:46 pm, 7/8/2024] Sakshyam Patro: Bro Lmk if you free weekend     
[10:46 pm, 7/8/2024] Sakshyam Patro: Or weekday any time
[10:46 pm, 7/8/2024] Sakshyam Patro: Let’s do gmeet
[10:46 pm, 7/8/2024] Sakshyam Patro: I just wanna see the whole project and stuff
[10:46 pm, 7/8/2024] Sakshyam Patro: If that’s fine for you
[10:53 pm, 7/8/2024] Siddhant Ghosh: Arre I can bring my laptop      
[10:53 pm, 7/8/2024] Siddhant Ghosh: On 10th
[11:28 am, 8/8/2024] Siddhant Ghosh: Yea that also works tho
[11:32 am, 8/8/2024] Sakshyam Patro: Anything is cool
'''
system_role = "you are a person named Siddhant who speaks hindi as well as english but prefer to text in English . You are a 3rd year Computer science student. Analize chat history and reply like Siddhant would (text message only)"
user_role = history
response = model.generate_content(f"{system_role}. {user_role} ")
print(response.text)

