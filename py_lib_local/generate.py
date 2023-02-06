import os

def generate_html(html, file_path):
    # Check if the directory already exists
    if not os.path.exists(f"html/{file_path}"):
        # If not, create the directory
        os.makedirs(f"html/{file_path}")

    # Create HTML file
    with open(f"html{file_path}/index.html", "w") as f:
        f.write(html)

def main():
    pass

if __name__ == '__main__':
   main()
