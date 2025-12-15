# 🌐 Web Scraping with Python (Beginner Friendly)

## 📌 Project Overview

This project demonstrates **web scraping using Python** with the `requests` and `BeautifulSoup` libraries.
The goal is to **download web pages, extract useful information, and scrape structured data** such as links, images, and HTML tables.

This project is designed for **beginners** and follows a **step-by-step, practical approach**, making it ideal for learning and portfolio use.

---

## 🎯 Objectives

By completing this project, you will learn how to:

* Download a webpage using the `requests` module
* Parse HTML using `BeautifulSoup`
* Scrape all links (`<a>` tags) from a webpage
* Scrape all image URLs (`<img>` tags) from a webpage
* Extract structured data from HTML tables
* Understand real-world web scraping workflows

---

## 🛠️ Technologies & Tools Used

* **Python 3**
* **Requests** – for downloading web pages
* **BeautifulSoup (bs4)** – for parsing and scraping HTML
* **PyCharm / VS Code / Jupyter Notebook** (any Python IDE)

---

## 📂 Project Structure

```text
web-scraping-lab/
│
├── web_scraping.py        # Main Python script
├── README.md              # Project documentation
└── requirements.txt       # Required Python libraries
```

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/web-scraping-lab.git
cd web-scraping-lab
```

### 2️⃣ Install Required Libraries

```bash
pip install requests beautifulsoup4
```

Or using `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## 🌍 URLs Used in This Project

### IBM Website (Links & Images)

```text
http://www.ibm.com
```

### HTML Table Dataset (Color Codes)

```text
https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html
```

---

## 🧪 Step-by-Step Functionality

### 1️⃣ Download a Webpage

```python
import requests

url = "http://www.ibm.com"
data = requests.get(url).text
```

---

### 2️⃣ Parse HTML Using BeautifulSoup

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(data, "html.parser")
```

---

### 3️⃣ Scrape All Links from the Page

```python
for link in soup.find_all('a'):
    print(link.get('href'))
```

---

### 4️⃣ Scrape All Image URLs

```python
for img in soup.find_all('img'):
    print(img.get('src'))
```

---

### 5️⃣ Scrape Data from an HTML Table

#### Download and Parse Table Page

```python
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
data = requests.get(URL).text
soup = BeautifulSoup(data, "html.parser")
```

#### Extract Table Data

```python
table = soup.find('table')

for row in table.find_all('tr'):
    cols = row.find_all('td')
    if len(cols) >= 4:
        color_name = cols[2].getText()
        color_code = cols[3].getText()
        print(f"{color_name} ---> {color_code}")
```

---

## 📊 Sample Output

```text
AliceBlue ---> #F0F8FF
AntiqueWhite ---> #FAEBD7
Aqua ---> #00FFFF
```

---

## 🚀 How to Run the Project

```bash
python web_scraping.py
```

Make sure you have an active internet connection.

---

## ⚠️ Important Notes

* Always inspect a webpage before scraping it
* Respect website terms and robots.txt
* This project is for **educational purposes**
* Avoid scraping sensitive or restricted data

---

## 📈 Skills Demonstrated

* Web scraping fundamentals
* HTML structure understanding
* Data extraction techniques
* Python automation
* Real-world data collection skills

---

## 🎓 Learning Outcome

This project builds a strong foundation for:

* Job market analysis
* API & web data collection
* Data analytics capstone projects
* Dashboard and reporting workflows

---

## 👤 Author

**Your Name**

Varrun Vashisht
Aspiring Data Analyst

---

## 📄 License

This project is for educational use only.
Dataset and lab content © IBM Corporation.







