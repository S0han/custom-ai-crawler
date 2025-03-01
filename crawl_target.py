import asyncio
import json
from crawl4ai import AsyncWebCrawler

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url="https://www.thekaneologist.com/")
        
        data = {
            "url": "https://www.thekaneologist.com/",
            "content": result.markdown
        }

        with open("output.json", "w") as f:
            json.dump(data, f, indent=2)

if __name__ == "__main__":
    asyncio.run(main())