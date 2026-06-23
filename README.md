# CoastGuard AI

### AI-Powered Infrastructure Monitoring & Early Warning System

**Built by Team Sentinova**

**Detect Early. Act Faster. Save Lives.**

CoastGuard AI is an intelligent infrastructure monitoring platform that leverages Artificial Intelligence, Computer Vision, Geolocation Tracking, and Automated Alerting to detect structural cracks in critical infrastructure and support timely decision-making for infrastructure safety.

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

## Screenshots

### Home Dashboard

<img width="1600" height="766" alt="image6" src="https://github.com/user-attachments/assets/b7e6093a-a8b2-434f-9a59-17888f350ab6" />

### Crack Detection Dashboard
<img width="1900" height="907" alt="image" src="https://github.com/user-attachments/assets/5113a61e-ca1f-42be-92e0-298cc469577c" />

<img width="1910" height="837" alt="image" src="https://github.com/user-attachments/assets/d243ee50-a143-4e3f-8ece-9c172e973bc0" />




### Severity Analysis
<img width="1907" height="837" alt="image" src="https://github.com/user-attachments/assets/a3a7de04-a6ea-4dc5-b60b-b2632aab4af3" />
<img width="1902" height="912" alt="image" src="https://github.com/user-attachments/assets/a07d9593-35b4-4e5c-ae04-ef2d20fe42c8" />
<img width="1600" height="708" alt="image8" src="https://github.com/user-attachments/assets/480b70f7-7964-4f21-a575-b21407cb5800" />
<img width="1596" height="690" alt="image" src="https://github.com/user-attachments/assets/613bc066-b7f5-425b-ad10-35fee056b19f" />

### Alert Generation

<img width="1602" height="757" alt="image" src="https://github.com/user-attachments/assets/9f700267-b799-42ec-83b9-0b8d9984f2ce" />
<img width="1595" height="676" alt="image" src="https://github.com/user-attachments/assets/7ad61999-e3b9-463d-9a79-249cfdc3a5f7" />



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
## Dataset

The training dataset is not included in this repository due to storage limitations.

The crack detection model was trained on a labeled crack/non-crack image dataset using MobileNetV2 transfer learning. The trained model (`crack_model.h5`) is included for inference and demonstration purposes.


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
├── requirements.txt
├── README.md

```

---

## Installation & Setup

### Clone the Repository

```bash
git clone https://github.com/Shrama-v-shetty/sentinova-coastguard-ai.git
cd sentinova-coastguard-ai
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

### Open in Browser

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

---

## Demo Video

Video Demonstration:

https://drive.google.com/file/d/1dzEhcPVZxo5UBpX2FSUT6x7n-1I_AnN9/view?usp=sharing

---

## Delpoyed website Demo

Access the deployed application here:

https://your-render-link.onrender.com

## Future Enhancements

* Engineer verification workflow
* Authority monitoring dashboard
* Community reporting portal
* Multi-language notifications
* Mobile application integration
* Real-time infrastructure monitoring
* Predictive maintenance analytics
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

## License

This project was developed for educational, research, and demonstration purposes.

---

Built with ❤️ by Team Sentinova.
