# ポートフォリオ

## 概要
このリポジトリでは、作成したポートフォリオをアップしていきます。

## リポジトリ構成
```
portfolio/
├── 2412_Electric_energy_consumption/
│   ├── 2412_電力消費予測1_可視化/
│      ├── 2412_電力消費予測1_可視化.ipynb            # データの可視化ノートブック
│      ├── 2412_電力消費予測1_可視化.pdf              # データの可視化ノートブック PDF版
│
│   ├── 2412_電力消費予測2_モデル化/
│      ├── 2412_電力消費予測2_モデル化.ipynb          # モデル構築ノートブック
│      ├── 2412_電力消費予測2_モデル化.pdf            # モデル構築ノートブック PDF版
│
│   ├── 2412_電力消費予測3_API化/
│      ├── 2412_電力消費予測3_API化1_入力フォーム.jpeg # API 入力画面
│      ├── 2412_電力消費予測3_API化2_結果.jpeg        # API 予測結果画面
│   ├── 概要.pdf                                     # ポートフォリオの概要を記載
│ 
├── 2501_Electric_energy_consumption/  
│   ├── 2501_電力消費予測_モデル化（深層学習）.ipynb    # モデル構築ノートブック
│   ├── 2501_電力消費予測_モデル化（深層学習）.pdf      # モデル構築ノートブック PDF版
│   ├── 概要.pdf                                     # ポートフォリオの概要を記載
│
├── 2501_PathMNIST_classification/  
│   ├── 2501_CNNを用いた医用画像分類.ipynb             # モデル構築ノートブック
│
├── 2503_HAM10000_classification/  
│   ├── config/                                      # モデルと可視化用のconfig
│   ├── datasets/                                    # データ読み込みと変換
│   ├── models/                                      # モデル構築
│   ├── notebooks/                                   # Vitのfine tuningとattention map / GradCAM
│   ├── utils/                                       # モデル以外の設定
│   ├── main_gradcam.py                              # XceptionNetのGradCAM
│   ├── main.py                                      # 学習（Vit / Xception Net）
│
├── 2507_multiomics_vae_go/  
│   ├── 1_single_go.ipynb                            # 単一オミクス GO解析
│   ├── 2_move_preprocessing.ipynb                   # MOVE用の前処理
│   ├── 3_MOVE_clustering.ipynb                      # MOVEで得た結果を使ってクラスタリング
│   ├── 4_multi_go_afterMOVE.ipynb                   # MOVEのクラスタ分けで再度GO解析
│
├── README.md                                        # このリポジトリの説明ファイル
```
<br><br>

## 各プロジェクトの概要
### 2412_Electric_energy_consumption（電力消費予測_可視化_モデル化_API化）
- **目的**：
  1. 東京エリアの2023年の電力消費量を予測モデルを作成すること
  2. 最良モデルでAPIを構築しWeb上で可視化すること
- **利用データ**：
  - 東京エリアの1時間ごとの電力消費量データ（2016年～2023年）（出典：[東京電力パワーグリッド でんき予報](https://www.tepco.co.jp/forecast/html/download-j.html)）
  - 1時間ごとの平均気温データ（同上）（出典：[国土交通省 気象庁 過去の気象データ・ダウンロード](https://www.data.jma.go.jp/risk/obsdl/index.php#)）
- **備考**：
  - ポートフォリオ内でplotlyを用いて可視化された結果がGitHub上では出力されないためPDF版も添付

### 2501_Electric_energy_consumption（電力消費予測_モデル化（深層学習））
- **目的**：
  1. 東京エリアの2023年の電力消費量を予測する深層学習モデルを作成すること
- **利用データ**：
  - データセットは引き続き2016年～2023年の1時間ごとの電力消費量データを用い、特徴量としては気象データ（気温など）や休日フラグを活用

### 2501_PathMNIST_classification（医用画像分類（病理組織））
- **目的**：
  1. 病理組織画像をCNN（畳み込みニューラルネットワーク）により9クラスに分類
- **利用データ**：
  - MedMNISTデータセットよりPathMNIST（28×28ピクセルの結腸の病理組織画像）をダウンロード（出典：[MedMNIST公式サイト](https://medmnist.com/)）
  - データ件数：107,180件（訓練データ89,996件 / 検証データ10,004件 / テストデータ7,180件）

### 2503_HAM10000_classification（医用画像分類（ダーモスコピー画像））
- **目的**：
  1. 皮膚病変（良性〜悪性）を写したダーモスコピー画像をCNN（畳み込みニューラルネットワーク）およびVision Transformerを用い7クラスに分類すること
  2. 結果は **Grad-CAM** およぼ **Attention Map** を用い可視化し解釈性を高めること
- **利用データ**：
  - HAM10000データセット（出典：[HARVARD DATABASE](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T)）
  - データ件数：10,015件（訓練データ7,010件 / 検証データ3,005件）

### 2507_multiomics_vae_go（TCGA-LUADデータを用いたマルチオミクス解析（機能解析およびVAE））
- **目的**：
  1. TCGA-LUAD の **RNA・メチル化（METH）・コピー数変異（CNV）** をそれぞれ解析し、がん組織内の役割（転写制御・免疫反応・代謝など）を整理すること
  2. データを統合した **変分オートエンコーダ（VAE）** で患者を再クラスタリングし、単一オミクスでは見えにくい多面的な特徴を抽出すること
- **利用データ**：
  - TCGA-LUAD（出典：[GDC Data Portal](https://portal.gdc.cancer.gov/)）
  - **RNA**： Gene Expression Quantification / STARでフィルター、*_gene_counts.tsvを使用（517症例）
  - **METH**：Methylation Beta Value / Illumina 450Kでフィルター、*level3betas.txtを使用（579症例）
  - **CNV**：Gene-level Copy Numberでフィルター、gene_level_copy_number*.tsvを使用（518症例）
<br><br>
## 今後の追加予定
このリポジトリでは、新しい分析結果を随時追加する予定です。  