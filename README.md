Comply-RAG: The Super Searcher

Precision Retrieval for Regulatory Documents

🌟 Project Overview: The RegTech Suite

This application is part of a three-piece RegTech Suite designed to automate critical compliance workflows using modern AI/ML simulation techniques. This specific component addresses the need for Knowledge Retrieval.

Key Value Proposition

The Comply-RAG simulates a Retrieval-Augmented Generation (RAG) system that allows auditors, compliance officers, and legal teams to find precise policy answers and their source citation instantly within vast document repositories.

🚀 Live Demo and Core Functionality

Live Application: https://comply-rag-lisa-silva.streamlit.app/

Feature

Description

Business Impact

Precision Citation (98.7% Score)

Generates a concise answer and provides the exact source (simulated page/line number) for full auditability.

Provides instant, reliable proof to auditors, drastically reducing manual review time.

Streamlit Interface

Provides a simple, interactive web interface built entirely in Python.

No special software installation needed for end-users; accessible via any browser.

High-Speed Retrieval

Simulates indexing and searching millions of documents instantaneously.

Cuts weeks of manual regulatory research down to seconds, minimizing regulatory risk exposure.

💻 Local Setup and Installation

To run this application locally, you will need Python 3.8+.

Prerequisites

Clone the Repository:

git clone https://github.com/lisa-silva/auditus-xai.git 
cd lisa-silva/regtech-suite


Create a Virtual Environment (venv):

python -m venv venv
.\venv\Scripts\activate  # Windows
# or source venv/bin/activate # macOS/Linux


Running the App

Install Dependencies:
This app requires streamlit (listed in requirements.txt).

pip install -r requirements.txt


Launch the Application:

streamlit run comply_rag_app.py 


The application will automatically open in your browser at http://localhost:8501.

🛠️ Technology Stack

Framework: Streamlit (Python)

Version Control: Git & GitHub

Deployment: Streamlit Cloud

Language: Python 3.x
