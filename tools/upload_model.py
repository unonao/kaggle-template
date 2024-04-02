import json
import shutil
from pathlib import Path
from typing import Any

import click
from kaggle.api.kaggle_api_extended import KaggleApi


def copy_files_with_exts(source_dir: Path, dest_dir: Path, exts: list):
    """
    source_dir: 探索開始ディレクトリ
    dest_dir: コピー先のディレクトリ
    exts: 対象の拡張子のリスト (例: ['.txt', '.jpg'])
    """

    # source_dirの中での各拡張子と一致するファイルのパスを探索
    for ext in exts:
        for source_path in source_dir.rglob(f"*{ext}"):
            # dest_dir内での相対パスを計算
            relative_path = source_path.relative_to(source_dir)
            dest_path = dest_dir / relative_path

            # 必要に応じてコピー先ディレクトリを作成
            dest_path.parent.mkdir(parents=True, exist_ok=True)

            # ファイルをコピー
            shutil.copy2(source_path, dest_path)
            print(f"Copied {source_path} to {dest_path}")


@click.command()
@click.option("--title", "-t", default="kami-model")
@click.option("--dir", "-d", type=Path, default="./output/experiments")
@click.option(
    "--extentions",
    "-e",
    type=list[str],
    default=["best_model.pt", ".hydra/*.yaml"],
)
@click.option("--user_name", "-u", default="kami634")
@click.option("--new", "-n", is_flag=True)
def main(
    title: str,
    dir: Path,
    extentions: list[str] = [".pth", ".yaml"],
    user_name: str = "kami634",
    new: bool = False,
):
    """extentionを指定して、dir以下のファイルをzipに圧縮し、kaggleにアップロードする。

    Args:
        title (str): kaggleにアップロードするときのタイトル
        dir (Path): アップロードするファイルがあるディレクトリ
        extentions (list[str], optional): アップロードするファイルの拡張子.
        user_name (str, optional): kaggleのユーザー名.
        new (bool, optional): 新規データセットとしてアップロードするかどうか.
    """
    tmp_dir = Path("./tmp")
    tmp_dir.mkdir(parents=True, exist_ok=True)

    # 拡張子が.pthのファイルをコピー
    copy_files_with_exts(dir, tmp_dir, extentions)

    # dataset-metadata.jsonを作成
    dataset_metadata: dict[str, Any] = {}
    dataset_metadata["id"] = f"{user_name}/{title}"
    dataset_metadata["licenses"] = [{"name": "CC0-1.0"}]
    dataset_metadata["title"] = title
    with open(tmp_dir / "dataset-metadata.json", "w") as f:
        json.dump(dataset_metadata, f, indent=4)

    # api認証
    api = KaggleApi()
    api.authenticate()

    if new:
        api.dataset_create_new(
            folder=tmp_dir,
            dir_mode="tar",
            convert_to_csv=False,
            public=False,
        )
    else:
        api.dataset_create_version(
            folder=tmp_dir,
            version_notes="",
            dir_mode="tar",
            convert_to_csv=False,
        )

    # delete tmp dir
    shutil.rmtree(tmp_dir)


if __name__ == "__main__":
    main()
