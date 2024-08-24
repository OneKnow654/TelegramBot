import os
import google.generativeai as genai
from dotenv import load_dotenv 

load_dotenv()

API =os.getenv("google_api")
genai.configure(
    api_key=API
)

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def Ask(text:str):
    if text.strip() == "":
     return "send some question or query "
    
    reply = chat.send_message(text).text
    return reply

def default_reply(text:str):
   st = "give me a formal reponses for this "+text.strip()
   try:
     return chat.send_message(st).text
   except Exception :
     return "sorry ,can't answer this question"
# while True:
#     question = input("Enter your question")

#     if(question.strip() == ""):
#         break
#     reponse = chat.send_message(question)
#     print(f"\nBot : {reponse.text}\n")
#     print(f"token left {reponse.usage_metadata.total_token_count} out of {reponse.usage_metadata.candidates_token_count}\n")