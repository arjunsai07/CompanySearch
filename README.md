Company Search with LangChain, OpenAI APIs & Streamlit

I'm pleased to share my latest mini-project: "Company Search," a Streamlit app that leverages the power of OpenAI's language models (LLMs) to understand information on Companies.

What it does?

Gives overview about the company: Tells about the company's history various other details, such as its products and services, in a nutshell.
Track performance: See a company's highest stock price in 2021(randomly chosen year) and discover competitors who outperformed them that year.
Powered by LLMs: Built using OpenAI's API, Langchain, and custom prompt chains to intelligently extract and present relevant information. The chain feature of Langchain enables inputs and outputs of conversations to seamlessly flow into a thread of interaction.

How it works?

1. Enter a company name.
2. Let the AI do the heavy lifting – it sifts through vast amounts of data in seconds. This is done with OpenAI's APIs of pre-trained models.
3. Get clear, concise results displayed in a user-friendly Streamlit interface.

Tech Stack:

OpenAI API (model -> gpt-3.5-turbo-instruct)
Langchain
ConversationBufferMemory
Sequential Chain
PromptTemplate
Streamlit
Python

Possible Use Cases:

Investors: Quickly assess company performance and compare against rivals for a particular year
Job Seekers: Research potential employers and gain insights into their competitive landscape.
Business Analysts: Streamline data collection and analysis for reports and presentations.

Why I Built This?

I'm passionate about using AI to make complex tasks easier and more accessible. "Company Search" is a small step toward democratizing access to valuable information about a company.

I would like to thank Krish Naik for his informative videos on LLM and Machine Learning, in YouTube. 

hashtag#AI hashtag#Streamlit hashtag#OpenAI hashtag#LLMs hashtag#DataScience hashtag#Python hashtag#LangChain
