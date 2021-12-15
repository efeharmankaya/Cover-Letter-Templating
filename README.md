# Cover Letter Templating
Cover Letter Templating aids in automating the repetitive task of copy and pasting in specific job information into a prewritten cover letter template. With this repo you can easily setup your cover letter template to accept parameterized sections and create an automated pdf file based on your template image.

# Setup

Clone repo to your local environment
```bash
git clone https://github.com/efeharmankaya/Cover-Letter-Templating.git
```
Install pip package for PDF writing
```bash
pip3 install fpdf
```

# Usage

Follow `TODO:` tags in main.py

0. Before beginning you must have a prewritten cover letter template 
1. After cloning the repo, replace lorem ipsum cover letter template with your letter template following the template convention from the given example (ie. any text that should be variable should be )
2) Set parameters based on job posting information

Once all TODOs are completed, simply run to generate n pdf files.
```bash
> python main.py
```

# Troubleshooting

### Issues with fpdf

```bash
# try one of the following
> pip install fpdf
> python -m pip install

# update pip
> python -m pip install --upgrade pip

# macOs/Linux
> sudo pip install fpdf
```
### Additional fpdf troubleshooting resources:
    
- [PyFPDF docs](https://pyfpdf.readthedocs.io/en/latest/index.html)
