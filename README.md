# 🐍 PyCoach AI

> An interactive Python full-stack mentor and code debugger powered by Qwen 2.5 and Gradio.

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/RGFoxy/PyCoach_ChatBot)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-brightgreen.svg)](https://www.python.org/)
[![Gradio](https://img.shields.io/badge/Gradio-UI-orange.svg)](https://gradio.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📌 Overview

**PyCoach AI** is a real-time conversational AI mentor designed to guide programmers, debug code, and explain Python full-stack concepts with clear, structured examples. Deployed live on Hugging Face Spaces using Gradio, it streams responses token-by-token using the **Qwen 2.5** instruct model family.

---

## ✨ Features

- **⚡ Real-Time Token Streaming:** Immediate token generation for low-latency responses.
- **🧠 Full-Stack Mentorship:** Explains core syntax, OOP, standard libraries, web frameworks (FastAPI/Flask), and data engineering libraries (NumPy, Pandas).
- **💻 Formatted Code Snippets:** Delivers clean, readable code with explicit package installation (`pip install`) commands and imports.
- **🎯 One-Click Example Prompts:** Preloaded interactive starter queries for instant exploration.
- **📱 Responsive UI:** Built with Gradio's chat component, supporting native dark mode across desktop and mobile.

---

## 🛠️ Tech Stack

- **Model Engine:** [Qwen/Qwen2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct)
- **Frontend / Framework:** [Gradio](https://gradio.app/)
- **Inference Client:** [Hugging Face Hub `InferenceClient`](https://huggingface.co/docs/huggingface_hub/index)
- **Cloud Hosting:** [Hugging Face Spaces](https://huggingface.co/spaces)

---

## 📂 Project Structure

```text
├── app.py              # Main Gradio application and streaming logic
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── .gitignore          # Git ignore rules

```
---

## 👤 Author

**Raja Ganapathi M**

📧 rajaganapathimaharajan@gmail.com · 🔗 [LinkedIn](https://www.linkedin.com/in/rajaganapathi-m) · 💻 [GitHub](https://github.com/RajaGanapathi-M)

---
