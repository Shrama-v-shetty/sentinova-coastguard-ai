# sentinova-coastguard-ai
CoastGuard AI is an AI-powered infrastructure monitoring and early warning system that detects structural defects, assesses risk severity, and supports authorities in proactive infrastructure safety management.
# CoastGuard AI

### AI-Powered Infrastructure Monitoring & Early Warning System

**CoastGuard AI** is an intelligent infrastructure monitoring platform developed by **Team Sentinova** for the Coastal Innovation Hackathon.

The system leverages Artificial Intelligence, Computer Vision, Geolocation Tracking, and Automated Alerting to detect structural cracks in critical infrastructure and support timely decision-making for infrastructure safety.

---

## Problem Statement

Critical infrastructure such as dams, bridges, coastal barriers, and flood protection structures are vulnerable to structural degradation over time.

Traditional monitoring methods often rely on manual inspections, which can be:

* Time-consuming
* Resource-intensive
* Difficult to perform frequently
* Prone to delayed reporting

Early signs of damage such as cracks may go unnoticed, increasing safety risks and delaying maintenance actions.

---

## Solution

CoastGuard AI provides an AI-powered platform that enables users to upload images of infrastructure for automated crack detection and severity analysis.

The platform combines computer vision, geolocation tracking, automated reporting, and emergency alert generation to assist engineers and authorities in identifying and responding to potential structural risks.

---

## Key Features

### AI-Based Crack Detection

* Detects cracks in concrete infrastructure using a trained deep learning model.
* Utilizes Transfer Learning with MobileNetV2.

### Severity Analysis

* Classifies detected defects into:

  * LOW
  * MEDIUM
  * HIGH

### Geolocation Tracking

* Address-based location input
* Latitude and longitude support
* Interactive map-based location selection
* Google Maps integration

### Emergency Alert System

* Sends email alerts for HIGH severity defects.
* Includes uploaded image evidence and location details.

### Weekly Reporting

* Automatically records detected issues.
* Generates and sends weekly monitoring reports.

### Interactive Dashboard

* Built using Streamlit.
* User-friendly interface for infrastructure monitoring.

---

## System Workflow

```text
User Uploads Infrastructure Image
            ↓
     AI Crack Detection
            ↓
    Severity Classification
            ↓
      Location Capture
            ↓
      Report Generation
            ↓
    Authority Notification
```

---

## Technology Stack

### Frontend & Dashboard

* Streamlit

### Programming Language

* Python

### AI & Computer Vision

* TensorFlow
* Keras
* MobileNetV2
* OpenCV
* NumPy

### Data Processing

* Pandas

### Geolocation & Mapping

* Folium
* Streamlit Folium
* Google Maps Integration

### Notification System

* SMTP Email Alerts

---

## Machine Learning Model

The crack detection model is built using Transfer Learning with MobileNetV2.

### Model Details

* Input Size: 128 × 128
* Architecture: MobileNetV2
* Output: Binary Classification

  * Crack
  * No Crack

### Training Process

* Dataset preprocessing using ImageDataGenerator
* Transfer Learning with pretrained ImageNet weights
* Binary classification using Sigmoid activation
* Model saved as `crack_model.h5`

---

## Project Structure

```text
sentinova-coastguard-ai/
│
├── app.py
├── train_model.py
├── email_alert.py
├── weekly_report.py
├── crack_model.h5
├── reports.txt
├── dam image.png
│
└── dataset/
    └── train/
        ├── crack/
        └── no_crack/
```

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/sentinova-coastguard-ai.git
cd sentinova-coastguard-ai
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run app.py
```

### 4. Open in Browser

```text
http://localhost:8501
```

---

## Required Libraries

```text
streamlit
tensorflow
opencv-python
numpy
pandas
folium
streamlit-folium
streamlit-geolocation
```

Generate automatically using:

```bash
pip freeze > requirements.txt
```

---

## Future Enhancements

* Engineer verification workflow
* Authority monitoring dashboard
* Multi-language notifications
* Mobile application integration
* Real-time infrastructure monitoring
* Predictive maintenance analytics
* Community reporting portal
* Emergency response coordination support

---

## Impact

CoastGuard AI aims to:

* Detect structural defects at an early stage
* Improve reporting efficiency
* Support proactive maintenance
* Reduce inspection delays
* Enhance infrastructure safety
* Strengthen disaster preparedness
* Improve coordination between citizens, engineers, and authorities

---

## Team Sentinova

### Project

**CoastGuard AI – Infrastructure Monitoring & Early Warning System**

### Tagline

**Detect Early. Act Faster. Save Lives.**

---

Built for the Coastal Innovation Hackathon.
