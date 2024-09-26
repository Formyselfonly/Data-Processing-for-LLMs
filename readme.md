

# Project about Data Pre-processing

- https://github.com/modelscope/data-juicer
- https://github.com/katanaml/sparrow
- https://github.com/stochasticai/xTuring
- https://github.com/labring/FastGPT 
  FastGPT have the feature about data processing

# Data Processing steps

1. Data Collection

2. Data Pre-processing

   1. Data cleaning

      1. Handling missing values
      2. Noise reduction
      3. Consistency checks Consistency checks ensure the data across the dataset adheres to consistent formats, rules, or conventions
      4. Deduplication

   2. Data Feature Engineeing 说白了就是特征提取

      ```python
      
      data = {
          'date': ['2024-01-01', '2024-01-02', '2024-01-03'],
          'category': ['A', 'B', 'A'],
          'value': [10, 20, 30]
      }
      df = pd.DataFrame(data)
      
      df['date'] = pd.to_datetime(df['date'])
      df['year'] = df['date'].dt.year
      df['month'] = df['date'].dt.month
      df['day'] = df['date'].dt.day
      ```

   3. Data Parsing Data parsing is converting data from one format to another. Widely used for data structuring, it is generally done to make the existing, often unstructured, unreadable data more comprehensible.

   4. Data Normalization Normalization is a crucial pre-processing technique for standardizing textual data to ensure uniformity and consistency in language usage and minimize complexity for NLP models. This process involves converting text to a common case, typically lowercase, to eliminate variations arising from capitalization.

3. Data Storage

4. Data Analysis 
   To show  insights with team which often using Data Visualization (Data visualization is a part of the data analysis , helping to present insights clearly to the team.)

# Data pre processing example demo

Here's an example that combines Retrieval-Augmented Generation (RAG) using Langchain with a language model and data processing. This example will demonstrate how to preprocess data, set up a retrieval mechanism, and generate answers using a language model.

## Code-LLM+RAG+Data Processing+LangChain

```code
pip install langchain transformers pandas
```

```code
import pandas as pd
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

# 1. Create a sample dataset
data = {
    'context': [
        "The capital of France is Paris.",
        "Jane Austen wrote 'Pride and Prejudice'.",
        "The blue whale is the largest mammal."
        "......"
    ]
}

df = pd.DataFrame(data)

# 2. Data preprocessing: convert context to a list
contexts = df['context'].tolist()

# 3. Create an OpenAI embedding model
embedding_model = OpenAIEmbeddings()

# 4. Build a vector store using FAISS
vectorstore = FAISS.from_texts(contexts, embedding_model)

# 5. Initialize the Langchain Retrieval-Generation Chain using OpenAI's model
llm = OpenAI(model_name="gpt-3.5-turbo")  # Change to "gpt-4" if you have access
retrieval_qa = RetrievalQA(llm=llm, retriever=vectorstore.as_retriever())

# 6. Use the model for inference
questions = [
    "What is the capital of France?",
    "Who wrote 'Pride and Prejudice'?",
    "What is the largest mammal?"
]

for question in questions:
    answer = retrieval_qa.run(question)
    print(f"Q: {question}\nA: {answer}\n")

```

## Explanation

1. **Create a Sample Dataset**: We define a simple dataset with contexts that will provide answers.
2. **Data Preprocessing**: Convert the context column to a list for easier handling.
3. **Create an Embedding Model**: Use a OpenAIEmbeddings model to create embeddings for the contexts.
4. **Build a Vector Store**: Use FAISS to index the embedded contexts for efficient retrieval.
5. **Initialize the RAG Chain**: Use Langchain to combine the retrieval and generation processes with OpenAI's language model.
6. **Inference**: Loop through predefined questions, retrieve relevant contexts, and generate answers.

# Pre processing tech code

The pre processing technology code can be found in the code folder.