# # from langchain_ollama import OllamaEmbeddings
# # from langchain_chroma import Chroma
# # from langchain_core.documents import Document
# # import os
# # import pandas as pd

# # df = pd.read_csv("data/realistic_restaurant_reviews.csv")
# import os
# print(os.path.getsize("data/realistic_restaurant_reviews.csv"))
import pandas as pd

df = pd.read_csv("data/realistic_restaurant_reviews.csv")
print(df.head())
print(df.shape)
print(df)