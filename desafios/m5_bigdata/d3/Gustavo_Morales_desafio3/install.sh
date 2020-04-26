YELLOW='\033[0;33m'
CYAN='\033[0;36m'
LRED='\033[1;31m'
NC='\033[0m' # No Color

echo "${YELLOW}SCRIPT START${NC}"
echo ""
echo "${CYAN}(1) Generating mock data${NC}"
python3.7 src/simulate_data.py 1000 11238 dat/train_delivery_data
python3.7 src/simulate_data.py 10000 42 dat/test_delivery_data
echo ""
echo "${CYAN}(2) Training models${NC}"
while true; do
    read -p "Select the best model now? (y/n) " yn
    case $yn in
        [Yy]* ) echo ""; python3.7 src/train_models.py | tee candidate_models.txt; mv candidate_models.txt txt/.; break;;
        [Nn]* ) echo "${LRED}SCRIPT ABORTED${NC}"; exit;;
        * ) echo "Please answer yes or no.";;
    esac
done
echo ""
echo "${CYAN}(3) Estimating probabilities${NC}"
python3.7 src/predict_model.py | tee eval_pr.txt
mv eval_pr.txt txt/.
echo ""
echo "${CYAN}(4.1) Exporting files to S3 bucket${NC}"
aws s3 cp src s3://adldesafio3/src --recursive
aws s3 cp txt s3://adldesafio3/txt --recursive
echo ""
echo "${CYAN}(4.2) Zipping project for evaluation${NC}"
zip Gustavo_Morales_desafio3.zip src/* dat/* txt/* scr/*
echo ""
echo "${YELLOW}SCRIPT END${NC}"