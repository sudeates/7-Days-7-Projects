# 🚀 Day 1: Building a Custom HTTP Web Server from Scratch

Welcome to **Day 1** of my "7 Days - 7 Systems" challenge! Today, I dived deep into the networking layer to build a functional Web Server using Python's low-level `socket` library, without relying on any external frameworks like Flask or Django.



## 📝 Project Overview
The goal of this project was to understand how the internet works at a fundamental level. By implementing a manual socket-based server, I gained hands-on experience with the **TCP/IP stack** and the **HTTP/1.1 protocol**.

## 🛠️ Technical Architecture: How It Works

The server follows a classic **Request-Response cycle**. Here is the step-by-step breakdown of the system's internal logic:

### 1. The Socket Lifecycle
* **Creation:** The server initializes a TCP socket using `socket.AF_INET` (IPv4) and `socket.SOCK_STREAM` (TCP).
* **Binding & Listening:** It binds to `127.0.0.1:8080` and starts listening for incoming connection attempts.
* **Acceptance:** When a client (browser) connects, the server performs the **TCP Three-Way Handshake** and creates a dedicated connection object.

### 2. Request Processing (The Parser)
Once connected, the server receives raw binary data from the client. 
* **Decoding:** The raw bytes are decoded into an ASCII/UTF-8 string.
* **Parsing:** The server extracts the **HTTP Method** (GET, POST, etc.) and the **Request URI** (the file path) from the first line of the header (e.g., `GET /index.html HTTP/1.1`).



### 3. File System Integration & MIME Mapping
The server acts as a gateway to the local `public/` directory:
* **Security:** It maps the requested URI to a local file path while ensuring it stays within the designated folder.
* **MIME Types:** To ensure the browser renders files correctly, the server dynamically sets the `Content-Type` header based on file extensions (`.html`, `.css`, `.jpg`, etc.).

### 4. Response Engineering & Error Handling
* **Successful Hits (200 OK):** The server constructs a valid HTTP response, attaches the file content (the payload), and calculates the `Content-Length`.
* **Graceful 404 Handling:** If the requested file doesn't exist, the server doesn't crash. Instead, it catches the `FileNotFoundError` and returns a custom-styled **404 Not Found** page with the appropriate status code.



## 🏗️ Project Structure
```text
.
├── server.py        # The "Brain": Handles sockets and HTTP logic
├── public/          # The "Assets": Static files served to the client
│   ├── index.html   # Main entry point
│   ├── style.css    # Custom CSS for styling
│   └── 404.html     # Custom error page
└── README.md        # Technical Documentation

# 🚀 Day 2: Build Your Own CLI Tool (GitHub Profiler)

Welcome to **Day 2** of my "7 Days - 7 Systems" challenge! Today, I moved away from the browser and into the terminal to build a **Command Line Interface (CLI)** tool that interacts with the GitHub REST API.



## 📝 Project Overview
The goal today was to understand how professional terminal tools (like `git`, `docker`, or `npm`) handle user inputs and fetch real-world data. I built a Python-based analyzer that retrieves a user's GitHub stats directly to the console.

## 🛠️ How It Works (The Engineering Logic)

### 1. Argument Parsing (`sys.argv`)
Unlike a web app where you click buttons, a CLI tool takes input directly from the command line. I used the `sys` module to capture the "arguments" you type after the script name.
* Example: `python analyzer.py gemini-user` -> The code grabs `gemini-user` and starts the search.

### 2. Consuming REST APIs
I utilized the `requests` library to communicate with the **GitHub REST API**. 
* The tool sends a `GET` request to `https://api.github.com/users/{username}`.
* It handles the **JSON response**, parsing keys like `public_repos`, `followers`, and `location`.

### 3. Status Code Management
A good tool must handle errors gracefully:
* **200 OK:** Data is found and printed with icons.
* **404 Not Found:** The tool alerts the user that the profile doesn't exist instead of crashing.

# 🎮 Day 3: Build Your Own 3D Wireframe Renderer

On **Day 3**, I explored the intersection of Linear Algebra and Computer Graphics. I built a real-time 3D renderer from scratch using Python and `pygame`.

## 🧠 The Math Behind the Magic
* **3D Projection:** Converting 3D coordinates $(x, y, z)$ into 2D screen coordinates $(x', y')$ using perspective projection formulas.
* **Rotation Matrices:** Implementing Trigonometric functions ($\sin$ and $\cos$) to rotate vertices in 3D space.
* **Rendering Pipeline:** Managing the frame loop: Clear -> Transform -> Draw -> Update.

## 🛠️ Tech Stack
* **Language:** Python
* **Library:** Pygame (for pixel drawing)
* **Concepts:** Linear Algebra, Trigonometry, Frame Buffers.

---
*Next up: **Day 4 - Build Your Own Version Control System (VCS)**!*