from datasets import load_dataset, Dataset, DatasetDict
from transformers import AutoModelForSeq2SeqLM, Seq2SeqTrainingArguments, Seq2SeqTrainer
from transformers import AutoTokenizer
from transformers import DataCollatorForSeq2Seq
import numpy as np
from datasets import load_metric


BASE_PATH = ""
TRAIN_RESTRICTED_PATH = "restricted_train_dataset.csv"
OOV_RESTRICTED_PATH = "restricted_test_dataset.csv"

restricted_train = load_dataset('csv', data_files=TRAIN_RESTRICTED_PATH)
restricted_test = load_dataset('csv', data_files=OOV_RESTRICTED_PATH)

dataset = DatasetDict({'train': restricted_train['train'],'test': restricted_test['train']})

tokenizer = AutoTokenizer.from_pretrained("t5-base")

source_lang = "en"
target_lang = "ltl"
prefix = "translate English to LTL: "

def preprocess_function(examples):
    inputs = [prefix + example.replace(',', ' ,') for example in examples[source_lang]]
    targets = [example for example in examples[target_lang]]
    model_inputs = tokenizer(inputs, max_length=256, truncation=True)

    with tokenizer.as_target_tokenizer():
        labels = tokenizer(targets, max_length=256, truncation=True)

    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

tokenized_dataset = dataset.map(preprocess_function, batched=True)

item = tokenized_dataset['train']['ltl'][0]
decoded_item = tokenizer.decode(tokenized_dataset['train']['labels'][0])

reversed_vocab = {i: w for w, i in tokenizer.get_vocab().items()}

print("item",item)
print("decoded_item",decoded_item)
print("len",len(item.split(' ')), len(tokenized_dataset['train']['labels'][0]), len(decoded_item.split(' ')))
print("tokenized_dataset",tokenized_dataset['train']['labels'][0])
print("reversed_vocab",[reversed_vocab[i] for i in tokenized_dataset['train']['labels'][0]])


print("len-test",len(item.split(' ')), len(tokenized_dataset['test']['labels'][0]), len(decoded_item.split(' ')))
print("tokenized_dataset-test",tokenized_dataset['test']['labels'][0])
print("reversed_vocab-test",[reversed_vocab[i] for i in tokenized_dataset['test']['labels'][0]])


model = AutoModelForSeq2SeqLM.from_pretrained("t5-base")

model.resize_token_embeddings(len(tokenizer))


print("For T5:")
print("Tokenizer vocab_size: {}".format(tokenizer.vocab_size))
print("Model vocab size: {}\n".format(model.config.vocab_size))

data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model)

RESULTS_DIR = "./restricted"
logs_dir = "./logfile"

training_args = Seq2SeqTrainingArguments(
    output_dir=RESULTS_DIR,
    evaluation_strategy="epoch",
    # evaluation_strategy="steps",
    learning_rate=0.0001,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    weight_decay=0.01,
    save_strategy='steps',
    save_steps=150,
    num_train_epochs=10,
    adam_beta2=0.98,
    warmup_steps=2500,
    optim="adamw_torch",
    predict_with_generate=True,
    generation_max_length=256,
    # logging_dir=logs_dir,
    # logging_steps=20,
    # save_strategy='epoch'
)


metric = load_metric("sacrebleu")

def postprocess_text(preds, labels):
    preds = [pred.strip() for pred in preds]
    labels = [[label.strip()] for label in labels]
    return preds, labels
def compute_metrics(eval_preds):
    preds, labels = eval_preds
    if isinstance(preds, tuple):
        preds = preds[0]
    preds = np.where(preds != -100, preds, tokenizer.pad_token_id)
    decoded_preds = tokenizer.batch_decode(preds, skip_special_tokens=True)
    # Replace -100 in the labels as we can't decode them.
    labels = np.where(labels != -100, labels, tokenizer.pad_token_id)
    decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)
    # Some simple post-processing
    decoded_preds, decoded_labels = postprocess_text(decoded_preds, decoded_labels)
    # print("decoded_preds:",decoded_preds)
    # print("decoded_labels:", decoded_labels)
    result = metric.compute(predictions=decoded_preds, references=decoded_labels)
    result = {"bleu": result["score"]}
    prediction_lens = [np.count_nonzero(pred != tokenizer.pad_token_id) for pred in preds]
    result["gen_len"] = np.mean(prediction_lens)
    result = {k: round(v, 4) for k, v in result.items()}
    return result


trainer = Seq2SeqTrainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["test"],
    tokenizer=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics,
)
trainer.train("./restricted1/checkpoint-9300/") # If u want to resume a checkpoint then use this
trainer.train()

# trainer.evaluate(tokenized_dataset["test"], metric_key_prefix='bleu', max_length=256)
