from dataclasses import dataclass


@dataclass
class EnvConfig:
    input_dir: str = "/kaggle/input"
    output_dir: str = "/kaggle/working/output"
    exp_output_dir: str = "/kaggle/working/output/experiments"
