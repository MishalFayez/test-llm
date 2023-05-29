import os
os.environ["OPENAI_API_KEY"] = "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"


from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9)

text = "hi"

# print(llm(text))


from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=['food'],
    template="what are 5 vacation destination for someone to eat {food}?"
)

# print(llm(prompt.format(food="Dessert")))

#------chain

from langchain.chains import LLMChain

prompt = PromptTemplate(
    input_variables=['food'],
    template="what are 5 vacation destination for someone to eat {food}?"
)

chain = LLMChain(llm=llm, prompt=prompt)

# print(chain.run("dates"))



# # agent
# from langchain.agents import load_tools, initialize_agent

# tools = load_tools(["serpapi", "llm-math"], llm=llm)

# agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

# agent.run("who is the current leader of japan? what is the largest prime number that is smaller than their age")


# memory

from langchain import ConversationChain

conversation = ConversationChain(llm=llm, verbose=True)


conversation.predict(input="Hi there")

conversation.predict(input="I'm doing well just having a conversation with an AI")

conversation.predict(input="What was the first thing i said to you?")

conversation.predict(input="what is an alternative phrase for the first thing i said to you?")