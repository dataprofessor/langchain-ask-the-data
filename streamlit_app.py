import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from langchain.llms import OpenAI
from langchain.agents import create_pandas_dataframe_agent

# Page title
st.set_page_config(page_title='🦜🔗 Ask the CSV App')
st.title('🦜🔗 Ask the CSV App')

def generate_response(input_csv, input_query):
  llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
  # Load CSV if file is uploaded
  df = pd.read_csv(input_csv)
  # Display DataFrame
  with st.expander('See DataFrame'):
    st.write(df)
  # Create Pandas DataFrame Agent
  agent = create_pandas_dataframe_agent(llm, df, verbose=True)
  # Perform Query using the Agent
  response = agent.run(input_query)
  return st.success(response)

# File upload
uploaded_file = st.file_uploader('Upload a CSV file', type=['csv'])
# Query text
# query_text = st.text_input('Enter your query:', placeholder = 'How many rows are there?', disabled=not uploaded_file)
question_list = [
  'How many rows are there?',
  'What is the range of values for MolWt with median solubility value greater than 0?',
  'How many rows have solubility value greater than 0.'
  ]
query_text = st.selectbox('Select an example query:', question_list, disabled=not uploaded_file)

openai_api_key = st.text_input('OpenAI API Key', type='password', disabled=not (uploaded_file and query_text))
if not openai_api_key.startswith('sk-'):
  st.warning('Please enter your OpenAI API key!', icon='⚠')
if openai_api_key.startswith('sk-') and (uploaded_file is not None):
  st.header('Output')
  generate_response(uploaded_file, query_text)
