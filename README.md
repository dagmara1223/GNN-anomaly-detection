# GNN-anomaly-detection
## Overview 🗾 
This project is part of my Engineering Thesis, which focuses on detecting anomalous user behavior in data systems. The system combines data engineering and machine learning techniques to identify unusual activity based on user interactions with data warehouse resources.
In this project, I explore graph-based approaches using Graph Neural Networks (GNNs) to model relationships between users, resources, and actions. The goal is to investigate whether graph-based approaches can improve anomaly detection and how are their results compared to other Machine Learning techniques. 

## Dataset selection 📂 
Link to the data (since size is 14 GB, dataset will not be directly stored in github repository): [https://kilthub.cmu.edu/articles/dataset/Insider_Threat_Test_Dataset/12841247](https://kilthub.cmu.edu/articles/dataset/Insider_Threat_Test_Dataset/12841247) <br>
I've used the r4.1 version. <br>

For this project, I chose the CERT Insider Threat Dataset, which simulates realistic user activity within an organization, including logins, file access, email communication, and device usage. <br>
The dataset models insider threat scenarios, where employees may exhibit anomalous behavior such as:
- data exfiltration before leaving the organization  
- sending sensitive files to external email addresses  
- visiting suspicious or job-related websites  
- copying data to external devices (e.g., USB drives)  
- accessing systems outside of regular working hours  

This dataset was selected because it provides a realistic representation of user behavior in enterprise environments, where anomalies may indicate potential security risks.

Before proceeding with the data analysis, I reviewed several research papers that inspired this project and helped shape its methodology. 
