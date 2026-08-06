from transformers import pipeline


class TextSummarizer:
    def __init__(self):
        """
        Load the summarization model.
        """
        self.summarizer = pipeline(
            "summarization",
            model="facebook/bart-large-cnn"
        )

    def summarize(self, text, max_length=120, min_length=30):
        """
        Summarize the input text.
        """

        if len(text.strip()) == 0:
            return ""

        summary = self.summarizer(
            text,
            max_length=max_length,
            min_length=min_length,
            do_sample=False
        )

        return summary[0]["summary_text"]


if __name__ == "__main__":

    sample_text = """
    Artificial Intelligence (AI) is transforming industries by automating tasks,
    improving decision-making, and enabling new innovations. Machine learning,
    natural language processing, and computer vision are among the most popular
    AI technologies. AI is widely used in healthcare, finance, education,
    transportation, and customer service. As AI continues to evolve,
    ethical considerations such as fairness, transparency, and privacy
    become increasingly important.
    """

    summarizer = TextSummarizer()

    result = summarizer.summarize(sample_text)

    print("Original Text:\n")
    print(sample_text)

    print("\nSummary:\n")
    print(result)