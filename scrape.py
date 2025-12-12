from playwright.sync_api import sync_playwright

def scrape_article(url, output_file):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        try:
            # Changed wait_until to 'domcontentloaded'
            page.goto(url, wait_until='domcontentloaded')
            content = page.content()
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Content successfully saved to {output_file}")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    url = "https://python.plainenglish.io/9-python-libraries-that-make-you-look-like-a-data-scientist-a9960893767a"
    output_file = "article_content_playwright.html"
    scrape_article(url, output_file)
