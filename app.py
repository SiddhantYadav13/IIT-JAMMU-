import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import google.generativeai as genai
import os

# Set your Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def scrape_news_headlines(keyword):
    print(f"\n🔍 Searching Bing News for: {keyword} ...")
    url = f"https://www.bing.com/news/search?q={keyword.replace(' ', '+')}&form=QBNH"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = [a.text for a in soup.select('a.title')]
    return headlines

def headlines_to_dataframe(headlines):
    df = pd.DataFrame(headlines, columns=['Headline'])
    df['Length'] = df['Headline'].apply(len)
    return df

def visualize_data(df):
    df['Length'].plot.hist(bins=10, color='skyblue', edgecolor='black')
    plt.title("📰 Headline Length Distribution")
    plt.xlabel("Characters")
    plt.ylabel("Number of Headlines")
    plt.tight_layout()
    plt.show()

def summarize_with_gemini(headlines):
    model = genai.GenerativeModel('gemini-1.5-pro')
    prompt = "Summarize the following news headlines:\n" + "\n".join(headlines[:6])
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"❌ Gemini error: {e}")
        return ""

def main():
    keyword = input("🔑 Enter a keyword to search news for: ")
    headlines = scrape_news_headlines(keyword)
    if not headlines:
        print("😕 No headlines found.")
        return
    df = headlines_to_dataframe(headlines)
    print("\n📋 Headlines Table:\n")
    print(df)

    filename = f"{keyword.replace(' ', '_')}_headlines.csv"
    df.to_csv(filename, index=False)
    print(f"\n📁 Headlines exported to: {filename}")

    visualize_data(df)

    print("\n📡 Calling Gemini for insight summary...")
    summary = summarize_with_gemini(headlines)
    print("\n📝 Insight Summary:\n")
    print(summary or "⚠️ Summary failed.")

if __name__ == "__main__":
    main()
