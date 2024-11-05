import os

# General config.
delete_files = True
use_gpu = os.environ.get("USE_GPU") == "1"

# RAG config
llm_name = "owl/t-lite:latest"
chunk_size = 1000
chunk_overlap = 200
temperature = 0.0

# Text-to-Speech config
is_slow = False

# Video-To-Text config
stt_model = "openai/whisper-large-v3"
