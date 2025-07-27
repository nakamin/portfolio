import hydra
from omegaconf import DictConfig
import torch
from sklearn.model_selection import train_test_split
import numpy as np
import mlflow

from utils.seed import set_seed
from datasets.load_datasets import metadata, make_dataloader
from utils.train_loop import objective
from utils.logger import setup_mlflow, parameter_info, best_log, log_dataset_info

@hydra.main(config_path="config", config_name="config", version_base="1.1")
def main(cfg: DictConfig):

    # GPUの確認
    print("CUDA Available:", torch.cuda.is_available())
    print("GPU Count:", torch.cuda.device_count())

    set_seed(cfg.experiment.seed)

    image_id, labels = metadata(cfg)

    train_idx, val_idx = train_test_split(
    np.arange(len(image_id)),
    test_size = 0.3,
    stratify=labels, # クラスごとに均等に分割
    random_state = cfg.experiment.seed
    )
    mode=cfg.train.mode
    train_loader, val_loader = make_dataloader(image_id, labels, train_idx, val_idx, cfg, mode=mode)

    # MLflow開始(mlflow.start_run() を呼び出す前に、前のRunが end_run() しておく)
    if mlflow.active_run() is not None:
        mlflow.end_run()
    
    # experimentやtracking_uriの設定
    setup_mlflow(cfg)

    # 実験を決める
    run_name = f"model_{cfg.train.model_name}_lr={cfg.train.lr}_bs={cfg.train.batch_size}"

    with mlflow.start_run(run_name=run_name) as run:
        run_id = run.info.run_id
        model_filename = f"best_model_{run_name}_id_{run_id}.pth"

        parameter_info(cfg)
        log_dataset_info(cfg, train_loader, val_loader)

        best_epoch, best_val_loss, best_acc, best_model_state = objective(
            cfg,
            train_loader,
            val_loader,
            num_classes=cfg.dataset.num_classes,
            num_epochs=cfg.train.epochs,
            model_filename=model_filename,
            mode=mode
        )

        best_log(best_val_loss, best_acc)

    print("Best Epoch:", best_epoch)
    print("Best Val Loss:", best_val_loss)
    print("Best Acc:", best_acc)

if __name__ == "__main__":
    main()