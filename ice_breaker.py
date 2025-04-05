import os
from langchain.llms import OpenAI  # Use OpenAI instead of ChatOpenAI
from langchain import PromptTemplate
from dotenv import load_dotenv
from third_parties.linkedin import scrape_linkedin_profile

if __name__ == '__main__':
    print("hello Langchain")
    load_dotenv() 
    print(os.environ['OPENAI_API_KEY'])

    summary_template = """
            given the Linkedin information {information} about a person from i want to create:
            1. a short summary of the person
            2. interesting fact about the person
            """ 
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
    
    llm = OpenAI(temperature=0)  # Use OpenAI instead of ChatOpenAI

    chain = summary_prompt_template | llm 

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/harrison-chase-961287118/")

    res = chain.invoke(input={"information": linkedin_data})

    print(res)