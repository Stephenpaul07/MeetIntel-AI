# MeetIntel AI

> Turn meeting notes into actionable intelligence.

MeetIntel AI is a full-stack application that helps teams organize meeting notes by project and ask AI-powered questions about their meetings.

Instead of manually searching through multiple meeting notes, users can ask questions in natural language and receive focused answers based on the relevant meeting discussions.

---

## ✨ Features

### 📁 Project Management
- Create and organize multiple projects
- Add project names and descriptions
- View all projects from a centralized dashboard

### 📝 Meeting Notes
- Add meeting notes to individual projects
- Include meeting title, date, and detailed content
- View meeting note previews
- Expand and read full meeting notes
- Delete meeting notes

### 🤖 AI-Powered Meeting Intelligence
- Ask questions about all meeting notes within a project
- AI searches relevant meeting-note content
- Generates focused answers using retrieved context
- Displays the sources used to generate the answer

### 🔍 RAG Pipeline

MeetIntel AI uses a Retrieval-Augmented Generation (RAG) architecture:

```text
Meeting Notes
      ↓
Text Chunking
      ↓
Embedding Generation
      ↓
Vector Database
      ↓
Similarity Search
      ↓
Relevant Context
      ↓
Ollama LLM
      ↓
AI Answer + Sources
