#!/usr/bin/env python3
"""
DAXXMUSIC Bot - Railway Deploy Ready
HTTP Server + Music Bot + All Commands
"""

import os
import sys
import threading
import time
from flask import Flask
import logging

# Fix path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Flask HTTP Server for Railway
app = Flask(__name__)

@app.route('/')
@app.route('/health')
def health():
    return {
        "status": "success",
        "service": "DAXXMUSIC",
        "version": "1.0",
        "commands": ["/play", "/vplay", "/cplay", "/playlist", "/help"],
        "healthy": True
    }

def run_http_server():
    """Railway Port Detection"""
    port = int(os.environ.get('PORT', 3000))
    host = '0.0.0.0'
    app.run(host=host, port=port, debug=False)

# Start HTTP Server FIRST
print("🌐 Starting HTTP Server...")
http_thread = threading.Thread(target=run_http_server, daemon=True)
http_thread.start()
time.sleep(8)  # Wait for Railway health check

print("✅ HTTP Server ready on PORT", os.environ.get('PORT', 3000))

# Start Music Bot
print("🎵 Launching DAXXMUSIC Bot...")
try:
    os.system("python3 -m DAXXMUSIC")
except Exception as e:
    print(f"Bot Error: {e}")
    # Keep alive
    while True:
        time.sleep(60)

if __name__ == "__main__":
    print("🚀 DAXXMUSIC Railway Edition")
    print("📱 Commands: /play /vplay /cplay /help")
