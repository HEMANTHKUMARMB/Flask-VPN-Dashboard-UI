# AI Virtual Private Network (VPN) for Secure Cloud Access

Demo web UI built with Python (Flask) that showcases a modal-based AI VPN experience and a secure login flow.

> **Note**: This is a UI demo only. It does **not** create a real VPN or route any network traffic.

## Features

- Landing page with **FREE CLOUD SECURE ACCESS** hero section
- AI-themed access modal (opens from landing page)
- Login page (`/login`) with demo credentials
- Simple authenticated dashboard (`/dashboard`)

## Tech stack

- Python 3.x
- Flask

## Getting started

1. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   python app.py
   ```

4. Open your browser and go to:

   ```
   http://127.0.0.1:5000/
   ```

## Demo login

On the login page (`/login`), use:

- **Username**: `demo`
- **Password**: `securepass`

After logging in you will be redirected to the dashboard with a simulated secure session.
