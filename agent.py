from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent,Browser, BrowserConfig
from pydantic import SecretStr
import os
from dotenv import load_dotenv
import asyncio
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Initialize the model
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(os.getenv('GEMINI_API_KEY')))
browser = Browser(
    config=BrowserConfig(
        # Specify the path to your Chrome executable
        chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',  # macOS path

    )
)
async def main():
    agent = Agent(
        task="help me to analyze current linked job page for me, because I try to apply for the jobs",
        llm=llm,
        browser=browser,

    )
    result = await agent.run()
    await browser.close()
    print(result)

asyncio.run(main())