import requests
from bs4 import BeautifulSoup

def scrape_headlines():
    # 1. Define the URL and User-Agent
    # (The User-Agent makes your script look like a real browser, preventing blocks)
    url = "https://news.ycombinator.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        # 2. Fetch the HTML
        print(f"Fetching news from {url}...")
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful (Status Code 200)
        response.raise_for_status()

        # 3. Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 4. Find the specific tags containing headlines
        # On Hacker News, headlines are usually in a <span> with class 'titleline'
        # Note: On other sites (like BBC), you might look for 'h2' or 'h3' tags
        headlines = soup.find_all('span', class_='titleline')
        
        # List to store cleaned text
        extracted_titles = []

        print(f"Found {len(headlines)} headlines. Saving to file...")

        # 5. Extract text and save to list
        for index, headline in enumerate(headlines, 1):
            title_text = headline.get_text()
            extracted_titles.append(f"{index}. {title_text}")

        # 6. Save to a .txt file
        with open("news_headlines.txt", "w", encoding="utf-8") as file:
            file.write(f"Top Headlines from {url}\n")
            file.write("=" * 40 + "\n\n")
            for title in extracted_titles:
                file.write(title + "\n")
        
        print("Success! Check 'news_headlines.txt' for your results.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    scrape_headlines()