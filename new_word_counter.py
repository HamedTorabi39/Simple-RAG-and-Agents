import os
from collections import Counter
import json
import csv
import string
import time

def load_sentiment_words():
    try:
        with open("sentiment_words.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "positive": {"great": 2, "good": 1, "awesome": 2},
            "negative": {"bad": -2, "poor": -1, "issue": -1}
        }

def save_sentiment_words(sentiment_words):
    with open("sentiment_words.json", "w", encoding="utf-8") as f:
        json.dump(sentiment_words, f, ensure_ascii=False, indent=2)

def load_analyses():
    try:
        with open("analyses.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_analysis(analysis):
    analyses = load_analyses()
    analyses.append(analysis)
    with open("analyses.json", "w", encoding="utf-8") as f:
        json.dump(analyses, f, ensure_ascii=False, indent=2)

def save_to_csv(analysis):
    file_exists = False
    if os.path.exists("analyses.csv"):
        file_exists = True
    with open("analyses.csv", "a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp", "text", "word_count", "top_words", "sentiment", "sentiment_score"])
        if not file_exists:
            writer.writeheader()
        writer.writerow(analysis)

def clean_text(text):
    stop_words = {"the", "a", "an", "and", "or", "to", "in", "is", "are"}
    text = text.lower().translate(str.maketrans("", "", string.punctuation))
    words = [word for word in text.split() if word not in stop_words]
    return words

def text_analyzer():
    sentiment_words = load_sentiment_words()
    positive_words = sentiment_words["positive"]
    negative_words = sentiment_words["negative"]

    print("Welcome to the Enhanced Text Analyzer! (Type 'exit' to quit)")
    print("Analyze text, manage sentiment words, or view summary reports.")

    while True:
        print("\nOptions: 1) Analyze text 2) Add positive word 3) Add negative word 4) View summary 5) Exit")
        choice = input("Your choice: ").strip()

        if choice == "1":
            text = input("Enter your text: ")
            words = clean_text(text)
            
            # Word count
            word_count = len(words)
            print(f"Total word count (after cleaning): {word_count}")
            
            # Most frequent words
            word_freq = Counter(words).most_common(3)
            print("Top 3 frequent words:", word_freq)
            
            # Sentiment analysis
            sentiment_score = 0
            for word in words:
                if word in positive_words:
                    sentiment_score += positive_words[word]
                elif word in negative_words:
                    sentiment_score += negative_words[word]
            sentiment = "Positive" if sentiment_score > 0 else "Negative" if sentiment_score < 0 else "Neutral"
            print(f"Text sentiment: {sentiment} (Score: {sentiment_score})")

            # Save analysis
            analysis = {
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "text": text[:50] + "..." if len(text) > 50 else text,
                "word_count": word_count,
                "top_words": str(word_freq),
                "sentiment": sentiment,
                "sentiment_score": sentiment_score
            }
            save_analysis(analysis)
            save_to_csv(analysis)
            print("Analysis saved to JSON and CSV.")

        elif choice == "2":
            word = input("Enter a new positive word: ").strip().lower()
            try:
                weight = float(input("Enter weight for this word (e.g., 1 or 2): "))
                if word and word not in positive_words:
                    positive_words[word] = weight
                    sentiment_words["positive"] = positive_words
                    save_sentiment_words(sentiment_words)
                    print(f"Word '{word}' with weight {weight} added to positive list.")
                else:
                    print("Invalid word or already exists!")
            except ValueError:
                print("Invalid weight! Please enter a number.")

        elif choice == "3":
            word = input("Enter a new negative word: ").strip().lower()
            try:
                weight = float(input("Enter weight for this word (e.g., -1 or -2): "))
                if word and word not in negative_words:
                    negative_words[word] = weight
                    sentiment_words["negative"] = negative_words
                    save_sentiment_words(sentiment_words)
                    print(f"Word '{word}' with weight {weight} added to negative list.")
                else:
                    print("Invalid word or already exists!")
            except ValueError:
                print("Invalid weight! Please enter a number.")

        elif choice == "4":
            analyses = load_analyses()
            if not analyses:
                print("No analyses found!")
                continue
            positive = sum(1 for a in analyses if a["sentiment"] == "Positive")
            negative = sum(1 for a in analyses if a["sentiment"] == "Negative")
            neutral = sum(1 for a in analyses if a["sentiment"] == "Neutral")
            total = len(analyses)
            print(f"Summary: {total} analyses")
            print(f"Positive: {positive} ({positive/total*100:.1f}%)")
            print(f"Negative: {negative} ({negative/total*100:.1f}%)")
            print(f"Neutral: {neutral} ({neutral/total*100:.1f}%)")
            print("Recent analyses:")
            for a in analyses[-3:]:
                print(f"{a['timestamp']}: {a['text']} (Sentiment: {a['sentiment']})")

        elif choice == "5" or choice.lower() == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    text_analyzer()