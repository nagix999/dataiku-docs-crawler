## Dataiku Docs Crawler

This repository contains code for crawling Dataiku documentation. The collected data serves as foundational input for a Dataiku chatbot. The data is organized into folders corresponding to each Dataiku Docs page and is saved with a markdown (.md) extension.

## Environment

-   Operating System: Windows
-   Python Version: 3.10.11

## Estimated Time Required

-   Approximately 10 ~ 15 minutes

## How to Use

1. Clone the repository:

```
git clone https://github.com/nagix999/dataiku-docs-crawler.git
```

2. Navigate to the project directory:

```
cd dataiku-docs-crawler
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Run the crawler script, specifying your desired output directory
   (default: ./data/dataiku):

```
python crawl_dataiku.py --output_dir your/save/directory
```
