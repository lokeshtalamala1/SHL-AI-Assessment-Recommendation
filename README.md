# SHL-AI-Assessment-Recommendation

Approach Overview

Objective:

Develop an intelligent recommendation system for SHL assessments that simplifies the hiring process by automatically suggesting the most relevant assessments based on a natural language query or a job description URL.

System Architecture:

Backend (Flask API):

- Functionality: Accepts a query via a POST request at /recommend.
- Processing: Uses a simple keyword-matching algorithm to score a hardcoded dataset of

`   `SHL assessments based on query relevance.

- Response: Returns up to 10 matching assessments in JSON format, each including the

`   `assessment name (with a URL), remote testing support, adaptive/IRT support, duration,    and test type.

Frontend (Streamlit Web Demo):

- User Interface: Provides a text area for entering queries or job description URLs.
- Integration: Sends user queries to the Flask API and displays the returned recommendations

`   `in a formatted table with clickable assessment names.

Tools and Libraries Used:

- Flask: For building the REST API that processes and returns recommendations.
- Streamlit: For creating the interactive web demo to showcase the system.
- Pandas: For managing and displaying tabular data.
- Requests: For API calls from the web demo to the backend.
- Python: The primary programming language for both backend and frontend components.

Enhancements and Future Work:

- Advanced Matching: Replace the simple keyword matching with advanced NLP or LLM-based

`   `semantic search to improve recommendation accuracy.

- Data Crawling: Automate crawling and indexing of the SHL product catalog for dynamic updates.
- Performance Improvements: Introduce caching and logging to enhance performance and monitoring.
- User Experience: Further refine the demo interface for better interactivity and responsiveness.

Conclusion:

This solution offers an end-to-end demonstration of an SHL assessment recommendation system that meets the assignment requirements. It includes a working demo, a functional API endpoint, and detailed documentation outlining the approach and tools used.
