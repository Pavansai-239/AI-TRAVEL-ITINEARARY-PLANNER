# 🧠 AI Travel Agent with ELK Stack Monitoring and Kubernetes Deployment

This project is an intelligent AI Travel Agent application built with Python and deployed using Docker and Kubernetes. It features real-time logging and observability through the **ELK stack (Elasticsearch, Logstash, Kibana)** and **Filebeat**, enabling powerful monitoring and analytics.

---

## 🚀 Features

- ✈️ **AI Travel Agent** logic with customizable query handling
- 🐍 Built using **Python**, with modularized code in the `src/` directory
- 📦 **Dockerized** for container-based deployments
- ☸️ **Kubernetes deployment-ready** via YAML configs
- 📊 Real-time monitoring using **ELK Stack**:
  - 🔍 Elasticsearch (storage & search engine)
  - 📈 Kibana (data visualization dashboard)
  - 📥 Logstash (log pipeline)
  - 📡 Filebeat (lightweight log shipper)
- 🔐 Environment configuration via `.env` file

---

## 🗂️ Project Structure

```bash
.
├── app.py                       # Entry point
├── setup.py                     # Python setup
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Container image setup
├── .env.example                 # Environment variables template
├── src/                         # Main source code
├── k8s-deployment/             # Kubernetes YAML manifests
├── elasticsearch/              # Elasticsearch configs
├── logstash/                   # Logstash pipeline configs
├── kibana/                     # Kibana setup
├── filebeat/                   # Filebeat configs
└── logs/                       # Log output (sample or template)
```

---

## 🛠️ Getting Started

### 🔧 Prerequisites
- Python 3.8+
- Docker
- Kubernetes with Minikube (for local setup)
- Make sure ports 9200, 5601, etc. are open if testing locally

### 📦 Install Dependencies
```bash
pip install -r requirements.txt
```

### 🧪 Run Locally (Dev Mode)
```bash
python app.py
```

---

## 🐳 Docker Usage
### 🔨 Build Image
```bash
docker build -t ai-travel-agent .
```

### ▶️ Run Container
```bash
docker run -d -p 5000:5000 --env-file .env ai-travel-agent
```

---

## ☸️ Kubernetes Deployment
```bash
kubectl apply -f k8s-deployment/
```
> Ensure all ELK services and Filebeat are up before launching the app.

---

## 📊 Monitoring Setup (ELK Stack)

### 🔹 Start Stack Services
```bash
docker-compose up -d
```

- Access **Kibana** dashboard at: `http://localhost:5601`
- Use saved index patterns to explore application logs

---

## 📃 .env Configuration (example)
```env
APP_PORT=5000
LOG_LEVEL=INFO
ELASTICSEARCH_HOST=http://localhost:9200
```

---

## 📌 Future Improvements
- Add authentication for Kibana dashboard
- Extend AI Travel Agent logic with NLP models
- Enable horizontal scaling in Kubernetes

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License
[MIT](https://choosealicense.com/licenses/mit/)

---

## 🙌 Acknowledgements
- Elastic Stack Docs
- Kubernetes Documentation
- Streamlit / Flask (optional UI extensions)
