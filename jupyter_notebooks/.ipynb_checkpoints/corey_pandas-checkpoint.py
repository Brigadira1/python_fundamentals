import pandas as pd

df = pd.read_csv("./jupyter_notebooks/survey_results_public.csv")
df_schema = pd.read_csv("./jupyter_notebooks/survey_results_schema.csv")

pd.set_option("display.max.columns", 31)
pd.set_option("display.max.rows", 100)

# df.shape
# df.info()
print(df.head(10))
# df.columns
#
# df.loc[0:100, "LearnCode"]
