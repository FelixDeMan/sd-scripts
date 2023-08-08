
import os 
from huggingface_hub import upload_folder, create_repo

toml_paths = [
    "train-results/constant-scheduler/test_config.toml",
    "train-results/constant-warmup-scheduler/test_config.toml",
    "train-results/cosine-scheduler/test_config.toml",
    ]



for toml_path in toml_paths:
    train_command = "accelerate launch --num_cpu_threads_per_process 1 sdxl_train_network.py --config_file={}".format(toml_path)
    
    print("TRAINING: Starting with the following command:")
    print(train_command)
    os.system(train_command)

    print("HUGGINGFACE: Creating repo...")
    repo_id = create_repo(
        repo_id=toml_path.split("/")[1], exist_ok=True, token="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"
    ).repo_id

    print("HUGGINGFACE: Pushing model to repo...")
    upload_folder(
        repo_id="fmattera/" + toml_path.split("/")[1],
        folder_path=toml_path.rsplit("/",1)[0],
        commit_message="End of training",
        ignore_patterns=["step_*", "epoch_*"],
        token="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"
)






