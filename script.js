document.addEventListener("DOMContentLoaded", function () {
    const searchForm = document.getElementById("search-form");
    const searchInput = document.getElementById("search-input");
    const resultsDiv = document.getElementById("results");

    searchForm.addEventListener("submit", async function (event) {
        event.preventDefault(); // Prevent page refresh

        const query = searchInput.value.trim();
        if (!query) return;

        resultsDiv.innerHTML = "<p>Searching...</p>";

        try {
            const response = await fetch(`http://127.0.0.1:5000/lotr?search=${encodeURIComponent(query)}`);
            const data = await response.json();

            if (!data || Object.keys(data).length === 0) {
                resultsDiv.innerHTML = `<p>No results found for "${query}".</p>`;
                return;
            }

            // Display results dynamically
            resultsDiv.innerHTML = `
                <h3>${data.name}</h3>
                <p><strong>Race:</strong> ${data.race || "Unknown"}</p>
                <p><strong>Title:</strong> ${data.title || "N/A"}</p>
                <p><a href="${data.wiki}" target="_blank">Read More on LotR Wiki</a></p>
            `;
        } catch (error) {
            resultsDiv.innerHTML = `<p>Error fetching data. Try again later.</p>`;
            console.error("Fetch error:", error);
        }
    });
});
