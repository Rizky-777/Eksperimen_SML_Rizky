import requests
import time

print("🚀 Menjalankan simulasi request ke model...")
while True:
    try:
        requests.get("http://localhost:8000")
        print("Memicu request metrik...")
    except:
        pass
    time.sleep(3)