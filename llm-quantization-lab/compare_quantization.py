#!/usr/bin/env python3
"""
macOS-Optimized Quantization Benchmark
Compares FP32 vs FP16 on CPU/MPS (Apple Silicon)
"""

import sys
import torch
import psutil
import time
from pathlib import Path
import json

def get_device():
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")

def benchmark_precision(model_name="facebook/opt-1.3b", precision="fp16"):
    device = get_device()
    print(f"\n Testing {precision.upper()} on {device}")
    
    initial_mem = psutil.Process().memory_info().rss / 1024**3
    
    dtype_map = {
        "fp32": torch.float32,
        "fp16": torch.float16,
    }
    
    try:
        from transformers import AutoModelForCausalLM, AutoTokenizer
        
        start = time.time()
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=dtype_map[precision],
            device_map="auto" if device.type != "cpu" else None,
            low_cpu_mem_usage=True
        )
        model.to(device)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        load_time = time.time() - start
        
        # Inference benchmark
        inputs = tokenizer("The future of AI is", return_tensors="pt").to(device)
        inf_start = time.time()
        with torch.no_grad():
            out = model.generate(**inputs, max_new_tokens=50, do_sample=False)
        inf_time = time.time() - inf_start
        
        current_mem = psutil.Process().memory_info().rss / 1024**3
        model_size = sum(p.numel() * p.element_size() for p in model.parameters()) / 1024**3
        
        result = {
            "precision": precision,
            "model_size_gb": round(model_size, 2),
            "memory_delta_gb": round(current_mem - initial_mem, 2),
            "load_time_s": round(load_time, 2),
            "tokens_per_sec": round(50 / inf_time, 2),
            "device": str(device)
        }
        
        print(f"✅ Size: {result['model_size_gb']}GB | RAM: +{result['memory_delta_gb']}GB | Speed: {result['tokens_per_sec']} tok/s")
        return result
        
    except Exception as e:
        print(f"❌ Failed {precision}: {e}")
        return None

if __name__ == "__main__":
    print(f"🍎 Running on: {get_device()} | Python {sys.version.split()[0]}")
    
    results = {}
    for p in ["fp32", "fp16"]:
        res = benchmark_precision(precision=p)
        if res:
            results[p] = res
    
    # Save
    Path("results").mkdir(exist_ok=True)
    with open("results/mac_benchmark.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print("\n Saved to results/mac_benchmark.json")
    print("📊 Paste this into the notebook or LinkedIn post!")