import os
import re
import time
from typing import List, Tuple
from collections import deque

import click
from bs4 import BeautifulSoup
import requests
import markdownify


ROOT_URL = "https://doc.dataiku.com/dss/latest"
LASTEST_STR_INDEX = ROOT_URL.split("/").index("latest")

def get_child_urls(parent_url: str) -> List[str]:
    response = requests.get(parent_url)
    soup = BeautifulSoup(response.content, "html.parser")
    main = soup.find("div", {"role": "main"})
    toctree_wrapper = main.find("div", {"class": "toctree-wrapper compound"})

    urls = re.findall('href="(.*)"', str(toctree_wrapper))
    urls = [url.split("#")[0] for url in urls]

    # 중복 url 제거
    urls = list(dict.fromkeys(urls))
    return urls

def crawl(url: str) -> str | None:
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        main = soup.find("div", {"role": "main"})

        md = markdownify.markdownify(str(main))
        return md
    
    except Exception as e:
        print(f"{url} failed")
        print(e)
        return None

def save_markdown(markdown: str, file_path: str) -> None:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(markdown)

def extract_save_path(url: str) -> Tuple[str, str]:
    url_splits = url.split("/")
    filename = url_splits[-1].replace("html", "md")
    save_path = "/".join(url_splits[LASTEST_STR_INDEX + 1:-1])

    return save_path, filename

@click.command()
@click.option("--output_dir", default="./data/dataiku", help="save directory")
def main(output_dir: str) -> None:
    start_time = time.time()
    processed  = []
    urls = get_child_urls(ROOT_URL)
    urls = deque([f"{ROOT_URL}/{url}" for url in urls])

    while urls:
        url = urls.popleft()
        print(f"url: {url}")

        if url in processed:
            continue

        markdown = crawl(url)

        if markdown is not None:
            save_path, filename = extract_save_path(url)
            os.makedirs(f"{output_dir}/{save_path}", exist_ok=True)
            file_path = f"{output_dir}/{save_path}/{filename}"

            save_markdown(markdown.strip(), file_path)

            if filename == "index.md":
                parent_url = ROOT_URL + "/" + save_path
                child_urls = [f"{ROOT_URL}/{save_path}/{url}" for url in get_child_urls(parent_url)]
                urls.extend(child_urls)
        
            processed.append(url)
    end_time = time.time()

    print(f"Crawling completed")
    print(f"Total: {len(processed)}")
    print(f"Collapsed time: {(end_time - start_time) / 60:.2f} min")


if __name__ == "__main__":
    main()