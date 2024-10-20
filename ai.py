import os
import subprocess
import sys

# Function to install packages if not already installed
def install(package):
    """Install a package using pip."""
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

# List of required packages
required_packages = ["ollama"]

# Check and install required packages
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"Package '{package}' not found. Installing...")
        install(package)
        print(f"Package '{package}' installed successfully.")
    else:
        print(f"Package '{package}' is already installed.")

# Import the ollama library after ensuring it's installed 
import ollama

# Initialize the Ollama client with the specified server URL
ollama_client = ollama.Client(host="https://ladybird-arriving-egret.ngrok-free.app")

# Define the model name to be used
model_name = "kaedeaiV2"  

def main():
    """
    Main function for the Kaede AI interface.
    This function handles user input and generates responses from the AI model.
    It streams the responses in real-time, providing a dynamic chat experience.
    """

    print("Welcome to the Kaede AI Interface!")
    print(f"Currently using model: {model_name}")
    print("\nType your message and press Enter. Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Exiting the chat. Goodbye!")
            break

        # Generate a response from the model using streaming
        stream = ollama_client.chat(
            model=model_name,
            messages=[{'role': 'user', 'content': user_input}],
            stream=True,
        )

        # Print the streamed response from the model
        print("Kaede AI: ",end='', flush=True)
        for chunk in stream:
            # Each chunk contains a part of the AI's response
            print(chunk['message']['content'], end='', flush=True)
        print()  # Add a newline after the response

if __name__ == "__main__":
    main()
