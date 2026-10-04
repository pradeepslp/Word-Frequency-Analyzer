# 📊 Word Frequency Analyzer

A modern, fast, and interactive **Word Frequency Analyzer** built with **Python** and **Streamlit**. It allows you to analyze paragraphs of text, compute statistical metrics, view word distributions in interactive tables, and visualize word counts with bar charts.

---

## ✨ Features

- **Text Input Area**: Easily type or paste paragraphs of any size.
- **Case-Insensitive & Punctuation Stripping**: Words are converted to lowercase and cleaned of punctuation marks automatically using regex.
- **Key Summary Metrics**:
  - **Total Words**: Total count of all parsed words.
  - **Unique Words**: Number of distinct vocabulary terms.
  - **Most Frequent Word**: Highlights the top-occurring word (or handles ties gracefully) with occurrence count.
  - **Lexical Diversity**: Ratio of unique words to total words as a percentage.
- **Visual Word Frequency Chart**: Interactive Altair bar chart displaying the top-ranking words with adjustable display limits and sorting.
- **Interactive Data Table**: View all words with Rank, Word, Frequency count, and Percentage share with sorting and filtering.
- **CSV Data Export**: One-click download of the complete word frequency table.
- **Sample Presets**: Quick-load sample texts from the sidebar for instant testing.
- **Empty State & Edge Case Handling**: Gracefully handles empty inputs, spaces, and non-alphanumeric characters.
- **Zero Paid APIs**: Runs 100% locally and offline without external API keys.

---

## 📁 Project Structure

```
Word Frequency Analyzer/
│
├── app.py              # Main Streamlit application logic and UI
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation and setup guide
```

---

## 🚀 Getting Started (Windows & VS Code)

Follow these step-by-step instructions to set up and run the application locally on Windows.

### Prerequisites

Ensure you have **Python 3.8+** installed. You can check your version by running:
```powershell
python --version
# or
py --version
```

---

### Step 1: Open the Project in VS Code

1. Open **Visual Studio Code**.
2. Go to **File** > **Open Folder...** and select the `Word Frequency Analyzer` directory.
3. Open a terminal in VS Code using the shortcut: <kbd>Ctrl</kbd> + <kbd>`</kbd> (or go to **Terminal** > **New Terminal**).

---

### Step 2: Create and Activate a Virtual Environment (Recommended)

In your VS Code terminal (PowerShell), run:

```powershell
# Create virtual environment (using python or py)
python -m venv venv
# or: py -m venv venv

# Activate virtual environment in PowerShell
.\venv\Scripts\Activate.ps1
```

> **Note for PowerShell execution policy:** If you encounter a script execution error, run:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
> .\venv\Scripts\Activate.ps1
> ```
> Or if using Command Prompt (cmd):
> ```cmd
> venv\Scripts\activate.bat
> ```

---

### Step 3: Install Dependencies

Install the required Python packages using `pip`:

```powershell
pip install -r requirements.txt
```

---

### Step 4: Run the Streamlit Application

Start the application with the following command:

```powershell
streamlit run app.py
```

Streamlit will launch the web application and automatically open your default browser at:
```
http://localhost:8501
```

---

## 🛠️ Technologies Used

- **[Python](https://www.python.org/)** (Core Logic)
- **[Streamlit](https://streamlit.io/)** (Web Interface & Dashboard)
- **[Pandas](https://pandas.pydata.org/)** (Data manipulation and table structure)
- **[Altair](https://altair-viz.github.io/)** (Interactive visualizations)

---

## 📄 License

This project is open-source and free to use for personal and educational purposes.
