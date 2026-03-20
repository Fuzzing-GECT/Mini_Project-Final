## VSFTPD Automata Learning Project

This project focuses on learning the behavior of a real FTP server (vsftpd) using automata learning techniques like the L* algorithm.

### Objective

To model the FTP server as a Mealy machine by interacting with it through commands and observing responses.

### Setup

* Install vsftpd
* Configure the server (e.g., enable/disable anonymous login)
* Run the server locally on `127.0.0.1:21`

### Key Components

* **Alphabet**: FTP commands (USER, PASS, LIST, RETR, etc.)
* **Oracle**: Sends commands to vsftpd and collects responses
* **Learner**: Implements the L* algorithm to infer the automaton
* **Evaluation**: Uses metrics like Accuracy, Precision, Recall, and F1-score

### Output

* Learned state machine (Mealy machine)
* Visualization using Graphviz (.dot files)

### Folder Structure
```
/oracle        → Membership queries (interaction with real FTP server)
/learner       → L* algorithm implementation and Mealy machine construction
/evaluation    → Evaluation metrics (F1-score, accuracy)
/ftp           → FTP client code
/configs       → vsftpd configuration files (includes settings and defined alphabet)
/algorithm     → Minimization of inferred automata
```
