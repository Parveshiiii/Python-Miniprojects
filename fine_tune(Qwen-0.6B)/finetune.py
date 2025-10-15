"""
%%capture
import os, importlib.util
!pip install --upgrade -qqq uv
if importlib.util.find_spec("torch") is None or "COLAB_" in "".join(os.environ.keys()):    
    try: import numpy; get_numpy = f"numpy=={numpy.__version__}"
    except: get_numpy = "numpy"
    !uv pip install -qqq \
        "torch>=2.8.0" "triton>=3.4.0" {get_numpy} torchvision bitsandbytes "transformers==4.56.2" \
        "unsloth_zoo[base] @ git+https://github.com/unslothai/unsloth-zoo" \
        "unsloth[base] @ git+https://github.com/unslothai/unsloth" \
        git+https://github.com/triton-lang/triton.git@05b2c186c1b6c9a08375389d5efe9cb4c401c075#subdirectory=python/triton_kernels
elif importlib.util.find_spec("unsloth") is None:
    !uv pip install -qqq unsloth
!uv pip install --upgrade --no-deps transformers==4.56.2 tokenizers trl==0.22.2
"""

from unsloth import FastLanguageModel
import torch
from datasets import load_dataset
from datasets import Dataset
import pandas as pd
import numpy as np
from trl import SFTTrainer, SFTConfig

max_seq_length = 2048 # Can increase for longer reasoning traces
lora_rank = 32 # Larger rank = smarter, but slower
dtype = torch.float16

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/Qwen3-0.6B",
    max_seq_length = max_seq_length,
    fast_inference = True,
    full_finetuning = True,
    dtype = dtype,
)

# Load your local JSONL file
dataset = load_dataset("json", data_files="dailydialog_sanitized.jsonl")

# Select the split (default is "train" when you pass one file)
dataset = dataset["train"]

# Now convert to pandas and pick the columns you want
dataset = dataset.to_pandas()[["input", "output"]]

def format_dataset(x):
    expected_answer = x["output"]
    problem = x["input"]
    return [
        {"role" : "user",      "content" : problem},
        {"role" : "assistant", "content" : expected_answer},
    ]

dataset["Messages"] = dataset.apply(format_dataset, axis = 1)

dataset["text"] = tokenizer.apply_chat_template(dataset["Messages"].values.tolist(), tokenize = False)
dataset = Dataset.from_pandas(dataset)
dataset

"""Let's now pre fine-tune the model so it follows our custom GRPO formatting!"""
trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset,
    args = SFTConfig(
        dataset_text_field = "Messages",
        per_device_train_batch_size = 1,
        gradient_accumulation_steps = 1, # Use GA to mimic batch size!
        warmup_steps = 5,
        num_train_epochs = 2, # Set this for 1 full training run.
        learning_rate = 2e-4, # Reduce to 2e-5 for long training runs
        logging_steps = 5,
        optim = "adamw_8bit",
        weight_decay = 0.01,
        lr_scheduler_type = "linear",
        seed = 3407,
        report_to = "none", # Use this for WandB etc
    ),
)

trainer.train()
