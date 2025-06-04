# アメリカンプットオプションの価格評価
## 概要
Longstaff-Schwartz Method(LSM)を用いてアメリカンプットオプションの価格を計算するPythonのプログラムです。
Black-ScholesのSDEで原資産価格のパスを発生させ、満期から順にholding valueとexercise valueを比較します。その際、holding valueの推定には多項式回帰を利用します。

## 主な機能
* LSMを用いたアメリカンプットの価格計算
* antithetic variatesによる分散低減法の実装
## ファイル構成
```
.
├── main.py                # LSMアルゴリズムを実行し、オプション価格を計算するメインスクリプト
├── make_path.py           # モンテカルロ法による株価パスを生成するモジュール
├── regression_module.py   # 多項式回帰計算を行うモジュール
├── config.json            # シミュレーションパラメータを設定するファイル
└── README.md              # 本ファイル (プロジェクト概要説明)
```

* **`main.py`**:
    * `config.json`からパラメータを読み込みます。
    * `make_path.py`を利用し、原資産価格のパスを生成します。
    * `regression_module.py`を利用し、インザマネーのパスに対しholding valueを推定します。
    * LSMに基づき、早期行使判断をしながらオプション価格を計算し、結果を出力します。
    * 使用したパラメータと、計算に要した時間を出力します。

* **`make_path.py`**:
    * 幾何ブラウン運動を仮定し、指定されたパラメータに基づいてパスを生成します。
    * 変数`antithetic`により、antithetic variates法を利用するか選択できます。

* **`regression_module.py`**
    *`polynomial_regression`関数: 与えられた点と次数を用いて最小二乗法を実行し、回帰係数を計算します。基底多項式はx^nを採用しています。
    *`polynomial_regression_value`関数: 算出された回帰係数と説明変数から、多項式モデルによる予測値を計算します。

* **`config.json`**:
    *必要なパラメータを定義します。

## パラメータ
シミュレーションのパラメータは`config.json`で設定する。
```json
{
"LSM_parameters": {
            "S": 36,
            "K": 40,
            "T": 1,
            "r": 0.06,
            "sig": 0.2,
            "N": 100,
            "M": 500000,
            "degree": 3,
            "seed": null,
            "antithetic": true
}
```
各パラメータの詳細:
* `S`: 初期株価
* `K`: 行使価格
* `T`: 満期までの期間 (年単位)
* `r`: リスクフリーレート (年率)
* `sig`: ボラティリティ (年率)
* `N`: 満期までの時間ステップ数
* `M`: モンテカルロシミュレーションのパス数
* `degree`: 回帰に使用する多項式の次数
* `seed`: 乱数生成のシード値 (`null` の場合はシードを指定しません)
* `antithetic`: 対照変量法を使用するか否か (`true` または `false`)

## 実行方法
1. **必要なライブラリ**
* `Numpy`

2. **パラメータの設定**:
   パラメータは`config.json`ファイルで設定します。必要に応じてconfig.jsonを編集してください。

3. **実行方法**
       以下の方法で`main.py`を実行してください。
   ```
   python main.py
   ```

