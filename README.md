# 🎓 College Assistant - AI-Powered College Recommendation System

An intelligent college recommendation system built with **LangChain orchestration**, **FastAPI backend**, and a **modern web frontend**. Get personalized college suggestions based on courses, location, fees, entrance exams, and more!

## ✨ Features

- 🤖 **AI-Powered Recommendations** - LangChain orchestration with multiple modes
- 🎯 **Intelligent Query Processing** - Understands course, location, fees, exams, etc.
- 💬 **Modern Chat Interface** - Responsive web UI with real-time messaging
- 🔄 **Multiple Orchestration Modes** - Simple, Enhanced (LCEL), Intelligent (Agent)
- 📊 **Vector Search** - ChromaDB for semantic college matching
- 🚀 **FastAPI Backend** - High-performance async API
- 🎨 **Beautiful UI** - Modern design with Font Awesome icons

## 🏗️ Architecture

```
College Assistant
├── 🎨 Frontend (HTML/CSS/JS)     # Modern chat interface
├── 🚀 API Layer (FastAPI)       # REST API with LangChain
├── 🧠 Orchestration (LangChain) # AI processing pipeline
├── 🔍 Vector DB (ChromaDB)      # College data storage
└── 📊 Data Layer (CSV)          # College dataset
```

## 📁 Project Structure

```
clg_bot/
├── frontend/                    # 🌐 Modern web interface
│   ├── index.html              # Main HTML file
│   ├── style.css               # Modern CSS styling
│   ├── script.js               # Frontend logic
│   └── README.md               # Frontend docs
├── api/                        # 🚀 FastAPI backend
│   └── app.py                  # API endpoints with orchestration
├── src/                        # 🧠 Core logic
│   ├── orchestration.py        # LangChain orchestration layer
│   ├── rag_pipeline.py         # RAG implementation
│   ├── retriever.py            # Vector DB setup
│   ├── ingestion.py            # Data processing
│   ├── domain_classifier.py    # Query classification
│   └── __init__.py
├── data/                       # 📊 College dataset
│   └── colleges.csv            # College information
├── chroma_db/                  # 🗄️ Vector database
├── requirements.txt            # 📦 Python dependencies
├── docker-compose.yml          # 🐳 Docker orchestration
├── .env.example                # 🔐 Environment template
└── LANGCHAIN_ORCHESTRATION.md  # 📚 Orchestration guide
```

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Modern web browser
- Git

### 1. Clone & Setup
```bash
git clone <repository-url>
cd clg_bot

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

### 2. Environment Setup
```bash
# Copy environment template
cp .env.example .env

# Edit .env with your API keys
# Required: OPENAI_API_KEY or GOOGLE_API_KEY
```

### 3. Start the System

#### Option A: Docker (Recommended)
```bash
docker-compose up -d
```

#### Option B: Manual Setup
```bash
# Terminal 1: Start FastAPI backend
python -m uvicorn api.app:app --reload --port 8000

# Terminal 2: Serve frontend
cd frontend
python -m http.server 3000
```

### 4. Access the Application
- 🌐 **Frontend**: http://localhost:3000
- 🚀 **API**: http://localhost:8000
- 📚 **API Docs**: http://localhost:8000/docs

## 🎯 Usage Examples

### Basic Queries
- "BBA colleges in Chennai"
- "colleges with low fees"
- "entrance exam requirements"
- "BDS colleges with good placements"

### Advanced Queries
- "top rated engineering colleges under 2 lakhs per year"
- "medical colleges in Delhi with scholarship options"
- "commerce colleges with high placement rates"

## 🔧 Orchestration Modes

### 1. **Simple Mode** (Default)
- Fast RAG-only responses (~200ms)
- Direct vector search
- Best for production/high-traffic

### 2. **Enhanced Mode (LCEL)**
- Intent classification + RAG (~800ms)
- Better response quality
- Structured processing pipeline

### 3. **Intelligent Mode (Agent)**
- ReAct agent with reasoning (~1-2s)
- Complex query understanding
- Best for detailed analysis

## 🛠️ Development

### Backend Development
```bash
# Run with auto-reload
python -m uvicorn api.app:app --reload --port 8000

# Check API health
curl http://localhost:8000/health

