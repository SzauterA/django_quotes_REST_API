function fetchQuote() {
    fetch("http://127.0.0.1:8000/api/quote/")
        .then(response => response.json())
        .then(data => {
            document.getElementById("quote-text").innerText = `"${data.text}"`;
            document.getElementById("quote-author").innerText = `- ${data.author}`;
        })
        .catch(error => {
            console.error("Error fetching quote:", error);
            document.getElementById("quote-text").innerText = "Oops! Something went wrong.";
            document.getElementById("quote-author").innerText = "";
        });
}

document.addEventListener("DOMContentLoaded", fetchQuote);

document.getElementById("new-quote").addEventListener("click", fetchQuote);