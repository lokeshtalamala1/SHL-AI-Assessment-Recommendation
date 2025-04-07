import streamlit as st
import requests
import pandas as pd

st.title("SHL Assessment Recommendation System")

st.markdown("""
This demo allows you to enter a natural language query or job description URL.
It then recommends up to 10 relevant SHL assessment solutions, displaying:
- **Assessment Name** (linked to SHL’s catalog)
- **Remote Testing Support** (Yes/No)
- **Adaptive/IRT Support** (Yes/No)
- **Duration**
- **Test Type**
""")

query = st.text_area("Enter your query or job description URL:")

if st.button("Get Recommendations"):
    if not query.strip():
        st.error("Please enter a valid query.")
    else:
        try:
            # Change the URL to your hosted API endpoint if not running locally
            response = requests.post("http://localhost:5000/recommend", json={"query": query})
            if response.status_code == 200:
                data = response.json()
                results = data.get("results", [])
                if results:
                    # Convert results to a DataFrame for display
                    df = pd.DataFrame(results)
                    # Format the Assessment Name as a clickable link
                    df["name"] = df.apply(lambda row: f"[{row['name']}]({row['url']})", axis=1)
                    st.markdown("### Recommended Assessments")
                    st.table(df[["name", "remote_support", "adaptive_support", "duration", "test_type"]])
                else:
                    st.info("No relevant assessments found for your query.")
            else:
                st.error("Error fetching recommendations from the API.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
