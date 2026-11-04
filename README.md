# 🌱 KrishiSense: AI Crop Recommendation Web App

KrishiSense helps farmers decide **what to sow**. The user enters soil nutrients and weather readings, and a trained Random Forest model suggests the three best-suited crops out of 22, with a confidence score, growing tips and plain-language soil advice.

Built with **Django**, **scikit-learn** and a responsive, mobile-friendly interface.

**Live demo:** _add your link here, e.g. https://yourname.pythonanywhere.com_

<!-- Add screenshots to a /screenshots folder and uncomment:
![Home](screenshots/home.png)
![Result](screenshots/result.png)
-->

---

## Features

**Accounts**
- Sign up, log in and log out
- Change password (secure Django authentication)
- Show/hide password eye icon on every password field

**Crop prediction**
- Seven inputs with linked sliders and number boxes: N, P, K, temperature, humidity, pH and rainfall
- One-tap example fields (wet paddy land, dry pulse land, warm and humid, cool hill orchard)
- Input validation within the ranges the model was trained on
- Top 3 crops with confidence percentages

**Extra information for farmers**
- Season, duration and water need for each recommended crop, plus a practical growing tip
- Soil notes: acidic or alkaline soil, low N/P/K, heavy rain, high humidity and heat stress
- Searchable crop guide for all 22 crops, filterable by season and water need
- Crop names in English and Hindi
- Prediction history per user, with delete
- Responsive layout for desktop and mobile, with an advisory warning in the footer

---

## Tech stack

| Layer | Tools |
|---|---|
| Backend | Python, Django |
| Machine learning | scikit-learn (RandomForestClassifier, 200 trees), NumPy, pandas |
| Database | SQLite |
| Frontend | HTML, CSS, vanilla JavaScript |

---

## How the model works

The model (`advisor/ml/Crop_recommender_Rf.pkl`) is a Random Forest classifier trained on seven features:

| Feature | Meaning | Training range used in the form |
|---|---|---|
| N | Nitrogen in soil | 0 – 140 |
| P | Phosphorus in soil | 5 – 145 |
| K | Potassium in soil | 5 – 205 |
| temperature | °C | 8 – 44 |
| humidity | % | 14 – 100 |
| ph | Soil pH | 3.5 – 9.9 |
| rainfall | mm | 20 – 300 |

It predicts one of 22 crops: apple, banana, blackgram, chickpea, coconut, coffee, cotton, grapes, jute, kidneybeans, lentil, maize, mango, mothbeans, mungbean, muskmelon, orange, papaya, pigeonpeas, pomegranate, rice and watermelon.

The app calls `predict_proba` and shows the three most probable crops. A low top percentage means several crops suit the field about equally well.

> **Dataset:** _add the source of your training data and your model's accuracy here._

---

## Getting started

**Requirements:** Python 3.10 or newer.

```bash
# 1. Clone
git clone https://github.com/<your-username>/KrishiSense.git
cd KrishiSense

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create the database
python manage.py migrate

# 5. Run
python manage.py runserver
```

Open http://127.0.0.1:8000, create an account and click **Find my crop**.

> The model was saved with **scikit-learn 1.6.1**, so that version is pinned in `requirements.txt`. Other versions may load it with a warning or fail.

**Optional:** `python manage.py createsuperuser` gives you access to the admin panel at `/admin/`.

---

## Project structure

```
KrishiSense/
├── manage.py
├── requirements.txt
├── cropsite/                 # Django project settings and root URLs
└── advisor/                  # Main app
    ├── ml/
    │   └── Crop_recommender_Rf.pkl   # Trained model
    ├── ml.py                 # Loads the model, predicts, builds soil notes
    ├── crop_data.py          # Season, water need, tips and Hindi names
    ├── forms.py              # Login, sign-up, password and prediction forms
    ├── models.py             # Prediction history
    ├── views.py
    ├── urls.py
    ├── templates/advisor/    # HTML pages
    └── static/advisor/       # CSS, JavaScript, logo, crop images
```

### Using real crop photos
Add images named after the model's labels (`rice.jpg`, `mango.jpg`, …) to `advisor/static/advisor/img/crops/`. They automatically replace the emoji icons.

---

## Deployment

Before going live, set these environment variables:

| Variable | Purpose |
|---|---|
| `DJANGO_SECRET_KEY` | A long random secret string |
| `DJANGO_DEBUG` | `0` in production |
| `DJANGO_ALLOWED_HOSTS` | Your domain, comma-separated |

Also add `STATIC_ROOT = BASE_DIR / "staticfiles"` to `settings.py` and run `python manage.py collectstatic`. This project has been deployed on PythonAnywhere.

---

## Disclaimer

KrishiSense gives **guidance only**. It is not a guarantee of yield. Confirm with a local soil test or your nearest Krishi Vigyan Kendra (KVK) or agriculture officer before sowing.

The model file is a Python pickle. Only load pickle files you created or fully trust.

---

## Future improvements

- Full Hindi and regional-language interface
- Live weather and rainfall lookup by location
- PDF export of results
- Fertiliser quantity suggestions

---


## Author

**Your Name**: [GitHub](https://github.com/your-username) · [LinkedIn](https://linkedin.com/in/your-profile)
