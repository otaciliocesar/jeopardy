import pandas as pd

jeopardy_data = pd.read_csv("jeopardy.csv")
print(jeopardy_data.columns)

# Renaming misformatted columns
jeopardy_data = jeopardy_data.rename(columns = {" Air Date": "Air Date", " Round" : "Round", " Category": "Category", " Value": "Value", " Question":"Question", " Answer": "Answer"})
print(jeopardy_data.columns)
# %%
print(jeopardy_data["Question"])
# %%