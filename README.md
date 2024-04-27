# Kaggle テンプレート

## 特徴
- Docker によるポータブルなKaggleと同一の環境
- Hydra による実験管理
- 実験用スクリプトファイルを major バージョンごとにフォルダごとに管理
- 実験用スクリプトと設定を同一フォルダで局所的に管理して把握しやすくする

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
└── yamls: データのパスなど各スクリプトに共通する設定を管理
```

## Docker による環境構築

```sh
docker compose build

# bash に入る場合
docker compose run --rm kaggle bash 

# jupyter lab を起動する場合
docker compose up 
```

## スクリプトの実行方法

```sh
python experiments/sample/run.py exp=001
python experiments/sample/run.py exp=base
```

### Hydra による Config 管理
- 各スクリプトに共通する基本的な設定は yamls/config.yaml 内にある
- 各スクリプトによって変わる設定は、実行スクリプトのあるフォルダ(`{major_exp_name}`)の中に `exp/{minor_exp_name}.yaml` として配置することで管理。
    - 実行時に `exp={minor_exp_name}` で上書きする
    - `{major_exp_name}` と `{minor_exp_name}` の組み合わせで実験が再現できるようにする
