from transformers import pipeline

class SummarizationService:
    """AI-based Summarization using BART Transformer"""
    
    def __init__(self):
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    def summarize_text(self, text: str, max_length=150) -> str:
        """Summarizes extracted text"""
        if len(text.split()) < 50: 
            return text
        
        summary = self.summarizer(text, max_length=max_length, min_length=50, do_sample=False)
        return summary[0]['summary_text']
