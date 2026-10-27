import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor

ACTIVE_NODES = [
    {"name": "Node-Alpha (Port 8080)", "url": "http://localhost:8080/v1/chat/completions"},
    {"name": "Node-Beta  (Port 8081)", "url": "http://localhost:8081/v1/chat/completions"}
]

def query_node(node, prompt):
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": "Phi-3-mini",
        "messages": [
            {"role": "system", "content": "You are a concise edge AI processing node."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5,
        "max_tokens": 25
    }

    start_time = time.time()
    try:
        response = requests.post(node['url'], headers=headers, data=json.dumps(payload), timeout=300)
        elapsed = round(time.time() - start_time, 2)
        if response.status_code == 200:
            content = response.json()['choices'][0]['message']['content'].strip()
            return node['name'], content, elapsed
        return node['name'], f"Error {response.status_code}", elapsed
    except Exception as e:
        return node['name'], f"Failed: {str(e)}", 0

def execute_parallel_mesh(sub_prompts):
    print("==================================================")
    print(" PROJECT BAOBAB: PARALLEL MESH PROCESSOR ")
    print("==================================================\n")

    results = []
    # Dispatch tasks concurrently across active nodes
    with ThreadPoolExecutor(max_workers=len(ACTIVE_NODES)) as executor:
        futures = [
            executor.submit(query_node, ACTIVE_NODES[i % len(ACTIVE_NODES)], prompt)
            for i, prompt in enumerate(sub_prompts)
        ]
        for future in futures:
            results.append(future.result())

    for node_name, response, latency in results:
        print(f"[{node_name}] Latency: {latency}s")
        print(f"Sub-output: {response}\n" + "-"*40)

if __name__ == "__main__":
    # Splitting a complex query into multi-node parallel sub-tasks
    sub_tasks = [
        "State one issue with big tech data center energy use.",
        "State one benefit of decentralized local edge computing."
    ]

    print("Splitting primary prompt into parallel edge tasks...\n")
    execute_parallel_mesh(sub_tasks)
