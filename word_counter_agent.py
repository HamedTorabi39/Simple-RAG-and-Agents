from collections import Counter
import json

def load_sentiment_words():
    try:
        with open("sentiment_words.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"positive": ["great", "good", "awesome"], "negative": ["bad", "poor", "issue"]}

def save_sentiment_words(sentiment_words):
    with open("sentiment_words.json", "w", encoding="utf-8") as f:
        json.dump(sentiment_words, f, ensure_ascii=False, indent=2)

def text_analyzer():
    sentiment_words = load_sentiment_words()
    positive_words = sentiment_words["positive"]
    negative_words = sentiment_words["negative"]

    print("Welcome to the Text Analyzer! (Type 'exit' to quit)")
    print("You can analyze text or add positive/negative words.")

    while True:
        print("\nChoose an option: 1) Analyze text 2) Add positive word 3) Add negative word 4) Exit")
        choice = input("Your choice: ").strip()

        if choice == "1":
            text = input("Enter your text: ").lower()
            words = text.split()
            
            # Word count
            word_count = len(words)
            print(f"Total word count: {word_count}")
            
            # Most frequent words
            word_freq = Counter(words).most_common(3)
            print("Top 3 frequent words:", word_freq)
            
            # Sentiment analysis
            sentiment_score = 0
            for word in words:
                if word in positive_words:
                    sentiment_score += 1
                elif word in negative_words:
                    sentiment_score -= 1
            sentiment = "Positive" if sentiment_score > 0 else "Negative" if sentiment_score < 0 else "Neutral"
            print(f"Text sentiment: {sentiment}")

        elif choice == "2":
            new_word = input("Enter a new positive word: ").strip().lower()
            if new_word and new_word not in positive_words:
                positive_words.append(new_word)
                sentiment_words["positive"] = positive_words
                save_sentiment_words(sentiment_words)
                print(f"Word '{new_word}' added to positive list.")
            else:
                print("Invalid word or already exists!")

        elif choice == "3":
            new_word = input("Enter a new negative word: ").strip().lower()
            if new_word and new_word not in negative_words:
                negative_words.append(new_word)
                sentiment_words["negative"] = negative_words
                save_sentiment_words(sentiment_words)
                print(f"Word '{new_word}' added to negative list.")
            else:
                print("Invalid word or already exists!")

        elif choice == "4" or choice.lower() == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    text_analyzer()