import pandas as pd

# Use the full file path
file_path = '/Users/aakanksharaj/Downloads/usecase.csv'
df = pd.read_csv(file_path)
df = df.fillna("")
df.columns = df.columns.str.strip()
text_col = []

for _, row in df.iterrows():
    prompt = "below is set of use cases that provides details of the use case and hence provides the process flow for the same"
    use_case = str(row["use_case"])
    input_query = str(row["details"])
    response = str(row["process_flow"])
    if len(input_query.strip())==0:
        text = (prompt 
                + "### use case:\n" 
                + use_case 
                + "\n### process flow\n" 
                + response)
        
        
    else:
        text = (prompt 
                + "### use case:\n" 
                + use_case + "\n details\n" 
                + input_query 
                + "\n### process flow\n" 
                + response)
    text_col.append(text)

df.loc[:, "text"] = text_col
print(df.head())   

df.to_csv("train.csv", index=False)