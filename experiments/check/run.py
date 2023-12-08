import time
from pathlib import Path

import hydra
from hydra.core.hydra_config import HydraConfig
from omegaconf import DictConfig, OmegaConf

import utils


@hydra.main(version_base=None, config_path=".", config_name="config")
def my_app(cfg: DictConfig) -> None:
    runtime_choices = HydraConfig.get().runtime.choices
    exp_name = f"{runtime_choices.exp}"

    print(f"exp_name: {exp_name}")
    ouput_path = Path(cfg.dir.output_dir) / exp_name
    print(f"ouput_path: {ouput_path}")
    # os.makedirs(output_path, exist_ok=True)

    with utils.timer("print"):
        time.sleep(1.1)
    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    my_app()
