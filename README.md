# 📊 WhatsApp Chat Analysis

A powerful and visually appealing Streamlit web app that provides detailed insights from WhatsApp chat exports. This tool helps you analyze both group and individual conversations, identifying top contributors, usage patterns, emoji usage, and much more.

---

## 🚀 Features

- 📈 **Top Statistics**: Total messages, words, media, and links shared.
- 🕰 **Timelines**: Monthly and daily message trends.
- 📅 **Activity Maps**: Most active days and months.
- 🔥 **Heatmaps**: Hourly activity distribution.
- 🧑‍🤝‍🧑 **Most Active Users** (for group chats).
- ☁️ **Word Cloud**: Frequently used words.
- 🗣 **Most Common Words**: 20 most used non-stop words.
- 😂 **Emoji Analysis**: Frequently used emojis and usage stats.

---

## 🖥 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Libraries**:
  - `matplotlib`, `seaborn` for visualization
  - `wordcloud` for word clouds
  - `emoji`, `collections.Counter` for emoji stats
  - `urlextract` for link detection
  - `pandas` for data handling
  - `re` for regex-based parsing

---
## 🧠 How It Works

1. Upload a `.txt` file exported from WhatsApp chat.
2. The app preprocesses the file using regular expressions and pandas.
3. Choose a specific user or "Overall" for complete group analysis.
4. View visualizations generated with `matplotlib` and `seabo


## 🛠 File Structure

```bash
whatsapp-chat-analyzer/
│
├── app.py                # Main Streamlit application
├── helper.py             # Analysis logic (stats, plots, etc.)
├── preprocessor.py       # File parsing and cleaning  
└── README.md             # You're here!

## 🖼️ Screenshots

| Statistics |
|-----------|------------|
|  ![stats](screenshots/stats.png) |

| Monthly Timeline | Heatmap |
|------------------|---------|
| ![monthly](screenshots/activitymap.png) | 

| WordCloud | Emoji Analysis |
|-----------|----------------|
| ![wordcloud](screenshots/worldcloud.png) | ![emoji](screenshots/emoji.png) |

> 💡 All screenshots are located inside the `screenshots/` folder.
