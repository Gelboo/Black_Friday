import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.model_selection import KFold,GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor
from sklearn.neural_network import MLPRegressor

pd.set_option('display.max_columns',15)
margin = '___________+++++____________________++++++_____________________+++++________'
asking = ['press y then Enter To View ',' else press any key: ']

X = pd.read_csv('X_train.csv')
Xs = pd.read_csv('X_train_StandardScaleDF.csv')
Y = pd.read_csv('Y_train.csv')
pca = PCA(4)
principalComp = pca.fit_transform(X)
print(pca.explained_variance_ratio_)
principalDf = pd.DataFrame(data=principalComp,columns=['c1','c2','c3','c4'])
print(principalDf.head())

kf = KFold(20)

Xs_array = Xs.values
Y_array = Y.values
for a,b in kf.split(Xs_array):
    X_train,X_test = Xs_array[a],Xs_array[b]
    y_train,y_test = Y_array[a],Y_array[b]

lr = LinearRegression()
DT = DecisionTreeRegressor()
RF = RandomForestRegressor()
GB = GradientBoostingRegressor()
NN = MLPRegressor(hidden_layer_sizes=(100,8),random_state=1)
inp = input("Do you want to fit the models "+asking[1])
if inp == 'y':
    model1 = lr.fit(X_train,y_train)
    model2 = DT.fit(X_train,y_train)
    model3 = RF.fit(X_train,y_train)
    model4 = GB.fit(X_train,y_train)
    model5 = NN.fit(Xs_array,Y_array)

    print("Accuracy Score of Linear regression on train set",model1.score(X_train,y_train)*100)
    print("Accuracy Score of Decision Tree on train set",model2.score(X_train,y_train)*100)
    print("Accuracy Score of Random Forests on train set",model3.score(X_train,y_train)*100)
    print("Accuracy Score of Gradient Boosting on train set",model4.score(X_train,y_train)*100)
    print("Accuracy Score of Neural Network on train set",model5.score(X_train,y_train)*100)

    print("\n\n")
    print("Accuracy Score of Linear regression on test set",model1.score(X_test,y_test)*100)
    print("Accuracy Score of Decision Tree on test set",model2.score(X_test,y_test)*100)
    print("Accuracy Score of Random Forests on test set",model3.score(X_test,y_test)*100)
    print("Accuracy Score of Gradient Boosting on testset",model4.score(X_test,y_test)*100)
    print("Accuracy Score of Neural Network on testset",model5.score(X_test,y_test)*100)


print("The accuracy of models using GridSearch")
param_grid = {'n_estimators':[1,3,10,30,100,300]}
grid_rf = GridSearchCV(RandomForestRegressor(),param_grid,cv=3,scoring='neg_mean_squared_error').fit(X_train,y_train)
print(grid_rf.cv_results_)
