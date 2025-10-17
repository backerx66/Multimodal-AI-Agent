from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY", "your-groq-api")  
MODEL_ID = "llama-3.3-70b-versatile"

# Scout Agent - Web research specialist
scout_agent = Agent(
    name="scout",
    role="Explore the open web to gather relevant and recent information.",
    model=Groq(id=MODEL_ID, api_key=API_KEY),
    tools=[DuckDuckGo()],
    instructions=[
        "Always provide direct source links with your findings.",
        "Keep the summary short and highlight only useful details.",
        "Focus on the most recent news (last 7 days).",
        "Search for breaking news, earnings updates, and market sentiment."
    ],
    show_tool_calls=False,  # Clean output for production
    markdown=True,
)

# Market Agent - Financial data specialist  
market_agent = Agent(
    name="market_sage",
    role="Retrieve financial metrics, company updates, and analyst perspectives.",
    model=Groq(id=MODEL_ID, api_key=API_KEY),
    tools=[
        YFinanceTools(
            stock_price=True,
            stock_fundamentals=True,
            analyst_recommendations=True,
            company_news=True
        )
    ],
    instructions=[
        "ALWAYS retrieve and display analyst recommendations with specific numbers.",
        "Present data in clear, organized tables when possible.",
        "Include buy/hold/sell ratings with exact counts from multiple analysts.",
        "Show target prices, price-to-earnings ratios, and key financial metrics.",
        "If analyst recommendations are available, summarize the sentiment clearly.",
        "Include current stock price, market cap, and recent performance.",
        "If any data is missing, clearly state 'Data not available' and explain why."
    ],
    show_tool_calls=False,  # Clean output for production
    markdown=True,
)

# Navigator Agent - Coordination and synthesis
navigator = Agent(
    name="navigator", 
    role="Coordinate the Scout and Market Sage outputs into a comprehensive investor brief.",
    team=[scout_agent, market_agent],
    model=Groq(id=MODEL_ID, api_key=API_KEY),
    instructions=[
        "Create a professional investment brief by combining all agent outputs.",
        "MUST include a dedicated 'Analyst Recommendations' section with specific numbers.",
        "Structure the brief as follows:",
        "1) Executive Summary - Brief overview of current situation",
        "2) Key Financial Metrics - Table with current price, analyst ratings, target prices",
        "3) Analyst Recommendations - Detailed breakdown of buy/hold/sell ratings",
        "4) Recent Developments - Key news and market events from Scout",
        "5) Investment Highlights - 3-5 bullet points covering opportunities and risks",
        "6) Sources - Complete list of all sources with links",
        "",
        "Ensure analyst recommendation numbers are prominently displayed.",
        "Do not fabricate any data or sources.",
        "If analyst data is incomplete, explicitly mention what's missing and why.",
        "Format all tables clearly and use markdown formatting consistently."
    ],
    show_tool_calls=False,  # Clean output for production
    markdown=True,
)

def main():
    """
    Main function to run the Financial Agent analysis
    """
    print(" Financial Agent Analysis Starting...")
    print(" Analyzing Tesla (TSLA) with multi-agent system")
    print("-" * 60)
    
    try:
        # Run comprehensive analysis
        navigator.print_response(
            "Provide a comprehensive investment analysis of Tesla (TSLA) including:\n"
            "- Latest analyst recommendations with exact buy/hold/sell numbers\n" 
            "- Recent news headlines and market developments\n"
            "- Current stock price and key financial metrics\n"
            "- Target prices from analysts if available\n"
            "- Investment opportunities and risks\n"
            "\nMake sure to include specific analyst recommendation counts in a dedicated section.",
            stream=True
        )
        
    except Exception as e:
        print(f" Error during analysis: {str(e)}")
        print(" Please check your API key and internet connection.")
        
    print("\n" + "-" * 60)
    print(" Analysis Complete!")

if __name__ == "__main__":

    main()
