# LLM Quantization Lab 🧪

**Compare FP32 vs FP16 vs INT8 vs INT4 quantization in real-world scenarios**
This project demonstrates how quantization reduces memory footprint and improves inference speed for Large Language Models, with practical benchmarks.

## 🎯 What You'll Learn

- Memory savings across different precision levels (FP32 → INT4)
- Inference speed comparisons
- Quality vs efficiency tradeoffs
- How to run 70B models on consumer hardware

## 📊 Key Findings

| Precision | Model Size | Memory Required | Speed | Quality |
|-----------|-----------|-----------------|-------|---------|
| FP32      | 280 GB    | 280 GB VRAM     | 1x    | 100%    |
| FP16      | 140 GB    | 140 GB VRAM     | 2x    | 99.5%   |
| INT8      | 70 GB     | 70 GB VRAM      | 3x    | 95%     |
| INT4      | 35 GB     | 16-24 GB RAM    | 4x    | 90%     |

## 🚀 Quick Start

### Prerequisites

```bash
python >= 3.9
pip install -r requirements.txt