from sklearn import linear_model
from sklearn import tree
from sklearn import ensemble
from sklearn import neighbors
from sklearn import naive_bayes

import trainer

def test_linear_models(column_name): 
    br = linear_model.BayesianRidge()
    trainer.test_model(br, column_name)
    l = linear_model.Lasso()
    trainer.test_model(l, column_name)
    ols = linear_model.LinearRegression()
    trainer.test_model(ols, column_name)
    en = linear_model.ElasticNet()
    trainer.test_model(en, column_name)

def test_decision_tree_models(column_name):
    dt = tree.DecisionTreeRegressor()
    trainer.test_model(dt, column_name)
    

def test_ensemble_models(column_name):
    rfr = ensemble.RandomForestRegressor()
    trainer.test_model(rfr, column_name)
    abr = ensemble.AdaBoostRegressor()
    trainer.test_model(abr, column_name)
    gbr = ensemble.GradientBoostingRegressor()
    trainer.test_model(gbr, column_name)

def test_nearest_neighbor_models(column_name):    
    knn = neighbors.KNeighborsRegressor()
    trainer.test_model(knn, column_name)

test_linear_models('with_robot_output')
test_decision_tree_models('with_robot_output')
test_ensemble_models('with_robot_output')
test_nearest_neighbor_models('with_robot_output')
