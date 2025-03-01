import streamlit as st
import time

def show_process_animation():
    """
    Display an animation showing the web scraping and analysis process.
    """
    steps = [
        "🤖 Understanding your requirements...",
        "🌐 Connecting to insurance websites...",
        "📝 Filling in your details...",
        "🔍 Scraping available plans...",
        "⚖️ Analyzing and comparing options...",
        "📊 Preparing personalized recommendations..."
    ]

    progress_bar = st.progress(0)
    status_text = st.empty()

    for idx, step in enumerate(steps):
        status_text.text(step)
        progress_bar.progress((idx + 1) * (100 // len(steps)))
        time.sleep(0.8)  # Longer delay to make the process more visible

    progress_bar.empty()
    status_text.empty()

def show_company_comparison_animation():
    """
    Display an animation for company comparison process.
    """
    steps = [
        "🔍 Analyzing company profiles...",
        "📊 Comparing service offerings...",
        "🎯 Identifying key differences...",
        "📋 Generating detailed comparison..."
    ]

    progress_bar = st.progress(0)
    status_text = st.empty()

    for idx, step in enumerate(steps):
        status_text.text(step)
        progress_bar.progress((idx + 1) * (100 // len(steps)))
        time.sleep(0.7)

    progress_bar.empty()
    status_text.empty()