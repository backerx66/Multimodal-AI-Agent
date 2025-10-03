Multi-Agent AI System for Financial Research and Web Intelligence

This project demonstrates a multi-agent AI setup that integrates large language models with specialized tools for web research and financial market analysis. The system leverages the Groq API (LLaMA-3.3-70B) to coordinate between agents that gather real-time news, stock fundamentals, and analyst recommendations, producing a structured investor brief.

Abstract

This project presents the development of a multi-agent AI framework that combines LLMs with external APIs to provide reliable and structured insights. By integrating:

Groq LLaMA-3.3-70B for reasoning and synthesis,

DuckDuckGo for web-based news search,

Yahoo Finance tools for stock data, analyst ratings, and company fundamentals,

the system generates concise, source-backed investment briefs. Results are formatted in Markdown tables and bullet lists, making them suitable for financial decision support.

Introduction

The rapid progress of LLMs has enabled the creation of AI agents that interact with external data sources in real time. Instead of relying solely on static model knowledge, these systems can query live APIs to retrieve updated financial metrics and market developments.

This project builds a multi-agent pipeline where:

A news scout agent gathers market sentiment and headlines.

A market sage agent retrieves stock metrics and analyst data.

A navigator agent synthesizes outputs into a professional investment brief.

This design illustrates the potential of collaborative AI agents in domains where both up-to-date facts and structured reasoning are critical.

Methodology
System Architecture

The architecture consists of three layers:

Scout Agent – Performs real-time searches using DuckDuckGo to gather market updates.

Market Agent – Uses YFinanceTools to retrieve stock prices, fundamentals, and analyst recommendations.

Navigator Agent – Coordinates both agents, synthesizing results into a structured investor report.

Tools and Technologies

LLM: LLaMA-3.3-70B (via Groq API).

DuckDuckGo Search: For real-time news and web data.

YFinanceTools: Provides stock metrics, company news, and analyst breakdowns.

PHI Framework: Python framework for agent orchestration.

Implementation

Each agent is instantiated with a specific role, model, and toolset.

Instructions guide agents to format responses (e.g., Markdown tables, explicit analyst numbers).

The navigator agent ensures results follow a consistent 6-part structure:

Executive Summary

Key Financial Metrics

Analyst Recommendations

Recent Developments

Investment Highlights

Sources

Results

When queried with:

“Provide a comprehensive investment analysis of Tesla (TSLA)”

The system produces a Markdown-formatted investor brief including:

Analyst ratings with exact Buy/Hold/Sell counts.

Stock fundamentals (price, market cap, P/E).

Recent company news with direct source links.

A concise summary of opportunities and risks.

This confirms that the multi-agent system successfully merges heterogeneous data into a unified report.

Discussion

Strengths:

Agents can divide tasks efficiently (news vs. finance).

Structured outputs (tables, bullet points) improve readability.

Scalable architecture allows adding new tools (e.g., social media sentiment, SEC filings).

Limitations:

Dependent on external APIs for data accuracy.

Response times vary with API latency.

Analyst data availability is sometimes incomplete.

Applications

FinTech platforms – automated investor reports.

Business Intelligence – synthesizing market and company data.

Research Assistants – real-time, source-backed knowledge retrieval.

Future Work

Integration with additional financial APIs (e.g., Bloomberg, Alpha Vantage).

Expanded domain coverage (healthcare, climate, legal research).

Personalized agent instructions based on user preferences.

Conclusion

This project demonstrates a multi-agent AI system capable of financial research and market analysis by combining Groq-powered LLM reasoning with domain-specific tools. The resulting structured investor briefs highlight the value of collaborative agents in delivering actionable insights for decision support in data-driven industries.
