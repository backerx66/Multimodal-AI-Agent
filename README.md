# Multimodal AI Agent for Web Research & Stock Insights  

This project shows how to build a multimodal AI agent that combines large language models (LLMs) with domain-specific tools for both **web research** and **financial analysis**. The agents are powered by the Groq API with **LLaMA-3.3-70B**, and make use of **DuckDuckGo** for real-time web results and **Yahoo Finance tools** for market data.  

---

## Abstract  
This work introduces a multimodal AI system designed to fetch, analyze, and present information from different sources in one place. By combining LLaMA-3.3-70B with DuckDuckGo search and Yahoo Finance APIs, the agent can track stocks, summarize company news, and provide analyst perspectives. The output is formatted in markdown, making it structured and easy to read.  

The goal is to explore how AI agents can integrate multiple data sources to support decision-making in fast-moving fields like finance and research.  

---

## Introduction  
As LLMs evolve, there is growing interest in combining them with tools that can directly pull real-world data. Such “multimodal agents” bridge natural language processing with external APIs, enabling smarter and more context-aware results.  

This project focuses on:  
- Running live web searches for relevant information.  
- Collecting financial metrics such as stock price, fundamentals, and news.  
- Returning clear and structured answers in markdown.  

---

## Methodology  

### System Architecture  
The solution is composed of three key agents:  
1. **Web Agent** – Queries DuckDuckGo for live web data.  
2. **Finance Agent** – Uses YFinanceTools to get stock market insights and company updates.  
3. **Coordinator Agent** – Orchestrates both agents and outputs unified, clean results.  

### Tools & Technologies  
- **LLaMA-3.3-70B (Groq API)** – Core large language model.  
- **DuckDuckGo API** – Web search integration.  
- **YFinanceTools** – Stock and company data.  
- **PHI Framework (Python)** – Used to build and configure agents.  

---

## Implementation  
The agents are built in Python with the PHI framework. Each agent is initialized with specific instructions and the right tools.  
> The full implementation can be found in the `code/` folder.  

---

## Results  
When tested with queries like *“Tesla stock update”*, the agent produced outputs combining:  
- Tables of stock price data.  
- Bullet-point news summaries.  
- Source-backed links.  

This demonstrates its ability to merge multiple data types into a single, structured response.  

---

## Discussion  
**Strengths**  
- Flexible: works across different tasks without retraining.  
- Extensible: new tools can be plugged in (e.g., healthcare, law).  

**Limitations**  
- Dependent on external API accuracy.  
- Real-time results may vary with network/API response speed.  

---

## Applications  
- **FinTech**: Automated market analysis for investors.  
- **Research**: Fast, source-backed information gathering.  
- **Business Intelligence**: Real-time insights for decision-makers.  

---

## Future Work  
- Add more domain-specific tools.  
- Upgrade to newer LLMs as they become available.  
- Personalization so users can set their own preferences.  

---

## Conclusion  
This project demonstrates a multimodal AI agent that blends **LLMs with web and financial data sources**. By leveraging LLaMA-3.3-70B alongside DuckDuckGo and Yahoo Finance, it shows the potential of such systems to enhance research and decision-making. With future improvements, these agents could become powerful everyday tools across industries.  
