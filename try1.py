import google.generativeai as genai

# Set the API key
genai.configure(api_key="AIzaSyCmVIQGMoY6gVPEwwfiE3dORcevd1uoKiw")

def chat_with_gemini(prompt):
    try:
        # Use the generate_message method
        response = genai.generate_message(
            model="models/chat-bison-001",  # A common model name
            messages=[{"author": "user", "content": prompt}]
        )
        
        # Extracting the assistant's reply from the response
        return response["messages"][0]["content"].strip()

    except Exception as e:
        return f"Error occurred: {str(e)}"

if __name__ == "__main__":
    while True:
        user_input = input("you: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        response = chat_with_gemini(user_input)
        print("chatbot: ", response)
