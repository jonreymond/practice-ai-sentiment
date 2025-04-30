''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer


app = Flask("Sentiment Analyzer")


@app.route("/sentimentAnalyzer")
def sent_analyzer():
    '''
    Retrieve the text to analyze, and return the corresponding label and score if entry is valid
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = sentiment_analyzer(text_to_analyze)

    # Extract the label and score from the response
    label = response['label']
    score = response['score']

    if label is None:
        return "Invalid input! Try again."
    return f"The given text is {label.split('_')[1]} with a score of {score}."

@app.route("/")
def render_index_page():
    '''
    Render html file
    '''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
