# Python 5 mini projects

- this is a collection of 5 (beginner-friendly) projects you can build _fast_ to develop your Python skills from [Shaw's](https://www.shawhintalebi.com/) Newsletter: `5 Python Projects You Can Build After Work`

---
Python is the native (programming) language of AI engineering 🐍

Yet, most newcomers to the field have **never written a single line of it**.

Here are 5 (beginner-friendly) projects you can build _fast_ to develop your Python skills
---

### 1) Automated Birthday Emailer

Create a .csv file containing the birthdays of your friends and family, and then write a simple Python script to email them on their birthdays automatically.

Check out this [example code](https://click.convertkit-mail2.com/v8uq2ovxg5brhv3z9omcghvq080llf9/08hwh9h2x0lo64ul/aHR0cHM6Ly9naXRodWIuY29tL1NoYXdoaW5UL0FJLUJ1aWxkZXJzLUJvb3RjYW1wLTEvYmxvYi9tYWluL3Nlc3Npb24tMS9leGFtcGxlXzEtZW1haWxfYnJvYWRjYXN0LmlweW5i) if you get stuck on the email sending part
---

### 2) PDF Summarizer

Extract the text from a PDF using PyMuPDF, then summarize it using GPT-4o-mini using OpenAI's API.

Here's what that looks like for a research paper: [repo link](https://click.convertkit-mail2.com/v8uq2ovxg5brhv3z9omcghvq080llf9/8ghqhoho3er064ik/aHR0cHM6Ly9naXRodWIuY29tL1NoYXdoaW5UL0FJLUJ1aWxkZXJzLUJvb3RjYW1wLTQvYmxvYi9tYWluL3Nlc3Npb24tMi9leGFtcGxlXzEtcGFwZXJfc3VtbWFyaXplci5pcHluYg==).

---

### 3) Stock Price Visualizer

Use the [yfinance](https://click.convertkit-mail2.com/v8uq2ovxg5brhv3z9omcghvq080llf9/vqh3hrho42wxz2fg/aHR0cHM6Ly9weXBpLm9yZy9wcm9qZWN0L3lmaW5hbmNlLw==) library to download stock price data and visualize it using [Plotly Dash](https://click.convertkit-mail2.com/v8uq2ovxg5brhv3z9omcghvq080llf9/l2hehmhl45x080a6/aHR0cHM6Ly9weXBpLm9yZy9wcm9qZWN0L2Rhc2gv).

Add features to the visualization, like selecting the ticker name and applying different moving average windows
---

### 4) AI Job Board Scraper

Use the requests library to scrape the first page of [https://aijobs.net/](https://click.convertkit-mail2.com/v8uq2ovxg5brhv3z9omcghvq080llf9/m2h7h5h39k4gdqbm/aHR0cHM6Ly9haWpvYnMubmV0Lw==) using [requests](https://click.convertkit-mail2.com/v8uq2ovxg5brhv3z9omcghvq080llf9/dpheh0hekzp4lkfm/aHR0cHM6Ly9weXBpLm9yZy9wcm9qZWN0L3JlcXVlc3RzLw==) and [BeautifulSoup4](https://click.convertkit-mail2.com/v8uq2ovxg5brhv3z9omcghvq080llf9/e0hph7h7e9rp8wt8/aHR0cHM6Ly9weXBpLm9yZy9wcm9qZWN0L2JlYXV0aWZ1bHNvdXA0Lw==).

_Bonus_: Analyze the data to find the top-paying roles and skills using [pandas](https://click.convertkit-mail2.com/v8uq2ovxg5brhv3z9omcghvq080llf9/7qh7h8h98vnkrmbz/aHR0cHM6Ly9weXBpLm9yZy9wcm9qZWN0L3BhbmRhcy8=)
---

### 5) Upwork Job Dashboard

Use [Streamlit](https://click.convertkit-mail2.com/v8uq2ovxg5brhv3z9omcghvq080llf9/owhkhqhwn3qk28sv/aHR0cHM6Ly9weXBpLm9yZy9wcm9qZWN0L3N0cmVhbWxpdC8=) to build a custom dashboard to analyze Upwork job postings.

You can find an extract of job data with example code [here](https://click.convertkit-mail2.com/v8uq2ovxg5brhv3z9omcghvq080llf9/z2hghnhe79l4qoap/aHR0cHM6Ly9naXRodWIuY29tL1NoYXdoaW5UL3Vwd29yay1qb2ItZGFzaGJvYXJk).

---

## Environment

This repo uses `uv` for Python environment.

To start with jupyter notebook, run the following command from terminal:

uv venv
source .venv/bin/activate  # On Windows, use:

```sh
.venv\Scripts\activate
uv pip install jupyter
jupyter notebook
```

or on Linux:

```sh
uv run --with jupyter jupyter lab
```
To create a kernel, you'll need to install `ipykernel` as a development dependency:

```sh
uv add --dev ipykernel
```
Then, you can create the kernel for project with:
```sh
uv run ipython kernel install --user --env VIRTUAL_ENV $(pwd)/.venv --name=project
```
From there, start the server with:
```sh
uv run --with jupyter jupyter lab
```
See more: https://docs.astral.sh/uv/guides/integration/jupyter/

## Resources

- `.gitignore` generate with
  ```sh
  curl -JL https://raw.githubusercontent.com/github/gitignore/refs/heads/main/Python.gitignore -o .gitignore
  ```
