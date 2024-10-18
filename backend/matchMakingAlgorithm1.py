import pdfminer.high_level as pdf
import docx2txt
import re
import subprocess
import nltk
import tkinter as tk
from tkinter import filedialog
from collections import Counter

nltk.download('stopwords')
nltk.download('punkt')

EMAIL_REG = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')
PHONE_REG = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')

SKILLS_DB = [
    'machine learning',
    'data science',
    'python',
    'word',
    'excel',
    'English',
]

def extract_text_from_pdf(pdf_path):
    return pdf.extract_text(pdf_path)

def extract_text_from_docx(docx_path):
    txt = docx2txt.process(docx_path)
    if txt:
        return txt.replace('\t', ' ')
    return None

def extract_emails(resume_text):
    return re.findall(EMAIL_REG, resume_text)

def extract_phone_number(resume_text):
    phone = re.findall(PHONE_REG, resume_text)
    if phone:
        number = ''.join(phone[0])
        if resume_text.find(number) >= 0 and len(number) < 16:
            return number
    return None

def extract_skills(input_text):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    word_tokens = nltk.tokenize.word_tokenize(input_text)

    # Remove the stop words
    filtered_tokens = [w for w in word_tokens if w not in stop_words]

    # Remove the punctuation
    filtered_tokens = [w for w in filtered_tokens if w.isalpha()]

    # Generate bigrams and trigrams (e.g., "artificial intelligence")
    bigrams_trigrams = list(map(' '.join, nltk.everygrams(filtered_tokens, 2, 3)))

    # Create a set to keep the results
    found_skills = set()

    # Search for each token in the skills database
    for token in filtered_tokens:
        if token.lower() in SKILLS_DB:
            found_skills.add(token)

    # Search for each bigram and trigram in the skills database
    for ngram in bigrams_trigrams:
        if ngram.lower() in SKILLS_DB:
            found_skills.add(ngram)

    return found_skills

def count_words(text):
    # Tokenize the text
    words = nltk.tokenize.word_tokenize(text)
    # Count occurrences of each word (case insensitive)
    word_count = Counter(word.lower() for word in words if word.isalpha())
    return dict(word_count)

def main(file_path):
    # Extract text from PDF or DOCX
    try:
        if file_path.endswith('.pdf'):
            text = extract_text_from_pdf(file_path)
        elif file_path.endswith('.docx'):
            text = extract_text_from_docx(file_path)
        else:
            print("Unsupported file type")
            return

        if text is None:
            print("Failed to extract text from the file.")
            return

        # Extract phone number from text
        phone_number = extract_phone_number(text)
        print("Phone Number:", phone_number)

        # Extract emails from text
        emails = extract_emails(text)
        if emails:
            print("Email:", emails[0])

        # Extract skills from text
        skills = extract_skills(text)
        print("Skills:", skills)

        # Count words and return a dictionary of word counts
        word_count_dict = count_words(text)
        print("Word Count Dictionary:", word_count_dict)

    except Exception as e:
        print(f"An error occurred: {e}")

def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(
        title="Select a PDF or DOCX file",
        filetypes=[("PDF files", "*.pdf"), ("DOCX files", "*.docx")]
    )
    return file_path

if __name__ == '__main__':
    # Use the file selection dialog to get the file path
    file_path = "C:\\Users\\advk2\\OneDrive\\Documents\\CSTL-LabCoat-\\backend\\ADVAITKHOPADE(RESUME).pdf"
    if file_path:
        main(file_path)
    else:
        print("No file selected.")