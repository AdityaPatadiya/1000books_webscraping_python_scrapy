# 1000books_webscraping_python_scrapy
This is a webscraping project using Python and Scrapy to scrape the [website](https://books.toscrape.com).
The [scrapy](https://scrapy.org/) library is very useful to scrap the large amount of data.
The [scrapeops api](https://scrapeops.io/) is used for the different BrowserHeaders.

## Table of Contents
- [Requirements](https://github.com/AdityaPatadiya/1000books_webscraping_python_scrapy/blob/main/README.md#requirements)
- [Installation](https://github.com/AdityaPatadiya/1000books_webscraping_python_scrapy/blob/main/README.md#installation)
- [How to Run the Project](https://github.com/AdityaPatadiya/1000books_webscraping_python_scrapy/blob/main/README.md#how-to-run-the-project)
- [What I've Done](https://github.com/AdityaPatadiya/1000books_webscraping_python_scrapy/blob/main/README.md#what-ive-done)
- [Key Files](https://github.com/AdityaPatadiya/1000books_webscraping_python_scrapy/blob/main/README.md#key-files)
- [Contributing](https://github.com/AdityaPatadiya/1000books_webscraping_python_scrapy/blob/main/README.md#contributing)

## Requirements: -
1. Python
2. [Scrapy](https://scrapy.org/)
3. [scrapeops api](https://scrapeops.io/) for use different BrowserHeaders.
4. [SQLite](https://www.sqlite.org/) Database

## Installation: -
1. Clone the repository
```sh
    git clone https://github.com/AdityaPatadiya/1000books_webscraping_python_scrapy.git
    
    cd bookscraper
```
2. Create a virtual environment using the following command:
```bash
python -m venv venv
```
3. Activate the virtual environment:
```bash
# for windows
.\venv\Scripts\activate

# for mac
source venv/bin/activate
```
4.install the required packages using the following commands:
```bash
pip install -r requirements.txt
```

## How to run the project: -
To run the project, use the following command:
```bash
cd bookscraper

scrapy crawl bookspider
```

## What I've done: -
I used to scrap 1000 of books from the website and store the data in the **JSON** file,
and also I used **SQLite** database to store the scraped data.
The scraped data is stored in **SQLite** database.
And also it will create the **JSON** file.

The **scrapeops api** provides different BrowserHeaders to avoid the blocking of the website.

> [!WARNING]
> Before going to scrape any website,
> we should obey the robots.txt file of that website
> to avoid violating the website's terms of service and potentially engaging in illegal or unethical behavior.

The settings.py provides that feature to avoid violating the website's terms of service.

### Key Files
- [bookspider.py](https://github.com/AdityaPatadiya/1000books_webscraping_python_scrapy/blob/main/bookscraper/bookscraper/spiders/bookspider.py): Main spider code for scraping data.
- [items.py](https://github.com/AdityaPatadiya/1000books_webscraping_python_scrapy/blob/main/bookscraper/bookscraper/items.py): Defines the fields to be scraped.
- [pipelines.py](https://github.com/AdityaPatadiya/1000books_webscraping_python_scrapy/blob/main/bookscraper/bookscraper/pipelines.py): Operations on scraped data and storage in SQLite.
- [middlewares.py](https://github.com/AdityaPatadiya/1000books_webscraping_python_scrapy/blob/main/bookscraper/bookscraper/middlewares.py): Applies ScrapeOps API Browser Headers.
- [settings.py](https://github.com/AdityaPatadiya/1000books_webscraping_python_scrapy/blob/main/bookscraper/bookscraper/settings.py): Scrapy project settings including ScrapeOps API credentials.

> [!TIP]
> We can also use the **scrapy shell** to test the code before running the spider.
> The **scrapy shell** is a command-line tool that allows you to test your XPath or CSS selectors and run Python code in the context of a Scrapy project.
>
> First we have to install the **ipython** package using the following command:
> ```bash
> pip install ipython
> ```
> and also add the following line in the **scrapy.cfg** file:
> ```bash
> shell = ipython
> ```
> To run the **scrapy shell**, use the following command in terminal:
> ```bash
> scrapy shell
> ```
> Here you can test your code in the shell by providing the XPath or CSS selectors.

## Contributing: -

We welcome contributions from the community! Here are some guidelines to help you get started:
### How to Contribute

1. **Fork the repository**: Click the "Fork" button at the top of this repository to create a copy of the repository under your own GitHub account.

2. **Clone your fork**: Clone your forked repository to your local machine using the following command:
    ```sh
    git clone https://github.com/AdityaPatadiya/1000books_webscraping_python_scrapy.git
    ```

3. **Create a new branch**: Create a new branch for your feature or bugfix with a descriptive name:
    ```sh
    git checkout -b your-branch-name
    ```

4. **Make your changes**: Make your changes to the codebase. Ensure that your code follows the project's coding standards and passes all tests.

5. **Commit your changes**: Commit your changes with a clear and descriptive commit message:
    ```sh
    git add .
    git commit -m "Description of your changes"
    ```

6. **Push to your fork**: Push your changes to your forked repository:
    ```sh
    git push origin your-branch-name
    ```

7. **Open a Pull Request**: Go to the original repository on GitHub and open a pull request. Provide a clear and descriptive title and description for your pull request.

Getting Help
If you need any help, feel free to ask questions in the [Discussions](https://github.com/AdityaPatadiya/1000books_webscraping_python_scrapy/discussions) section or contact the maintainers.

Thank you for your interest in contributing!