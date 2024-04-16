# Components
import os
from textsummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk
from textsummarizer.entity import DataTransformationConfig


class DataTransformation:
  def __init__(self, config: DataTransformationConfig):
    self.config = config
    self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)


# Converting the data into feature by tokenizing it to fed ML model
  def convert_example_to_features(self, example_batch):
    input_embeddings = self.tokenizer(example_batch['dialogue'], max_length = 1024, truncation = True)

    with self.tokenizer.as_target_tokenizer():
      target_embeddings = self.tokenizer(example_batch['summary'], max_length = 128, truncation = True)

    return {

      'input_ids' : input_embeddings['input_ids'],
      'attention_mask' : input_embeddings['attention_mask'],
      'labels' : target_embeddings['input_ids']

    }
  

  def convert(self):
    dataset_samsum = load_from_disk(self.config.data_path)
    dataset_smasum_pt = dataset_samsum.map(self.convert_example_to_features, batched=True)
    dataset_smasum_pt.save_to_disk(os.path.join(self.config.root_dir, "samsum_dataset"))