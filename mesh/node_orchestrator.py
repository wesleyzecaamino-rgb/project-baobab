import requests
import json
import time

# List of active edge nodes in your distributed mesh network
ACTIVE_NODES = [
    {"name": "Node-Alpha (Port 8080)", "url": "http://localhost:8080/v1/chat/completions"},
    {"name": "Node-Beta  (Port 8081)", "url": "http://localhost:8081/v1/chat/completions"}
]

def query_node(node, prompt):
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": "Phi-3-mini",
        "messages": [
            {"role": "system", "content": "You are a decentralized edge AI node."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 30
    }
    
    print(f"[*] Routing request to -> {node['name']}...")
    start_time = time.time()
    
    try:
        response = requests.post(node['url'], headers=headers, data=json.dumps(payload), timeout=300)
        elapsed_time = round(time.time() - start_time, 2)
        
        if response.status_code == 200:
            result = response.json()
            content = result['choices'][0]['message']['content'].strip()
            return content, elapsed_time
        else:
            return f"Error: {response.status_code}", elapsed_time
    except requests.exceptions.ConnectionError:
        return f"Error: {node['name']} unreachable.", 0

def run_distributed_mesh():
    prompts = [
        "Explain how decentralized computing saves power.",
        "What is the environmental impact of traditional data centers?"
    ]
    
    print("==================================================")
    print(" PROJECT BAOBAB: DISTRIBUTED MESH FABRIC ROUTER ")
    print("==================================================\n")
    
    for i, prompt in enumerate(prompts):
        # Round-robin distribution across available micro-nodes
        assigned_node = ACTIVE_NODES[i % len(ACTIVE_NODES)]
        
        print(f"Task #{i+1}: '{prompt}'")
        output, latency = query_node(assigned_node, prompt)
        
        print(f"Response: {output}")
        print(f"Latency: {latency}s | Zero Data Center Power Used")
        print("-" * 50 + "\n")

if __name__ == "__main__":
    run_distributed_mesh()
