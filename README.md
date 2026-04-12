# JSON vs Protobuf Benchmark

This project compares JSON and Protobuf serialization in terms of:

* CPU usage
* Execution time
* Scalability with increasing payload size

---

## ⚙️Setup

```bash
pip install protobuf psutil
```

---

## ▶️ Run Benchmark

```bash
python3 benchmark.py
```

---

##  Results

### Small Payload

| Format   | Time (s) | CPU (s) |
| -------- | -------- | ------- |
| JSON     | 0.2173   | 0.2100  |
| Protobuf | 0.0726   | 0.0800  |

---

### Medium Payload (array of 100 elements)

| Format   | Time (s) | CPU (s) |
| -------- | -------- | ------- |
| JSON     | 0.7765   | 0.7700  |
| Protobuf | 0.0707   | 0.0700  |

---

### Large Payload (array of 1000 elements)

| Format   | Time (s) | CPU (s) |
| -------- | -------- | ------- |
| JSON     | 5.2262   | 5.2300  |
| Protobuf | 0.0740   | 0.0700  |

---

##  Key Observations

* Protobuf is significantly faster than JSON
* CPU usage for JSON increases sharply with payload size
* Protobuf remains nearly constant even for large data

---

##  Conclusion

As payload size increases:

* JSON performance degrades rapidly
* Protobuf scales efficiently

For large payloads:

* ~70× faster serialization
* ~75× lower CPU usage

---

##  Use Cases

Protobuf is better suited for:

* High-performance systems
* Telemetry pipelines
* Network protocols
* Distributed systems

---
