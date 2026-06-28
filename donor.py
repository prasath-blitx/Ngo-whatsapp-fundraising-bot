import csv
from datetime import datetime
import pywhatkit

# ================================================
# NGO WhatsApp Fundraising Bot
# Built for: Manavalarchi Kunriya Maruvazlvu Illam
# Developer: Prasath BJ
# ================================================

# Path to your donor CSV file
csv_path = 'donors.csv'

# UPI ID for donations
UPI_ID = "your-upi-id@bank"  # Replace with your actual UPI ID

# Date format used in CSV (example: 09.06.2024)
CSV_DATE_FORMAT = "%d.%m.%Y"

# Get today's date in day-month format
today = datetime.now().strftime("%d-%m")

print("=" * 50)
print("  NGO WhatsApp Fundraising Bot")
print(f"  Running for date: {datetime.now().strftime('%d-%m-%Y')}")
print("=" * 50)

# Open and read the CSV file
with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    reader.fieldnames = [h.strip() for h in reader.fieldnames]  # Clean headers

    rows = list(reader)
    print(f"\n Total donors loaded: {len(rows)}")

    matched = 0

    for row in rows:
        # Clean keys and values
        row = {k.strip(): v.strip() for k, v in row.items()}

        date_str = row.get('date')
        if not date_str:
            continue

        try:
            donor_date = datetime.strptime(date_str, CSV_DATE_FORMAT).strftime("%d-%m")
        except ValueError:
            print(f"❌ Date format error in row: {row}")
            continue

        # Compare today's date with donor date
        if donor_date == today:
            matched += 1
            name = row.get('name', 'Donor').upper()
            occasion = row.get('occasion', 'Special Day')

            raw_phone = row.get('phone', '').replace(" ", "").replace("+", "").strip()
            if not raw_phone.isdigit():
                print(f"❌ Invalid phone number: {raw_phone}")
                continue

            # Ensure phone number includes country code
            if not raw_phone.startswith("91"):
                raw_phone = "91" + raw_phone
            phone = "+" + raw_phone

            # Personalized Tamil message
            message = f"""
அன்புடையீர் வணக்கம்! 🙏
🎉இந்த மாதத்தில் ஒரு நாள் உங்களுக்கு முக்கியமான நாள்.🎉
அந்த நாளை மனவளர்ச்சி குன்றிய குழந்தைகளுக்கான பள்ளிக் காப்பகத்தில்
அன்னதானம் செய்யும் புண்ணிய வாய்ப்பை ஏற்படுத்தி, இறைவனிடம் நன்றியுடன் வேண்டுகிறோம்🙏

🙏தங்களுடைய கடந்த உதவிக்கு நன்றி🙏

இன்று மீண்டும் இணைந்து கொள்ள விரும்புகிறோம்💖

உங்கள் சிறிய உதவியும், ஒரு பெரிய மகிழ்ச்சியாக மாறும்! 💖
(UPI: {UPI_ID})

வாழ்த்துக்கள் மற்றும் வாழ்வில் வளம் பெருக வாழ்த்துகிறோம்!🎉

இப்படிக்கு
மனவளர்ச்சி குன்றிய மறுவாழ்வு இல்லம் - கீரனூர்
"""

            print(f"\n📤 Sending message to {name} ({phone})...")

            try:
                pywhatkit.sendwhatmsg_instantly(
                    phone_no=phone,
                    message=message,
                    wait_time=20,
                    tab_close=True,
                    close_time=180
                )
                print(f"✅ Message sent successfully to {name} ({phone})")
            except Exception as e:
                print(f"⚠️ Failed to send to {name} ({phone}). Error: {e}")

    if matched == 0:
        print("\n✅ No donors with today's occasion. Bot finished.")
    else:
        print(f"\n✅ Done! Messages sent to {matched} donor(s).")
