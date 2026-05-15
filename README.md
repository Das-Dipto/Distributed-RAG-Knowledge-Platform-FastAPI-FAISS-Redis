# Distributed RAG Knowledge Platform

A production-grade backend system for building Retrieval-Augmented Generation (RAG) pipelines using a fully containerized, distributed architecture.

This project focuses on backend engineering, asynchronous processing, and scalable AI infrastructure design using open-source tools.

---

## 🚀 Current Status

### ✅ Completed Infrastructure Phase

The system now has a fully operational distributed backend foundation:

- Dockerized FastAPI service (API layer)
- Dockerized Redis (message broker + caching layer)
- Dockerized RQ Worker (async background processing)
- Docker Compose orchestration for all services
- Healthcheck-based service dependency management
- Container networking fully configured
- Async job queue system functional (`document-processing`)
- Swagger/OpenAPI documentation enabled

👉 The system is now a working distributed backend runtime.

---

## 🏗️ Architecture Overview

```
Client
   ↓
FastAPI API
   ↓
Redis Queue (RQ)
   ↓
RQ Worker
   ↓
Future Ingestion Pipeline
   ↓
Future Embedding Pipeline
   ↓
Future FAISS Vector Store
```

---

## 🧩 System Components

### API Layer
- FastAPI-based backend
- Exposes REST endpoints
- Enqueues background ingestion jobs
- Provides API documentation via Swagger

### Queue System
- Redis + RQ (Redis Queue)
- Handles asynchronous task execution
- Decouples API from processing layer

### Worker Layer
- Background job processor
- Executes ingestion tasks
- Currently listening to `document-processing` queue

### Redis Layer
- Message broker for distributed tasks
- Future caching layer
- Shared across API and worker services

---

## 🐳 Dockerized Services

### API Container
- Name: `rag-api`
- Runs FastAPI application
- Exposes port `8000`
- Command:
  ```bash
  uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
  ```

### Redis Container
- Name: `rag-redis`
- Base image: `redis:7-alpine`
- Provides queue + messaging + caching infrastructure

### Worker Container
- Name: `rag-worker`
- Executes background jobs using RQ
- Starts worker process:
  ```bash
  python -m app.workers.worker
  ```

---


## 🐧 Development Environment

The project is now fully developed inside a Linux environment:

- OS: Ubuntu (inside Oracle VirtualBox VM)
- No longer developed on Windows host system
- All Docker operations executed inside Linux environment

This ensures:
- production-like environment consistency
- proper container networking behavior
- realistic backend engineering workflow

---

## ⚙️ Docker Workflow

### Start full system
```bash
docker compose up
```

### Run in background
```bash
docker compose up -d
```

### Stop system
```bash
docker compose down
```

### Rebuild containers
```bash
docker compose build --no-cache
```

### View running containers
```bash
docker ps
```

### View logs
```bash
docker compose logs -f
```

---

## 🧠 Tech Stack

- FastAPI
- Redis
- RQ (Redis Queue)
- Docker & Docker Compose
- Python 3.11
- Ubuntu (VM environment)

---

## 🎯 Project Goals

- Build a scalable distributed RAG backend system
- Maintain strict separation of concerns
- Follow production-grade backend architecture principles
- Design asynchronous AI processing pipelines
- Ensure modular and extensible system design

---

## 🧱 Architectural Principles

- Separation of concerns (API / Queue / Worker / Ingestion / Retrieval)
- Containerized infrastructure as the execution layer
- Async-first backend design
- Centralized configuration management
- Scalable distributed processing model

---

## 🗺️ Roadmap

### Infrastructure Phase (Completed)
- [x] Dockerized distributed backend setup
- [x] Redis + RQ integration
- [x] Worker orchestration
- [x] API service setup

### RAG Pipeline Phase (Next)
- [ ] Document upload system
- [ ] File persistence layer
- [ ] Chunking pipeline design
- [ ] Embedding generation (Sentence Transformers)
- [ ] FAISS vector indexing
- [ ] Semantic retrieval system
- [ ] Query + ranking layer

### Advanced Phase
- [ ] LLM integration (Ollama)
- [ ] Optimization & caching layer
- [ ] Horizontal scaling improvements

---

## 📌 Use Cases

- AI-powered document search systems
- Enterprise knowledge bases
- Semantic retrieval engines
- RAG-based AI applications
- Internal data intelligence systems

---

## 🧠 Philosophy

This project is built as a **real backend distributed systems engineering exercise**, not a demo application.

Every stage follows:

- Architecture-first design
- Modular system separation
- Production-style infrastructure thinking
- Scalable distributed computing principles
```
```