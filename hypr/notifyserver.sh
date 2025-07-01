#!/bin/bash

cd ~/.config/notifyserver/

venv/bin/streamlit run main.py --server.port=8501 --server.headless true
