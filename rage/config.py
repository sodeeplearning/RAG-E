from torch.cuda import is_available
from torch import float16 as torch_float_dtype

# General config.
delete_files = True
use_cuda = True
use_gpu = use_cuda * is_available()
num_gpu = 1
torch_dtype = torch_float_dtype

# RAG config
llm_name = "owl/t-lite:latest"
chunk_size = 400
chunk_overlap = 100
temperature = 0.1

# Text-to-Speech config
is_slow = False  # For machine speaker
audio_speed = 1.0  # For neural speaker

# Video-To-Text config
stt_model = "openai/whisper-large-v3"
