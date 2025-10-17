# Multi-Agent AI System for Web Research & Financial Insights  

This project demonstrates how to build a **multi-agent AI system** that combines large language models (LLMs) with **domain-specific tools** for both **web research** and **financial analysis**.  
The agents are powered by the **Groq API (LLaMA-3.3-70B)** and use **DuckDuckGo** for real-time web data and **Yahoo Finance tools** for market insights.  

---

## Abstract  
This work introduces a **multi-agent AI system** designed to fetch, analyze, and present information from multiple text-based sources in one place.  
By combining **LLaMA-3.3-70B** with **DuckDuckGo search** and **Yahoo Finance APIs**, the agents can track stock performance, summarize company news, and present analyst perspectives in a **structured markdown report**.  

The goal is to explore how multiple AI agents can collaborate and integrate diverse data sources to support decision-making in fast-moving domains like finance and research.  

---

## Introduction  
As large language models evolve, there is growing interest in **connecting them with external tools and APIs** to make them more useful in real-world contexts.  

This project focuses on:  
- Running **live web searches** to gather recent information.  
- Collecting **financial metrics** such as stock prices, company fundamentals, and analyst ratings.  
- Producing **clear, well-structured markdown reports** combining these insights.  

Although often described as "multimodal," this system currently operates in a **single modality (text)** — it processes and generates only textual information, but from multiple data sources.  

---

## Methodology  

### System Architecture  
The system is composed of three main agents:  
1. **Web Agent (Scout)** – Queries DuckDuckGo for live web data.  
2. **Finance Agent (Market Sage)** – Uses YFinanceTools to retrieve market data and analyst insights.  
3. **Coordinator Agent (Navigator)** – Orchestrates the other agents and produces a unified investment brief.  

### Tools & Technologies  
- **LLaMA-3.3-70B (Groq API)** – Core large language model.  
- **DuckDuckGo API** – For web search.  
- **YFinanceTools** – For stock and company data.  
- **PHI Framework (Python)** – For building and managing AI agents.  

---

## Discussion  

**Strengths**  
- **Collaborative**: multiple agents handle different tasks efficiently.  
- **Extensible**: new domain-specific tools can easily be added (e.g., healthcare, legal, education).  

**Limitations**  
- Operates in **text-only mode** (not multimodal).  
- Dependent on **external APIs** for data quality and availability.  
- Real-time results may vary based on network and API response time.  

---

## Applications  
- **FinTech**: automated market research for investors.  
- **Academic Research**: quick and source-backed information gathering.  
- **Business Intelligence**: real-time data summaries for decision-making.  

---

## Future Work  
- Add **visual outputs** (charts, graphs) for true multimodal capability.  
- Integrate **additional APIs** (news feeds, alternative data).  
- Add **user personalization** for preferred stocks or report formats.  

---

## Conclusion  
This project showcases a **multi-agent, text-based AI system** that integrates LLMs with real-world data sources like web search and financial APIs.  
By coordinating multiple specialized agents, it demonstrates how AI can deliver structured, actionable insights for research and decision-making.  
Future versions could expand to **true multimodal capabilities**, adding visual analytics and richer data representations.  
