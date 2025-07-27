from torchvision import transforms
from timm.data import create_transform

# Xception Netの前処理
train_transform = transforms.Compose([
    transforms.Resize((int(299/ 0.875)), interpolation=transforms.InterpolationMode.BICUBIC),
    transforms.CenterCrop(299),
    transforms.RandomRotation(10),
    transforms.ToTensor(), # PIL 画像を (C, H, W) の torch.Tensor に変換
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5]),
    ])
val_transform = transforms.Compose([
    transforms.Resize((int(299/ 0.875)), interpolation=transforms.InterpolationMode.BICUBIC),
    transforms.CenterCrop(299),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])

# Vitの前処理
train_transform_vit = create_transform(
    input_size=224,  # ViTの入力サイズ
    is_training=True,  # 学習時のデータ拡張を有効化
    auto_augment="rand-m9-mstd0.5-inc1",  # RandAugment + 正規化の設定
    interpolation="bicubic"  # 画像の補間方法
)

val_transform_vit = create_transform(
    input_size=224,
    is_training=False  # 検証時はデータ拡張なし
)