# Test API endpoint
curl "http://localhost:8000/ask?query=BBA+colleges&mode=lcel"
```

### Frontend Development
```bash
cd frontend

# Serve with live reload
npx serve . -p 3000

# Or use Python server
python -m http.server 3000
```

### Data Management
```bash
# Rebuild vector database
python -c "from src.retriever import create_vector_db; create_vector_db()"

# Check data
python -c "import pandas as pd; print(pd.read_csv('data/colleges.csv').head())"
```

## 🔧 Configuration

### Environment Variables
```bash
# Required
OPENAI_API_KEY=sk-your-key-here
GOOGLE_API_KEY=your-google-key-here

# Optional
ORCHESTRATION_MODE=simple  # simple, lcel, agent
FASTAPI_PORT=8000
LOG_LEVEL=info
```

### API Configuration
- **Base URL**: `http://localhost:8000`
- **Health Check**: `GET /health`
- **Ask Question**: `GET /ask?query=<text>&mode=<mode>`

## 🐳 Docker Deployment

### Development
```bash
docker-compose up -d
```

### Production
```bash
# Build optimized image
docker build -t college-assistant .

# Run with environment
docker run -p 8000:8000 --env-file .env college-assistant
```

## 📊 Data Format

### College Dataset (colleges.csv)
```csv
College_Name,District,Preferred_Course,UG_Fee,Ratings,Entrance_Exam_Name,Entrance_Exam_Rank,Eligibility,Scholarship_Status,Placement
IIT Madras,Chennai,BTech,200000,9.5,JEE Advanced,100,BTech eligibility,Available,95
...
```

### Supported Queries
- **Courses**: BBA, BCom, BDS, BTech, ECE, Civil, BJMC
- **Locations**: Chennai, Jaipur, Noida, Lucknow, Mysore, Ahmedabad
- **Intents**: fees, exam, eligibility, scholarship, placement

## 🔍 API Reference

### Health Check
```http
GET /health
```
Response: `{"status": "healthy", "orchestration": "simple"}`

### Ask Question
```http
GET /ask?query={question}&mode={mode}
```

Parameters:
- `query` (string): User's question
- `mode` (string): Orchestration mode (simple/lcel/agent)

Response:
```json
{
    "query": "BBA colleges in Chennai",
    "response": "Here are some top BBA colleges in Chennai...",
    "mode": "lcel"
}
```

## 🎨 Frontend Features

- **Real-time Chat** - Instant messaging interface
- **Mode Switching** - Change orchestration modes on-the-fly
- **Status Indicators** - Backend connectivity status
- **Quick Questions** - Pre-built question tags
- **Responsive Design** - Mobile and desktop friendly
- **Loading States** - Visual feedback during processing

## 🧪 Testing

### API Testing
```bash
# Health check
curl http://localhost:8000/health

# Simple query
curl "http://localhost:8000/ask?query=test"

# Different modes
curl "http://localhost:8000/ask?query=test&mode=lcel"
curl "http://localhost:8000/ask?query=test&mode=agent"
```

### Frontend Testing
- Open `frontend/index.html` in browser
- Check console for errors
- Test different orchestration modes
- Verify mobile responsiveness

## 🚨 Troubleshooting

### Common Issues

**Backend not starting:**
```bash
# Check Python version
python --version  # Should be 3.10+

# Check dependencies
pip list | grep langchain

# Check environment variables
echo $OPENAI_API_KEY
```

**Frontend not loading:**
- Check if backend is running on port 8000
- Verify CORS settings in FastAPI
- Check browser console for errors

**Slow responses:**
- Switch to "simple" mode
- Check vector database size
- Monitor API response times

**Data issues:**
- Verify `data/colleges.csv` exists and is valid
- Rebuild vector database if needed

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 for Python code
- Use semantic HTML and modern CSS
- Test all orchestration modes
- Update documentation for new features

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **LangChain** - For the amazing orchestration framework
- **FastAPI** - For the high-performance API framework
- **ChromaDB** - For vector database functionality
- **OpenAI/Google** - For LLM capabilities

## 📞 Support

- 📧 **Email**: your-email@example.com
- 💬 **Issues**: GitHub Issues
- 📚 **Docs**: See `LANGCHAIN_ORCHESTRATION.md`

---

**Ready to find your perfect college? Start chatting with the AI assistant! 🎓🤖**