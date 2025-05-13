import os
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path

import hydra
import wandb
from hydra.core.config_store import ConfigStore
from hydra.core.hydra_config import HydraConfig
from omegaconf import OmegaConf

from utils.env import EnvConfig
from utils.logger import get_logger
from utils.timing import trace

LOGGER = None
WANDB_PROJECT_NAME = "kaggle-template"


####################
# Config 設定
####################
@dataclass
class ExpConfig:
    debug: bool = False
    seed: int = 7
    learning_rate: float = 0.001
    batch_size: int = 32
    folds: list = field(default_factory=lambda: [0, 1, 2, 3, 4])


@dataclass
class Config:
    env: EnvConfig = field(default_factory=EnvConfig)
    exp: ExpConfig = field(default_factory=ExpConfig)


# hydra用にdefaultを設定
cs = ConfigStore.instance()
cs.store(name="default", group="env", node=EnvConfig)
cs.store(name="default", group="exp", node=ExpConfig)


####################
# 実験用コード
####################
def log_config(cfg: Config) -> None:
    LOGGER.info("Config: %s", cfg)


@hydra.main(version_base=None, config_path=".", config_name="config")
def main(
    cfg: Config,
) -> None:  # Duck typing: cfgは実際にはDictConfigだが、Configクラスのように扱える
    print(cfg)

    exp_name = f"{Path(sys.argv[0]).parent.name}/{HydraConfig.get().runtime.choices.exp}"  # e.g. 000_sample/default
    output_dir = Path(cfg.env.exp_output_dir) / exp_name
    os.makedirs(output_dir, exist_ok=True)
    print(f"output_dir: {output_dir}")

    with trace("sleep"):
        time.sleep(1.1)

    global LOGGER
    LOGGER = get_logger(__name__, output_dir)
    LOGGER.info("Start")

    log_config(cfg)

    wandb.init(
        project=WANDB_PROJECT_NAME,
        name=exp_name,
        notes=", ".join(HydraConfig.get().overrides.task),  # オーバーライドの内容
        config=OmegaConf.to_container(cfg.exp, resolve=True),
        mode="disabled" if cfg.exp.debug else "online",
    )


if __name__ == "__main__":
    main()
