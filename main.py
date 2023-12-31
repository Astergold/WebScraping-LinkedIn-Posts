import csv
from bs4 import BeautifulSoup
# from time import sleep
# Read HTML content from file
with open('index.html', 'r', encoding='utf-8') as file:
    html_code = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html_code, 'html.parser')

# Find all posts in the HTML document
all_posts = soup.find_all('div', class_='feed-shared-update-v2--wrapped')

# Open a CSV file for writing
csv_file_path = 'output.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)

    # Write header row
    csv_writer.writerow(['Post Number', 'Name', 'Profile Link', 'Description', 'Post Content'])

    # Iterate over each post
    for i, post in enumerate(all_posts, start=1):
        # Find the relevant HTML blocks within each post
        profile_block = post.find('div', class_='update-components-actor__meta')

        # Extracting name
        name_element = profile_block.find('span', class_='update-components-actor__name')
        name = name_element.get_text(strip=True) if name_element else ''

        # Extracting profile link
        profile_link_element = profile_block.find('a', class_='update-components-actor__meta-link')
        profile_link = profile_link_element['href'] if profile_link_element else ''

        # Extracting description
        description_element = profile_block.find('span', class_='update-components-actor__description')
        description = description_element.get_text(strip=True) if description_element else ''

        # Extracting post content
        post_content_element = post.find('div', class_='update-components-text')
        post_content = post_content_element.get_text(strip=True) if post_content_element else ''



        # Printing the extracted information for each post in the terminal
        print(f"\nPost Number: {i}")
        print(f"Name: {name}")
        print(f"Profile Link: {profile_link}")
        print(f"Description: {description}")
        print(f"Post Content: {post_content}")


        # Write the information to the CSV file
        csv_writer.writerow([i, name, profile_link, description, post_content])
        # sleep(1)

print(f"\nCSV file has been created: {csv_file_path}")
