from dotenv import load_dotenv
import os
load_dotenv()
api_key=os.getenv("API_KEY")
print("My API_KEY is:",api_key)
