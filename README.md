# 🦜🔗 Langchain - Ask the Data App

Build an LLM powered Ask the Data App with LangChain (using the Pandas DataFrame Agent) and Streamlit.

## Overview of the App

This app uses the Pandas DataFrame Agent from LangChain to allow you to ask questions about a Pandas DataFrame.

## Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://langchain-ask-the-data.streamlit.app/)

## Get an OpenAI API key

You can get your own OpenAI API key by following the following instructions:
1. Go to https://platform.openai.com/account/api-keys.
2. Click on the `+ Create new secret key` button.
3. Next, enter an identifier name (optional) and click on the `Create secret key` button.

## Try out the app

Once the app is loaded, do the following in sequential order:
1. Upload a CSV file (you can also tweak the underlying code to have it read in other tabular formats such as Excel or tab delimited files.
2. Select an example query from the drop-down menu or provide your own custom query (by selecting the *Other* option)
3. Enter your OpenAI API key

That's all and the Pandas DataFrame Agent will start to work on your query. 

