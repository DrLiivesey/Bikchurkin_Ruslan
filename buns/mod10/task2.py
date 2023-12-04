import re
import requests

# Fetch the webpage content
url = 'http://www.columbia.edu/~fdc/sample.html'
response = requests.get(url)
content = response.text

# Extract the subheadings using regular expressions
subheadings = re.findall(r'<h3 id=".*?">(.*?)</h3>', content)

# Print the subheadings
print(subheadings)
