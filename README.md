# Shopify_AI_Analytics-project
# AI-Powered Shopify Analytics App

##  Overview
This project is a mini AI-powered analytics application designed to work with a Shopify store.
It allows users to ask natural-language business questions (sales, inventory, customers),
and returns simple, human-readable insights generated using an AI agent.

The system demonstrates backend API design, agentic reasoning, and AI-driven analytics
rather than production-level Shopify integration.

## Objective
- Connect to a Shopify store (conceptually)
- Accept natural-language business questions
- Use an AI agent to interpret intent
- Generate ShopifyQL-style queries
- Convert raw data into simple business insights

##  System Architecture

User
↓
Rails API (Gateway Layer)
↓
Python AI Service (LLM-Powered Agent)
↓
Shopify API / Mock Data
↓
Business-Friendly Answer


##  Project Structure

shopify-ai-analytics/
│
├── rails_api/ # Rails API Gateway (Design-level)
│ ├── app/controllers/
│ ├── app/services/
│ ├── config/routes.rb
│ ├── Gemfile
│ └── Gemfile.lock
│
├── python_ai_service/ # Python AI Agent (Runnable)
│ ├── app.py
│ ├── agent.py
│ ├── shopify_client.py
│ ├── requirements.txt
│
└── README.md

##  Tech Stack

- Backend Gateway : Ruby on Rails (API-only)
- AI Service : Python (FastAPI)
- LLM (Conceptual) : OpenAI / Claude / Gemini (mocked logic)
- Query Language : ShopifyQL (simulated)
- API Testing : Postman / curl / VS Code REST Client

##  AI Agent Workflow

1. Intent Detection
   - Identifies whether the question is about sales, inventory, or customers

2. Planning
   - Determines required Shopify data (orders, products, inventory)
   - 
3. Query Generation
   - Generates a ShopifyQL-style query

4. Execution
   - Fetches data (mocked Shopify response)

5. Explanation
   - Converts metrics into simple business language





 
