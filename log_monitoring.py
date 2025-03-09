import os
import smtplib
from email.mime.text import MIMEText

# Configuration
LOG_FILE = "D:\\Python_Github_projects\\logg_monitoring\\server1.log"  # Path to your log file
WARNING_KEYWORD = "WARNING"
ERROR_KEYWORD = "ERROR"

# Email configuration (update with your actual Gmail details)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "abc@gmail.com"
EMAIL_PASSWORD = "1234"  # Use your generated App Password
EMAIL_RECEIVER = "abc@gmail.com"

def send_email_alert(message):
    msg = MIMEText(message)
    msg['Subject'] = "Log Alert: Warning and Error Detected"
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        server.quit()
        print("Email alert sent!")
    except Exception as e:
        print("Failed to send email:", e)

def read_log_file():
    if not os.path.exists(LOG_FILE):
        print("Log file not found!")
        return None
    with open(LOG_FILE, "r") as file:
        return file.read()

def main():
    content = read_log_file()
    if content is None:
        return

    lines = content.splitlines()
    # Collect warnings and errors separately
    warnings = [line for line in lines if WARNING_KEYWORD in line]
    errors = [line for line in lines if ERROR_KEYWORD in line]

    # Only send alert if both warnings and errors exist
    if warnings and errors:
        alert_message = "Detected the following warnings and errors:\n\n"
        alert_message += "\n".join(warnings + errors)
        print(alert_message)
        send_email_alert(alert_message)
    else:
        print("No combined warning and error detected.")

if __name__ == "__main__":
    main()
