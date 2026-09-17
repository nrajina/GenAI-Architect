import pandas as pd
from src.preprocess import refine_message, classify_log
from src.retriever import IncidentRetriever

df = pd.read_csv("data/JobFailures_masked_refined.csv")

# AI friendly summary
df["Message_Refined"] = df["Message"].apply(refine_message)

# New AI columns
df[["Error_Category", "Severity", "Recommended_Action"]] = (
    df["Message"]
      .apply(classify_log)
      .apply(pd.Series)
)

print(
    df[
        [
            "LogDt",
            "LoggerName",
            "Error_Category",
            "Severity",
            "Message_Refined",
        ]
    ].tail(5).to_string(index=False)
)
retriever = IncidentRetriever(df)

question = input("\nAsk a production support question: ")

result = retriever.search(question)

print("\n" + "="*60)
print(" MOST RELEVANT INCIDENT ")
print("="*60)

print(f"Date       : {result['LogDt']}")
print(f"Application: {result['LoggerName']}")
print(f"Category   : {result['Error_Category']}")
print(f"Severity   : {result['Severity']}")

print("\nSummary")
print(result["Message_Refined"])

print("\nRecommendation")
print(result["Recommended_Action"])