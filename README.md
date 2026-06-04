# ApplyAI 🚀

**An AI-Powered Job Application Assistant that automates job discovery, matching, company research, recruiter outreach, and application tracking.**

ApplyAI helps job seekers spend less time manually searching and applying for jobs by leveraging AI agents to discover opportunities, evaluate fit, research companies, identify hiring contacts, and generate personalized outreach emails.

---

## 🌟 Overview

Traditional job hunting is repetitive, time-consuming, and often inefficient. ApplyAI streamlines the process by combining multiple AI-powered agents into a single automated workflow.

Users simply:

1. Upload their CV
2. Specify their desired role
3. Launch the pipeline

ApplyAI then:

* Discovers relevant job opportunities
* Matches jobs against the user's profile
* Researches target companies
* Finds recruiter or hiring manager contacts
* Generates personalized outreach emails
* Tracks applications and statuses

---

## 🏗 Architecture

```text
CV Upload
    ↓
CV Processing & Embedding
    ↓
Job Discovery Pipeline
    ↓
CV Matching Engine
    ↓
Company Research Agent
    ↓
Email Hunter Agent
    ↓
Email Draft Agent
    ↓
Application Dashboard
```

---

## 🤖 AI Agents

### 1. Job Discovery Agent

Discovers relevant opportunities from multiple job sources.

**Responsibilities:**

* LinkedIn job discovery
* JSearch integration
* Job aggregation
* Deduplication
* Job normalization

---

### 2. CV Matching Agent

Ranks jobs based on relevance to the candidate.

**Responsibilities:**

* Embedding generation
* Cosine similarity scoring
* Skill matching
* Experience matching
* Ranking and prioritization

---

### 3. Company Research Agent

Collects company intelligence to personalize outreach.

**Responsibilities:**

* Company profiling
* Industry classification
* Culture insights
* Technology stack identification
* Recent company updates

---

### 4. Email Hunter Agent

Identifies recruiter and hiring contacts.

**Responsibilities:**

* Company domain discovery
* Recruiter contact identification
* Hiring manager lookup
* Confidence scoring

---

### 5. Email Draft Agent

Creates personalized outreach emails.

**Responsibilities:**

* Job-specific personalization
* Company-specific personalization
* Professional email drafting
* Subject line generation

---

## 🛠 Technology Stack

### Backend

* FastAPI
* Python 3.12+
* Redis
* Celery
* Supabase
* LangGraph
* OpenAI
* Groq
* Tavily

### Frontend

* Next.js 15
* TypeScript
* Tailwind CSS
* Shadcn UI
* Framer Motion
* Zustand
* React Query

### Infrastructure

* Docker
* Docker Compose
* GitHub Actions
* Vercel (Frontend)
* Railway / Render (Backend)

---

## 📂 Project Structure

```text
ApplyAI/
│
├── backend/
│   ├── agents/
│   │   ├── company_research.py
│   │   ├── email_hunter.py
│   │   └── email_draft.py
│   │
│   ├── config/
│   ├── modules/
│   ├── schema/
│   ├── services/
│   ├── src/
│   └── utils/
│
├── Frontend/
│
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── README.md
```

---

## 🔌 API Endpoints

### Health Check

```http
GET /api/health
```

Response:

```json
{
  "status": "ok"
}
```

---

### Upload CV

```http
POST /api/cv/upload
```

Request:

```multipart
file: PDF
```

Response:

```json
{
  "success": true,
  "text_length": 12345
}
```

---

### Start Pipeline

```http
POST /api/pipeline/run
```

Headers:

```http
Authorization: Bearer <JWT>
```

Response:

```json
{
  "run_id": "uuid",
  "status": "queued"
}
```

---

### Stream Pipeline Progress

```http
GET /api/pipeline/{run_id}/stream
```

Server-Sent Events:

```text
queued
running
job_discovery
cv_matching
research
email_generation
done
failed
```

---

### Get Matched Jobs

```http
GET /api/jobs/{run_id}
```

---

### Get Job Details

```http
GET /api/job/{job_match_id}
```

---

### Generate Email Draft

```http
POST /api/email-draft/{job_match_id}
```

---

### Update Job Status

```http
PATCH /api/jobs/{job_match_id}
```

Statuses:

```text
saved
applied
rejected
interviewing
```

---

### Applications Dashboard

```http
GET /api/applications
```

---

## ⚡ Local Development

### Clone Repository

```bash
git clone https://github.com/<username>/ApplyAI.git
cd ApplyAI
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

### Install Backend Dependencies

```bash
uv sync
```

### Configure Environment Variables

Create:

```text
.env
```

Example:

```env
OPENAI_API_KEY=
GROQ_API_KEY=
TAVILY_API_KEY=
SUPABASE_URL=
SUPABASE_KEY=
REDIS_URL=
JWT_SECRET_KEY=
```

### Start Backend

```bash
uv run uvicorn backend.app:app --reload
```

Backend:

```text
http://localhost:8000
```

---

### Frontend Setup

```bash
cd Frontend
npm install
npm run dev
```

Frontend:

```text
http://localhost:3000
```

---

## 🎯 Current Features

* CV Upload
* PDF Parsing
* Job Discovery Pipeline
* Company Research Agent
* Email Hunter Agent
* Email Draft Generation
* Real-Time Pipeline Updates (SSE)
* JWT Authentication
* Application Tracking
* Modern Responsive Frontend

---

## 🚧 Future Enhancements

* Multi-CV Support
* LinkedIn OAuth
* One-Click Apply
* Interview Preparation Agent
* Resume Optimization Agent
* Cover Letter Generation
* Analytics Dashboard
* AI Career Coach

---

## 👩‍💻 Author

**Wajeeha Ghazi**

* Stanford Code in Place Section Leader
* Harvard CS50x Puzzle Day Winner
* UC Berkeley CALICO Competitor
* AI & Software Engineering Enthusiast

---

## 📜 License

This project is intended for educational, research, and portfolio purposes.

© 2026 ApplyAI. All rights reserved.
