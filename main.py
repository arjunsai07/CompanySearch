import os
from constants import openai_key
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain
from langchain.memory import ConversationBufferMemory
import streamlit as st

os.environ['OPENAI_API_KEY']=openai_key

#streamlit framework
st.title('Company Search')
input_text=st.text_input('Search the company name you want:') #stores the input of the person entered in textbox

company_details_mem=ConversationBufferMemory(input_key='company_name',memory_key='chat_history')
company_revenue_mem=ConversationBufferMemory(input_key='company_details',memory_key='chat_history')
highest_stock_2021_memory=ConversationBufferMemory(input_key='highest_stock_price_2021',memory_key='chat_history')

#OPENAI LLMS
llm=OpenAI(temperature=0.8)

st.write(f"Using OpenAI model: {llm.model_name}")

#Prompt Templates, every prompt template will have an LLM Chain
first_input_prompt=PromptTemplate(input_variables=['company_name'],template='Tell me about the company {company_name}')
chain1=LLMChain(llm=llm,prompt=first_input_prompt,verbose=True,output_key='company_details',memory=company_details_mem) #revenue of the company will be mapped to revenue

#Prompt Templates, every prompt template will have an LLM Chain
second_input_prompt=PromptTemplate(input_variables=['company_details'],template='what was {company_details}\'s highest stock price in 2021?')
chain2=LLMChain(llm=llm,prompt=second_input_prompt,verbose=True,output_key='highest_stock_price_2021',memory=company_revenue_mem) #name of the celebrity will be mapped to person

third_input_prompt=PromptTemplate(input_variables=['highest_stock_price_2021'],template='What other companies secured more stock price than {highest_stock_price_2021} in 2021?')
chain3=LLMChain(llm=llm,prompt=third_input_prompt,verbose=True,output_key='better_companies_of_2021',memory=highest_stock_2021_memory) #name of the celebrity will be mapped to person

#parent_chain=SimpleSequentialChain(chains=[chain1,chain2],verbose=True)

parent_chain=SequentialChain(chains=[chain1,chain2,chain3],input_variables=['company_name'],output_variables=['company_details','highest_stock_price_2021','better_companies_of_2021'],verbose=True)

if input_text:
    #st.write(llm(input_text))
    #st.write(parent_chain.run(input_text))
    #st.write(parent_chain.run(input_text))
    st.write(parent_chain({'company_name':input_text}))
    with st.expander('Company details'):
        st.info(company_details_mem.buffer)
    with st.expander('Company\'s highest stock price in 2021'):
        st.info(company_revenue_mem.buffer)
    with st.expander('Companies better than chosen Company'):
        st.info(highest_stock_2021_memory.buffer)
        
