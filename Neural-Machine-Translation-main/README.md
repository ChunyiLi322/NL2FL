# Neural-Machine-Translation for LTL


This reposiroty contains the jupyter notebook for running the experiment related to the paper "Neural Machine Translation: from Natural Language requirements to Linear Temporal Logic formulas” by Riccardo Coltrinari, Flavio Corradini, Marco Piangerelli and Barbara Re.

Temporal Logic is a type of formal logic used in software engineering and formal methods to check properties of a system behavior over time, with the goal of ensuring its reliability and correctness. Despite the advantages of using a precise syntax, the advanced expertise required to use temporal logic and the risk of errors in the expressed properties have limited the use of formal logic by favoring the use of natural language.
In the literature, there have been attempts to make the construction of formal properties from natural language easier, but most focus on simplified use cases to make the problem easier. However, the ability to translate (unrestricted) natural language requirements into temporal logic formulas could extend its use to various domains.
In this paper, we make a distinction between restricted and unrestricted natural language requirements and how they can be translated into Temporal Logic formulas, specifically Linear Temporal Logic (LTL) formulas. We present a new approach for synthesizing English-to-LTL pairs and we use pre-trained language models to perform the translation, reaching high performance, in terms of BLEU, on out-of-vocabulary test data-sets. We also propose a combined hierarchical solution to address the difficulties of fine-tuning a single model to translate both forms of requirements. Finally, we discuss potential improvements, both for the present work and more in general for the field.

### Using the Notebook

Each experiment has been performed on Google Colab, hence all the relative dataset paths are related to Google Drive.
For this reason you need to create a Google account if you don't have one already, otherwise you can change the relative paths within the notebooks to run it locally.

If you want to run the notebooks on Google Colab without changing paths, you need to create a folder named "experiments" in your Google Drive's "My Drive" section.
Then add the dataset files to the folder so that you can simply run the notebooks.

If you want to replicate the same experiments as the ones in the paper, you can either download the datasets from the following link:

https://huggingface.co/datasets/cRick/NL-to-LTL-Synthetic-Dataset

or you can recreate them using the dataset generator with the same parameters showed in the paper.

The dataset generator is available at the following link:

https://github.com/RiccardoColtrinari/nl2ltl-dataset-generator




