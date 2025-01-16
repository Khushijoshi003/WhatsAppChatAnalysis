import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import seaborn as sns
st.markdown(
    """
    <style>
        .stButton>button {
            background-color: #f39c12;
            color: white;
            font-size: 18px;
            border-radius: 5px;
            padding: 10px 20px;
        }
        .stSidebar .css-1d391kg {
            background-color: #ecf0f1;
        }
        .stTitle {
            color: #2c3e50;
        }
        .stText {
            font-size: 16px;
            color: #34495e;
        }
        .stHeader {
            font-size: 20px;
            font-weight: bold;
            color: #2980b9;
        }
    </style>
    """,
    unsafe_allow_html=True
)
# Sidebar Title and File Uploader
st.sidebar.title("WhatsApp Chat Analyzer")
uploaded_file = st.sidebar.file_uploader("Choose a file")
# Preprocessing of file
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)
    # Analyze data for specific individuals or entire group.
    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"Overall")

    selected_user = st.sidebar.selectbox("Show analysis wrt", user_list)

    if st.sidebar.button("Show Analysis"):

        # Stats Area
        num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)
        # Top Statistics Section
        st.title("Top Statistics", anchor="stats")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Total Messages")
            st.subheader(num_messages)
        with col2:
            st.header("Total Words")
            st.subheader(words)
        with col3:
            st.header("Media Shared")
            st.subheader(num_media_messages)
        with col4:
            st.header("Links Shared")
            st.subheader(num_links)

        # Monthly Timeline
        st.title("Monthly Timeline")
        timeline = helper.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(timeline['time'], timeline['message'], color='green')
        ax.set_xlabel("Month")
        ax.set_ylabel("Messages")
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # Daily Timeline
        st.title("Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
        ax.set_xlabel("Date")
        ax.set_ylabel("Messages")
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # Activity Map
        st.title('Activity Map')
        col1, col2 = st.columns(2)

        with col1:
            st.header("Most Busy Day")
            busy_day = helper.week_activity_map(selected_user, df)
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.bar(busy_day.index, busy_day.values, color='purple')
            ax.set_xlabel("Day of Week")
            ax.set_ylabel("Messages")
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.header("Most Busy Month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.bar(busy_month.index, busy_month.values, color='orange')
            ax.set_xlabel("Month")
            ax.set_ylabel("Messages")
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        # Weekly Activity Map (Heatmap)
        st.title("Weekly Activity Map")
        user_heatmap = helper.activity_heatmap(selected_user, df)
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(user_heatmap, annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

        # Most Busy Users (Group Level)
        if selected_user == 'Overall':
            st.title('Most Busy Users')
            x, new_df = helper.most_busy_users(df)
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.bar(x.index, x.values, color='red')
            ax.set_xlabel("User")
            ax.set_ylabel("Messages")
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
            st.dataframe(new_df)

        # WordCloud Section
        st.title("Wordcloud")
        df_wc = helper.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.imshow(df_wc)
        ax.axis('off')
        st.pyplot(fig)

        # Most Common Words
        most_common_df = helper.most_common_words(selected_user, df)
        st.title('Most Common Words')
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.barh(most_common_df[0], most_common_df[1], color='skyblue')
        ax.set_xlabel("Frequency")
        ax.set_ylabel("Words")
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # Emoji Analysis
        emoji_df = helper.emoji_helper(selected_user, df)
        st.title("Emoji Analysis")

        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.pie(emoji_df[1].head(), labels=emoji_df[0].head(), autopct="%0.2f", colors=sns.color_palette("Set2"))
            st.pyplot(fig)
