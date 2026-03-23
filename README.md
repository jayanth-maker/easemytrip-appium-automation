# ✈️ EaseMyTrip Mobile Automation Framework (Appium + AI)

This project is a mobile automation framework for the EaseMyTrip Android application built using Python and Appium.  
It follows the Page Object Model (POM) design pattern and integrates AI-generated test cases for intelligent validation and failure detection.

---

## 📌 Project Overview

This framework automates the flight search functionality of the EaseMyTrip mobile application.

### 🔥 Key Features

- Appium-based mobile automation  
- Page Object Model (POM) design pattern  
- AI-generated test case module for intelligent validation  
- Screenshot capture for failed test cases  
- HTML test reports generation  
- Config-driven framework  
- Git version control  

---

## 🛠 Tech Stack

- Python  
- Appium  
- Selenium  
- PyTest  
- Android Studio  
- Node.js  

---

## 📂 Project Structure

EasyTripAutomation/
├── ai/            # AI-generated test case module  
├── config/        # Configuration files  
├── pages/         # Page Object Model classes  
├── reports/       # HTML test reports  
├── screenshots/   # Test screenshots  
│   ├── POM_test/      # Manual/POM test screenshots  
│   └── ai_failures/   # AI-generated failure screenshots  
├── test_data/     # AI test data  
├── tests/         # Test scripts  
├── utils/         # Driver setup & helpers  
├── easemytrip_test.py  
├── test_connection.py  
└── README.md  

---

## ⚙️ Prerequisites

Before running the framework, install:

- Python 3.9+  
- Appium Server  
- Android Studio  
- Android Emulator / Real Device  
- Node.js  

---

## 🚀 How to Run

1. Clone the repository:  
git clone https://github.com/jayanth-maker/easemytrip-appium-automation.git  
cd easemytrip-appium-automation  

2. Create virtual environment:  
python -m venv venv  
source venv/bin/activate  

3. Install dependencies:  
pip install -r requirements.txt  

4. Start Appium server  

5. Run tests:  
pytest tests/  

---

## 📸 Test Case Validation Details

### 🔹 POM-Based Test Cases

The framework includes manually designed test cases using the Page Object Model.

Example scenarios covered:

- Invalid city input validation  
- Empty search validation  
- UI interaction and navigation checks  

For each failed test case:
- Screenshots are captured automatically  
- Stored in: `screenshots/POM_test/`  
- Helps in debugging UI and validation issues  

---

### 🤖 AI-Generated Test Case Failures

The project includes an AI module that generates test scenarios dynamically.

Key details:

- AI-generated test cases are stored in `test_data/`  
- Failures from AI-generated scenarios are captured in:  
  `screenshots/ai_failures/`  

These screenshots help identify:

- Unexpected UI behavior  
- Edge case failures  
- Input validation issues  

This adds an extra layer of intelligent testing beyond manual test cases.

---

## 📊 Reports

- HTML reports are generated inside the `reports/` folder  
- Provides detailed execution results and logs  

---

## 🎯 Highlights

- Designed using scalable automation architecture (POM)  
- Integrated AI for smart test case generation  
- Handles real-world scenarios like invalid inputs and edge cases  
- Clean folder structure for maintainability  

---

## 👨‍💻 Author

Jayanth Nandakumar  

---

## ⭐ If you like this project, give it a star!
