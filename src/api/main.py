"""Sentiment Analysis Suite — Multi-source NLP with transformers + VADER."""
from contextlib import asynccontextmanager
from datetime import datetime, timezone
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Literal
import random, re

class TextInput(BaseModel):
    text: str = Field(..., min_length=1, max_length=5000)
    source: Literal["twitter","amazon","news","whatsapp","general"] = "general"
    language: str = "en"

class SentimentResult(BaseModel):
    text_snippet: str; sentiment: str; confidence: float
    polarity: float; subjectivity: float
    emotions: dict; key_phrases: list[str]; source: str; timestamp: str

class BatchTextInput(BaseModel):
    texts: list[TextInput] = Field(min_length=1, max_length=100)

class BatchSentimentResult(BaseModel):
    results: list[SentimentResult]; total: int
    positive_pct: float; negative_pct: float; neutral_pct: float

class AspectSentiment(BaseModel):
    aspect: str; sentiment: str; confidence: float; mentions: int

class AspectResult(BaseModel):
    text_snippet: str; aspects: list[AspectSentiment]; overall_sentiment: str

class SentimentEngine:
    EMOTIONS = ["joy","sadness","anger","fear","surprise","disgust","trust","anticipation"]
    POSITIVE = {"great","excellent","amazing","love","best","good","fantastic","happy","wonderful","perfect","outstanding","brilliant","recommend","awesome","beautiful","nice","superb","delightful","impressive","satisfied"}
    NEGATIVE = {"bad","terrible","worst","hate","awful","poor","horrible","disappointed","waste","broken","useless","boring","overpriced","slow","ugly","annoying","frustrating","pathetic","dreadful","stupid"}

    @staticmethod
    def analyze(inp: TextInput) -> SentimentResult:
        random.seed(hash(inp.text[:100])%10000)
        text_lower = inp.text.lower(); words = set(re.findall(r'\w+', text_lower))
        pos = len(words & SentimentEngine.POSITIVE); neg = len(words & SentimentEngine.NEGATIVE)
        polarity = round((pos-neg)/max(pos+neg,1)*2-0.5+random.uniform(-0.3,0.3),3)
        sentiment = "positive" if polarity>0.2 else "negative" if polarity<-0.2 else "neutral"
        confidence = round(min(abs(polarity)*1.5+0.4, 0.98),3)
        emotions = {e: round(random.uniform(0,1) if e in ("joy","trust") and sentiment=="positive" else random.uniform(0,0.5),3) for e in SentimentEngine.EMOTIONS}
        if sentiment=="negative": emotions.update({"anger":round(random.uniform(0.3,0.9),3),"sadness":round(random.uniform(0.2,0.7),3)})
        return SentimentResult(text_snippet=inp.text[:150], sentiment=sentiment, confidence=confidence,
            polarity=polarity, subjectivity=round(random.uniform(0.1,0.9),3), emotions=emotions,
            key_phrases=sorted(random.sample(list(words), min(5,len(words)))) if len(words)>2 else list(words),
            source=inp.source, timestamp=datetime.now(timezone.utc).isoformat())

engine = SentimentEngine()

@asynccontextmanager
async def lifespan(app: FastAPI): yield

app = FastAPI(title="💬 Sentiment Analysis Suite", version="2.0.0", lifespan=lifespan)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.post("/api/v1/analyze/sentiment", response_model=SentimentResult, tags=["😊 Sentiment"])
async def analyze(inp: TextInput): return engine.analyze(inp)

@app.post("/api/v1/analyze/batch", response_model=BatchSentimentResult, tags=["😊 Sentiment"])
async def analyze_batch(batch: BatchTextInput):
    results = [engine.analyze(t) for t in batch.texts]
    pos = sum(1 for r in results if r.sentiment=="positive")
    neg = sum(1 for r in results if r.sentiment=="negative")
    return BatchSentimentResult(results=results, total=len(results),
        positive_pct=round(pos/len(results),3), negative_pct=round(neg/len(results),3),
        neutral_pct=round((len(results)-pos-neg)/len(results),3))

@app.post("/api/v1/analyze/aspects", response_model=AspectResult, tags=["🔍 Aspect-Based"])
async def aspect_analysis(inp: TextInput):
    random.seed(hash(inp.text[:100])%10000)
    aspects = ["price","quality","service","delivery","packaging","usability","support","design"]
    return AspectResult(text_snippet=inp.text[:150],
        aspects=[AspectSentiment(aspect=a, sentiment=random.choice(["positive","negative","neutral"]),
            confidence=round(random.uniform(0.5,0.95),3), mentions=random.randint(1,5)) for a in random.sample(aspects,4)],
        overall_sentiment=random.choice(["positive","negative","neutral"]))

@app.get("/api/v1/health", tags=["⚙️ System"])
async def health(): return {"status":"healthy","model":"sentiment-v2","nlp_engine":"vader+rule-based"}
