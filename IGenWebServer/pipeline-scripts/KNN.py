import pandas as pd
import argparse 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

parser=argparse.ArgumentParser()
#parser.add_argument("-i", required=True)
parser.add_argument("-d")
args=parser.parse_args()



column_names=["pop", "pop_dup", "PC1", "PC2", "PC3", "PC4", "PC5", "PC6", "PC7", "PC8", "PC9", "PC10", "PC11", "PC12", "PC13", "PC14", "PC15", "PC16", "PC17", "PC18", "PC19", "PC20"]
df=pd.read_csv(args.d + "/PCA/1000G_PCA_merged.eigenvec", sep=' ', names=column_names)


# splitting dataframe by row index 
df_1 = df.loc[:500,:] 
df_2 = df.loc[500,:] 

#pick the number of dimensions 
X=df_1.iloc[:, 2:7].values

#labels 
df_1["pop"]=df_1["pop"].str.replace('.\d+', '')
y =df_1["pop"]

#split into test and training data 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

#scaling the data 
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

#KNN
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)

#making sample array from the  
sample_array=[]
sample=[]
sample.append(df_2[2])
sample.append(df_2[3])
sample.append(df_2[4])
sample.append(df_2[5])
sample.append(df_2[6])
sample_array.append(sample)

#scaling the sample 
test=scaler.transform(sample_array)

#predicting ancestry of sample
y_pred = classifier.predict(test)

with open(args.d + "/token_s_d.txt", "w") as f:
	f.write(y_pred[0])
	f.write("\n")