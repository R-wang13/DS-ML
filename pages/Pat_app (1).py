import os

# Install ngrok for tunneling
!pip install pyngrok -q
from pyngrok import ngrok

# Terminate any existing ngrok tunnels
ngrok.kill()

# Get ngrok authentication token from environment variable or user input
# You can get your auth token from https://ngrok.com/dashboard/authtokens
# and set it as an environment variable or uncomment the input line below.
NGROK_AUTH_TOKEN = os.environ.get("NGROK_AUTH_TOKEN", "YOUR_NGROK_AUTH_TOKEN") # Replace with your ngrok auth token if not set as environment variable
# if NGROK_AUTH_TOKEN == "YOUR_NGROK_AUTH_TOKEN":
#   NGROK_AUTH_TOKEN = input("Enter your ngrok auth token (from https://ngrok.com/dashboard/authtokens): ")

# Authenticate ngrok
ngrok.set_auth_token(NGROK_AUTH_TOKEN)

# Run Streamlit app and create a public URL
!streamlit run clean_app.py &>/dev/null& # Run Streamlit in background

# Wait for Streamlit to start and then get the public URL
import time
time.sleep(5) # Give Streamlit some time to start

public_url = ngrok.connect(8501)
print(f"Streamlit App URL: {public_url}")
