import os
import sys
from pathlib import Path
from omegaconf import DictConfig, OmegaConf
from hydra.core.hydra_config import HydraConfig
import hydra
import time
sys.path.append(os.pardir)

import utils

@hydra.main(version_base=None, config_path="../yamls", config_name="config")
def my_app(cfg : DictConfig) -> None:
    runtime_choices = HydraConfig.get().runtime.choices
    exp_name = f"{Path(sys.argv[0]).stem}/{runtime_choices.check}"

    output_path = Path(f"./output/{exp_name}")
    print(output_path)
    #os.makedirs(output_path, exist_ok=True)

    with utils.timer("print"):
        time.sleep(1.1)
    print(OmegaConf.to_yaml(cfg))

if __name__ == "__main__":
    my_app()