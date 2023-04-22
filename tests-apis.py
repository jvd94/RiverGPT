import pandas as pd
import openai
from dotenv import load_dotenv
import os






if __name__ == '__main__':
    load_dotenv()
    OPEN_AI_KEY = os.getenv("OPENAI_API_KEY")
    print(OPEN_AI_KEY)