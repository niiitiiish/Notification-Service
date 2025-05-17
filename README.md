
# Notification Service

This project is a basic notification service API built with FastAPI and PostgreSQL.

## Features

- Send notifications (email, SMS, in-app)
- Retrieve user notifications

## Setup Instructions

1. Clone the repo
2. Create and activate a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Run the server: `uvicorn main:app --reload`

## Assumptions

- Notifications are stored in a PostgreSQL database
- No actual sending of email/SMS yet (can be added later)
