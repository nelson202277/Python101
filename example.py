import csv
import openai
import os
import time

# Set your OpenAI API key here
# openai.api_key = os.getenv("OPENAI_API_KEY")  # or replace with your key as a string
# client = openai.OpenAI()
client = openai.OpenAI(base_url="http://127.0.0.1:8000/v1", api_key="test")
input_file = "test/example.csv"
output_file = "test/example_output.csv"


def get_capital(nation):
    prompt = f"What is the capital of {nation}?"
    try:
        response = client.chat.completions.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
        )
        answer = response.choices[0].message.content.strip()
        return answer
    except Exception as e:
        return f"Error: {e}"


def main():
    results = []
    with open(input_file, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            nation = row["City"]
            answer = get_capital(nation)
            print(f"Nation: {nation} -> {answer}")
            results.append({"Nation": nation, "Capital_Answer": answer})
            time.sleep(1)  # avoid rate limiting

    with open(output_file, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["City", "Capital_Answer"])
        writer.writeheader()
        writer.writerows(results)


main()
