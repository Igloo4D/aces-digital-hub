from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def fetch_lotr_wiki(character_name):
    base_url = "https://lotr.fandom.com/wiki/"
    search_url = f"{base_url}{character_name.replace(' ', '_')}"

    response = requests.get(search_url)
    if response.status_code != 200:
        return {"error": "Character not found"}

    soup = BeautifulSoup(response.text, "html.parser")

    name = soup.find("h1").text if soup.find("h1") else character_name
    title = soup.find("i").text if soup.find("i") else "No title found"
    race = "Unknown"

    # Searching for race in the sidebar
    infobox = soup.find(class_="portable-infobox")
    if infobox:
        for row in infobox.find_all("tr"):
            if "Race" in row.text:
                race = row.find("td").text.strip()

    return {
        "name": name,
        "title": title,
        "race": race,
        "wiki": search_url
    }

@app.route("/lotr", methods=["GET"])
def get_lotr_character():
    query = request.args.get("search", "")
    if not query:
        return jsonify({"error": "No character provided"}), 400

    data = fetch_lotr_wiki(query)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
