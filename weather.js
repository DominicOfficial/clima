const API_BASE_URL = "http://127.0.0.1:5000"; // Flask backend URL

// Fetch weather data
async function fetchWeather(city) {
    try {
        const response = await fetch(`${API_BASE_URL}/weather?city=${city}`);
        const data = await response.json();

        if (data.error) {
            alert(data.error);
            return;
        }

        // Update the Current Weather section
        document.getElementById("location").innerHTML = `<span>${data.city}</span>`;
        document.getElementById("temperature").innerHTML = `<span>${data.temperature}</span>°C`;
        document.getElementById("condition").innerHTML = `<span>${data.condition}</span>`;
        document.getElementById("details").innerHTML = `
            Wind: <span>${data.details.wind_speed}</span> km/h<br>
            Humidity: <span>${data.details.humidity}</span>%<br>
            Pressure: <span>${data.details.pressure}</span> hPa
        `;
        document.getElementById("sun-times").innerHTML = `
            Sunrise: <span>${data.sunrise}</span><br>
            Sunset: <span>${data.sunset}</span>
        `;
    } catch (error) {
        console.error("Error fetching weather data:", error);
    }
}

// Fetch alerts
async function fetchAlerts() {
    try {
        const response = await fetch(`${API_BASE_URL}/alerts`);
        const alerts = await response.json();

        const alertsContainer = document.getElementById("alerts-container");
        alertsContainer.innerHTML = alerts.map(alert => `
            <div>
                <h3>${alert.title}</h3>
                <p>${alert.description}</p>
            </div>
        `).join("");
    } catch (error) {
        console.error("Error fetching alerts:", error);
    }
}

// Fetch news
async function fetchNews() {
    try {
        const response = await fetch(`${API_BASE_URL}/news`);
        const news = await response.json();

        const newsContainer = document.getElementById("news-container");
        newsContainer.innerHTML = news.map(article => `
            <div>
                <h3>${article.title}</h3>
                <p>${article.description}</p>
            </div>
        `).join("");
    } catch (error) {
        console.error("Error fetching news:", error);
    }
}

// Event listener for search
document.getElementById("search-btn").addEventListener("click", () => {
    const city = document.getElementById("city-input").value;
    if (city) {
        fetchWeather(city);
    }
});

// Apply the saved theme on page load
document.addEventListener("DOMContentLoaded", () => {
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme === "dark") {
        document.body.classList.add("dark-theme");
    }

    // Fetch initial data
    fetchAlerts();
    fetchNews();
});

// Toggle theme functionality
document.getElementById("theme-toggle-btn").addEventListener("click", () => {
    const body = document.body;
    body.classList.toggle("dark-theme");

    // Save the theme preference in localStorage
    const isDarkTheme = body.classList.contains("dark-theme");
    localStorage.setItem("theme", isDarkTheme ? "dark" : "light");
});