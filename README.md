# OLR_price_analysis

This code runs a parser to retrieve information from Kabum website (example) and get processor prices listed on files.
It provides a preview of the values printed together with the runtime value benchmarked in atual run.

## Features
- Get Processor `title` Name
- Get Processor `price` Value
- Saves theses `values` on a file storing the date when it was requested to run
- Also has a proxy (if needed, as my case)

# How to run
First you need to install these libs:
`pip install bs4`
`pip install urllib`
`pip install requests`

# Updates
Firstly the code was running using chromedirver (selenium), but the performance was very low.
Below is the Benchmark of the updat from Selenium to bs4 + urllib.

### Example
![Selenium to bs4 + urllib](https://i.imgur.com/D9PEkwQ.png)


### Further Examples
Here I searched for a russian website (dns-shop) to scrap the price:
![dns-shop](https://i.imgur.com/7CqKcqM.png)

Every website is built different, so parsing url for each site needs some work first*


`Where to improve`
- Remove the "hardcoded" links
- Study an automated faster way to parse different websites
- Creating a better way to preview and analyze the parsed data
