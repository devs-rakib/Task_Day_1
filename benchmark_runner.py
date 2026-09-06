import json
import os
import time

from dotenv import load_dotenv
from openai import OpenAI

from prompts import ZERO_SHOT_PROMPT, FEW_SHOT_PROMPT


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MODEL = "gpt-4o-mini"


def load_dataset():
    with open("test_clauses.json", "r", encoding="utf-8") as file:
        return json.load(file)


def classify_clause(clause, prompt_template):
    prompt = prompt_template.format(clause=clause)

    start_time = time.perf_counter()

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    end_time = time.perf_counter()

    latency_ms = (end_time - start_time) * 1000

    content = response.choices[0].message.content

    usage = response.usage

    input_tokens = usage.prompt_tokens
    output_tokens = usage.completion_tokens
    total_tokens = usage.total_tokens

    return {
        "response": content,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": total_tokens,
        "latency_ms": latency_ms
    }


def run_benchmark(dataset, prompt_template, approach_name):

    results = []

    for item in dataset:

        print(
            f"{approach_name}: "
            f"Processing clause {item['id']}/{len(dataset)}"
        )

        result = classify_clause(
            item["clause"],
            prompt_template
        )

        results.append({
            "id": item["id"],
            "clause": item["clause"],
            "ground_truth": item["risk_category"],
            "model_response": result["response"],
            "input_tokens": result["input_tokens"],
            "output_tokens": result["output_tokens"],
            "total_tokens": result["total_tokens"],
            "latency_ms": result["latency_ms"]
        })

    return results


def main():

    dataset = load_dataset()

    zero_shot_results = run_benchmark(
        dataset,
        ZERO_SHOT_PROMPT,
        "Zero-Shot"
    )

    few_shot_results = run_benchmark(
        dataset,
        FEW_SHOT_PROMPT,
        "Few-Shot"
    )

    output = {
        "zero_shot": zero_shot_results,
        "few_shot": few_shot_results
    }

    with open(
        "benchmark_results.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            output,
            file,
            indent=2,
            ensure_ascii=False
        )

    print("\nBenchmark completed.")
    print("Results saved to benchmark_results.json")


if __name__ == "__main__":
    main()
