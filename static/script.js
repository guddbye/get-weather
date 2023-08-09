document.addEventListener("DOMContentLoaded", () => {
    const submitBtn = document.getElementById("submitBtn");
    const weatherContainer = document.getElementById("weatherContainer");

    submitBtn.addEventListener("click", async () => {
        const cityInput = document.getElementById("cityInput").value;

        if (cityInput) {
            try {
                const response = await fetch(`/weather/${cityInput}`);
                const data = await response.json();

                weatherContainer.innerHTML = `
                    <h2>${data.location.name}, ${data.location.region}, ${data.location.country}</h2>
                    <p>Current Weather: ${data.current.condition.text}</p>
                    <p>Temperature: ${data.current.temp_c}°C</p>
                    <p>Wind Speed: ${data.current.wind_kph} km/h</p>
                `;
            } catch (error) {
                console.error("Error fetching weather data:", error);
            }
        }
    });
});
