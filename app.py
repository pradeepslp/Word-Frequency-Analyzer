import re
from collections import Counter
import pandas as pd
import streamlit as st
import altair as alt

# Set page configuration
st.set_page_config(
    page_title="Word Frequency Analyzer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for clean, modern styling
st.markdown("""
<style>
    /* Metric Card Styling */
    .metric-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.04);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
    }
    .metric-title {
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #64748b;
        margin-bottom: 8px;
    }
    .metric-value {
        font-size: 1.85rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 4px;
    }
    .metric-subtext {
        font-size: 0.8rem;
        color: #94a3b8;
    }
    
    /* Header badge */
    .app-badge {
        display: inline-block;
        background: #e0f2fe;
        color: #0369a1;
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-bottom: 10px;
    }

    /* Dark mode compatibility for custom cards */
    @media (prefers-color-scheme: dark) {
        .metric-card {
            background: #1e293b;
            border-color: #334155;
        }
        .metric-title {
            color: #94a3b8;
        }
        .metric-value {
            color: #f8fafc;
        }
        .metric-subtext {
            color: #64748b;
        }
        .app-badge {
            background: #0c4a6e;
            color: #7dd3fc;
        }
    }
</style>
""", unsafe_allow_html=True)

# Sample texts for quick demonstration
SAMPLE_TEXTS = {
    "Technology & AI": (
        "Artificial intelligence and machine learning are transforming modern technology. "
        "Machine learning models learn patterns from data, while artificial intelligence aims "
        "to solve complex problems. As technology evolves, data and intelligence will continue "
        "to shape innovation across the world."
    ),
    "Literature / Proverb": (
        "To be or not to be, that is the question. Whether 'tis nobler in the mind to suffer "
        "the slings and arrows of outrageous fortune, or to take arms against a sea of troubles, "
        "and by opposing end them."
    ),
    "Data & Analytics": (
        "Data science is all about data analysis, data visualization, and data modeling. "
        "Good data leads to good insights, and good insights empower effective decision making."
    )
}

def clean_and_tokenize(text: str) -> list[str]:
    """
    Cleans text by converting to lowercase and stripping punctuation.
    Extracts alphanumeric words (handling basic contractions like it's, don't).
    """
    if not text:
        return []
    # Match alphanumeric words, preserving internal apostrophes
    words = re.findall(r"\b[a-zA-Z0-9]+(?:'[a-zA-Z0-9]+)?\b", text.lower())
    return words

# --- Sidebar Controls ---
with st.sidebar:
    st.header("⚙️ Settings & Samples")
    
    st.markdown("### 📝 Quick Samples")
    selected_sample = st.selectbox(
        "Load a sample paragraph:",
        ["-- Select Sample --"] + list(SAMPLE_TEXTS.keys()),
        index=0
    )
    
    if selected_sample != "-- Select Sample --":
        if st.button("Load Selected Sample", use_container_width=True):
            st.session_state["user_input_text"] = SAMPLE_TEXTS[selected_sample]
            st.rerun()

    st.markdown("---")
    st.markdown("### 📊 Visualization Options")
    top_n = st.slider(
        "Max words in bar chart:",
        min_value=5,
        max_value=50,
        value=15,
        step=5,
        help="Controls how many top-ranking words are displayed in the chart."
    )
    
    chart_sort_order = st.radio(
        "Chart Sorting:",
        options=["Descending (Highest first)", "Ascending (Lowest first)"],
        index=0
    )

    st.markdown("---")
    if st.button("🧹 Clear Input", use_container_width=True):
        st.session_state["user_input_text"] = ""
        st.rerun()

# --- Main App Header ---
st.markdown('<span class="app-badge">Text Analysis Tool</span>', unsafe_allow_html=True)
st.title("📊 Word Frequency Analyzer")
st.markdown(
    "Analyze any paragraph to extract word counts, determine unique terms, "
    "discover the most frequent words, and visualize the distribution."
)

# Text Input Area
default_value = st.session_state.get("user_input_text", "")
user_text = st.text_area(
    label="**Enter or paste your text below:**",
    value=default_value,
    height=180,
    placeholder="Type or paste a paragraph here to analyze word frequencies...",
    key="text_input_area"
)

# Keep session state synchronized
if user_text != st.session_state.get("user_input_text", ""):
    st.session_state["user_input_text"] = user_text

# --- Processing and Analysis ---
if not user_text.strip():
    # Empty state message
    st.info("💡 **Ready to analyze!** Please enter or paste some text into the box above or select a sample from the sidebar.")
else:
    words = clean_and_tokenize(user_text)
    
    if not words:
        st.warning("⚠️ No valid words found in the input. Please ensure your text contains letters or numbers.")
    else:
        total_words = len(words)
        frequency_map = Counter(words)
        unique_words = len(frequency_map)
        
        # Most frequent word calculation
        most_common_items = frequency_map.most_common()
        highest_freq = most_common_items[0][1]
        top_words = [word for word, count in most_common_items if count == highest_freq]
        
        if len(top_words) == 1:
            most_frequent_display = f'"{top_words[0]}"'
            most_frequent_sub = f"Appeared {highest_freq} time{'s' if highest_freq > 1 else ''}"
        else:
            most_frequent_display = f"{len(top_words)} words (tie)"
            most_frequent_sub = f"{', '.join(top_words[:3])}{'...' if len(top_words) > 3 else ''} ({highest_freq}x each)"

        lexical_diversity = (unique_words / total_words) * 100

        # --- Metrics Row ---
        st.markdown("### 📈 Summary Metrics")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">Total Words</div>
                <div class="metric-value">{total_words:,}</div>
                <div class="metric-subtext">All words parsed</div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">Unique Words</div>
                <div class="metric-value">{unique_words:,}</div>
                <div class="metric-subtext">Distinct terms</div>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">Most Frequent</div>
                <div class="metric-value" style="font-size: 1.4rem;">{most_frequent_display}</div>
                <div class="metric-subtext">{most_frequent_sub}</div>
            </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">Lexical Diversity</div>
                <div class="metric-value">{lexical_diversity:.1f}%</div>
                <div class="metric-subtext">Unique / Total ratio</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Build DataFrame
        df_freq = pd.DataFrame(
            [
                {
                    "Rank": idx + 1,
                    "Word": word,
                    "Frequency": count,
                    "Percentage": round((count / total_words) * 100, 2)
                }
                for idx, (word, count) in enumerate(most_common_items)
            ]
        )

        # --- Visualizations & Table Layout ---
        tab_chart, tab_table = st.tabs(["📊 Frequency Chart", "📋 Data Table & Export"])

        with tab_chart:
            st.subheader(f"Top {min(top_n, unique_words)} Word Frequencies")
            
            # Prepare subset for visualization
            chart_df = df_freq.head(top_n).copy()
            if "Ascending" in chart_sort_order:
                chart_df = chart_df.sort_values(by="Frequency", ascending=True)
            else:
                chart_df = chart_df.sort_values(by="Frequency", ascending=False)

            # Interactive Altair Bar Chart
            chart = (
                alt.Chart(chart_df)
                .mark_bar(cornerRadiusTopRight=6, cornerRadiusBottomRight=6, color="#3b82f6")
                .encode(
                    x=alt.X("Frequency:Q", title="Occurrence Count", axis=alt.Axis(tickMinStep=1)),
                    y=alt.Y("Word:N", sort=None, title="Word"),
                    tooltip=[
                        alt.Tooltip("Rank:Q", title="Rank"),
                        alt.Tooltip("Word:N", title="Word"),
                        alt.Tooltip("Frequency:Q", title="Count"),
                        alt.Tooltip("Percentage:Q", title="Share (%)", format=".2f")
                    ]
                )
                .properties(height=max(350, min(top_n, unique_words) * 28))
                .interactive()
            )
            st.altair_chart(chart, use_container_width=True)

        with tab_table:
            st.subheader("All Word Frequencies")
            
            # Formatted Streamlit DataFrame
            st.dataframe(
                df_freq,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "Rank": st.column_config.NumberColumn("Rank", format="#%d", width="small"),
                    "Word": st.column_config.TextColumn("Word", width="medium"),
                    "Frequency": st.column_config.ProgressColumn(
                        "Frequency",
                        help="Number of times this word occurs",
                        format="%d",
                        min_value=0,
                        max_value=int(df_freq["Frequency"].max())
                    ),
                    "Percentage": st.column_config.NumberColumn("Share (%)", format="%.2f %%", width="small")
                }
            )

            # CSV Export
            csv_data = df_freq.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Download Frequency Data as CSV",
                data=csv_data,
                file_name="word_frequency_analysis.csv",
                mime="text/csv"
            )

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #94a3b8; font-size: 0.85rem;'>"
    "Word Frequency Analyzer • Built with Python & Streamlit • Local & Offline"
    "</div>",
    unsafe_allow_html=True
)
