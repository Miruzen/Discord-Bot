import random
import json

def read_intents(intents_data):
  try:
    with open(intents_data, 'r') as file:
      data = json.load(file)
      return data
  except FileNotFoundError:
    print(f"Error: File '{intents_data}' not found.")
    return None

# Load intents data from the file
Data_intent = read_intents("intents.json")

def get_response1(message : str )-> str :
  p_message = message 
  for intent in Data_intent["intents"]:
    if any(pattern in p_message for pattern in intent["patterns"]):
      answer = random.choice(intent["responses"])
      print(f"Matched intent: {intent['tag']}")  # Print matched intent for debugging
      return answer
    if p_message == "shut" :
      return exit () 
  return "I didn't understand what you wrote , Access this drive to see command : https://drive.google.com/drive/folders/1q-ay7_QwgntvurYjeNC-KgRijvamwVj0?usp=sharing"

# if Data_intent:
#     while True:
#         user_input = input("You: ")
#         response = get_response1(user_input)
#         print("Bot: ", response)
#         if user_input == "shut":
#             break
#         if user_input == "/help " or "/Help" :
#             print ("Try typing [hey , bye , coding , program , ngoding , stok , organisasi]")
# else:
#     print("Failed to load intents.json. Exiting program.")

