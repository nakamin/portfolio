import timm
import torch.nn as nn

# def create_model(cfg):
#     return timm.create_model(cfg.train.model_name, pretrained=True, num_classes=cfg.dataset.num_classes)

def create_model(cfg, mode):
    model = timm.create_model(cfg.train.model_name, pretrained=True, num_classes=cfg.dataset.num_classes)
    if mode=="Vit":
        model.head = nn.Linear(model.num_features, 7)
    return model