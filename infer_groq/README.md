# infer_groq

## Overview
**infer_groq** is a minimal FastAPI-based microservice that connects to the Groq API for chat completions.  
It exposes a single POST endpoint that accepts user input and returns a generated response using Groq's language model.

## Features
- FastAPI backend for easy deployment and scalability
- Environment-based API key management using `python-dotenv`
- Simple interface for sending prompts and receiving completions

## Requirements
- Python 3.8+
- [groq](https://pypi.org/project/groq/)
- [fastapi](https://fastapi.tiangolo.com/)
- [uvicorn](https://www.uvicorn.org/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

Install dependencies:
```bash
pip install groq fastapi uvicorn python-dotenv

