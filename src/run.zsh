#!/bin/zsh
# Run from cd /Users/kartiksastry/Dropbox\ \(GaTech\)/Gatech/CS\ 7641\ -\ Machine\ Learning/ML_Project/src
clear

echo "########################################"
echo "run.zsh: Activating conda environment"
echo "########################################"
# running "conda activate ml-project-env" from a shell requires some modification
source activate ml-project-env
echo "Done"
echo ""

echo "########################################"
echo "run.zsh: Combining Trip Data"
echo "########################################"
python3 combine_data.py
echo ""

echo "########################################"
echo "run.zsh: Preprocessing Combined Data"
echo "########################################"
python3 preprocess_data.py
echo ""

echo "########################################"
echo "run.zsh: Visualizing Preprocessed Data"
echo "########################################"
python3 visualize_data.py
echo ""

echo "########################################"
echo "run.zsh: Evaluating Regression Models"
echo "########################################"
python3 evaluate_models.py
echo ""

echo "########################################"
echo "run.zsh: Deactivating conda environment"
echo "########################################"
conda deactivate
echo "Done"
echo ""
