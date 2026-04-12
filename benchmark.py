import time
import json
import psutil
import os
import telemetry_pb2

process = psutil.Process(os.getpid())

ITER = 100000

data = {
    "id": 1,
    "temperature": 25.5,
    "status": "OK",
    "values": list(range(1000))
}

# Protobuf object
msg = telemetry_pb2.Telemetry()
msg.id = 1
msg.temperature = 25.5
msg.status = "OK"

def benchmark_json():
    start_cpu = process.cpu_times().user
    start = time.time()

    for _ in range(ITER):
        json.dumps(data)

    return time.time() - start, process.cpu_times().user - start_cpu


def benchmark_proto():
    start_cpu = process.cpu_times().user
    start = time.time()

    for _ in range(ITER):
        msg.SerializeToString()

    return time.time() - start, process.cpu_times().user - start_cpu


json_time, json_cpu = benchmark_json()
proto_time, proto_cpu = benchmark_proto()

print("\n--- Results ---")
print(f"JSON     -> Time: {json_time:.4f}s | CPU: {json_cpu:.4f}s")
print(f"Protobuf -> Time: {proto_time:.4f}s | CPU: {proto_cpu:.4f}s")
