# 🐍 Python Learning Path — From Basics to Building Apps

A structured Python curriculum designed for first-year university students who have basic Python exposure but need to solidify their foundation before advancing to real-world application development.

## 📋 Overview

| | |
|---|---|
| **Target Audience** | First-year university students with basic Python knowledge |
| **Goal** | Build complete applications independently (GUI & Web) |
| **Total Sessions** | 20 sessions × 90 minutes each |
| **Language** | Vietnamese (code comments & explanations) |

## 🗺️ Curriculum Structure

### Phase 1 — Foundation (Sessions 1–6)
Core Python fundamentals: variables, data types, control flow, loops, strings, data structures, functions, file I/O, and exception handling. Ends with a console-based contact manager project.

### Phase 2 — Object-Oriented Programming (Sessions 7–10)
Classes, inheritance, polymorphism, encapsulation, modules, packages, and virtual environments. Ends with a student management system using OOP + JSON.

### Phase 3 — Working with Data (Sessions 11–14)
SQLite databases, REST APIs, JSON processing, list comprehensions, lambda functions, and functional programming patterns. Ends with a weather lookup app using API + database.

### Phase 4 — Building Applications (Sessions 15–20)
Desktop GUI with Tkinter, web applications with Flask, database integration, authentication, and deployment. Ends with a capstone project where students present their own application.

## 📁 Project Structure

```
lo-trinh-hoc/
├── OVERVIEW.md
├── README.md
├── giai-doan-1/                    # Phase 1: Foundation
│   ├── buoi-01-on-tap-nen-tang/
│   │   ├── bai-hoc.md             # Lesson content
│   │   ├── vi-du/                 # Code examples
│   │   └── thuc-hanh/             # Practice exercises
│   ├── buoi-02-vong-lap-va-chuoi/
│   ├── buoi-03-list-tuple-dict/
│   ├── buoi-04-ham/
│   ├── buoi-05-file-va-ngoai-le/
│   └── buoi-06-mini-project-1/
├── giai-doan-2/                    # Phase 2: OOP
│   ├── buoi-07 → buoi-10
├── giai-doan-3/                    # Phase 3: Data
│   ├── buoi-11 → buoi-14
└── giai-doan-4/                    # Phase 4: Applications
    ├── buoi-15 → buoi-20
```

Each session folder contains:
- `bai-hoc.md` — Lesson notes and theory
- `vi-du/` — Annotated code examples
- `thuc-hanh/` — Hands-on practice exercises

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- A code editor (VS Code recommended)

### Setup

```bash
# Clone the repository
git clone https://github.com/<your-username>/python-learning-path.git
cd python-learning-path

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install dependencies (needed for later sessions)
pip install requests flask
```

### Running Examples

```bash
# Navigate to any session and run a Python file
python lo-trinh-hoc/giai-doan-1/buoi-01-on-tap-nen-tang/vi-du/01_bien_va_kieu_du_lieu.py
```

## 🛠️ Technologies Used

| Technology | Sessions | Purpose |
|---|---|---|
| Python 3 | All | Core language |
| SQLite | 11, 14, 17, 19 | Database |
| requests | 12, 14 | HTTP / API calls |
| Tkinter | 15–17 | Desktop GUI |
| Flask | 18–19 | Web application framework |

## 📖 How to Use This Repository

**As a student:** Follow the sessions in order. Read `bai-hoc.md` first, study the examples in `vi-du/`, then attempt the exercises in `thuc-hanh/` on your own before checking the solutions.

**As an instructor:** Each session is designed for 90 minutes. Start with a 5-minute review of the previous session, walk through the theory and examples, then let students work on the practice exercises.

## 🤝 Contributing

Contributions are welcome. If you'd like to improve a lesson, fix a bug, or add new exercises:

1. Fork the repository
2. Create a feature branch (`git checkout -b improve-session-03`)
3. Commit your changes (`git commit -m 'Add extra exercises for session 3'`)
4. Push to the branch (`git push origin improve-session-03`)
5. Open a Pull Request

## 📄 License

This project is licensed under the [MIT License](LICENSE).
