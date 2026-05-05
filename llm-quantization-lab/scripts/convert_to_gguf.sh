#!/bin/bash
# Convert HuggingFace models to GGUF format for INT4 quantization

echo "🔄 Converting model to GGUF format..."

MODEL_NAME=${1:-"meta-llama/Llama-2-7b-hf"}
OUTPUT_DIR=${2:-"./models"}

echo "Model: $MODEL_NAME"
echo "Output: $OUTPUT_DIR"

# Clone llama.cpp if not exists
if [ ! -d "llama.cpp" ]; then
    echo "📥 Cloning llama.cpp..."
    git clone https://github.com/ggerganov/llama.cpp.git
    cd llama.cpp
    make
    cd ..
fi

# Download model
echo "⬇️  Downloading model from HuggingFace..."
python -m pip install huggingface_hub
huggingface-cli download $MODEL_NAME --local-dir $OUTPUT_DIR/model

# Convert to GGUF
echo "🔧 Converting to GGUF (FP16 first)..."
python llama.cpp/convert.py $OUTPUT_DIR/model --outfile $OUTPUT_DIR/model_fp16.gguf --outtype f16

# Quantize to INT4
echo "📦 Quantizing to INT4..."
./llama.cpp/quantize $OUTPUT_DIR/model_fp16.gguf $OUTPUT_DIR/model_q4_0.gguf q4_0

echo "✅ Conversion complete!"
echo "📁 Output: $OUTPUT_DIR/model_q4_0.gguf"
echo ""
echo "💡 Run with:"
echo "   ./llama.cpp/main -m $OUTPUT_DIR/model_q4_0.gguf -p \"Hello, AI!\" -n 128"