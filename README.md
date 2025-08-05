# ⚡ FastAPI ML API for Artist Advance Prediction

This project exposes a machine learning model through a REST API built with FastAPI. The model estimates advance payments for music artists based on historical earnings and metadata.

---

## 🚀 Project Overview

The API receives a JSON payload with artist data and returns the estimated advance amount. It is designed for internal tools or integration with a royalty forecasting system.

---

## 🔌 Endpoints

- `GET /status` – Check if the API is running
- `POST /predict` – Send artist data and receive the estimated advance

### 📥 Example input:
```json
{
  "royalties_last_6_months": 95431.5,
  "instagram_followers": 1200000,
  "track_release_count": 5,
  "sentiment_score": 0.72
}
```

### 📤 Example output:
```json
{
  "estimated_advance": 47600.27
}
```

---

## 🧠 Model & Workflow

- Trained with `XGBoost` or similar regression model
- Served using `FastAPI` + `pydantic` for input validation
- Deployed locally or via cloud (e.g. Azure App Service)

---

## 📁 Folder Structure

```
fastapi-ml-api/
│
├── app/
│   ├── main.py             # API entrypoint
│   ├── model.py            # Load model and prediction logic
│   └── schemas.py          # Input/output definitions
├── tests/                  # Unit tests
├── requirements.txt        # Dependencies
└── README.md
```

---

## 🧪 How to Run

1. Clone the repo:
```bash
git clone https://github.com/tu-usuario/fastapi-ml-api.git
cd fastapi-ml-api
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the API:
```bash
uvicorn app.main:app --reload
```

4. Open in browser:
```
http://localhost:8000/docs
```

---

## 📚 Tech Stack

- Python
- FastAPI
- Uvicorn
- XGBoost or Scikit-learn
- pydantic

---

## 👩‍💻 Author

**Florencia Federico**  
Data & Machine Learning Engineer  
[LinkedIn](https://www.linkedin.com/in/florenciafederico88/)
