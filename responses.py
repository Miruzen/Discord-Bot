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
  p_message = message.lower()
  for intent in Data_intent["intents"]:
    if any(pattern in p_message for pattern in intent["patterns"]):
      answer = random.choice(intent["responses"])
      print(f"Matched intent: {intent['tag']}")  # Print matched intent for debugging
      return answer
    if p_message == "shut" :
      return exit () 
  return "I didn't understand what you wrote."

if Data_intent:
    while True:
        user_input = input("You: ")
        response = get_response1(user_input)
        print("Bot: ", response)
        if user_input == "shut":
            break
else:
    print("Failed to load intents.json. Exiting program.")

