from google import genai
import os
import sys
from google.genai import types
import gemini_config as config
    
class GeminiClient:
    def __init__(self):
        gemini_api_key = config.GEMINI_API_KEY
        if gemini_api_key is None:
            print("Your API key is not set correctly!")
            sys.exit()
        else:
            self.client = genai.Client(api_key=gemini_api_key)
            self.chat_history = []

    def generate_response(self, user_input):
        if self.chat_history is None:  
            return "AI Assistant is not configured correctly"
    
        system_instruction = "You are an AI assistant. Answer the user's questions accurately and politely."
    
    # Build full conversation
        contents = [
            types.Content(
            role="system",
            parts=[types.Part.from_text(text=system_instruction)]
        )
        ] + self.chat_history + [
            types.Content(
                role='user',
                parts=[types.Part.from_text(text=user_input)]
            )
        ]


            # TO DO: Use the client's chat history & system instruction to prompt Gemini
        response = self.client.models.generate_content(
            model="gemini-1.5-flash",
            contents=self.chat_history,
            config = types.GenerateContentConfig(system_instruction=system_instruction)
            system_instruction=system_instruction
        )

        x = self.client.models.generate_content()

            # TO DO: Add the response text from Gemini to the client's chat history
        response_text = response.text
        self.chat_history.append(
            types.Content(
            role="model",
            parts=[types.Part.from_text(text=response_text)]
        )
    )

            # TO DO: Return the response text from Gemini
        return response_text