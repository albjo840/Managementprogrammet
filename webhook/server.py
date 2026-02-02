#!/usr/bin/env python3
"""
Enkel GitHub webhook-mottagare som kör git pull när någon pushar.
"""
from flask import Flask, request
import subprocess
import hmac
import hashlib
import os

app = Flask(__name__)

# Hemlig nyckel för att verifiera att requesten kommer från GitHub
WEBHOOK_SECRET = os.environ.get('WEBHOOK_SECRET', 'managementprogrammet2026')
REPO_PATH = '/repo'

def verify_signature(payload, signature):
    """Verifiera GitHub webhook signature"""
    if not signature:
        return False
    expected = 'sha256=' + hmac.new(
        WEBHOOK_SECRET.encode(),
        payload,
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected, signature)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Verifiera signature
    signature = request.headers.get('X-Hub-Signature-256')
    if not verify_signature(request.data, signature):
        return 'Invalid signature', 403

    # Kör git pull
    try:
        result = subprocess.run(
            ['git', 'pull', 'origin', 'main'],
            cwd=REPO_PATH,
            capture_output=True,
            text=True
        )
        print(f"Git pull output: {result.stdout}")
        if result.returncode != 0:
            print(f"Git pull error: {result.stderr}")
            return f'Git pull failed: {result.stderr}', 500
        return 'OK', 200
    except Exception as e:
        print(f"Error: {e}")
        return str(e), 500

@app.route('/health', methods=['GET'])
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
