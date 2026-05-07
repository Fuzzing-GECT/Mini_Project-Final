Here’s a **complete, clean, compact, ready-to-copy README** (standard GitHub style, not overloaded, recruiter-friendly 👇)

---

# VSFTPD State Machine Learning

## 📌 Project Overview

This project focuses on learning the behavior of FTP servers such as **vsftpd** and **pyftpdlib** by treating them as **black-box systems**. Using the **L*** automata learning algorithm, the system interacts with the server through FTP commands and observes responses to automatically construct a **Mealy Machine (state machine)** representing the server’s internal logic.
This approach enables understanding of protocol behavior without requiring access to source code.

## 🎯 Objective

* Infer FTP server behavior using input–output interactions
* Automatically construct a state machine model using the L* algorithm
* Minimize and visualize the learned model
* Validate the model against real server responses
* Provide a foundation for protocol testing and analysis

## ⚙️ Approach

* Perform **Membership Queries** by sending FTP commands and collecting responses
* Use **Equivalence Queries** to validate and refine the learned model
* Iteratively construct and minimize the **Mealy Machine**
* Compare the learned model with actual server behavior

## 🧩 Key Components

* **Learner** – Implements the L* algorithm
* **Oracle** – Acts as an interface between the learner and the FTP server
* **Target System** – FTP servers (vsftpd / pyftpdlib)
* **Evaluation** – Metrics such as Accuracy, Precision, Recall, F1-score
* **Visualization** – Graph representation using Graphviz

## 🛠️ Setup

* Install and configure an FTP server (vsftpd or pyftpdlib)
* Run the server locally (e.g., `127.0.0.1:21`)
* Execute the learning modules to begin state inference

## 📂 Project Structure

```
/oracle        → Handles interaction with FTP server
/learner       → L* algorithm implementation
/evaluation    → Metrics and validation
/ftp           → FTP client implementation
/configs       → Server configurations and input alphabet
/algorithm     → Automata minimization
```

## 📊 Results
- Successfully inferred the **state machine model** of FTP servers (vsftpd and pyftpdlib)  
- Identified multiple states representing authentication, session handling, and data transfer behavior  
- Generated **visual representations** of the learned models using Graphviz  
- Evaluated performance using **Accuracy, Precision, Recall, and F1-score**  
- Learned model shows strong consistency with actual server responses  

**Custom FTP Server Results**
<img width="2048" height="939" alt="unnamed" src="https://github.com/user-attachments/assets/58926767-2705-439d-96f9-c360b9eec254" />
**Real System using PYFTPDlib**
<img width="1522" height="1600" alt="unnamed" src="https://github.com/user-attachments/assets/5102ee42-2fc7-4bb3-951a-3a4d3947af2c" />
**Real System using VSFTPD**
<img width="2048" height="1060" alt="unnamed" src="https://github.com/user-attachments/assets/5a3ed159-2c20-428e-b87c-f84dad5b9e1c" />






## 👥 Team Members
- **Aryadevi P N**  
- **A Sireesha Menon**  
- **Goury Unnikrishnan**  
- **Gayathri Shaji**
