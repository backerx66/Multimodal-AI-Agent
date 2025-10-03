# Multi-Agent AI System for Financial Research and Web Intelligence  

This project demonstrates a **multi-agent AI setup** that integrates large language models with specialized tools for web research and financial market analysis. The system leverages the **Groq API (LLaMA-3.3-70B)** to coordinate between agents that gather real-time news, stock fundamentals, and analyst recommendations, producing a **structured investor brief**.  

---

## 📑 Abstract  

This project presents the development of a multi-agent AI framework that combines **LLMs with external APIs** to provide reliable and structured insights. By integrating:  

- **Groq LLaMA-3.3-70B** for reasoning and synthesis  
- **DuckDuckGo** for real-time web-based news search  
- **Yahoo Finance tools** for stock data, analyst ratings, and company fundamentals  

…the system generates concise, source-backed investment briefs. Results are formatted in **Markdown tables and bullet lists**, making them suitable for financial decision support.  

---

## 📖 Introduction  

The rapid progress of LLMs has enabled the creation of AI agents that interact with **external data sources in real time**. Instead of relying solely on static model knowledge, these systems can query live APIs to retrieve updated financial metrics and market developments.  

This project builds a **multi-agent pipeline** where:  

- A **Scout Agent** gathers market sentiment and headlines.  
- A **Market Agent** retrieves stock metrics and analyst data.  
- A **Navigator Agent** synthesizes outputs into a professional investment brief.  

This design illustrates the potential of collaborative AI agents in domains where both **up-to-date facts** and **structured reasoning** are critical.  

---

## ⚙️ Methodology  

### System Architecture  

The architecture consists of three layers:  

- **Scout Agent** – Performs real-time searches using DuckDuckGo to gather market updates.  
- **Market Agent** – Uses YFinanceTools to retrieve stock prices, fundamentals, and analyst recommendations.  
- **Navigator Agent** – Coordinates both agents, synthesizing results into a structured investor report.  

### Tools and Technologies  

- **LLM**: LLaMA-3.3-70B (via Groq API)  
- **DuckDuckGo Search**: For real-time news and web data  
- **YFinanceTools**: Provides stock metrics, company news, and analyst breakdowns  
- **PHI Framework**: Python framework for agent orchestration  

---

## 💻 Installation  

1. **Clone the repository**  
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
