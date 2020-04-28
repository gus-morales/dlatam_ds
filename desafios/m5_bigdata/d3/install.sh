YELLOW='\033[0;33m'
CYAN='\033[0;36m'
LRED='\033[1;31m'
NC='\033[0m' # No Color

#echo "${YELLOW}SCRIPT START${NC}"
echo "SCRIPT START"
echo ""
#echo "${CYAN}(*) Install basic Python libraries?${NC} (y/n)"
echo "(*) Install basic Python libraries? (y/n)"
while true; do
    read -p "" yn
    case $yn in
        [Yy]* ) echo "";\
        sudo pip-3.7 install ipython pandas numpy scikit-learn; break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no.";;
    esac
done
echo ""

#echo "${CYAN}(0) Download source files from GitHub?${NC} (y/n)"
echo "(0) Download source files from GitHub? (y/n)"
while true; do
    read -p "" yn
    case $yn in
        [Yy]* ) echo "";\
        wget -L -nv https://raw.githubusercontent.com/gus-morales/dlatam_ds/master/desafios/m5_bigdata/d3/src/1_simulate_data.py;\
        wget -L -nv https://raw.githubusercontent.com/gus-morales/dlatam_ds/master/desafios/m5_bigdata/d3/src/2_train_models.py;\
        wget -L -nv https://raw.githubusercontent.com/gus-morales/dlatam_ds/master/desafios/m5_bigdata/d3/src/3_predict_model.py;\
        mkdir src; mv *.py src/.; break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no.";;
    esac
done
echo ""

#echo "${CYAN}(1) Generating mock data${NC}"
echo "(1) Generating mock data"
python3.7 src/1_simulate_data.py 1000 11238 dat/train_delivery_data
python3.7 src/1_simulate_data.py 10000 42 dat/test_delivery_data
echo ""

#echo "${CYAN}(2) Training models${NC}"
echo "(2) Training models"
while true; do
    read -p "Proceed? (y/n) " yn
    case $yn in
        [Yy]* ) echo "";\
                python3.7 src/2_train_models.py | tee candidate_models.txt;\
                mv candidate_models.txt txt/.; break;;
        #[Nn]* ) echo "${LRED}SCRIPT ABORTED${NC}"; exit;;
        [Nn]* ) echo "SCRIPT ABORTED"; exit;;
        * ) echo "Please answer yes or no.";;
    esac
done
echo ""

#echo "${CYAN}(3) Estimating probabilities${NC}"
echo "(3) Estimating probabilities"
python3.7 src/3_predict_model.py | tee eval_pr.txt
mv eval_pr.txt txt/.
echo ""

#echo "${CYAN}(4.1) Exporting files to S3 bucket${NC}"
echo "(4.1) Exporting files to S3 bucket"
while true; do
    read -p "Proceed? (y/n) " yn
    case $yn in
        [Yy]* ) echo "";\
                aws s3 cp src s3://adldesafio3/src --recursive;\
                aws s3 cp txt s3://adldesafio3/txt --recursive; break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no.";;
    esac
done
echo ""

#echo "${CYAN}(4.2) Zipping project for evaluation${NC}"
echo "(4.2) Zipping project for evaluation"
zip Gustavo_Morales_desafio3.zip src/* dat/* txt/* scr/*
echo ""

#echo "${YELLOW}SCRIPT END${NC}"
echo "SCRIPT END"
