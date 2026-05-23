# 03 — Automated Email Digest

A script that loads a dataset, builds a formatted summary, and sends it as an automated email digest. Designed for daily reporting workflows where summaries need to be delivered without manual intervention.

## Features

- Loads credentials securely from a `.env` file — never hardcoded
- Reads any CSV and builds a formatted summary automatically
- Sends via SMTP with TLS encryption
- Currently configured for local SMTP testing via `aiosmtpd`
- Easy to upgrade to live Gmail send with app password

## Usage

```bash
# Install dependencies
pip install pandas python-dotenv aiosmtpd

# Set up your .env file
cp .env.example .env
# Edit .env with your credentials

# Start the local SMTP debug server (second terminal)
python -m aiosmtpd -n -l localhost:1025

# Run the digest
python digest.py sample_data.csv
```

## Environment Variables

Create a `.env` file in this folder — never commit it to git:

```
EMAIL_SENDER=your_email@example.com
EMAIL_RECEIVER=recipient@example.com
```

> ⚠️ The `.env` file is listed in `.gitignore` and must never be committed.
> Exposing credentials in version control is one of the most common
> and dangerous security mistakes a developer can make.

## Upgrading to Live Gmail Send

1. Enable 2FA on a Gmail account
2. Generate an app password at `myaccount.google.com/apppasswords`
3. Add `EMAIL_PASSWORD` to your `.env`
4. Update `send_email()` to use `smtp.gmail.com:587` with `starttls()` and `smtp.login()`

## Concepts Covered

| Concept | Description |
|---------|-------------|
| `.env` files | Secure credential storage |
| `os.getenv()` | Reading environment variables |
| `python-dotenv` | Loading `.env` at runtime |
| `smtplib` | Python's built-in email sender |
| SMTP + TLS | Email protocol with encryption |
| `MIMEText` | Building structured email messages |
| `try/except` | Graceful error handling |
| `.gitignore` | Preventing credential exposure |
