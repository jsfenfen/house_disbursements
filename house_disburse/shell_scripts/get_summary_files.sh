# retrieve some files. 


# use relative path... 
datadir=../disbursements/data
for year in  '2009' '2010' '2011' '2012' '2013'
do
    for quarter in 'Q1' 'Q2' 'Q3' 'Q4'
    do
        echo "retrieving http://assets.sunlightfoundation.com.s3.amazonaws.com/expenditures/house/$year$quarter-summary.csv"
        curl -o $datadir/$year$quarter-summary.csv "http://assets.sunlightfoundation.com.s3.amazonaws.com/expenditures/house/$year$quarter-summary.csv"
        sleep 2
    done
done
