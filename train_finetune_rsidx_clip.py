from lightning import Trainer  # noqa: F401
from lightning.pytorch.cli import LightningCLI

from datasets import CaptioningDataModule
from models import RSDiXClip
from utils import enable_matmul_precision


def cli_main():
    LightningCLI(model_class=RSDiXClip, datamodule_class=CaptioningDataModule,
                 parser_kwargs={"fit": {"default_config_files": ["clip_config.yaml"]}},
                 save_config_kwargs={"overwrite": True, "config_filename": "clip_config_CLI.yaml"})


if __name__ == "__main__":
    enable_matmul_precision()
    cli_main()
