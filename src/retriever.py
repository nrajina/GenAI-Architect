from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class IncidentRetriever:

    def __init__(self, dataframe):

        self.df = dataframe

        # Create searchable text
        self.df["document"] = (
            self.df["LoggerName"] + " " +
            self.df["Error_Category"] + " " +
            self.df["Severity"] + " " +
            self.df["Message_Refined"]
        )

        self.vectorizer = TfidfVectorizer()
        self.vectors = self.vectorizer.fit_transform(
            self.df["document"]
        )

    def search(self, question):

        query_vector = self.vectorizer.transform([question])

        scores = cosine_similarity(
            query_vector,
            self.vectors
        )

        best_index = scores.argmax()

        return self.df.iloc[best_index]