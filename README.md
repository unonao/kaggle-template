# Kaggle テンプレート

## 特徴
- Docker によるポータブルでKaggleと同一の環境
- Hydra による実験管理
    - パスなど各スクリプトに共通する設定を yamls/config.yaml で管理
    - 実験用スクリプトファイルの変更を major バージョンとしてフォルダごとに管理
    - スクリプトごとの細かいパラメータ管理をminor バージョンとして同一フォルダ内に管理することでフォルダ移動の手間をなくす

## Structure
```text
.
├── .jupyter-settings: jupyter-lab の設定ファイル。compose.yamlでJUPYTERLAB_SETTINGS_DIRを指定している
├── Dockerfile
├── Dockerfile.cpu
├── LICENSE
├── README.md
├── compose.cpu.yaml
├── compose.yaml
├── exp
├── input
├── notebook
├── output
├── utils
└── yamls
```

## Docker による環境構築

```sh
docker compose biuld

# bash に入る場合
docker compose run --rm kaggle bash 

# jupyter lab を起動する場合
docker compose up 
```

## スクリプトの実行方法

```sh
python exp/check/run.py exp=check/001
python exp/check/run.py exp=check/base
```

### Hydra による Config 管理
- 各スクリプトに共通する基本的な設定は yamls/config.yaml 内にある
- 各スクリプトによって変わる設定は、実行スクリプトの近くに配置するために `exp/{major_exp_name}` フォルダの中に `{minor_exp_name}.yaml` として配置する
    - 実行時に `exp={major_exp_name}/{minor_exp_name}.yaml` で上書きして