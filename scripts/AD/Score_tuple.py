import json
import re

def update_tuple(record):
    """Update the tuple field based on the content field."""
    # Extract the score using regex
    match = re.search(r"Score: (\d+) out of 10.", record["content"])
    if match:
        score = int(match.group(1))
        record["tuple"] = [score, 10]
    return record

def process_file(input_path, output_path):
    """Process the file, updating the tuple for each record."""
    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    updated_records = [update_tuple(json.loads(line)) for line in lines]
    
    # Saving the updated records to the output file
    with open(output_path, "w", encoding="utf-8") as f:
        for record in updated_records:
            f.write(json.dumps(record) + "\n")

process_file("/path/to/AD/Review/124_data_review.json","/path/to/AD/Review/tuple/124_data_review_updated.json")
# Example usage:
# process_file("/path/to/original_file.jsonl", "/path/to/updated_file.jsonl")
