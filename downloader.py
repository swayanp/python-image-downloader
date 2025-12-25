import requests
from pathlib import Path

# 1. SETUP
folder = Path("Automated_Downloads")
folder.mkdir(exist_ok=True)

# 2. OPEN AND ENUMERATE
# We open the file and pass the file object 'f' directly into enumerate
with open("links.txt", "r") as f:
    
    # enumerate starts at 0 by default, but we can tell it to start at 1!
    for count, line in enumerate(f, start=1):
        
        clean_url = line.strip()
        
        if clean_url:
            print(f"Processing line {count}...")
            
            try:
                response = requests.get(clean_url)
                
                if response.status_code == 200:
                    # Use the count provided by enumerate for the filename
                    file_name = f"image_{count}.png"
                    
                    with open(folder / file_name, "wb") as img_file:
                        img_file.write(response.content)
                        
                    print(f"Successfully saved {file_name}")
                else:
                    print(f"Line {count}: Website returned error {response.status_code}")
                    
            except Exception as e:
                print(f"Line {count}: Logic error - {e}")

print("--- Automation Complete ---")