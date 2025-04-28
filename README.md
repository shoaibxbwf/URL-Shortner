# 📦 URL Shortener App

A simple and clean **Python Flask** app to shorten your long URLs easily!

Frontend is made with **HTML + TailwindCSS**.  
Backend is powered by **Flask (Python)**.
## 📂 Project Structure
your_project/
├── app.py
└── home_pages/
    └── index.html
- `app.py` → Flask Python application
- `home_pages/index.html` → Frontend page (served by Flask)
## 🛠 How to Run (Step-by-Step)

1. **Open Terminal or Command Prompt**  
   (📍 Go to your project folder where `app.py` is present)

2. **Install Flask** (only first time)

```bash
pip install flask
3. **Run the App**

```bash
python app.py

or if you accidentally typed wrong like `python.Ap` (no problem!), just type again correctly:

```bash
python app.py

✅ After running, Flask will show something like:

```
 * Running on http://127.0.0.1:5000
```

4. **Open Browser**

Go to the address shown →  
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

5. **Use the App**

- Paste your long URL
- Click `Shorten URL`
- Copy your short link!
- Share it anywhere 🚀

---

## 📋 Features

- Clean simple UI (TailwindCSS)
- Copy Button to copy short URL
- Clear Button to empty the input fields
- Redirection to original URL when opening short link
- All data stored temporarily in memory
- `/clear` endpoint to delete all saved links

---

## ⚡ Notes

- App runs **locally** only (localhost).
- If you restart app, all shortened links will reset (stored only in RAM).
- Folder `home_pages/` must be next to `app.py`.
- This project is for **learning purposes** — not production ready.

---

## 🚀 Quick Commands

| Action | Command |
|:--|:--|
| Install Flask | `pip install flask` |
| Run App | `python app.py` |
| Open App | Visit [http://localhost:5000](http://localhost:5000) in browser |

---

## 🧠 Extra Tip

If you want **to auto-open browser** after `python app.py`, you can modify the code slightly

# ✅ That's it!
Enjoy shortening your URLs with your own personal app!  
Have fun building more projects 🚀🎯
