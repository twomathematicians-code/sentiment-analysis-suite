<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=venom&height=200&color=gradient&text=Sentiment%20Analysis&fontSize=45&fontColor=ffffff&textBg=false" />
</p>

<h3 align="center">Multi-Source NLP Sentiment Engine with Emotion Detection</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue" />
  <img src="https://img.shields.io/badge/FastAPI-Async-009688" />
  <img src="https://img.shields.io/badge/Transformers-NLP-FFD21E" />
  <img src="https://img.shields.io/badge/Stars-⭐-FFD700" />
</p>

---

## 🧠 Sentiment + Emotion Engine

This API goes beyond positive/negative. It detects:

- **Sentiment polarity** (-1 to +1)
- **Subjectivity score** (0 = objective, 1 = subjective)
- **8 basic emotions** (joy, sadness, anger, fear, surprise, disgust, trust, anticipation)
- **Aspect-based analysis** (what specifically is positive/negative)

## Quick Start

```bash
docker compose up -d
curl -X POST http://localhost:8000/api/v1/analyze/sentiment \
  -H "Content-Type: application/json" \
  -d '{"text": "The food was amazing but the service was terrible", "source": "amazon"}'
```

## Endpoints

| Endpoint | What It Does |
|:--|:--|
| `POST /api/v1/analyze/sentiment` | Single text → sentiment + emotions |
| `POST /api/v1/analyze/batch` | Bulk analysis with aggregate stats |
| `POST /api/v1/analyze/aspects` | Aspect-level sentiment breakdown |

---

<p align="center"><i>Mahesh Solanki</i> · 
<a href="https://linkedin.com/in/maheshsolanki-16b9a6a5">LinkedIn</a></p>
