# DeepThought ICP Discovery Pipeline

## Overview

This project is an AI-assisted pipeline for discovering and qualifying Indian manufacturing companies matching DeepThought's ICP (Ideal Customer Profile).

The pipeline automates:

* company research
* website scraping
* AI-based ICP scoring
* qualification workflow
* dashboard visualization

---

## Objective

To build a scalable system capable of identifying high-fit specialty manufacturing companies using web scraping and LLM-based scoring.

---

## Workflow

Company Dataset
↓
Website Scraper
↓
Text Extraction
↓
AI ICP Scoring
↓
Final CSV Output
↓
Analytics Dashboard

---

## Technologies Used

* Python
* Playwright
* Pandas
* Streamlit
* OpenAI API

---

## Features

* Automated website scraping
* AI-assisted qualification
* Pass/Fail scoring
* Modular architecture
* Dashboard visualization

---

## Folder Structure

data/ → company dataset
scrapers/ → scraping scripts
scoring/ → AI scoring pipeline
output/ → generated outputs
dashboard/ → Streamlit dashboard

---

## Future Improvements

* Parallel scraping
* Better deduplication
* Multi-agent scoring
* Confidence-based QA
* PostgreSQL integration
* CRM enrichment

---

## Scaling Strategy

This MVP processes a small sample set but is designed to scale to thousands of companies using:

* batch AI scoring
* asynchronous scraping
* automated filtering
* structured enrichment pipelines
