📄 ResumeIQ (NLP)

An NLP-based web application that extracts relevant skills from resumes using intelligent text processing techniques.


## 🚀 Overview

Recruiters often scan resumes quickly to identify key skills. This project automates that process by extracting important skills from a PDF resume using Natural Language Processing.

Upload a resume → get a list of detected skills instantly.


## ✨ Features

* 📂 Upload PDF resumes
* 🧠 NLP-based text preprocessing
* 🎯 Skill extraction using pattern matching
* 🔍 Improved detection using Named Entity Recognition (NER)
* ⚡ Fast and simple web interface using Streamlit


## 🧠 NLP Concepts Used

* Tokenization
* Lemmatization
* Stopword Removal
* Phrase Matching
* Named Entity Recognition


## 🛠️ Tech Stack

* Python
* spaCy
* Streamlit
* pdfplumber

---

📁 Project Structure


resume-skill-extractor/
│
├── data/
│   └── skills_list.txt
│
├── src/
│   ├── pdf_extractor.py
│   ├── preprocessing.py
│   ├── skill_extractor.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

⚙️ How It Works

1. Upload a resume (PDF)
2. Extract text using pdfplumber
3. Clean and preprocess text using spaCy
4. Match skills using PhraseMatcher
5. Enhance detection using NER
6. Display extracted skills

▶️ Run Locally

bash
git clone https://github.com/rudrakshibedi/ResumeIQ.git
cd resume-skill-extractor
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py

📌 Example Output


Extracted Skills:
python, machine learning, sql, data analysis

🎯 Use Cases

* Resume screening automation
* HR tech tools
* Personal resume analysis
* NLP learning project

 🔮 Future Improvements

* Match resume with job descriptions
* Skill ranking / scoring system
* Support for DOCX files
* Deployment on cloud (Streamlit Cloud)

👩‍💻 Author

Rudrakshi Bedi

 ⭐ If you found this useful

Give this repo a star and share it!
