# DECibits
 
DECibits is an end-to-end Telco customer churn prediction web application that combines machine learning with interactive UI visualization. It predicts whether a customer is likely to churn based on their service and demographic data. The application features a Python-based Flask backend for handling data processing and serving predictions via a RESTful API. It utilizes a pre-trained classification model built with scikit-learn to perform churn inference. On the frontend, the app offers a responsive user interface designed with Tailwind CSS and JavaScript, and includes a dynamic Gauge.js meter to visually represent churn probability in real time.

<br><br>

## ⚙️ Tech Stack

<div style="display:flex;">
<img src="https://skillicons.dev/icons?i=sklearn,python,flask,html,js,css,tailwind"/>
<img src="https://raw.githubusercontent.com/bernii/gauge.js/refs/heads/gh-pages/favicon.ico" />
</div>

<br><br>

## 🚀 Usage Guide

#### 📥 1. Clone the Repository

```bash
git clone https://github.com/thxrxsh/DECibits.git
```
```bash
cd DECibits
```

<br>

#### 📦 2. Set Up a Virtual Environment (Recommended)

Create a Environment:
```bash
python -m venv venv
```
Activate the Environment:
- linux:
  ```bash
  source venv/bin/activate
  ```
- Windows:
  ```bash
  venv\Scripts\activate
  ```

<br>

#### 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

<br>

#### ▶️ 4. Run the Application

```bash
flask run
```

You should see output like:

`* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`

<br>

#### 🌐 5. Access the App in Your Browser

```bash
http://127.0.0.1:5000/
```

