LRED='\033[1;31m'
NC='\033[0m' # No Color

while true; do
    read -p "${LRED}ARE YOU SURE?${NC} (y/n) " yn
    case $yn in
        [Yy]* ) echo "";\
                rm -r dat; rm -r pkl; rm -r txt; rm -r scr;\
                rm *.zip; break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no.";;
    esac
done

echo "${LRED}Removed all output files${NC}"