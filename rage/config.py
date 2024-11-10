# General config.
delete_files = True
use_gpu = False

# RAG config
llm_name = "owl/t-lite:latest"
chunk_size = 1000
chunk_overlap = 200
temperature = 0.0

# Text-to-Speech config
is_slow = False  # For machine speaker
audio_speed = 1.0  # For neural speaker

# Video-To-Text config
stt_model = "openai/whisper-large-v3"
