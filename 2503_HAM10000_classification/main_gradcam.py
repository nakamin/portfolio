import torch
import timm
import hydra
from omegaconf import DictConfig
from datasets.load_datasets import metadata, ImageDataset, CustomSubset
from sklearn.model_selection import train_test_split
from datasets.data_transforms import val_transform
from utils.gradcam_utils import get_valdata, get_heatmap, visualize_heatmap

@hydra.main(config_path="config", config_name="config", version_base="1.1")
def main_gradcam(cfg: DictConfig):
    """
    model_save_pathからmodelを読み込み、gradcamを計算し可視化する
    """

    # メタデータとラベル読み込み
    image_id, labels = metadata(cfg)

    # validationデータのインデックス取得（再現のために seed 使用）
    _, val_idx = train_test_split(
        range(len(image_id)),
        test_size=0.3,
        stratify=labels,
        random_state=cfg.experiment.seed
    )

    model = timm.create_model(cfg.gradcam.model_name, pretrained=False, num_classes=7, mode=None)
    model_save_path = cfg.gradcam.model_save_path
    device = torch.device('cpu')
    model.load_state_dict(torch.load(model_save_path))
    model.eval()

    dataset = ImageDataset(image_id, labels, image_dir=cfg.dataset.image_dir, transform=None)
    val_subset = CustomSubset(dataset, val_idx, transform=val_transform)

    correct_samples = get_valdata(val_idx, dataset, image_id, device, model)

    heatmaps, correct_samples = get_heatmap(cfg, correct_samples, val_idx, val_subset, device, model)
    visualize_heatmap(cfg, correct_samples, heatmaps, "Correct")

if __name__ == '__main__':
    main_gradcam()