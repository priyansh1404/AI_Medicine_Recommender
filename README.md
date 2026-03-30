# 💊 AI Medicine Recommender

A lightweight, AI-powered command-line tool that recommends over-the-counter (OTC) medications based on your described symptoms — no internet connection or external libraries required.

---

## 📌 What It Does

You type in a symptom (e.g., *"headache"*, *"loose motion"*, *"dry cough"*), and the assistant intelligently matches it to a known condition using fuzzy string matching, then suggests an appropriate OTC medication along with a brief explanation.

**Covered Categories:**
- 🫁 Respiratory & Cold
- 🍽️ Digestive System
- 🩹 Skin & First Aid
- 👁️ Eye & Ear Care
- 💢 Pain & General

---

## 🚀 Getting Started

### Prerequisites

- Python **3.6 or higher**
- No third-party packages needed — uses only Python's standard library

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/priyansh1404/VITyarthi_AI&ML_Project.git
   cd VITyarthi_AI&ML_Project
   ```

2. **Run the script directly:**
   ```bash
   python medicine_recommender.py
   ```

That's it — no `pip install`, no virtual environment setup required.

---

## 🖥️ How to Use

Once you run the script, you'll see:

```
========================================
      AI MEDICINE RECOMMENDER
========================================

[Categories: Respiratory, Digestive, Skin, Eye/Ear, Pain]
Describe your symptom (or 'quit'):
```

**Step 1:** Type your symptom in plain English.  
**Step 2:** The AI matches it and displays the recommended medication.  
**Step 3:** Type `quit` or `exit` to close the program.

### Example Session

```
Describe your symptom (or 'quit'): headche

🔍 AI matched your symptom to: Headache
💊 Recommended OTC: Ibuprofen (Advil) or Aspirin
ℹ️  Details: Relieves tension and inflammatory pain.
----------------------------------------
DISCLAIMER: This is not a substitute for professional medical advice.
If the problem is serious, consult a doctor as soon as possible.
```

> ✅ Notice that even with the typo "headche", the AI correctly identifies "Headache" — thanks to fuzzy matching.

---

## 🧠 How It Works

The core matching logic uses Python's built-in [`difflib`](https://docs.python.org/3/library/difflib.html) module:

```python
difflib.get_close_matches(user_query.title(), self.symptoms, n=1, cutoff=0.4)
```

- **`user_query.title()`** — normalizes input to title case for consistent matching
- **`n=1`** — returns only the single best match
- **`cutoff=0.4`** — minimum similarity ratio; low enough to handle typos, high enough to avoid false matches

The knowledge base (`medical_kb`) is a Python dictionary with 30+ conditions mapped to their recommended medications and descriptions.

---

## 📁 Project Structure

```
VITyarthi_AI&ML_Project/
│
├── medicine_recommender.py   # Main script (knowledge base + AI logic + interaction loop)
└── README.md                 # This file
```

---

## ⚠️ Disclaimer

> This tool is intended for **educational and informational purposes only**.  
> It is **not** a substitute for professional medical advice, diagnosis, or treatment.  
> Always consult a qualified healthcare provider for any medical concerns.

---

## 🛠️ Extending the Project

Want to add more symptoms? Simply add entries to the `medical_kb` dictionary in this format:

```python
"Symptom Name": {
    "med": "Medication Name (Brand)",
    "info": "Brief description of how it helps."
},
```

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
