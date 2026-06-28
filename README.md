# 🤖 NGO WhatsApp Fundraising Bot

An automated WhatsApp messaging bot built for a real NGO to send personalized Tamil fundraising messages to donors on their special occasions.

---

## 💡 How It Works

1. Reads donor data (name, phone, occasion, date) from a CSV file
2. Checks if today's date matches any donor's special occasion
3. Automatically opens WhatsApp Web and sends a personalized Tamil message
4. Logs all sent messages with timestamp

---

## ✨ Features

- Reads donor list automatically from CSV
- Matches today's date with donor occasions (birthdays, anniversaries etc.)
- Sends heartfelt personalized Tamil language messages
- Auto-closes WhatsApp tab after sending
- Handles invalid phone numbers and date format errors gracefully
- Console log showing success/failure for each message

---

## 🛠️ Tools & Libraries

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| pywhatkit | WhatsApp Web automation |
| csv | Reading donor data |
| datetime | Date matching logic |
| Windows | Runs as a daily scheduled task |

---

## 🌍 Real World Impact

Built and **deployed for a real NGO:**

> **Manavalarchi Kunriya Maruvazlvu Illam, Keeranur**
> Helping children with intellectual disabilities

This bot has successfully sent fundraising messages to real donors, helping raise funds for children in need.

---

## 🚀 Setup & Usage

### 1. Install required library
```bash
pip install pywhatkit
```

### 2. Add donor details to donors.csv
```
name,phone,occasion,date
Donor Name,919000000000,Birthday,06.06.2025
```

### 3. Update your UPI ID in donor.py
```python
UPI_ID = "your-upi-id@bank"
```

### 4. Run the script
```bash
python donor.py
```

### 5. Automate daily (Windows Task Scheduler)
- Open Task Scheduler
- Create Basic Task
- Set trigger: Daily at 9:00 AM
- Action: Run `python donor.py`

---

## 📁 Project Structure

```
ngo-whatsapp-fundraising-bot/
├── donor.py          # Main bot script
├── donors.csv        # Donor database (sample data)
└── README.md         # Project documentation
```

---

## 📋 Sample CSV Format

| name | phone | occasion | date |
|------|-------|----------|------|
| Rajesh Kumar | 919000000001 | Birthday | 06.06.2025 |
| Meena Devi | 919000000002 | Wedding Anniversary | 15.07.2025 |

---

## 👨‍💻 Developer

**Prasath BJ**
Aspiring Data Analyst | Python Developer
📧 prasath12c310@gmail.com
🔗 [GitHub](https://github.com/prasath-blitx)

---

## ⚠️ Note
This repo uses sample donor data. Real donor information is kept private for data protection.
