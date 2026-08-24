# ============================================================
# Stage 1: Build
# ============================================================
FROM python:3.11-slim-bookworm AS builder

WORKDIR /build

# Install Python dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir \
    --target=/build/packages \
    -r requirements.txt

# Copy application source
COPY app ./app

# Compile Python source code to bytecode
RUN python -m compileall -q -b app

# Remove original Python source files
RUN find app -type f -name "*.py" -delete

# Remove unnecessary cache directories
RUN find app -type d -name "__pycache__" -exec rm -rf {} +


# ============================================================
# Stage 2: Hardened Distroless Runtime
# ============================================================
FROM gcr.io/distroless/python3-debian12:nonroot

WORKDIR /app

# Copy only installed dependencies
COPY --from=builder /build/packages /app/packages

# Copy only compiled Python bytecode
COPY --from=builder /build/app /app/app

# Use Python bytecode directly
ENV PYTHONPATH=/app/packages:/app

EXPOSE 8000


ENTRYPOINT ["/usr/bin/python3", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
