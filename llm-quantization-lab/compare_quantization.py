#!/usr/bin/env python3
"""
Secure Quantization Benchmark (macOS/Apple Silicon optimized)
Automatically masks tokens & paths in all outputs.
"""

import sys
import torch
import psutil
import time
import json
from pathlib import Path
from config import (
    DEFAULT_MODEL, OUTPUT_DIR, MAX_NEW_TOKENS,
    get_device, sanitize_log
)

def get_device():
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")

def benchmark_precision(model_name: str, precision: str = "fp16"):
    device = get_device()
    print(f"\n Testing {precision.upper()} on {sanitize_log(device)}")
    
    initial_mem = psutil.Process().memory_info().rss / 1024**3
    
    dtype_map = {"fp32": torch.float32, "fp16": torch.float16}
    
    try:
        from transformers import AutoModelForCausalLM, AutoTokenizer
        
        start = time.time()
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            dtype=dtype_map[precision],
            device_map="auto" if device.type != "cpu" else None,
            low_cpu_mem_usage=True,
            resume_download=True
        )
        model.to(device)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        load_time = time.time() - start
        
        inputs = tokenizer("The future of AI is", return_tensors="pt").to(device)
        inf_start = time.time()
        with torch.no_grad():
            out = model.generate(**inputs, max_new_tokens=MAX_NEW_TOKENS, do_sample=False)
        inf_time = time.time() - inf_start
        
        current_mem = psutil.Process().memory_info().rss / 1024**3
        model_size = sum(p.numel() * p.element_size() for p in model.parameters()) / 1024**3
        
        result = {
            "precision": precision,
            "model_size_gb": round(model_size, 2),
            "memory_delta_gb": round(current_mem - initial_mem, 2),
            "load_time_s": round(load_time, 2),
            "tokens_per_sec": round(MAX_NEW_TOKENS / inf_time, 2),
            "device": str(device)
        }
        
        print(f"✅ Size: {result['model_size_gb']}GB | RAM: +{result['memory_delta_gb']}GB | Speed: {result['tokens_per_sec']} tok/s")
        return result
        
    except Exception as e:
        print(f" Failed {precision}: {sanitize_log(e)}")
        return None

if __name__ == "__main__":
    print(f"🍎 Running on: {sanitize_log(get_device())} | Python {sys.version.split()[0]}")
    
    OUTPUT_DIR.mkdir(exist_ok=True)
    results = {}
    
    for p in ["fp32", "fp16"]:
        res = benchmark_precision(DEFAULT_MODEL, precision=p)
        if res:
            results[p] = res
    
    output_file = OUTPUT_DIR / "mac_benchmark.json"
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"\n💾 Saved to {sanitize_log(output_file)}")
    print("📊 Ready for GitHub/LinkedIn!")