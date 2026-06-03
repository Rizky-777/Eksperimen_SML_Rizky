import time
import random
import psutil
from prometheus_client import start_http_server, Counter, Gauge, Summary

# Menyiapkan 5 Metrik untuk target Skilled
REQUEST_COUNT = Counter('model_request_total', 'Total request ke model')
ERROR_COUNT = Counter('model_error_total', 'Total error pada model')
LATENCY = Summary('model_latency_seconds', 'Waktu proses prediksi')
CPU_USAGE = Gauge('model_cpu_usage_percent', 'Penggunaan CPU')
RAM_USAGE = Gauge('model_ram_usage_bytes', 'Penggunaan RAM')

def process_request():
    REQUEST_COUNT.inc()
    start_time = time.time()
    
    time.sleep(random.uniform(0.1, 0.5))
    
    if random.random() < 0.1:
        ERROR_COUNT.inc()
        
    LATENCY.observe(time.time() - start_time)
    CPU_USAGE.set(psutil.cpu_percent())
    RAM_USAGE.set(psutil.virtual_memory().percent)

if __name__ == '__main__':
    start_http_server(8000)
    print("✅ Exporter metrik berjalan di port 8000...")
    while True:
        process_request()
        time.sleep(2)