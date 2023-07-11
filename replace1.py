# Open and read the HTML file.
with open('updated.txt', 'rb') as file:
    html_content = file.read().decode(errors='replace')

# List of placeholders
placeholders    = [
'[linklink]',

]

# List of replacements
replacements = [
    'https://e6d24pnxocj7cyb9v2zhl4zp8z.hop.clickbank.net/?tid=endopeak',





    
    
    ]

# Check if both lists have same length
if len(placeholders) != len(replacements):
    print(len(placeholders))
    print(len(replacements))

    raise ValueError("Both lists should have same number of elements")

# Replace placeholders with replacements
for i in range(len(placeholders)):
    if(placeholders[i] in html_content ):
        html_content = html_content.replace(placeholders[i], replacements[i])

# Write the new HTML to a file.
with open('updated.html', 'wb') as file:
    file.write(html_content.encode())
 


with open('top-recomendations updated.txt', 'rb') as file:
    html_content = file.read().decode(errors='replace')

# Replace placeholders with replacements
for i in range(len(placeholders)):
    if(placeholders[i] in html_content ):
        html_content = html_content.replace(placeholders[i], replacements[i])


# Write the new HTML to a file.
with open('article.html', 'wb') as file:
    file.write(html_content.encode())
