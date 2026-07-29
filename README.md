# 💬 ML Sentiment Analysis Suite

[![CI/CD](https://github.com/twomathematicians-code/ml-sentiment-analysis-suite/actions/workflows/ci.yml/badge.svg)](https://github.com/twomathematicians-code/ml-sentiment-analysis-suite/actions)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker)](https://hub.docker.com/)
[![HuggingFace](https://img.shields.io/badge/🤗_Transformers-Ready-FFD21E)](https://huggingface.co/)

**Multi-source NLP sentiment analysis API: Twitter/X, product reviews, news articles, and WhatsApp chats — powered by HuggingFace transformers with zero-shot and few-shot capabilities.**

---

## 🎯 Analysis Modules

| Module | Model | Sources |
|---|---|---|
| **Social Media Sentiment** | DistilBERT / RoBERTa | Twitter/X, Reddit |
| **Product Review Analysis** | DeBERTa + Aspect-Based | Amazon, Flipkart, Google Play |
| **News Sentiment** | FinBERT / Zero-Shot | Financial news, general news |
| **Chat Analysis** | VADER + TextBlob Ensemble | WhatsApp, Telegram |

---

## 🚀 Quick Start

```bash
git clone https://github.com/twomathematicians-code/ml-sentiment-analysis-suite.git
cd ml-sentiment-analysis-suite
docker-compose up --build
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/v1/analyze/social` | Social media sentiment |
| `POST` | `/api/v1/analyze/review` | Product review analysis |
| `POST` | `/api/v1/analyze/news` | News sentiment |
| `POST` | `/api/v1/analyze/batch` | Batch analysis |
| `GET` | `/api/v1/health` | Health check |

---

## 👤 Author

**Mahesh Solanki** — [LinkedIn](https://linkedin.com/in/maheshsolanki-16b9a6a5) | [GitHub](https://github.com/twomathematicians-code)
