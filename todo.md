# LinkedInForge Agent - TODO

## Goal

Build an AI agent that reads my resume, opens LinkedIn on my laptop, identifies missing information, and updates my profile automatically through browser interaction.

---

# Phase 1: Resume Knowledge Base

* [x] Convert resume into structured JSON
* [x] Store Projects
* [x] Store Skills
* [x] Store Certifications
* [x] Store Achievements
* [x] Store Experience
* [x] Store Education

---

# Phase 2: Computer Agent

## Screen Understanding

* [x] Capture screen
* [x] Detect LinkedIn UI elements
* [x] Read profile sections
* [x] Identify buttons and forms
* [x] Track current page

## Vision Layer

* [x] OCR using Tesseract/EasyOCR
* [x] UI element detection
* [x] Button detection
* [x] Text extraction

---

# Phase 3: LinkedIn Analyzer

## Profile Scanner

* [x] Open LinkedIn profile
* [x] Scan About section
* [x] Scan Experience section
* [x] Scan Projects section
* [x] Scan Skills section
* [x] Scan Certifications section

## Gap Detection

* [x] Find missing projects
* [x] Find missing skills
* [x] Find missing certifications
* [x] Find missing achievements
* [x] Detect outdated descriptions

---

# Phase 4: AI Brain

## Content Generation

* [x] Generate About section
* [x] Generate project descriptions
* [x] Generate experience descriptions
* [x] Generate achievement descriptions

## Decision Making

* [x] Decide what needs updating
* [x] Rank updates by importance
* [x] Ask user for approval

---

# Phase 5: Browser Automation

## Navigation

* [x] Open LinkedIn
* [x] Navigate to profile
* [x] Open edit dialogs
* [x] Scroll intelligently

## Actions

* [x] Click buttons
* [x] Fill text fields
* [x] Save changes
* [x] Verify updates

---

# Phase 6: Agent Workflow

1. Read Resume
2. Scan LinkedIn
3. Compare Data
4. Generate Missing Content
5. Show Proposed Changes
6. User Approves
7. Agent Updates Profile
8. Generate Report

---

# Tech Stack

## AI

* [ ] Gemini 2.5 Pro
* [ ] OpenAI GPT-5
* [ ] LangGraph

## Vision

* [ ] EasyOCR
* [ ] OpenCV
* [ ] PyAutoGUI

## Automation

* [ ] Playwright
* [ ] Browser-Use
* [ ] Selenium (Fallback)

## Backend

* [ ] FastAPI

## Database

* [ ] Supabase

---

# Advanced Features

* [ ] GitHub Profile Analyzer
* [ ] Portfolio Website Scanner
* [ ] Resume Change Detection
* [ ] Auto-Generated LinkedIn Posts
* [ ] Recruiter Score
* [ ] ATS Score
* [ ] Career Recommendations

---

# MVP

Input:

* Resume PDF

Output:

* Scan LinkedIn
* Find Missing Skills
* Find Missing Projects
* Generate Better Descriptions
* Automatically Update LinkedIn

Success Metric:
Profile updated in under 5 minutes with one approval click.
