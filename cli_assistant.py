from gemini_client import *

def main():
  client = GeminiClient()

  while True:
      user_input = input("What's your question today? ").strip()

      if user_input.lower() == "exit":
        print("Goodbye!")
          break

    response = client.generate_response(user_input)
    print("AI: {response}")

if __name__ == "__main__":
  main()