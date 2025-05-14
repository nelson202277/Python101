import csv
import openai
import os
import time

# Set your OpenAI API key here
openai.api_key = os.getenv("OPENAI_API_KEY")  # or replace with your key as a string
client = openai.OpenAI()
input_file = "test/example.csv"
output_file = "test/example_output.csv"


def get_capital_test(city):
    return city[::-1]


def get_capital(city):
    prompt = f"What is the capital of {city}?"
    try:
        response = client.chat.chatcompletions.create(
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
            city = row["City"]
            answer = get_capital(city)
            print(f"City: {city} -> {answer}")
            results.append({"City": city, "Capital_Answer": answer})
            time.sleep(1)  # avoid rate limiting

    with open(output_file, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["City", "Capital Answer"])
        writer.writeheader()
        writer.writerows(results)


if __name__ == "__main__":
    main()
