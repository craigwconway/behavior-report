import os
import timeit

from experiment import DoExperiment
from data import ReportCards
from model import TinyConv


if __name__ == "__main__":
    general_results_dir = os.path.join(os.getcwd(), "results")

    tot0 = timeit.default_timer()
    DoExperiment(
        descriptor="TinyConv_ReportCards",
        general_results_dir=general_results_dir,
        custom_net=TinyConv,
        custom_net_args={},
        learning_rate=1e-3,  # default 1e-3
        weight_decay=1e-7,  # default 1e-7
        num_epochs=3,
        patience=3,
        batch_size=1,
        debug=True,
        use_test_set=False,
        task="train_eval",
        old_params_dir="",
        chosen_dataset=ReportCards,
        chosen_dataset_args={},
    )
    tot1 = timeit.default_timer()
    print("Total Time", round((tot1 - tot0) / 60.0, 2), "minutes")
