Here's a complete Python script that reads a list of cities from a CSV file (with a column named "City"), queries the OpenAI API for the capital of each city, and writes the answers to a new CSV file:

🔧 Prerequisites:

* Install the OpenAI Python client: pip install openai
* Set your OpenAI API key (via environment variable or directly in the script)

📜 Script:

```python
import csv
import openai
import os
import time

# Set your OpenAI API key here
openai.api_key = os.getenv("OPENAI_API_KEY")  # or replace with your key as a string

input_file = "cities.csv"
output_file = "city_capitals.csv"

def get_capital(city):
    prompt = f"What is the capital of {city}?"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )
        answer = response['choices'][0]['message']['content'].strip()
        return answer
    except Exception as e:
        return f"Error: {e}"

def main():
    results = []
    with open(input_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            city = row["City"]
            answer = get_capital(city)
            print(f"City: {city} -> {answer}")
            results.append({"City": city, "Capital Answer": answer})
            time.sleep(1)  # avoid rate limiting

    with open(output_file, "w", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["City", "Capital Answer"])
        writer.writeheader()
        writer.writerows(results)

if __name__ == "__main__":
    main()
```

📝 Notes:

* The script adds a 1-second delay between requests to be polite to the API and avoid rate limits.
* Replace the model name if you want to use a different version (e.g., gpt-3.5-turbo).

Would you like this to be parallelized or to use local knowledge instead of the OpenAI API?
