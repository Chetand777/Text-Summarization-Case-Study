# Create Entity. Return type of a function
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
  root_dir: Path
  source_url: str
  local_data_file: Path
  unzip_dir: Path



# Entity
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataValidationConfig:
  root_dir: Path
  STATUS_FILE: str
  ALL_REQUIRED_FILES: list



# Entity
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataTransformationConfig:
  root_dir: Path
  data_path: Path
  tokenizer_name: Path



# Entity for model trainer
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class ModelTrainerConfig:
  root_dir: Path
  data_path: Path
  model: Path
  num_train_epochs: int
  warmup_steps: int
  per_device_train_batch_size: int
  weight_decay: float
  logging_steps: int
  evaluation_strategy: str
  eval_steps: int
  save_steps: int
  gradient_accumulation_steps: int



# Entity for model evaluation
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class ModelEvaluationConfig:
  root_dir: Path
  data_path: Path
  model_path: Path
  tokenizer_path: Path
  metric_file_name: Path