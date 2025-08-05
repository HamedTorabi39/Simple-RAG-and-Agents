# Simple-RAG-and-Agents
RAG and Agents that have a simple structure

---

## 📄 word_counter_agent and new_word_counter

A simple yet extensible text analysis tool that performs **sentiment analysis**, **word frequency counting**, and stores the results in both **JSON** and **CSV** formats.

---

### ✨ Features

* Sentiment analysis (Positive, Negative, Neutral)
* Word count and top 3 frequent words
* Add custom positive/negative words with sentiment weight
* Save analysis results to `JSON` and `CSV`
* View summary reports of previous analyses

---

### ⚙️ Requirements

* Python 3.7 or higher

---

### 🚀 Installation & Usage

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
python main.py
```

> No external libraries are required (only standard Python libraries are used).

---

### 🧠 How It Works

After running the program, you'll see a menu:

```
Options:
1) Analyze text
2) Add positive word
3) Add negative word
4) View summary
5) Exit
```

* **Analyze text** – Enter text to analyze sentiment and word stats.
* **Add positive/negative word** – Add custom words with sentiment weight.
* **View summary** – See aggregated stats from all analyses.
* **Exit** – Quit the program.

---

### 💾 Output Files

* `analyses.json`: Stores all text analyses in JSON format.
* `analyses.csv`: Stores all text analyses in CSV format for easy use in Excel or BI tools.
* `sentiment_words.json`: Stores user-defined sentiment words and their weights.

---

### 📂 Project Structure

```
project/
├── main.py                # Main executable script
├── analyses.json          # Saved analyses (JSON)
├── analyses.csv           # Saved analyses (CSV)
└── sentiment_words.json   # Sentiment word dictionary
```

---

### 📝 Example Sentiment Results

* Input: `This product is awesome and really great!`
  → Sentiment: **Positive** (Score: +4)

* Input: `The experience was bad and poor.`
  → Sentiment: **Negative** (Score: -3)

---

### 🪪 License

This project is licensed under the **MIT License**.

---

Let me know if you'd like me to turn this into a downloadable `README.md` file or improve it for open-source publishing (e.g., with badges, contributing guidelines, etc).
