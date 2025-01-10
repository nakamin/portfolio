# ポートフォリオ

## 概要
このリポジトリでは、作成したポートフォリオをアップしていきます。

## リポジトリ構成
```
portfolio/
├── 2412_Electric_energy_consumption/   
│   ├── portfolio1_visualization.ipynb  　 # データの可視化ノートブック
│   ├── portfolio2_modeling.ipynb          # モデル構築ノートブック
│   ├── spec_sheet.md                      # プロジェクトスペックシート
│   ├── WebAPI1_input_form.jpeg            # API 入力画面
│   ├── WebAPI2_prediction_result.jpeg     # API 予測結果画面
├── 2501_Electric_energy_consumption/  
│   ├── portfolio3_neuralnetwork.ipynb  　 # モデル構築ノートブック
├── README.md                              # このリポジトリの説明ファイル
```

### 2412_Electric_energy_consumption：電力消費予測モデル化およびWeb API化
- **目的**: 東京エリアの2023年の電力消費量を予測モデルを作成すること。また、最良モデルでAPIを構築しWeb上で可視化すること。
- **利用データ**:
  - 東京エリアの1時間ごとの電力消費量データ（2016年～2023年）。出典：[東京電力パワーグリッド でんき予報](https://www.tepco.co.jp/forecast/html/download-j.html)
  - 1時間ごとの平均気温データ（同上）。出典：[国土交通省 気象庁 過去の気象データ・ダウンロード](https://www.data.jma.go.jp/risk/obsdl/index.php#)

### 2501_Electric_energy_consumption：電力消費予測モデル化（深層学習）
- **目的**：東京エリアの2023年の電力消費量を予測する深層学習モデルを作成。
  - 非深層学習モデルと比較し、深層学習を用いた場合の精度向上を目指す。
  - データセットは引き続き2016年～2023年の1時間ごとの電力消費量データを用い、特徴量としては気象データ（気温など）や休日フラグを活用。

## 今後の追加予定
このリポジトリでは、新しい分析結果を随時追加する予定です。
「CNNを用いた医用画像分類（病理組織）」を近日アップします。