from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SEQUENCE_1 = "ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAA"
SEQUENCE_2= "CGAACTTTAAAATCTGTGTGGCTGTCACTCGGCTGCATGCTTAGTGCACTCACGCAGTATAATTAATAAC"
completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "user", "content": "Given two gene sequences, please output your best guess of what the 3rd sequence would be based on these rules. 1) The third sequence must remain at least 90% the same as the second sequence. 2) The third sequence must capture the same patterns of differences between the first and second sequences. Here's the first sequence: " + SEQUENCE_1 + ". And here's the second sequence: " + SEQUENCE_2}
  ]
)

print(completion.choices[0].message.content)