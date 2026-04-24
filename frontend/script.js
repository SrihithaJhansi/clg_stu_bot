// College Assistant Frontend - Fixed Version

class CollegeAssistant {
    constructor() {
        this.apiUrl = "http://127.0.0.1:8000";
        this.orchestrationMode = "simple";
        this.isTyping = false;

        this.initializeElements();
        this.bindEvents();

        // 🔥 Initial check
        this.checkBackendStatus();

        // 🔥 Keep checking backend every 2 seconds
        setInterval(() => {
            this.checkBackendStatus();
        }, 2000);
    }

    initializeElements() {
        this.chatMessages = document.getElementById("chat-messages");
        this.userInput = document.getElementById("user-input");
        this.sendButton = document.getElementById("send-button");
        this.modeSelect = document.getElementById("mode-select");
        this.statusIndicator = document.getElementById("status-indicator");
        this.statusText = document.getElementById("status-text");
        this.typingIndicator = document.getElementById("typing-indicator");
        this.charCount = document.getElementById("char-count");
    }

    bindEvents() {
        this.sendButton.addEventListener("click", () => this.sendMessage());

        this.userInput.addEventListener("keypress", (e) => {
            if (e.key === "Enter" && !e.shiftKey) {
                e.preventDefault();
                this.sendMessage();
            }
        });

        this.userInput.addEventListener("input", () => {
            this.updateCharCount();
        });

        this.modeSelect.addEventListener("change", (e) => {
            this.orchestrationMode = e.target.value;
            this.showNotification(`Switched to ${this.orchestrationMode} mode`);
        });

        this.updateCharCount();
    }

    // ✅ FIXED STATUS CHECK
    async checkBackendStatus() {
        try {
            const response = await fetch(`${this.apiUrl}/health`);

            if (response.ok) {
                this.setStatus("connected", "Backend Connected ✅");
            } else {
                this.setStatus("error", "Backend Issue");
            }

        } catch (error) {
            this.setStatus("error", "Backend Offline ❌");
        }
    }

    setStatus(status, text) {
        this.statusIndicator.className = `status-indicator ${status}`;
        this.statusText.textContent = text;
    }

    updateCharCount() {
        const count = this.userInput.value.length;
        this.charCount.textContent = count;
        this.charCount.style.color = count > 450 ? "#ef4444" : "#666";
    }

    async sendMessage() {
        const query = this.userInput.value.trim();
        if (!query || this.isTyping) return;

        this.addMessage(query, "user");
        this.userInput.value = "";
        this.updateCharCount();
        this.setTyping(true);

        try {
            const response = await fetch(
                `${this.apiUrl}/ask?query=${encodeURIComponent(query)}&mode=${this.orchestrationMode}`
            );

            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }

            const data = await response.json();

            // ✅ FORCE status update
            this.setStatus("connected", "Backend Connected ✅");

            this.addMessage(data.response, "bot");

        } catch (error) {
            console.error("API Error:", error);

            this.setStatus("error", "Backend Offline ❌");

            this.addMessage(
                "⚠️ Backend connection failed. Please check server.",
                "bot"
            );
        } finally {
            this.setTyping(false);
        }
    }

    addMessage(text, type) {
        const messageDiv = document.createElement("div");
        messageDiv.className = `message ${type}`;

        const avatar = document.createElement("div");
        avatar.className = "avatar";
        avatar.innerHTML = type === "user"
            ? "👤"
            : "🤖";

        const content = document.createElement("div");
        content.className = "message-content";

        const textDiv = document.createElement("div");
        textDiv.className = "message-text";
        textDiv.innerHTML = this.formatMessage(text);

        const timeDiv = document.createElement("div");
        timeDiv.className = "message-time";
        timeDiv.textContent = new Date().toLocaleTimeString([], {
            hour: '2-digit',
            minute: '2-digit'
        });

        content.appendChild(textDiv);
        content.appendChild(timeDiv);

        messageDiv.appendChild(avatar);
        messageDiv.appendChild(content);

        this.chatMessages.appendChild(messageDiv);
        this.scrollToBottom();
    }

    formatMessage(text) {
        return text.replace(/\n/g, "<br>");
    }

    setTyping(typing) {
        this.isTyping = typing;
        this.sendButton.disabled = typing;

        this.typingIndicator.style.display = typing ? "flex" : "none";
    }

    scrollToBottom() {
        setTimeout(() => {
            this.chatMessages.scrollTop = this.chatMessages.scrollHeight;
        }, 100);
    }

    showNotification(message) {
        alert(message);
    }
}

// Init
document.addEventListener("DOMContentLoaded", () => {
    window.collegeAssistant = new CollegeAssistant();
});