from bs4 import BeautifulSoup

# XML data as a string
xml_data = """
<books>
    <book id="1">
        <title>The Great Catalog</title>
        <author>Marithong</author>
    </book>
</books>
"""

# Parse the XML
soup = BeautifulSoup(xml_data, "xml")

# Save the XML data to a file
with open(r"C:\Users\Dell\Documents\BS.xml", 'w') as f:
    f.write(soup.prettify()) 

# Read and parse the saved XML
with open(r"C:\Users\Dell\Documents\BS.xml", 'r') as file:
    soup = BeautifulSoup(file, "xml")
    title = soup.find("author").text   
    print(title)
