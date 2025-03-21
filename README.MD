# **MockBot - A Discord Bot for Mocking Users**

![Azure](https://img.shields.io/badge/Azure-Cloud-blue)
![Python](https://img.shields.io/badge/Python-3.9-green)
![Docker](https://img.shields.io/badge/Docker-Container-orange)
![Discord](https://img.shields.io/badge/Discord-Bot-purple)

MockBot is a fun and interactive Discord bot that mocks users by alternating the case of their messages. It is hosted on **Azure Container Instances (ACI)** and deployed using **Docker**. This project demonstrates my skills in Python, Docker, Azure, and DevOps.

---

## **Features**
- **Mock Command**: Mocks a user's last message in the current channel.
- **Slash Commands**: Built using `py-cord` for seamless integration with Discord.
- **Azure Hosting**: Deployed on Azure Container Instances for scalability and reliability.
- **Dockerized**: Containerized for easy deployment and environment consistency.

---

## **Technologies Used**
- **Programming Language**: Python
- **Libraries**: `py-cord` (Discord API wrapper)
- **Cloud Platform**: Microsoft Azure
  - Azure Container Instances (ACI)
  - Azure Container Registry (ACR)
- **Containerization**: Docker
- **Version Control**: Git/GitHub

---

## **How It Works**
1. The bot listens for the `/mock @User` command in a Discord channel.
2. It fetches the last 100 messages in the channel and finds the most recent message from the specified user.
3. The bot mocks the message by alternating uppercase and lowercase letters.
4. The mocked message is sent back to the channel.

---

## **Setup and Deployment**

### **Prerequisites**
- Python 3.9 or higher
- Docker installed locally
- Azure account (free tier available)
- Discord bot token (from the [Discord Developer Portal](https://discord.com/developers/applications))

---

### **Local Development**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/mockbot.git
   cd mockbot