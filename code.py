def sentiment(text):
    positive_words = ["good", "great", "awesome", "happy"]
    negative_words = ["bad", "sad", "terrible", "angry"]
    
    for word in text.split():
        if word.lower() in positive_words:
            return "Positive sentiment"
        elif word.lower() in negative_words:
            return "Negative sentiment"
    return "Neutral sentiment"

print(sentiment("Today is a great day!"))
