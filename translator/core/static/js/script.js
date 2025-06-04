// 🎤 Start speech recognition and fill input box
function startListening() {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = document.getElementById("sourceLang").value;
    recognition.interimResults = false;

    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;
        document.getElementById("inputText").value = transcript;
    };

    recognition.onerror = function(event) {
        alert("Speech recognition error: " + event.error);
    };

    recognition.start();
}

// 🌐 Call backend to translate text
function translateText() {
    const inputText = document.getElementById("inputText").value;
    const sourceLang = document.getElementById("sourceLang").value;
    const targetLang = document.getElementById("targetLang").value;

    if (!inputText.trim()) {
        alert("Please enter or speak text first.");
        return;
    }

    fetch("/translate/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken()
        },
        body: JSON.stringify({
            text: inputText,
            src: sourceLang,
            tgt: targetLang
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("outputText").value = data.translated_text;
    })
    .catch(error => {
        console.error("Translation error:", error);
        alert("Translation failed. *Combination not available. *Check the server console or network tab.");
    });
}

// 🔊 Speak the translated text
function speakText() {
    const outputText = document.getElementById("outputText").value;
    const targetLang = document.getElementById("targetLang").value;

    if (!outputText.trim()) {
        alert("Nothing to speak!");
        return;
    }

    const utterance = new SpeechSynthesisUtterance(outputText);
    utterance.lang = targetLang;
    speechSynthesis.speak(utterance);
}

// 🔐 Helper to get CSRF token from cookie
function getCSRFToken() {
    const name = 'csrftoken';
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
        const c = cookie.trim();
        if (c.startsWith(name + '=')) {
            return c.substring(name.length + 1);
        }
    }
    return '';
}
