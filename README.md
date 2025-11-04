```markdown
# Immutable Emotion Journal  
### Capture Real Moments — No Edits, No Deletes

> **"Every note is a snapshot of your soul. Editing or deleting it means erasing a piece of your true self."**

This is a **real, unchangeable journal**.  
You can **only write** — **no editing, no deleting**.  
The dashboard shows **live sentiment analysis** (positive, negative, neutral) of all your notes.

---

## Why No Edit or Delete?

| Action | Consequence |
|-------|-------------|
| **Editing a note** | Distorts the raw emotion of the moment |
| **Deleting a note** | Escapes the experience → risk of repeating mistakes |
| **Write-once, forever** | Deep self-awareness through untouched data |

> **Goal: Self-discovery through raw, honest records**

---

## Features

- Write notes (create-only)  
- English sentiment analysis (positive, negative, neutral)  
- Live analytics dashboard with charts  
- Secure login with **Google**  
- Permanent, tamper-proof storage  

---

## Requirements

- Python 3.8+
- Google Cloud Console (for Google login)

---

## Setup & Installation

### 1. Clone the Project

```bash
git clone https://github.com/username/immutable-journal.git
```

### 2. Create `.env` File

In the project root, create a `.env` file and add your Google OAuth credentials:

```env
CLIENT_ID=your-google-client-id.apps.googleusercontent.com
SECRET_ID=your-google-client-secret
```

> Get these from [Google Cloud Console](https://console.cloud.google.com/)

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Collect Static Files

```bash
python3 manage.py collectstatic
```

---

### 5. Run Database Migrations

```bash
python3 manage.py makemigrations core
python3 manage.py migrate
```

---

### 6. Start the Server

```bash
python3 manage.py runserver
```

Visit:  
[http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Google Login Setup (One-Time)

1. Go to [Google Cloud Console](https://console.cloud.google.com/)  
2. Create an **OAuth 2.0 Client ID** (type: **Web application**)  
3. Under **Authorized redirect URIs**, add **exactly** these two:

```
http://localhost:8000/auth/complete/google-oauth2/
http://127.0.0.1:8000/auth/complete/google-oauth2/
```

> Then copy `CLIENT_ID` and `CLIENT_SECRET` into your `.env` file.

---

## Dashboard

- **Line Chart**: Emotion distribution (positive / negative / neutral)  

---

## Project Structure

```
immutable-journal/
|__ codfig/        # Settings
├── core/          # Note creation + sentiment analysis
├── templates/     # HTML templates
├── .env           # (ignored in .gitignore)
├── manage.py
└── requirements.txt
```

---

## Developer

- [MohammadRezaMahdian]  
- [github.com/PyRz-Tech](https://github.com/PyRz-Tech)

---

## License

MIT © 2025

---
