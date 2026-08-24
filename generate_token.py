import os
from datetime import datetime, timedelta, timezone

import jwt
from dotenv import load_dotenv

load_dotenv()

secret_key = os.getenv("JWT_SECRET_KEY")
algorithm = os.getenv("JWT_ALGORITHM", "HS256")

payload = {
    "sub": "student-admin",
    "role": "admin",
    "exp": datetime.now(timezone.utc) + timedelta(minutes=30),
}

token = jwt.encode(
    payload,
    secret_key,
    algorithm=algorithm,
)

print(token)