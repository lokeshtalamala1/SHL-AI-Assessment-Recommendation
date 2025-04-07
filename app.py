from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample assessments data from SHL's catalog (for demo purposes)
assessments = [
    {
        "name": "Java Developer Cognitive Test",
        "url": "https://www.shl.com/solutions/products/product-catalog/java-developer-cognitive-test",
        "remote_support": "Yes",
        "adaptive_support": "No",
        "duration": "40 minutes",
        "test_type": "Cognitive"
    },
    {
        "name": "Python Developer Technical Test",
        "url": "https://www.shl.com/solutions/products/product-catalog/python-developer-technical-test",
        "remote_support": "Yes",
        "adaptive_support": "Yes",
        "duration": "60 minutes",
        "test_type": "Technical"
    },
    {
        "name": "Analyst Cognitive and Personality Test",
        "url": "https://www.shl.com/solutions/products/product-catalog/analyst-cognitive-personality-test",
        "remote_support": "No",
        "adaptive_support": "No",
        "duration": "45 minutes",
        "test_type": "Cognitive/Personality"
    },
    {
        "name": "Mid-level Professional Multi-skills Test",
        "url": "https://www.shl.com/solutions/products/product-catalog/mid-level-multiskills-test",
        "remote_support": "Yes",
        "adaptive_support": "No",
        "duration": "60 minutes",
        "test_type": "Technical/Cognitive"
    },
    # ... Additional assessments can be added here ...
]

def simple_match(query, assessment):
    """
    A basic keyword matching function that assigns a score based on the presence of query words
    in the assessment's name and test type.
    """
    score = 0
    keywords = query.lower().split()
    text = (assessment["name"] + " " + assessment["test_type"]).lower()
    for word in keywords:
        if word in text:
            score += 1
    return score

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    query = data.get("query", "")
    if not query:
        return jsonify({"error": "No query provided"}), 400

    # Score each assessment
    scored_assessments = []
    for assessment in assessments:
        score = simple_match(query, assessment)
        if score > 0:
            scored_assessments.append((score, assessment))

    # Sort by score in descending order and pick top 10 results
    scored_assessments.sort(key=lambda x: x[0], reverse=True)
    results = [item[1] for item in scored_assessments][:10]
    
    return jsonify({"results": results})

if __name__ == '__main__':
    app.run(debug=True)
