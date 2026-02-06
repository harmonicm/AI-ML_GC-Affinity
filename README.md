# AI-ML_GC-Affinity
# 📊 Automated Investment Teaser Generator 


this project focuses on:
- Automation
- Data-to-deck transformation
- Consistent branding
- Sector-aware analytics
- Zero manual intervention

---

## 🚀 Key Features

- 📄 **Markdown → PowerPoint automation**
- 🧠 **Sector detection** (Technology, Logistics, Pharma, Manufacturing, etc.)
- 📊 **Sector-specific charts generated from data**
- ⚡ **Single-command execution**

---
## ⚙️ Requirements

- Python **3.9+**
- Library:
  - `python-pptx`
---

## 🧩 How It Works

1. **Markdown Loader**  
   Loads structured company profiles written in Markdown.

2. **Markdown Parser**  
   Extracts standardized sections (Business Description, Products, Market Size, Financials, etc.).

3. **Sector Classifier**  
   Automatically detects the company sector using keyword-based rules.

4. **PPT Generator**  
   - Creates 5-slide investment teaser decks
   - Applies Kelp branding on every slide
   - Generates sector-specific charts
   - Maintains strict anonymity

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd IITB-Hackathon

Install dependency:

pip install python-pptx

▶️ How to Run

The system is executed using one command per company.

python main.py <company-slug>

📁 Output

Generated PowerPoint decks are saved automatically in:

output/<company-slug>.pptx


